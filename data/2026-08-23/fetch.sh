#!/bin/bash
# Fetch GitHub commits + releases for ROS2 weekly digest, window 2026-08-17..2026-08-23
source ~/.zshrc 2>/dev/null
export GITHUB_TOKEN
DIR=/home/hermes/ros2-weekly-digest/data/2026-08-23
SINCE="2026-08-17T00:00:00Z"
UNTIL="2026-08-23T23:59:59Z"
AUTH="Authorization: token ${GITHUB_TOKEN}"

# repos: "owner/repo"
CORE="ros2/rclcpp ros2/rclpy ros2/ros2cli ros2/launch ros2/rosbag2 ros2/rmw ros2/rcl ros2/rcl_interfaces ros2/rosidl ros2/ros2"
ECO="ros-navigation/navigation2 ros-controls/ros2_control moveit/moveit2 gazebosim/gz-sim eProsima/Fast-DDS micro-ROS/micro-ROS-Agent"

fetch_repo() {
  repo="$1"
  safe=$(echo "$repo" | tr '/' '_')
  curl -s -H "$AUTH" "https://api.github.com/repos/$repo/commits?since=$SINCE&until=$UNTIL&per_page=100" > "$DIR/${safe}_commits.json"
  curl -s -H "$AUTH" "https://api.github.com/repos/$repo/releases?per_page=20" > "$DIR/${safe}_releases.json"
  echo "$repo done $(wc -c < $DIR/${safe}_commits.json) $(wc -c < $DIR/${safe}_releases.json)"
}

for repo in $CORE $ECO; do
  fetch_repo "$repo"
  sleep 0.3
done
echo "ALL DONE"
