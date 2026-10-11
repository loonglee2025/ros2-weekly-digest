Title: Introducing NoDL: the Node Definition Language (ROSCon recap) - ROS / ROS General - Open Robotics Discourse

URL Source: https://discourse.ros.org/t/introducing-nodl-the-node-definition-language-roscon-recap/58501

Published Time: 2026-09-29T22:49:47+00:00

Markdown Content:
## post by alistair-english on Sep 29

**TLDR:** come work on [NoDL](https://nodl.readthedocs.io/en/latest/) in the [rosgraph-wg](https://docs.google.com/document/d/1xFqQECOKVCR3sZIUHGCPUi2huXw6nvgMxu6G3qBuQDU/edit?tab=t.0). Join the mailing list for automatic calendar invites to meetings: [https://groups.google.com/u/1/g/rosgraph-wg](https://groups.google.com/u/1/g/rosgraph-wg)

Hi everyone!

[@emersonknapp](https://discourse.ros.org/u/emersonknapp) and I presented “The Legible Node” at ROSCon last week. We talked about two things:

1.   Thin nodes - your _node_ is an interface adapter, it should not contain robot logic
2.   NoDL - the node definition language that allows you to statically declare your node interfaces

If you didnt catch it, [here are the slides (the_legible_node_slides.pdf)](https://sea2.discourse-cdn.com/flex022/404) (5.4 MB) - go check out the recording once its up. Working example code [here](https://github.com/emersonknapp/roscon2026_the_legible_node) too.

We had a great response from everyone at the conference, and we’re really excited to keep building NoDL with the community.

## [](https://discourse.ros.org/t/introducing-nodl-the-node-definition-language-roscon-recap/58501#p-118576-nodl-recap-1)NoDL Recap

A NoDL document looks like this:

```
nodl_version: 2
description: Drives a differential-base robot along a sequence of waypoints.

include:
  - ref: nodl://rclcpp/node

parameters:
  max_linear_speed:
    type: double
    default_value: 0.8
    description: Upper bound on commanded forward speed, in m/s.

publishers:
  - name: ~/status
    type: std_msgs/msg/String
    qos: {history: KEEP_LAST, depth: 1, reliability: RELIABLE}
    description: Human-readable status of the waypoint follower.

subscriptions:
  - name: odom
    type: nav_msgs/msg/Odometry
    qos: {history: KEEP_LAST, depth: 10, reliability: BEST_EFFORT}
    description: Wheel/inertial odometry used to track pose.

service_servers:
  - name: ~/cancel
    type: std_srvs/srv/Trigger
    description: Drops any queued waypoints and stops the robot.

service_clients:
  - name: /global_costmap/clear_entirely
    type: std_srvs/srv/Trigger
    description: Asks the costmap server to clear itself before a retry.

action_servers:
  - name: ~/follow_waypoints
    type: nav2_msgs/action/FollowWaypoints
    description: Follows an ordered list of waypoints to completion.

action_clients:
  - name: /navigate_to_pose
    type: nav2_msgs/action/NavigateToPose
    description: Delegates single-goal navigation to the planner stack.
```

You write this as part of your source code to declare the interface of your node (pub, sub, service, action, clients, params).

You can manually write a nodl document, or you can scrape an existing interface from a running node, using `ros2 nodl describe <node_name>`.

Once you have a nodl document you can:

*   assert that a running node conforms to the spec
*   generate node documentation
*   generate node boilerplate
*   (currently working on it) map out your application rosgraph statically

All of these concepts are covered in our documentation here: [https://nodl.readthedocs.io](https://nodl.readthedocs.io/) - go read it

## [](https://discourse.ros.org/t/introducing-nodl-the-node-definition-language-roscon-recap/58501#p-118576-come-work-with-us-2)Come work with us

We are building NoDL in the ROSGraph Working Group ([link](https://docs.google.com/document/d/1xFqQECOKVCR3sZIUHGCPUi2huXw6nvgMxu6G3qBuQDU/edit?tab=t.0)). Currently, its [@emersonknapp](https://discourse.ros.org/u/emersonknapp), Luke Sy and myself - we would love more friends!

You can check out what we’re working on in our current [milestone](https://github.com/ros-tooling/nodl/milestone/3). Exciting ones:

*   Pluggable code generator system, and more code generation features
*   Library-based node extension/mixin features
*   Graph analysis through launchfiles

We meet fornightly, next meeting is October 13, 2026 8:00 PM→9:00 PM (Abidjan) The meeting link is open to anyone: [Google Meet meeting](http://meet.google.com/veu-qkhb-iim)

## [](https://discourse.ros.org/t/introducing-nodl-the-node-definition-language-roscon-recap/58501#p-118576-how-to-get-involved-3)How to get involved

*   Join the mailing list and you’ll automatically get a meeting calendar invite: [https://groups.google.com/u/1/g/rosgraph-wg](https://groups.google.com/u/1/g/rosgraph-wg)
*   say hi in Zulip - [Public view of Open Source Robotics Foundation | Zulip team chat](https://openrobotics.zulipchat.com/#narrow/channel/546182-ROSGraph-Working-Group/)
*   read the docs: [https://nodl.readthedocs.io](https://nodl.readthedocs.io/)
*   check out the repo: [GitHub - ros-tooling/nodl: ROS 2 Node Definition Lanaguage (NoDL) · GitHub](https://github.com/ros-tooling/nodl)
*   have a look at our milestones and project board 
    *   [ROSGraph WG · GitHub](https://github.com/orgs/ros-tooling/projects/6/views/1)
    *   [GitHub · Where software is built](https://github.com/ros-tooling/nodl/milestone/3)

## [](https://discourse.ros.org/t/introducing-nodl-the-node-definition-language-roscon-recap/58501#p-118576-links-4)LINKS

*   ROSCon Presentation materials (slides and _working examples)_
    *   [GitHub - emersonknapp/roscon2026_the_legible_node: Materials from ROSCon 2026 talk "The Legible Node: Patterns and tools for clearer, more declarative ROS applications" · GitHub](https://github.com/emersonknapp/roscon2026_the_legible_node)

*   **NoDL**
    *   docs: [NoDL: Node Definition Language](https://nodl.readthedocs.io/en/latest/)
    *   repo: [GitHub - ros-tooling/nodl: ROS 2 Node Definition Lanaguage (NoDL) · GitHub](https://github.com/ros-tooling/nodl)

*   **ROSGraph-wg**
    *   Info page: [ROSGraph Working Group - Google Docs](https://docs.google.com/document/d/1xFqQECOKVCR3sZIUHGCPUi2huXw6nvgMxu6G3qBuQDU/edit?tab=t.0)

    *   Meeting link: [Google Meet meeting](http://meet.google.com/veu-qkhb-iim)

    *   Mailing list: [https://groups.google.com/u/1/g/rosgraph-wg](https://groups.google.com/u/1/g/rosgraph-wg)

    *   Zulip channel: [Public view of Open Source Robotics Foundation | Zulip team chat](https://openrobotics.zulipchat.com/#narrow/channel/546182-ROSGraph-Working-Group/)

    *   Project board: [ROSGraph WG · GitHub](https://github.com/orgs/ros-tooling/projects/6/views/1)

    *   Current milestone: [GitHub · Where software is built](https://github.com/ros-tooling/nodl/milestone/3)

## post by mjcarroll on Sep 29

## post by kylefranz on Sep 30

## post by alistair-english on Oct 1
