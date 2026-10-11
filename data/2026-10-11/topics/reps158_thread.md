Title: Draft REP 158: OpenUSD Conventions for Simulation Asset Interoperability in Open Source Robotics - ROS / ROS Ideas - Open Robotics Discourse

URL Source: https://discourse.ros.org/t/draft-rep-158-openusd-conventions-for-simulation-asset-interoperability-in-open-source-robotics/55526

Published Time: 2026-06-17T10:40:36+00:00

Markdown Content:
## post by adamdbrw on Jun 17

Dear ROS Community,

Following the **REP-0001:2025** process, I am opening this public discussion thread for **Draft REP 158: OpenUSD Conventions for Simulation Asset Interoperability in Open Source Robotics**.

The goal of this REP is to define a standardized way to use OpenUSD (Universal Scene Description) so that simulation assets, such as environments and robots, can be built once and run across various simulation and visualization platforms.

I would love to hear your feedback, questions, and ideas on this proposal.

### [](https://discourse.ros.org/t/draft-rep-158-openusd-conventions-for-simulation-asset-interoperability-in-open-source-robotics/55526#p-114202-quick-links-1)Quick Links

*   **REP PR (merged):**[openrobotics/reps#29](https://github.com/openrobotics/reps/pull/29)
*   **Core Schema PR:**[ros-simulation/openusd-schemas#1](https://github.com/ros-simulation/openusd-schemas/pull/1)
*   **Compliance Checker PR:**[ros-simulation/openusd-schemas#5](https://github.com/ros-simulation/openusd-schemas/pull/5)

_Related Extensions (Not core to this REP, but highly relevant):_

*   **Extended Physics:**[ros-simulation/openusd-schemas#2](https://github.com/ros-simulation/openusd-schemas/pull/2)
*   **Controller Schemas:**[ros-simulation/openusd-schemas#4 (DRAFT)](https://github.com/ros-simulation/openusd-schemas/pull/4)

* * *

### [](https://discourse.ros.org/t/draft-rep-158-openusd-conventions-for-simulation-asset-interoperability-in-open-source-robotics/55526#p-114202-abstract-2)Abstract

This REP defines a standard way to use OpenUSD so that simulation assets such as environments and robots can be built once and used anywhere. Our goal is to ensure a single 3D asset works seamlessly across different physics engines (like Gazebo, O3DE, Isaac Sim, Newton, MuJoCo, and Genesis), ROS runtimes, and web visualizers (like glTF). To make this a reality, the REP standardizes how ROS interfaces are represented in USD, establishes clear rules for format conversions, and sets up community registries for extensions and compliant assets.

### [](https://discourse.ros.org/t/draft-rep-158-openusd-conventions-for-simulation-asset-interoperability-in-open-source-robotics/55526#p-114202-motivation-3)Motivation

While URDF and SDF serve ROS well, OpenUSD has emerged as a broader industry standard vital for Physical AI workflows and artist-engineer collaboration. However, OpenUSD currently lacks standardized semantics for ROS concepts (e.g., TF trees), and its flexibility permits proprietary extensions that cause vendor lock-in. Rather than replacing existing formats, this REP regulates OpenUSD to prevent fragmentation, standardize ROS interfaces, and promote ecosystem interoperability.

### [](https://discourse.ros.org/t/draft-rep-158-openusd-conventions-for-simulation-asset-interoperability-in-open-source-robotics/55526#p-114202-proposed-functionality-4)Proposed Functionality

This REP establishes a vendor-neutral OpenUSD profile for robotics through four primary pillars:

1.   **Standardized Asset Baseline:** Mandates MKS units, ROS-standard coordinates (Z-up), and a modular Extract-Transform-Load (ETL) structure. This cleanly separates visual geometries from neutral physics, while strictly isolating any proprietary simulator extensions into discrete, optional layers.
2.   **Declarative ROS Interface Schemas:** Introduces engine-agnostic OpenUSD schemas (`RosContextAPI`, Topics, Services, Actions, and Frames). By declaring intent rather than baking in execution logic, these schemas standardize how simulators handle namespaces, sensor data, and TF tree generation.
3.   **Export & Conversion Rules:** Guarantees assets can seamlessly down-convert to lightweight formats like glTF 2.0 and URDF. It enforces standard PBR materials (`UsdPreviewSurface`), web-safe textures, and rigid rules for geometry, instancing, and variant baking.
4.   **Ecosystem Tooling & Registries:** Creates a canonical community registry for core schemas, plus extension pipelines for sensors, controls, and incubating physics features. It also introduces a native compliance checker to automatically validate and sanitize assets.

* * *

### [](https://discourse.ros.org/t/draft-rep-158-openusd-conventions-for-simulation-asset-interoperability-in-open-source-robotics/55526#p-114202-how-to-participate-5)How to Participate

Joint the discussion, even if you are new to OpenUSD - this REP is also about interoperable simulation for ROS in general.

*   Does the proposed separation of visual geometries, neutral physics, and simulator-specific layers match your asset workflows?
*   Are the declarative schemas (`RosContextAPI`, Topics, etc.) flexible enough to map to your existing simulator interfaces?
*   Do you have any suggestions or concerns regarding the proposed export and down-conversion pathways to glTF or URDF?
*   Is this REP compatible with your simulator concepts?

I look forward to your feedback!

read  12 min

## post by khalidbourr on Jun 17

## post by peci1 on Jun 18

## post by adamdbrw on Jun 24

## post by Z3ZEL on Jun 24

## post by Renato_Gasoto on Jun 24

## post by akaufman on Jun 25

## post by akaufman on Jun 25

## post by khalidbourr on Jun 26

## post by adamdbrw on Jun 29

## post by khalidbourr on Jun 29

## post by jimmy-mcelwain on Jul 2

## post by jimmy-mcelwain on Jul 8

## post by Renato_Gasoto on Jul 9

## post by adamdbrw on Jul 10

## post by adamdbrw on Jul 13

17 days later

## post by adamdbrw on Jul 30

## post by solonovamax on Jul 30

12 days later

## post by Renato_Gasoto on Aug 12

## post by zakmat on Aug 12

## Load more posts below
