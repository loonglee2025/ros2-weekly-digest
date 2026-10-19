Title: [RFC] Consolidating and Modernizing Integration Test Architecture for gz_ros2_control - ros-controls / ros-controls Ideas - Open Robotics Discourse

URL Source: https://discourse.ros.org/t/rfc-consolidating-and-modernizing-integration-test-architecture-for-gz-ros2-control/58883

Published Time: 2026-10-15T16:10:35+00:00

Markdown Content:
- [x] 
*   [Open Source Robotics Foundation](https://openrobotics.org/)
*   [ROS](https://ros.org/)
    *   [Project homepage](https://ros.org/)
    *   [Documentation](https://docs.ros.org/)
    *   [Getting help and support](https://docs.ros.org/en/jazzy/Contact.html#support)
    *   [ROS Packages Index](https://index.ros.org/)
    *   [Media and trademarks](https://www.ros.org/blog/media)

*   [ros-controls](https://control.ros.org/)
    *   [Project homepage](https://control.ros.org/)
    *   [Documentation](https://control.ros.org/)

*   [Gazebo](https://gazebosim.org/)
    *   [Project homepage](https://gazebosim.org/)
    *   [Documentation](https://gazebosim.org/docs/latest/)
    *   [Fuel models database](https://app.gazebosim.org/dashboard)

*   [Open-RMF](https://open-rmf.org/)
    *   [Project homepage](https://open-rmf.org/)
    *   [Documentation](https://osrf.github.io/ros2multirobotbook/)

*   [Infrastructure](https://infrastructure.openrobotics.org/)
*   [Community](https://openrobotics.zulipchat.com/)
    *   [Chat Server](https://openrobotics.zulipchat.com/)
    *   [Submit a related event](https://docs.google.com/forms/d/e/1FAIpQLSdIhzm7-DnAlBIUSsU6lITnV6SHpl1Oo8otnhUKp3pUqUAhSA/viewform?usp=dialog)
    *   [Official events calendar](https://calendar.google.com/calendar/embed?src=agf3kajirket8khktupm9go748%40group.calendar.google.com)
    *   [Community events calendar](https://calendar.google.com/calendar/embed?src=c_3fc5c4d6ece9d80d49f136c1dcd54d7f44e1acefdbe87228c92ff268e85e2ea0%40group.calendar.google.com)

*   [Service Status](https://status.openrobotics.org/)

[Skip to main content](https://discourse.ros.org/t/rfc-consolidating-and-modernizing-integration-test-architecture-for-gz-ros2-control/58883#main-container)

[![Image 1: Open Robotics Discourse](https://us1.discourse-cdn.com/flex022/uploads/ros/original/3X/7/b/7b98914132076b3a570a1e6d77ebf9e752704b7b.svg)](https://discourse.ros.org/)

Sign Up Log In
*    ​ 

*   [Topics](https://discourse.ros.org/latest "All topics")
*    More 

 Categories 

*   [![Image 2: ros](https://us1.discourse-cdn.com/flex022/uploads/ros/original/3X/2/6/26123a37f7aac0c6c95da44564ca0d81836a8628.png?v=15) ROS General](https://discourse.ros.org/c/ros/ros-general/8)
*   [![Image 3: hammer](https://emoji.discourse-cdn.com/noto/hammer.png?v=15) Projects](https://discourse.ros.org/c/projects/10)
*   [![Image 4: person_in_suit_levitating](https://emoji.discourse-cdn.com/noto/person_in_suit_levitating.png?v=15) Jobs](https://discourse.ros.org/c/jobs/15)
*   [Site Feedback](https://discourse.ros.org/c/site-feedback/3)
*   [All categories](https://discourse.ros.org/categories)

 Tags 

*   [gazebo](https://discourse.ros.org/tag/gazebo/67)
*   [infrastructure](https://discourse.ros.org/tag/infrastructure/379)
*   [open-rmf](https://discourse.ros.org/tag/open-rmf/346)
*   [ros](https://discourse.ros.org/tag/ros/118)
*   [All tags](https://discourse.ros.org/tags)

 ​ 

 ​ 

Open Robotics has a survey asking for _your_ feedback. Fill it in to enter a prize draw!

[Open Robotics](https://www.openrobotics.org/) works to support the development, distribution, and adoption of open-source software for use in robotics research, education, and product development. As an organisation and as a movement, we know a lot about the software, tools and standards that we build, but _we do not know enough about the people who use them_ in their work, in their hobbies, and in their studies.

What motivates people to use the Open Robotics Suite (ROS, ros-controls, Space ROS, Gazebo, Open-RMF, and the infrastructure that supports them), in whole or in part? What motivates companies to make their products depend on our software? What features are actually relied upon every day, and which are no longer necessary? Or, conversely, what motivates someone to _not_ use the Open Robotics Suite? To begin answering these questions, we are starting a new annual survey of everyone who is or could be using our software.

We are asking anyone and everyone who is in robotics, in any way, to answer this survey. Even if you do not use any Open Robotics software, or you think that ROS is not suitable for your work, or you’ve only just started learning Gazebo, or you tried and have abandoned ROS, we still want to hear from you. If you’ve never used ROS, Gazebo, or any of our other software, we want to hear from you!

Achieving our mission requires knowing who we are or should be building software for, no matter who they are or where they use it. This survey is how we get to know our community better.

**You can fill in the survey by following this link**: [https://go.openrobotics.org/orsurvey26](https://go.openrobotics.org/orsurvey26)

### [](https://discourse.ros.org/t/rfc-consolidating-and-modernizing-integration-test-architecture-for-gz-ros2-control/58883#p-118556-prize-draw-1)Prize draw

All survey participants will have the opportunity to enter a prize draw to win one item of their choice from the [Open Robotics Store](https://store.openrobotics.org/). At the end of the survey you will have the opportunity to enter your email address for the purposes of entering this prize draw. You must enter a valid email address to be eligible for the prize draw. **50 participants will be chosen at random** from those who enter.

### [](https://discourse.ros.org/t/rfc-consolidating-and-modernizing-integration-test-architecture-for-gz-ros2-control/58883#p-118556-deadline-2)Deadline

**The survey period ends on the 30th of November, 2026**. All _completed_ surveys received by this date will be eligible for the prize draw.

### [](https://discourse.ros.org/t/rfc-consolidating-and-modernizing-integration-test-architecture-for-gz-ros2-control/58883#p-118556-who-should-fill-in-the-survey-3)Who should fill in the survey?

_Everyone_! We want the opinions of everyone working in, studying in, and playing in robotics. We want the opinions of every individual - not just one response per company. Get your colleagues to fill it in, your team mates, your staff, your classmates. The more information we have, the better we can work to ensure that the software you depend on better meets your needs - or, if you don’t use it, gets to the point where you want to!

# [[RFC] Consolidating and Modernizing Integration Test Architecture for gz_ros2_control](https://discourse.ros.org/t/rfc-consolidating-and-modernizing-integration-test-architecture-for-gz-ros2-control/58883)

[![Image 5: ros-controls](https://us1.discourse-cdn.com/flex022/uploads/ros/original/3X/b/d/bd001b435bdafbfd264f8651019edc51e1d61413.png?v=15)ros-controls](https://discourse.ros.org/c/ros-controls/106)[![Image 6: light_bulb](https://emoji.discourse-cdn.com/noto/light_bulb.png?v=15)ros-controls Ideas](https://discourse.ros.org/c/ros-controls/ros-controls-ideas/110)

*   [ros2](https://discourse.ros.org/tag/ros2/12),
*   [gazebo](https://discourse.ros.org/tag/gazebo/67),
*   [ros_control](https://discourse.ros.org/tag/ros-control/65),
*   [testing](https://discourse.ros.org/tag/testing/434)

You have selected **0** posts.

[select all](https://discourse.ros.org/t/rfc-consolidating-and-modernizing-integration-test-architecture-for-gz-ros2-control/58883)

[cancel selecting](https://discourse.ros.org/t/rfc-consolidating-and-modernizing-integration-test-architecture-for-gz-ros2-control/58883)

[Oct 15](https://discourse.ros.org/t/rfc-consolidating-and-modernizing-integration-test-architecture-for-gz-ros2-control/58883/1 "Jump to the first post")

 1 / 1 

 Oct 15 

[4d ago](https://discourse.ros.org/t/rfc-consolidating-and-modernizing-integration-test-architecture-for-gz-ros2-control/58883/1)

## post by Vanjoseluis 4 days ago

[![Image 7](https://sea2.discourse-cdn.com/flex022/user_avatar/discourse.openrobotics.org/vanjoseluis/48/33961_2.png)](https://discourse.ros.org/u/vanjoseluis)

[Vanjoseluis](https://discourse.ros.org/u/vanjoseluis)

[4d](https://discourse.ros.org/t/rfc-consolidating-and-modernizing-integration-test-architecture-for-gz-ros2-control/58883 "Post date")

Hi everyone,

Over time, the integration test suite in `gz_ros2_control` has grown incrementally as new controllers, demos, and interfaces were introduced. While these tests prevent regressions, the lack of a explicit test architecture currently leads to duplicate simulation launches, unnecessary CI runtime, and varying coverage across ROS 2 distributions (Rolling down to Humble).

I’ve opened an RFC on GitHub ([#964](https://github.com/ros-controls/gz_ros2_control/issues/964)) to discuss and define a consolidated integration test architecture before driving a broader refactor.

### [](https://discourse.ros.org/t/rfc-consolidating-and-modernizing-integration-test-architecture-for-gz-ros2-control/58883#p-119068-key-goals-proposed-direction-1)Key Goals & Proposed Direction:

1.   **Explicit Behavioral & Requirement Coverage:** Shift from merely checking process/topic existence to validating physical feedback (joint position, velocity, effort command responses) for test mechanisms (slider, pendulum, gripper).

2.   **Simulation Lifecycle Consolidation:** Reduce redundant Gazebo/ROS 2 launches by running sequential/parallel behavioral assertions within shared simulation sessions (without sacrificing granular failure reports).

3.   **Distro Harmonization:** Unify semantics and implementation across _Rolling_, _Lyrical_, _Kilted_, _Jazzy_, and _Humble_, avoiding API lock-ins that break backports.

I’ve already validated parts of this approach in [PR [#831](https://github.com/ros-controls/gz_ros2_control/pull/831)] by redesigning the pendulum position test and introducing reusable observation utilities.

Before proceeding with follow-up PRs, I’d love to gather feedback from maintainers, contributors, and the broader ROS 2 community:

*   What specific behavioral regressions are highest priority for your workflows?

*   Are there known edge cases in `gz_ros2_control` integration testing that we should address during this refactor?

Feel free to share your thoughts here or join the discussion directly on the GitHub RFC issue: [[RFC] Define and consolidate the integration test architecture · Issue #964 · ros-controls/gz_ros2_control · GitHub](https://github.com/ros-controls/gz_ros2_control/issues/964)

Best regards,

**José Luis Pérez Martín**

  

 ​ 

 ​ 

*   [ROS News for the Week of October 12th, 2026](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-october-12th-2026/58909)

48 views 1 link 

Reply

  

### Related topics

Topic list, column headers with buttons are sortable.
| Topic | Replies | Views | Activity |
| --- | --- | --- | --- |
| [Integration testing in ROS (2)](https://discourse.ros.org/t/integration-testing-in-ros-2/6859) [Quality Assurance](https://discourse.ros.org/c/archive/quality/37) | [2](https://discourse.ros.org/t/integration-testing-in-ros-2/6859/1) | 3.1k | [Nov 2018](https://discourse.ros.org/t/integration-testing-in-ros-2/6859/3) |
| [Test Framework in ROS2](https://discourse.ros.org/t/test-framework-in-ros2/2667) [![Image 8: ros](https://us1.discourse-cdn.com/flex022/uploads/ros/original/3X/2/6/26123a37f7aac0c6c95da44564ca0d81836a8628.png?v=15)ROS General](https://discourse.ros.org/c/ros/ros-general/8) * [ros2](https://discourse.ros.org/tag/ros2/12) | [3](https://discourse.ros.org/t/test-framework-in-ros2/2667/1) | 9.1k | [Sep 2017](https://discourse.ros.org/t/test-framework-in-ros2/2667/4) |
| [Towards a ROSdoc integation testing tutorial](https://discourse.ros.org/t/towards-a-rosdoc-integation-testing-tutorial/40701) [Quality Assurance](https://discourse.ros.org/c/archive/quality/37) * [ros2](https://discourse.ros.org/tag/ros2/12), * [documentation](https://discourse.ros.org/tag/documentation/130), * [test](https://discourse.ros.org/tag/test/364), * [cmake](https://discourse.ros.org/tag/cmake/283) | [4](https://discourse.ros.org/t/towards-a-rosdoc-integation-testing-tutorial/40701/1) | 396 | [Dec 2024](https://discourse.ros.org/t/towards-a-rosdoc-integation-testing-tutorial/40701/5) |
| [Gazebo support for ros2_control breakout session](https://discourse.ros.org/t/gazebo-support-for-ros2-control-breakout-session/18468) [![Image 9: ros](https://us1.discourse-cdn.com/flex022/uploads/ros/original/3X/2/6/26123a37f7aac0c6c95da44564ca0d81836a8628.png?v=15)ROS General](https://discourse.ros.org/c/ros/ros-general/8) * [gazebo](https://discourse.ros.org/tag/gazebo/67), * [ros_control](https://discourse.ros.org/tag/ros-control/65), * [wg-ros2-control](https://discourse.ros.org/tag/wg-ros2-control/138) | [2](https://discourse.ros.org/t/gazebo-support-for-ros2-control-breakout-session/18468/1) | 996 | [Jan 2021](https://discourse.ros.org/t/gazebo-support-for-ros2-control-breakout-session/18468/3) |
| [New ROS online courses: GTest Framework for ROS2](https://discourse.ros.org/t/new-ros-online-courses-gtest-framework-for-ros2/27632) [![Image 10: graduation_cap](https://emoji.discourse-cdn.com/noto/graduation_cap.png?v=15)Training & Education](https://discourse.ros.org/c/training/58) * [ros2](https://discourse.ros.org/tag/ros2/12) | [0](https://discourse.ros.org/t/new-ros-online-courses-gtest-framework-for-ros2/27632/1) | 451 | [Oct 2022](https://discourse.ros.org/t/new-ros-online-courses-gtest-framework-for-ros2/27632/1) |
