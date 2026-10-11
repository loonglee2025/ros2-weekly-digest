Title: knoblog: a changelog of default-parameter changes from git history (Nav2, PX4, ArduPilot), feedback wanted

URL Source: https://discourse.ros.org/t/knoblog-a-changelog-of-default-parameter-changes-from-git-history-nav2-px4-ardupilot-feedback-wanted/58763

Published Time: 2026-10-10T22:10:43+00:00

Markdown Content:
## post by fitzyracing1 19 hours ago

Hi all,

I’ve been building a small tool called knoblog, and I’d like feedback from people who actually maintain or depend on parameter files.

The problem: a default changes in a params file, the commit is called something like “update params”, and you find out when the robot behaves differently after an update. knoblog walks a repo’s git history, pulls out every parameter/gain/threshold/flag default from each commit, and writes down what changed, old → new, with the commit link.

A real example from the Nav2 demo (nav2_bringup/params/nav2_params.yaml, commit 04c6ca5, Dec 13 2023):

```
global_costmap.global_costmap.inflation_layer.inflation_radius   0.55 → 0.7   (+27.3%)
local_costmap.local_costmap.inflation_layer.inflation_radius     0.55 → 0.70  (+27.3%)
collision_monitor.FootprintApproach.time_before_collision        2.0  → 1.2   (−40%)
```

In one commit, the default robot keeps further from obstacles and its collision monitor reacts with less lead time. Neither shows up in a changelog unless someone writes it down.

Live demos (rebuilt weekly by a GitHub Action):

*   Nav2 default parameters: [Nav2 default-parameter changelog (demo)](https://fitzyracing1.github.io/knoblog/demo/nav2/) (the 100 most recent commits touching the params files)
*   PX4 controller parameters: [PX4 controller-parameter changelog (demo)](https://fitzyracing1.github.io/knoblog/demo/px4/)

What it reads today:

*   ROS 2 `ros__parameters` YAML, including multi-node files like nav2_params.yaml. Arrays are diffed per element (`max_accel[0] 2.5 → 3.0`), and `1` vs `1.0` is kept distinct because ROS 2 cares about int vs double.
*   PX4 `module.yaml` / `*_params.yaml` and legacy `PARAM_DEFINE_*`. A move from `.c` to `.yaml` is shown as a move.
*   ArduPilot `AP_GROUPINFO` tables and `GSCALAR`/`ASCALAR` defaults (the newest and least tested part).
*   Plain YAML/JSON/TOML and C/C++/Python/Rust constants.

Outputs are a static HTML site, an Atom feed, `changes.json` for your own tooling, and optional post text. It’s deterministic: values are quoted from the diff, never generated. An LLM summary is optional and off unless you configure it.

Limits, so nobody is surprised:

*   It only sees what’s committed in the repo. Your own overrides, launch-file arguments and values set at runtime aren’t covered.
*   Needs Python 3.11+, so on Humble / Ubuntu 22.04 (system Python 3.10) use the GitHub Action or a newer interpreter.
*   It’s v0.1.1 and has been tested on Nav2, PX4 and ArduPilot history, not much else yet.

Try it:

```
pip install knoblog
knoblog init --preset ros2      # writes knoblog.yml; set watch.paths to your params files
knoblog run --repo . --config knoblog.yml --out site
```

or in CI with `uses: fitzyracing1/knoblog@v0`. Source (MIT): [GitHub - fitzyracing1/knoblog: Plain-English changelogs, Atom/JSON feeds and X-ready post text for parameter, gain, threshold, flag and config changes (ROS 2, PX4, ArduPilot, C/C++, YAML/JSON/TOML). GitHub Action + CLI. · GitHub](https://github.com/fitzyracing1/knoblog)

Questions I’d really like answers to:

1.   Would a per-commit list like this be useful for your team, or do you track default changes some other way?
2.   Which parameter formats or repos should it handle next (MoveIt configs, ros2_control, Autoware)?
3.   Is “old → new + % change” the right level of detail, or would you want something else, like the related PR or the doc string?

Thanks for reading. Bug reports and “this is wrong for X” are very welcome.

Joshua
