import re
h=open('/home/hermes/ros2-weekly-digest/data/2026-08-23/discourse_jina.md').read()
# find topic links + titles
topics=re.findall(r'\[([^\]]+)\]\(https://discourse\.ros\.org/t/[^)]+\)',h)
seen=set()
print("=== TOPIC TITLES ===")
for t in topics:
    t=t.strip()
    if t and t not in seen:
        seen.add(t)
        print(t[:120])
