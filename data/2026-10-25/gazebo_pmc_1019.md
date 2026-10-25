Title: Gazebo PMC Meeting Minutes 2026-10-19 - Gazebo / Gazebo PMC - Open Robotics Discourse

URL Source: https://discourse.openrobotics.org/t/gazebo-pmc-meeting-minutes-2026-10-19/58995

Published Time: 2026-10-20T21:03:42+00:00

Markdown Content:
## post by azeey 5 days ago

Hi Gazebo Community!

This week’s meeting was held on October 19, 2026 6:00 PM and the following is a summary:

## [](https://discourse.openrobotics.org/t/gazebo-pmc-meeting-minutes-2026-10-19/58995#p-119223-pmc-business-1)PMC Business

*   Approved adding Luca Della Vedova as a mentee PMC member.

## [](https://discourse.openrobotics.org/t/gazebo-pmc-meeting-minutes-2026-10-19/58995#p-119223-new-agenda-items-2)New agenda items

*   **Community Meeting**: A reminder for this week’s [community meeting on Scalable Multi-Robot Simulation in ROS 2 and Gazebo](https://discourse.openrobotics.org/t/community-meeting-scalable-multi-robot-simulation-in-ros-2-and-gazebo/58728), featuring multi-robot simulation, namespaces, and automatic bridging. Please note the **change in date and time** this month (7:00 PM Pacific) to better accommodate the Asia-Pacific region.
*   **Fuel Server Outage & Maintenance**: The Fuel server experienced downtime over the weekend due to high memory consumption triggered by crawler traffic downloading models in parallel. The server was restarted, and backend changes are being prepared to avoid loading full models into RAM along with an updated deployment mechanism ([fuel-server#25](https://github.com/gazebo-web/fuel-server/pull/25)).
*   **Auto-Merge & Required CI Checks**: Maintainers are reminded to verify which CI checks are required before enabling GitHub auto-merge. A recent Fortress backport ([gz-sim#4076](https://github.com/gazebosim/gz-sim/pull/4076)) auto-merged despite failing builds because only the DCO check was required, and had to be reverted ([gz-sim#4079](https://github.com/gazebosim/gz-sim/pull/4079)). Branch protection rules are being updated in [terraform_github_repos#10](https://github.com/gazebosim/terraform_github_repos/pull/10) to require Jenkins and GitHub Actions CI checks.
*   **Lightweight 2D Physics Engine Exploration (Box2D vs. TPE)**: Discussed experimenting with Box2D as a physics engine plugin to support very large-scale planar simulations with hundreds of robots requiring only collisions and basic kinematic motion. Compared against the existing Trivial Physics Engine (TPE), which currently lacks joint support; a deeper comparison between Box2D and extending TPE will be conducted.

## [](https://discourse.openrobotics.org/t/gazebo-pmc-meeting-minutes-2026-10-19/58995#p-119223-updates-3)Updates

### [](https://discourse.openrobotics.org/t/gazebo-pmc-meeting-minutes-2026-10-19/58995#p-119223-simulation-physics-c20-migration-4)Simulation, Physics & C++20 Migration

*   **Bullet-Featherstone Kinematic Mode**: Merged the full set of PRs enabling kinematic mode in Bullet-Featherstone on Rotary, with backports planned after verification on a demo world: 
    *   Enforce position limits on kinematically driven joints ([gz-physics#1118](https://github.com/gazebosim/gz-physics/pull/1118))
    *   Fix toggling links between kinematic and dynamic ([gz-physics#1122](https://github.com/gazebosim/gz-physics/pull/1122))
    *   Kinematic base velocity for links with a CoM offset ([gz-physics#1123](https://github.com/gazebosim/gz-physics/pull/1123))
    *   Fix force-torque sensor in hybrid kinematic/dynamic modes ([gz-physics#1124](https://github.com/gazebosim/gz-physics/pull/1124))
    *   Fix root joint position and velocity ([gz-physics#1125](https://github.com/gazebosim/gz-physics/pull/1125))

*   **ECM Batch Queries**: Merged runtime-typed `EntityComponentManager` (ECM) batch queries and exposed them to Python ([gz-sim#4006](https://github.com/gazebosim/gz-sim/pull/4006)).
*   **C++20 Migration**: Continuing work on [gz-cmake#580](https://github.com/gazebosim/gz-cmake/issues/580) to avoid hardcoding the C++ standard so builds follow the exported target standard. PRs are in review for `sdformat` examples ([sdformat#1733](https://github.com/gazebosim/sdformat/pull/1733)), `gz-sim` plugin examples and tutorials ([gz-sim#4086](https://github.com/gazebosim/gz-sim/pull/4086)), and the DART `ContactSurface` check in `gz-physics` ([gz-physics#1134](https://github.com/gazebosim/gz-physics/pull/1134)).

### [](https://discourse.openrobotics.org/t/gazebo-pmc-meeting-minutes-2026-10-19/58995#p-119223-rendering-sensors-transport-5)Rendering, Sensors & Transport

*   **Ogre 1.12 Migration**: The large Ogre 1.12 migration PR was split into stacked PRs for easier review ([gz-rendering PRs](https://github.com/j-rivero/gz-rendering/pulls)). While general custom shaders were fixed, custom terrain heightmap shaders remain broken due to upstream class removals in Ogre 1.12; the PMC agreed to merge without custom terrain shader support if a quick fix is not found, and request examples from users if needed later.
*   **PixelBuffer API Adaptations**: Backports adapting `gz-sensors` to the `PixelBuffer` API ([gz-sensors#674](https://github.com/gazebosim/gz-sensors/pull/674)) have been merged for Harmonic and Fortress, and are in review for Jetty ([gz-sensors#677](https://github.com/gazebosim/gz-sensors/pull/677)) and Ionic ([gz-sensors#678](https://github.com/gazebosim/gz-sensors/pull/678)) ahead of upcoming point releases.
*   **Zenoh CI in gz-sim**: A PR is in review to run Ubuntu Resolute CI tests a second time using Zenoh on `gz-sim``main` ([gz-sim#4085](https://github.com/gazebosim/gz-sim/pull/4085)). The team agreed that `gz-transport` should fail explicitly when Zenoh is selected via environment variable but not compiled in, rather than silently falling back to ZeroMQ.

### [](https://discourse.openrobotics.org/t/gazebo-pmc-meeting-minutes-2026-10-19/58995#p-119223-web-documentation-6)Web & Documentation

*   **Gazebo Web Ecosystem**: Ongoing work to modernize the `gazebosim-app` web frontend ([gazebosim-app PRs](https://github.com/gazebo-web/gazebosim-app/pulls)). We are also evaluating the feasibility of rewriting `gzweb` in Rust using the Bevy engine to improve performance, realism, and modern SDFormat support.
*   **Maintainer Guidelines**: Merged documentation updates covering backport timing, downstream testing tradeoffs, and prerelease version bump review policies ([docs#723](https://github.com/gazebosim/docs/pull/723)).

### [](https://discourse.openrobotics.org/t/gazebo-pmc-meeting-minutes-2026-10-19/58995#p-119223-infrastructure-packaging-release-tooling-7)Infrastructure, Packaging & Release Tooling

*   **macOS 26 (Tahoe) & Homebrew**: 
    *   Tahoe bottling is in progress ([homebrew-simulation#3599](https://github.com/osrf/homebrew-simulation/issues/3599)). The primary hurdle is compiling `ogre1.9` without the Apple Graphics Library (AGL, removed in macOS 26), for which a community contributed patch is in review ([homebrew-simulation#3615](https://github.com/osrf/homebrew-simulation/pull/3615)).
    *   Investigated flaky Homebrew build failures on Harmonic and Fortress caused by a Doxygen bug ([homebrew-simulation#3616](https://github.com/osrf/homebrew-simulation/issues/3616)); mitigation is complete for Harmonic and in review for Fortress.

*   **Pixi on macOS**: Prerequisites for supporting Pixi on macOS are in review ([release-tools#1566](https://github.com/gazebo-tooling/release-tools/pull/1566), [release-tools#1568](https://github.com/gazebo-tooling/release-tools/pull/1568)). Discussed the possibility of eventually phasing out Homebrew bottle builds if Pixi provides a smooth macOS developer experience, while keeping the Homebrew tap available.
*   **Release & CI Tooling**: 
    *   An automated changelog generation tool is up for review ([release-tools#1447](https://github.com/gazebo-tooling/release-tools/pull/1447)).
    *   A PR to skip Linux `CI-pr` Jenkins jobs when modified files match an ignore list is awaiting final updates ([release-tools#1558](https://github.com/gazebo-tooling/release-tools/pull/1558)).
    *   Build warning fixes are in review for `gz-physics` ([gz-physics#1127](https://github.com/gazebosim/gz-physics/pull/1127)) and `gz-cmake` ([gz-cmake#603](https://github.com/gazebosim/gz-cmake/pull/603)).
    *   `rosdistro-extension` work is underway to generate binary packages for testing distributions and handle automatic sourcing of `setup.bash` from child to parent workspaces.

As always, the meeting notes are available at [![Image 1: :classical_building:](https://emoji.discourse-cdn.com/noto/classical_building.png?v=15) Gazebo PMC meeting weekly agenda - Google Docs](https://docs.google.com/document/d/1RpVMkwiKqXKnDjqtkviz4qp73oehivf4Z1x-fTITgZY/).

The next Gazebo PMC meeting will be on Tomorrow 6:00 PM  
 (See [Open Source Robotics Foundation official events](https://calendar.google.com/calendar/u/0/embed?src=agf3kajirket8khktupm9go748@group.calendar.google.com&ctz=UTC))
