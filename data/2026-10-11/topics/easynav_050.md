Title: EasyNav 0.5.0 released for Humble, Jazzy, Kilted and Lyrical - Projects - Open Robotics Discourse

URL Source: https://discourse.ros.org/t/easynav-0-5-0-released-for-humble-jazzy-kilted-and-lyrical/58721

Published Time: 2026-10-09T08:15:43+00:00

Markdown Content:
## post by fmrico 2 days ago

![Image 1: EasyNav robots](https://us1.discourse-cdn.com/flex022/uploads/ros/original/3X/6/e/6eb2f7eaa5b41bc0fb4b1f37ec0f3d2c34d14b38.jpeg)

Hi everyone!

We are happy to announce **EasyNav 0.5.0**, a new release of EasyNavigation, the open-source navigation system for ROS 2 developed at the [Intelligent Robotics Lab](https://intelligentroboticslab.gsyc.urjc.es/)

The same version is available for **Humble, Jazzy, Kilted and Lyrical**, and you can install it in two ways:

*   **APT**: the packages are already in the ROS 2 buildfarm and will be installable after the **next sync**.

*   **Pixi**: available **now**, also for Rolling. It needs no ROS 2 installed on the system: the environment brings its own.

## [](https://discourse.ros.org/t/easynav-0-5-0-released-for-humble-jazzy-kilted-and-lyrical/58721#p-118873-why-easynav-1)**Why EasyNav?**

*   ![Image 2: :world_map:](https://emoji.discourse-cdn.com/noto/world_map.png?v=15)**The map your environment needs**: 2D maps for indoor floors, 3D surfaces for ramps and uneven terrain, voxel maps, or a combination of them.

*   ![Image 3: :high_voltage:](https://emoji.discourse-cdn.com/noto/high_voltage.png?v=15)**Fast and predictable**: a real-time control cycle, with little latency between what the robot senses and how it moves.

*   ![Image 4: :puzzle_piece:](https://emoji.discourse-cdn.com/noto/puzzle_piece.png?v=15)**Configure it, don’t code it**: choose localization, planning and control for your robot in a parameter file.

*   ![Image 5: :rocket:](https://emoji.discourse-cdn.com/noto/rocket.png?v=15)**Simple to deploy**: one process and one parameter file.

*   ![Image 6: :test_tube:](https://emoji.discourse-cdn.com/noto/test_tube.png?v=15)**Try it first in simulation**, with ready-to-run PlayGrounds.

*   ![Image 7: :shield:](https://emoji.discourse-cdn.com/noto/shield.png?v=15)**Ready for industrial deployment**: it works alongside your certified safety system (safety PLC, safety laser scanner) and never stands in its way, with a safety mode that validates and freezes the configuration, enforces velocity limits and monitors the real-time cycle and a heartbeat. When something fails (localization, a sensor, a stuck robot), its recovery system detects it and reacts, even adjusting the navigation while it runs.

*   ![Image 8: :bullseye:](https://emoji.discourse-cdn.com/noto/bullseye.png?v=15)**For every user**: hobbyists who want a robot navigating in minutes, research labs that experiment with new methods, and integrators who need predictable, safe behavior on real robots.

Coming from Nav2? `easynav_nav2_bridge` lets your existing Nav2 clients send goals to EasyNav unchanged, and the [migration guide](https://easynavigation.github.io/0.5.0/migration_guide/index.html) walks you through trying EasyNav on your robot.

## [](https://discourse.ros.org/t/easynav-0-5-0-released-for-humble-jazzy-kilted-and-lyrical/58721#p-118873-four-playgrounds-ready-to-use-2)**Four PlayGrounds, ready to use**

0.5.0 comes with **four PlayGrounds**: complete Gazebo simulations with a robot, its worlds, maps and EasyNav configurations, installed as packages:

*   **Kobuki (TurtleBot 2)** in a small house.

*   **Robotnik Summit XL** outdoors in an excavation and indoors in a warehouse.

*   **PAL Robotics TIAGo** in a small house.

*   **Omnidirectional robots** (three to six wheels) in two mazes.

[![Image 9: robots](https://us1.discourse-cdn.com/flex022/uploads/ros/optimized/3X/c/3/c35dca0453f437ef5a9675a6ebb0f7c487a36f57_2_690x295.jpeg)](https://us1.discourse-cdn.com/flex022/uploads/ros/original/3X/c/3/c35dca0453f437ef5a9675a6ebb0f7c487a36f57.jpeg "robots")

Two commands and the Kobuki is navigating:

```
sudo apt install ros-<distro>-easynav-playground-kobuki

ros2 launch easynav_playground_kobuki easynav_costmap_rpp.launch.yaml
```

(The PlayGrounds are available on Jazzy, Kilted and Lyrical.)

## [](https://discourse.ros.org/t/easynav-0-5-0-released-for-humble-jazzy-kilted-and-lyrical/58721#p-118873-get-started-3)**Get started**

*   ![Image 10: :books:](https://emoji.discourse-cdn.com/noto/books.png?v=15) Documentation, installation (APT and Pixi) and tutorials: **[https://easynavigation.github.io](https://easynavigation.github.io/)**

*   ![Image 11: :laptop:](https://emoji.discourse-cdn.com/noto/laptop.png?v=15) Source code and issues: **[EasyNavigation · GitHub](https://github.com/EasyNavigation)**

## [](https://discourse.ros.org/t/easynav-0-5-0-released-for-humble-jazzy-kilted-and-lyrical/58721#p-118873-get-a-sticker-4)**Get a sticker! ![Image 12: :robot:](https://emoji.discourse-cdn.com/noto/robot.png?v=15)**

[![Image 13: pegatinas](https://us1.discourse-cdn.com/flex022/uploads/ros/optimized/3X/9/c/9c9c85aca5e10cb622c3ee8b57c52bc1be6ba8f4_2_333x250.jpeg)](https://us1.discourse-cdn.com/flex022/uploads/ros/original/3X/9/c/9c9c85aca5e10cb622c3ee8b57c52bc1be6ba8f4.jpeg "pegatinas")

Are you running EasyNav on your robot? **Share a video of it in this thread** and we will send you a _powered by EasyNav_ sticker to put on it.

Questions, feedback and contributions are very welcome. Happy navigating!
