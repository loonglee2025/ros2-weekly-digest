Title: Gazebo PMC Meeting Minutes 2026-10-05 - Gazebo / Gazebo PMC - Open Robotics Discourse

URL Source: https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-05/58601

Published Time: 2026-10-05T20:47:48+00:00

Markdown Content:
## post by azeey on Oct 5

Hi Gazebo Community!

This week’s meeting was held on October 5, 2026 6:00 PM and the following is a summary:

## [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-05/58601#p-118731-pmc-business-1)PMC Business

*   **PMC Membership & Mentee Committer Voting**: Voting is currently open for adding Cherry as a mentee committer, and an asynchronous email vote is being opened for Luca Della Vedova’s nomination to the PMC.
*   **Asynchronous Meeting Engagement**: The PMC agreed to encourage members and contributors in conflicting time zones to participate asynchronously by adding agenda items and updates directly to the meeting agenda document or discussing topics on Zulip.
*   **Process for Inactive Members**: The committee discussed procedures for handling inactive PMC members and committers to prevent quorum issues. The PMC agreed to research official processes while prioritizing informal outreach to overburdened members first to ask if they wish to step down.

## [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-05/58601#p-118731-new-agenda-items-2)New agenda items

*   **Phase 2 of Gazebo Maintainer Audit & Rebalancing**: Phase 2 of the maintainer audit is currently underway with a due date of October 16, 2026. Contributors interested in maintaining a project are encouraged to sign up on the [Maintainer Audit & Rebalancing Workspace (2026) (not public)](https://docs.google.com/spreadsheets/d/1Dk0cYyfQ-Ig1VztV74WaAkqRf-fdvgduxQHkhMWnfD4/edit?pli=1&gid=0#gid=0). Multiple individuals can sign up for the same project; final assignments will be rebalanced across the team at the end of Phase 2.
*   **Introduction to `rosdistro-extension` and its Impact on Gazebo**: A presentation was given on the [rosdistro-extension project](https://docs.google.com/presentation/d/1p9nxRFW4K5xV7HOAFEe3DfuLY9ml3Pek3JbVdaKCOr8/edit?slide=id.h4e946404cb58fd26_0_26#slide=id.h4e946404cb58fd26_0_26), which extends the ROS Distro metadata index and Python library. This project explores allowing ROS distributions to consume Gazebo packages directly through source imports (where ROS rebuilds packages from source, e.g., ROS Rolling extending Gazebo Jetty) and binary imports. While this could potentially replace Gazebo vendor packages in ROS and simplify release maintenance, CMake shims and upstream CI testing will still need to be addressed.
*   **Handling Unreleased Breaking Changes in `gz-rendering` and `gz-sensors`**: Following changes in [gazebosim/gz-rendering#1331](https://github.com/gazebosim/gz-rendering/pull/1331), a newly added image constructor was backported and later deprecated in stable branches. Because this function was never part of an official release, the PMC aligned on removing it directly from Jetty (and verifying other stable branches) rather than keeping an unreleased deprecated function, addressing warnings like [gazebosim/gz-sensors#675](https://github.com/gazebosim/gz-sensors/issues/675).
*   **Automating “Build Bottle” in Release Tooling**: The team discussed [gazebo-tooling/release-tools#1560](https://github.com/gazebo-tooling/release-tools/issues/1560) regarding automating the `build bottle` step when running `release.py` for Homebrew simulation pull requests. Consensus was reached to automate this step while implementing guardrails (such as detecting existing tags or PRs) to prevent duplicate script runs and duplicate PRs.
*   **Gazebo Mosaic Next Steps**: With the community naming process concluding and “Mosaic” selected as the name for the Gazebo M release, next steps for finalizing the naming rollout and repository setup will be coordinated.

## [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-05/58601#p-118731-updates-3)Updates

### [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-05/58601#p-118731-buildfarm-ci-4)Buildfarm & CI

*   The [Greenness report](https://docs.google.com/spreadsheets/d/1gX7Hw_aVsI4U05i2-NxCY66a4CmRy1Yyb6dokK5QtMg/edit?gid=1341902889#gid=1341902889) continues to show strong test coverage (>90–95%).

### [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-05/58601#p-118731-written-updates-not-discussed-live-5)Written Updates (Not Discussed Live)

_The following items were submitted as written updates in the agenda but were not discussed live during the meeting due to time constraints:_

#### [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-05/58601#p-118731-package-updates-6)Package Updates

*   **gz-sim**: 
    *   Added detection for WindowServer and Metal support on macOS in `FindDRI` ([gazebosim/gz-sim#4036](https://github.com/gazebosim/gz-sim/pull/4036), currently in review), eliminating the need for XQuartz on macOS.
    *   Preparing for a second round of prereleases for Rotary.

*   **gz-rendering**: Stabilizing Image changes in `main` and released branches.
*   **gz-transport**: Preparing a PR for Jetty with Zenoh backports and two manual fixes for ABI compatibility.
*   **sdformat**: A PR is awaiting review to support URDF 1.1 capsules in SDFormat ([gazebosim/sdformat#1722](https://github.com/gazebosim/sdformat/pull/1722)). Note: the `urdfdom` version in bazel-central-registry is currently outdated.
*   **gz-cmake**: 
    *   Added `REQUIRE` support ([gazebosim/gz-cmake#595](https://github.com/gazebosim/gz-cmake/pull/595)).
    *   Suppressed warnings when optional components are not found, fixing CMake issues in `gz-sensors` when the `gz-rendering` ogre1 component is absent ([gazebosim/gz-cmake#587](https://github.com/gazebosim/gz-cmake/pull/587)).

#### [](https://discourse.ros.org/t/gazebo-pmc-meeting-minutes-2026-10-05/58601#p-118731-release-tooling-infrastructure-7)Release Tooling & Infrastructure

*   **release-tools**: 
    *   Started work on supporting parameterless execution of `release.py` ([gazebo-tooling/release-tools#1564](https://github.com/gazebo-tooling/release-tools/issues/1564)).
    *   Improving the auto-changelog generator tool to handle backports with squash/rebase ([gazebo-tooling/release-tools#1447](https://github.com/gazebo-tooling/release-tools/pull/1447/changes/de0b90164d5fba137b5bf0dcb6ab2a96ecd39183)).
    *   Drafting Pixi support for macOS CI.
    *   Speeding up builds by skipping Linux CI-pr jobs when modified files match an ignore list ([gazebo-tooling/release-tools#1558](https://github.com/gazebo-tooling/release-tools/pull/1558)), along with a port of this exclusion feature to `gzdev`.

As always, the meeting notes are available at [![Image 1: :classical_building:](https://emoji.discourse-cdn.com/noto/classical_building.png?v=15) Gazebo PMC meeting weekly agenda - Google Docs](https://docs.google.com/document/d/1RpVMkwiKqXKnDjqtkviz4qp73oehivf4Z1x-fTITgZY/).

The next Gazebo PMC meeting will be on Tomorrow 6:00 PM  
 (See [Open Source Robotics Foundation official events](https://calendar.google.com/calendar/u/0/embed?src=agf3kajirket8khktupm9go748@group.calendar.google.com&ctz=UTC))
