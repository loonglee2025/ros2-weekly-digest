#!/usr/bin/env python3
import json, glob, os, re
from datetime import datetime, timezone

DIR="/home/hermes/ros2-weekly-digest/data/2026-08-23"
SINCE=datetime(2026,8,17,tzinfo=timezone.utc)
UNTIL=datetime(2026,8,23,23,59,59,tzinfo=timezone.utc)

def parse_dt(s):
    try:
        return datetime.fromisoformat(s.replace("Z","+00:00"))
    except Exception:
        return None

print("="*70)
print("COMMITS IN WINDOW (2026-08-17 .. 2026-08-23)")
print("="*70)
for f in sorted(glob.glob(f"{DIR}/*_commits.json")):
    repo=os.path.basename(f).replace("_commits.json","").replace("_","/")
    try:
        data=json.load(open(f))
    except Exception as e:
        print(f"{repo}: PARSE ERR {e}"); continue
    if not isinstance(data,list) or len(data)==0:
        print(f"\n### {repo}: no commits in window"); continue
    print(f"\n### {repo} ({len(data)} commits)")
    for c in data:
        sha=c.get("sha","")[:8]
        msg=c.get("commit",{}).get("message","").split("\n")[0]
        date=parse_dt(c.get("commit",{}).get("committer",{}).get("date",""))
        ds=date.strftime("%m-%d") if date else "??"
        author=c.get("commit",{}).get("author",{}).get("name","?")
        print(f"  [{ds}] {msg}  ({author})")

print()
print("="*70)
print("RELEASES (published this window or recent)")
print("="*70)
for f in sorted(glob.glob(f"{DIR}/*_releases.json")):
    repo=os.path.basename(f).replace("_releases.json","").replace("_","/")
    try:
        data=json.load(open(f))
    except Exception as e:
        print(f"{repo}: PARSE ERR {e}"); continue
    if not isinstance(data,list) or len(data)==0:
        print(f"\n### {repo}: no releases"); continue
    for r in data[:8]:
        tag=r.get("tag_name","")
        name=r.get("name","") or ""
        pub=r.get("published_at","")
        pdate=parse_dt(pub)
        inwin = pdate and SINCE <= pdate <= UNTIL
        mark=" <<<IN WINDOW" if inwin else ""
        print(f"  {repo} {tag} | {name} | {pub}{mark}")
