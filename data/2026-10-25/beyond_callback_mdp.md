Title: Beyond Callback Scheduling: Choosing Where Computation Executes in ROS 2 with C++26 - ROS / ROS Ideas - Open Robotics Discourse

URL Source: https://discourse.openrobotics.org/t/beyond-callback-scheduling-choosing-where-computation-executes-in-ros-2-with-c-26/59021

Published Time: 2026-10-21T15:54:55+00:00

Markdown Content:
Recently, I had the opportunity to present:

**“From Callbacks to Senders: Rethinking PX4 Precision Landing with C++26 Execution.”**

The experiment led me to a question I’d love to discuss with the ROS 2 community:

**As robotic systems become more scalable and interconnected, shouldn’t we have more explicit control over where application computations execute, and which execution resources they consume?**

## [](https://discourse.openrobotics.org/t/beyond-callback-scheduling-choosing-where-computation-executes-in-ros-2-with-c-26/59021#p-119259-what-ros-2-already-provides-1)What ROS 2 already provides

ROS 2 has several execution models, including `SingleThreadedExecutor`, `MultiThreadedExecutor`, callback groups, and event-driven executors.

Looking at [`rclcpp::executors::MultiThreadedExecutor`](https://github.com/ros2/rclcpp/blob/rolling/rclcpp/src/rclcpp/executors/multi_threaded_executor.cpp), worker threads retrieve ready executable entities and invoke their callbacks.

Callback groups allow us to constrain concurrency, while multiple executors can provide greater isolation between groups of callbacks.

With a well-designed multithreaded configuration, an expensive callback doesn’t necessarily prevent unrelated callbacks from executing.

But there is a distinction I find particularly interesting:

**Controlling callback concurrency is not the same as explicitly choosing the execution resources consumed by computations initiated within those callbacks.**

When a callback performs expensive processing synchronously, that computation occupies the thread executing the callback, whether it belongs to a single-threaded, multithreaded, or event-driven executor.

ROS 2 applications can already introduce separate workers and custom scheduling. What interests me is how modern C++ can make these decisions more explicit, composable, and standardized.

## [](https://discourse.openrobotics.org/t/beyond-callback-scheduling-choosing-where-computation-executes-in-ros-2-with-c-26/59021#p-119259-my-px4-precision-landing-experiment-2)My PX4 precision-landing experiment

In my demonstration, a ROS 2 node receives ArUco marker observations, transforms the detected target into PX4’s local reference frame, and supplies the resulting target position to the precision-landing controller.

In the original implementation, target processing occurred synchronously inside the subscription callback.

For the alternative implementation, I used NVIDIA’s `stdexec`, following the C++26 `std::execution` model.

The callback captures an owned snapshot of the observation and returns quickly. A separate application-controlled scheduler executes the target-processing operation, and the node later consumes its completed result during a control update.

**What interested me most wasn’t making the computation faster. It was being able to choose where that computation executes.**

Instead of occupying a ROS executor worker for the entire processing operation, I could dispatch the computational work to a separate execution resource while keeping ROS callbacks focused on their responsibilities.

I could also decide how work is admitted, whether waiting observations are replaced, and how completed results become available to the control path.

The latest-wins policy was an application-level decision; sender/receiver abstractions provided the asynchronous execution model around it.

The presentation includes benchmark results comparing synchronous callback processing with the application-controlled approach. It is not a performance comparison against a properly configured ROS 2 `MultiThreadedExecutor`.

**The point of the experiment was execution placement, not demonstrating that one executor is faster than another.**

## [](https://discourse.openrobotics.org/t/beyond-callback-scheduling-choosing-where-computation-executes-in-ros-2-with-c-26/59021#p-119259-why-execution-placement-becomes-critical-for-scalable-robotics-and-drone-swarms-3)Why execution placement becomes critical for scalable robotics and drone swarms

Now imagine moving from one PX4 vehicle to a fleet of autonomous drones operating as a coordinated system.

ROS 2 may no longer be responsible only for communication between perception, planning, and control components on an individual vehicle.

It may also participate in a larger architecture coordinating multiple robots, processing network information, maintaining formation state, exchanging mission updates, and interacting with external systems.

This changes the importance of execution resources.

**A ROS 2 executor thread is no longer simply a worker available to process the next callback. It may be part of a communication and coordination path with significant timing requirements.**

Consider a node responsible for several operations:

*   Receiving formation-state updates from other drones.

*   Processing fleet coordination and mission-state information.

*   Handling telemetry and time-sensitive communication through ROS-integrated interfaces.

*   Performing computationally expensive perception or local planning.

*   Processing mission-level information exchanged through MAVLink gateways.

With developments such as **MAVLink-M (MAVLink Military)**, interoperability is extending beyond conventional vehicle telemetry toward standardized mission-level information, including structured observations, tracking, and coordination with external systems.

The recent [MAVLink-M Integration Hackathon](https://www.autonomyglobal.co/the-mavlink-m-integration-hackathon-why-interoperability-is-becoming-the-warfighters-competitive-advantage/) illustrates how increasingly heterogeneous autonomous systems are being integrated through shared interfaces.

Not every MAVLink message is handled by a ROS 2 executor, of course. But when these communication paths are exposed through ROS 2 nodes, services, subscriptions, or gateways, their callbacks compete for execution resources with other ROS application work.

**And this is where I believe execution placement becomes an architectural concern rather than merely a performance optimization.**

Imagine that an expensive perception operation occupies an executor worker while the system is also receiving formation updates or mission-critical messages.

A well-configured `MultiThreadedExecutor`, appropriate callback groups, or separate executors can reduce this interference. However, available worker capacity, scheduling policies, and the duration of executing callbacks still matter.

As the system scales, simply increasing the number of executor threads may not be the appropriate answer for every workload.

**Why should a computationally expensive operation consume a ROS executor thread for its entire lifetime if that computation could execute on a resource selected specifically for it?**

I would rather reserve sufficient execution capacity for communication and coordination callbacks, while dispatching expensive perception, planning, or other computational tasks to independently managed execution resources.

And importantly, those decisions must respect the hierarchy of the system’s actual timing and safety requirements. Fleet coordination is important, but it must not interfere with safety-critical vehicle control.

This is the opportunity I see in **C++26 `std::execution`**.

Senders and receivers provide a model for describing and composing asynchronous computations, while schedulers allow the execution context to become an explicit part of the design.

One operation might execute on a CPU worker pool. Another could use a specialized accelerator. Another might be scheduled through an execution resource integrated with ROS 2 itself.

Instead of tying every computational operation to the callback thread that receives its input, the application can express where that operation belongs.

Of course, `std::execution` does not automatically provide hard real-time guarantees, memory safety, or priority isolation. These depend on the scheduler implementations, synchronization, resource ownership, and system-level design.

**But it provides a standardized vocabulary for separating computational work from the execution resources responsible for running it.**

## [](https://discourse.openrobotics.org/t/beyond-callback-scheduling-choosing-where-computation-executes-in-ros-2-with-c-26/59021#p-119259-what-could-this-bring-to-rclcpp-4)What could this bring to `rclcpp`?

I’m not suggesting that `std::execution` should replace ROS 2 executors.

In fact, I see these models as complementary.

ROS 2 executors already provide the infrastructure for coordinating ROS callbacks, while `std::execution` provides a standardized model for composing asynchronous operations and associating them with schedulers.

**Could `rclcpp` eventually expose scheduler abstractions compatible with C++26 `std::execution`, while also allowing nodes to explicitly select independent execution resources?**

Some operations may naturally belong on ROS executor-managed threads. Others may benefit from dedicated computational resources, especially when protecting communication and coordination responsiveness is important.

This also opens interesting design questions about cancellation, scheduling priorities, resource ownership, operation lifetimes, and how sender operations could interact with callback groups.

And perhaps the most important question:

**As ROS 2 becomes part of increasingly complex robotic systems, how do we ensure its execution resources remain available for the work that matters most, rather than being occupied by whichever computation happens to run inside a callback?**

To me, the opportunity isn’t simply executing more things in parallel.

**It’s giving robotic applications explicit control over where computations execute, so the framework can remain responsive as the surrounding system becomes more demanding.**

I’d love to hear the perspectives of `rclcpp` contributors and ROS 2 developers on whether C++26 `std::execution` could help achieve this alongside the existing executor architecture.

* * *

**Related references:**

*   [ROS 2 MultiThreadedExecutor implementation](https://github.com/ros2/rclcpp/blob/rolling/rclcpp/src/rclcpp/executors/multi_threaded_executor.cpp)

*   [MAVLink-M Integration Hackathon](https://www.autonomyglobal.co/the-mavlink-m-integration-hackathon-why-interoperability-is-becoming-the-warfighters-competitive-advantage/)
