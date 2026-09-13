import re
h=open('/home/hermes/ros2-weekly-digest/data/2026-08-23/discourse_jina.md').read()
# extract all discourse topic links with their titles
pairs=re.findall(r'\[([^\]]+)\]\((https://discourse\.ros\.org/t/[^)]+)\)',h)
seen=set()
for t,u in pairs:
    t=t.strip()
    if not t or t in seen: continue
    # only include topics (not profile links etc)
    if '/t/' in u:
        seen.add(t)
        print(u.split('/t/')[1].split('/')[0], '|', t[:80])
