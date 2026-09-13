#!/bin/bash
DIR=/home/hermes/ros2-weekly-digest/data/2026-08-23/discourse_posts
declare -A TOPICS=(
  [news_0817]="ros-news-for-the-week-of-august-17th-2026"
  [kilted_sync]="preparing-for-kilted-sync-2026-08-21"
  [kilted_pkgs]="new-packages-for-kilted-kaiju-2026-08-21"
  [rcl_executors]="proposal-rcl-executors-a-unified-canonical-reference-executor-package-for-all-client-libraries"
  [rosidl_buffer]="has-a-cpu-shared-memory-backend-for-rosidl-buffer-been-explored"
  [otel]="ros2-x-opentelemetry-end-to-end-telemetry-for-robotics"
  [ros2probe]="ros2probe-observe-ros-2-traffic-without-the-probe-effect-swap-ros2-rp"
  [protoros2]="announcing-protoros2-use-protobuf-in-ros2-without-compromise"
  [yerp_rosbag]="yerp-rosbag2-snapshot-can-we-capture-why-a-ros-perception-latency-spike-happened"
  [inspector]="ros-2-inspector-static-architecture-analysis-and-visualization-for-ros-2-workspaces"
  [foxglove]="foxglove-has-agents-now"
)
for key in news_0817 kilted_sync kilted_pkgs rcl_executors rosidl_buffer otel ros2probe protoros2 yerp_rosbag inspector foxglove; do
  slug="${TOPICS[$key]}"
  curl -s "https://r.jina.ai/https://discourse.ros.org/t/$slug" -o "$DIR/$key.md"
  sz=$(wc -c < "$DIR/$key.md")
  echo "$key: $sz bytes"
  sleep 3
done
echo DONE
