import json, re, html, os, glob

DIR='/home/hermes/ros2-weekly-digest/data/2026-08-23/discourse_posts'

def strip_tags(s):
    s=re.sub(r'<pre[^>]*>.*?</pre>', lambda m: '\n[CODE]'+re.sub('<[^>]+>','',m.group(0))+'[/CODE]\n', s, flags=re.S)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n\n',s)
    return s.strip()

def parse_file(path):
    raw=open(path).read()
    # jina wraps json in markdown block; extract from first { to last }
    start=raw.find('{')
    end=raw.rfind('}')
    if start==-1 or end==-1:
        return "PARSE ERR"
    data=json.loads(raw[start:end+1])
    title=data.get('title','')
    out=[f"##### TITLE: {title}", f"created: {data.get('created_at')}"]
    posts=data.get('post_stream',{}).get('posts',[])
    out.append(f"REPLIES: {len(posts)-1}")
    for p in posts:
        uname=p.get('username','?')
        created=p.get('created_at','')[:10]
        cooked=p.get('cooked','')
        txt=strip_tags(cooked)
        out.append(f"\n--- [{created}] {uname} ---")
        out.append(txt)
    return '\n'.join(out)

os.makedirs(DIR+'/text', exist_ok=True)
for f in sorted(glob.glob(DIR+'/*.json')):
    key=os.path.basename(f).replace('.json','')
    txt=parse_file(f)
    with open(DIR+'/text/'+key+'.txt','w') as fh:
        fh.write(txt)
    print(key, len(txt))
