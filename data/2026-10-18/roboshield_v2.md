Title: RoboShield v2: an inline command firewall gateway for ROS 2 (Rust + rclrs, two-domain bridge, SROS2)

URL Source: https://discourse.ros.org/t/roboshield-v2-an-inline-command-firewall-gateway-for-ros-2-rust-rclrs-two-domain-bridge-sros2/58826

Published Time: 2026-10-13T16:13:01+00:00

Markdown Content:
## post by Amin_Ahmed_G on Oct 13

Hi all,

Follow-up on RoboShield, my ROS 2 security project. v1 was a passive Rust watchdog that parsed raw RTPS packets with libpcap and flagged unknown GUID prefixes, unauthorized publishers and topic floods. It could alert, but it couldn’t stop anything. v2 is an inline gateway that protects the robot.

**Repo:**[GitHub - Amin-Ahmed-G/robotshield: Embedded out-of-band NIDS for ROS 2 RTPS/DDS networks in Rust with libpcap packet inspection and topic spoofing detection. · GitHub](https://github.com/Amin-Ahmed-G/robotshield) (v1 is kept on branch `roboshield-v1-nids`)

### [](https://discourse.ros.org/t/roboshield-v2-an-inline-command-firewall-gateway-for-ros-2-rust-rclrs-two-domain-bridge-sros2/58826#p-118995-architecture-1)Architecture

```
Laptop  ~~ WiFi ~~  NanoPi (gateway)  ── Ethernet ──  Robot
domain 10           robot_firewall                   domain 20
untrusted           only bridge                      isolated LAN
```

*   One process creates **two contexts with different domain IDs** (rclrs / rclpy both support `domain_id` per context). It’s the only thing that bridges the two domains; the kernel doesn’t forward packets (`ip_forward=0`, nftables default-drop, port and peer allowlists per interface).
*   **SROS2 only on the WiFi side:** rcl reads `ROS_SECURITY_ENABLE` when each context initializes, so setting it per context gives an enforced enclave on the untrusted side and a plain domain on the robot side, for robots that can’t do DDS-Security.
*   Every command (`sensor_msgs/JointState`, or `Float64MultiArray` for `forward_command_controller`) passes through a rule engine that checks: joint names and array lengths, NaN/inf, per-joint position/velocity/effort limits (clamp or drop), sudden jumps since the last accepted command, a token-bucket rate limit, and stale or replayed header stamps.
*   Repeated incidents, a second publisher on the robot’s command topic (a rogue device on the robot LAN), extra `joint_states` publishers (state spoofing), or the robot reporting a position out of bounds trigger **LOCKDOWN**: all input is dropped and the robot is held at its last safe pose until an operator re-arms it. It also boots locked, and the systemd unit has a watchdog.
*   **Per-message publisher filtering:** each command’s `MessageInfo.publisher_gid` is matched to a node via the graph, so only a spoofing node’s messages are dropped and the real operator keeps control.

### [](https://discourse.ros.org/t/roboshield-v2-an-inline-command-firewall-gateway-for-ros-2-rust-rclrs-two-domain-bridge-sros2/58826#p-118995-results-laptop-ryzen-7-7435hs-jazzy-fast-dds-nanopi-numbers-pending-2)Results (laptop, Ryzen 7 7435HS, Jazzy, Fast DDS; NanoPi numbers pending)

|  |  |
| --- | --- |
| Rule engine, per 6-joint command | 1.37 µs median in Rust (Python: 9.5 µs) |
| Latency the gateway adds end to end | +0.5 ms median (Python version: +1.0 ms), 1000/1000 delivered |
| Attack self-test, SROS2 on, a cert-less publisher spamming throughout | 8/8 detected, robot never past its limit |
| 600 msg/s flood → lockdown | ~10 ms |

Benchmark scripts and raw data are in `bench/`.

### [](https://discourse.ros.org/t/roboshield-v2-an-inline-command-firewall-gateway-for-ros-2-rust-rclrs-two-domain-bridge-sros2/58826#p-118995-things-i-hit-that-might-help-others-3)Things I hit that might help others

1.   **rclrs on Jazzy binaries:** the message crates shipped in `/opt/ros/jazzy/share/*/rust` are built against `rosidl_runtime_rs` 0.6, so rclrs **0.7.0** works and 0.8 fails with `MessageIDL` trait errors. rclrs 0.7 also links against `test_msgs`, so `ros-jazzy-test-msgs` must be installed.
2.   **rclrs `TopicEndpointInfo` doesn’t expose `endpoint_gid`.** I vendored rclrs with a one-field patch (`vendor/rclrs/PATCH.md`) so publisher GIDs can be matched to node names.
3.   **rclpy (Jazzy) message info has no `publisher_gid`**, so the Python gateway can’t attribute individual messages and falls back to locking down when an unknown publisher appears.
4.   **Discovery race:** DDS can deliver data before the ROS node info for that endpoint arrives, so the publisher shows up as `_NODE_NAME_UNKNOWN_`. The gateway fails closed but gives new publishers a 2 s grace period before raising an alarm.

### [](https://discourse.ros.org/t/roboshield-v2-an-inline-command-firewall-gateway-for-ros-2-rust-rclrs-two-domain-bridge-sros2/58826#p-118995-questions-for-the-community-4)Questions for the community

*   Would an `endpoint_gid` field on `TopicEndpointInfo` be welcome upstream in rclrs? Happy to open a PR.
*   Is there interest in exposing `publisher_gid` in rclpy’s message info?
*   In Fast DDS, what’s the cleanest way to pin each participant in one process to its own interface? Right now I rely on nftables for that.
*   Has anyone shipped least-privilege SROS2 policy files for a teleop/commander enclave they’d recommend as a template?

A note on v1: my earlier post described inline blocking. That was the plan, but v1 shipped as alert-only; v2 is where enforcement actually lives.

Feedback on the threat model and the lockdown semantics is very welcome, especially from anyone running ros2_control over untrusted networks.

Thanks,  
 Amin
