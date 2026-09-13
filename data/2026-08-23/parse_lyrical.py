import json, re, html, os
def strip(s):
    s=re.sub(r'<[^>]+>',' ',s); return re.sub(r'\s+',' ',html.unescape(s)).strip()
f='/home/hermes/ros2-weekly-digest/data/2026-08-23/discourse_posts/lyrical_sync.json'
raw=open(f).read()
s=raw.find('{'); e=raw.rfind('}')
d=json.loads(raw[s:e+1])
print('TITLE:',d.get('title'))
print('CREATED:',d.get('created_at'))
posts=d.get('post_stream',{}).get('posts',[])
print('POSTS:',len(posts))
for p in posts[:4]:
    print('---',p.get('username'),p.get('created_at','')[:10])
    print(strip(p.get('cooked',''))[:1000])
    print()
