import re, datetime, json, sys

with open('/home/hermes/ros2-weekly-digest/ros_discourse_latest_rss.md','r') as f:
    text = f.read()

entries = []
parts = text.split('###')
for part in parts[1:]:
    lines = part.strip().split('\n')
    if not lines:
        continue
    title_line = lines[0].strip()
    m = re.match(r'\[(.*?)\]\((.*?)\)', title_line)
    if not m:
        continue
    title = m.group(1)
    url = m.group(2)
    date_str = None
    for line in lines:
        line = line.strip()
        if line.startswith(('Mon,','Tue,','Wed,','Thu,','Fri,','Sat,','Sun,')):
            date_str = line
            break
    if not date_str:
        continue
    try:
        dt = datetime.datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
    except Exception:
        continue
    start = datetime.datetime(2026,6,1, tzinfo=datetime.timezone.utc)
    end = datetime.datetime(2026,6,7,23,59,59, tzinfo=datetime.timezone.utc)
    if start <= dt <= end:
        entries.append({
            'title': title,
            'url': url,
            'date': dt.strftime('%Y-%m-%d'),
            'date_raw': date_str
        })

print(f'Total posts in date range: {len(entries)}')
for e in entries:
    print(f"- {e['date']} | {e['title']}")
    print(f"  {e['url']}")

with open('/home/hermes/ros2-weekly-digest/ros_discourse_week_2026-06-01_2026-06-07.json','w') as f:
    json.dump(entries, f, indent=2)
