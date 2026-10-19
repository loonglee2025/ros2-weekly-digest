Title: Gazebo PMC Meeting Minutes 2026-10-12 - Gazebo / Gazebo PMC - Open Robotics Discourse

URL Source: https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-12/58829

Published Time: 2026-10-13T17:23:17+00:00

Markdown Content:
## post by azeey on Oct 13

Hi Gazebo Community!

This week’s meeting was held on October 12, 2026 6:00 PM and the following is a summary:

## [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-12/58829#p-119001-pmc-business-1)PMC Business

*   Approved Cherrie Lu for mentee committer status.
*   Voting is currently open via email on adding Luca Della Vedova as a mentee PMC member.

## [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-12/58829#p-119001-new-agenda-items-2)New agenda items

*   **Gazebo Maintainer Audit & Rebalancing (Phase 2)**: A reminder that Phase 2 of the [Gazebo Maintainer Audit & Rebalancing Workspace (2026)](https://docs.google.com/spreadsheets/d/1Dk0cYyfQ-Ig1VztV74WaAkqRf-fdvgduxQHkhMWnfD4/edit?pli=1&gid=0#gid=0) (not public) is open through October 16, 2026. Committers interested in taking primary or secondary roles on packages can sign up in the spreadsheet before assignments are finalized and balanced across the team.
*   **Homebrew Support Timeline**: 
    *   Gazebo Ionic reaches end-of-life in December, 2026.
    *   Due to Homebrew’s scheduled removal of FreeImage on January 10, 2027 ([homebrew-simulation#3298](https://github.com/osrf/homebrew-simulation/issues/3298)), Homebrew support for Gazebo Harmonic ([homebrew-simulation#3598](https://github.com/osrf/homebrew-simulation/pull/3598)) and Fortress ([homebrew-simulation#3597](https://github.com/osrf/homebrew-simulation/pull/3597)) will be dropped on the same date.
    *   Qt5 support in Homebrew will also be dropped in May 2027. An announcement post will be drafted and shared on Discourse.

*   **Review Policy for Prerelease Version Bumps**: Discussed streamlining the prerelease process by removing individual pull request review requirements for version bumps (such as Rotary prereleases). The agreed approach is to announce upcoming prereleases in advance with a short waiting window (up to 24 hours) before merging. Documentation will be updated to reflect this workflow.
*   **Backport Policy & Downstream Testing**: Discussed guidelines for backporting multi-stage pull requests or features spanning multiple packages. While clean backports without conflicts can be merged directly, authors are encouraged to consider pausing backports until all related changes land on `main` and downstream continuous integration runs have completed.

## [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-12/58829#p-119001-updates-3)Updates

### [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-12/58829#p-119001-infrastructure-buildfarm-4)Infrastructure & Buildfarm

*   **macOS Tahoe Support**: A new macOS Tahoe runner (`mac-six.tahoe`) is online and operational. Tahoe bottling is underway ([homebrew-simulation#3592](https://github.com/osrf/homebrew-simulation/pull/3592)).
*   **Python 3.15 Compatibility on Homebrew**: Formula test failures caused by the Python 3.15 rollout are being resolved with formula updates and bottle rebuilds for packages with Python bindings.
*   **CI Optimization**: A pull request is in review to skip Linux CI PR jobs when changes only affect ignored files such as documentation, Bazel rules, or workflows ([release-tools#1558](https://github.com/gazebo-tooling/release-tools/pull/1558)).
*   **Test Networking**: Merged [gz-sim#4047](https://github.com/gazebosim/gz-sim/pull/4047) to set `GZ_IP` across all test suites, preventing unintended multicast behavior.

### [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-12/58829#p-119001-simulation-physics-5)Simulation & Physics

*   **Bullet-Featherstone Kinematics Mode**: Added kinematics mode improvements in `gz-physics`, fixing non-base link velocity calculations ([gz-physics#1112](https://github.com/gazebosim/gz-physics/pull/1112)) and supporting multi-link models ([gz-physics#1113](https://github.com/gazebosim/gz-physics/pull/1113)).
*   **Thruster Test Stability**: Addressed intermittent thruster test failures by waiting for thruster commands before stepping simulation time, backported across branches ([Jetty](https://github.com/gazebosim/gz-sim/pull/4065), [Ionic](https://github.com/gazebosim/gz-sim/pull/4064), [Harmonic](https://github.com/gazebosim/gz-sim/pull/4063)).

### [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-12/58829#p-119001-rendering-sensors-6)Rendering & Sensors

*   **Image Constructor Cleanup**: Removed an unreleased raw pointer `Image` constructor in `gz-rendering` ([Rotary](https://github.com/gazebosim/gz-rendering/pull/1366), [Jetty](https://github.com/gazebosim/gz-rendering/pull/1367), [Ionic](https://github.com/gazebosim/gz-rendering/pull/1369), [Harmonic](https://github.com/gazebosim/gz-rendering/pull/1368)), resolving deprecation warnings in `CameraSensor` ([gz-sensors#675](https://github.com/gazebosim/gz-sensors/issues/675)).
*   **Ogre 2.2 macOS Compatibility**: Patched `ogre2.2` for Xcode 16.3 compatibility ([homebrew-simulation#3591](https://github.com/osrf/homebrew-simulation/issues/3591)).
*   **Sensor Test Scoping**: Updated `gz-sensors` to skip `CustomCameraInfoTopic` tests on render engines other than Ogre 2 ([Rotary](https://github.com/gazebosim/gz-sensors/pull/681), [Jetty](https://github.com/gazebosim/gz-sensors/pull/682), [Ionic](https://github.com/gazebosim/gz-sensors/pull/683)).

### [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-12/58829#p-119001-transport-communication-7)Transport & Communication

*   **Zenoh 1.8.0 Integration**: In-review backport to integrate Zenoh 1.8.0 into Gazebo Jetty ([gz-transport#977](https://github.com/gazebosim/gz-transport/pull/977)).
*   **Publication Routing**: Merged changes to route Zenoh publications exclusively to other sessions ([Rotary](https://github.com/gazebosim/gz-transport/pull/961), [Jetty](https://github.com/gazebosim/gz-transport/pull/965)).

### [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-12/58829#p-119001-releases-8)Releases

*   **Gazebo Rotary**: Completed the second prerelease of Gazebo Rotary.
*   **gz-rendering**: Released 10.1.0 ([Jetty](https://github.com/gazebosim/gz-rendering/pull/1371)), 9.6.0 ([Ionic](https://github.com/gazebosim/gz-rendering/pull/1372)), 8.3.0 ([Harmonic](https://github.com/gazebosim/gz-rendering/pull/1373)), and 6.7.0 ([Fortress](https://github.com/gazebosim/gz-rendering/pull/1374)).
*   **gz_rendering_vendor**: Released 0.4.5 ([Lyrical](https://github.com/gazebo-release/gz_rendering_vendor/pull/27)), 0.2.9 ([Kilted](https://github.com/gazebo-release/gz_rendering_vendor/pull/28)), and 0.0.8 ([Jazzy](https://github.com/gazebo-release/gz_rendering_vendor/pull/29)).

As always, the meeting notes are available at [![Image 1: :classical_building:](https://emoji.discourse-cdn.com/noto/classical_building.png?v=15) Gazebo PMC meeting weekly agenda - Google Docs](https://docs.google.com/document/d/1RpVMkwiKqXKnDjqtkviz4qp73oehivf4Z1x-fTITgZY/).

The next Gazebo PMC meeting will be on Today 6:00 PM  
 (See [Open Source Robotics Foundation official events](https://calendar.google.com/calendar/u/0/embed?src=agf3kajirket8khktupm9go748@group.calendar.google.com&ctz=UTC))
