import re, html, os
h=open('/home/hermes/ros2-weekly-digest/data/2026-08-23/ros_blog.html').read()
# Find blog post entries: titles and dates
# Common structure: <a href="/blog/...">Title</a> and <time> or date text
links=re.findall(r'<a[^>]+href="([^"]*)"[^>]*>(.*?)</a>',h,re.S)
seen=set()
print("=== BLOG LINKS ===")
for href,txt in links:
    txt=re.sub('<[^>]+>','',txt).strip()
    if not txt: continue
    if 'blog' in href or 'post' in href or 'news' in href:
        if (href,txt) in seen: continue
        seen.add((href,txt))
        print(href,'|',txt[:90])
print("\n=== DATES FOUND ===")
for m in re.findall(r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+20\d\d|20\d\d-\d\d-\d\d|(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+20\d\d)',h):
    print(m)
print("\n=== TITLE/H1 ===")
for m in re.findall(r'<h[12][^>]*>(.*?)</h[12]>',h,re.S)[:40]:
    t=re.sub('<[^>]+>','',m).strip()
    if t: print(t[:90])
