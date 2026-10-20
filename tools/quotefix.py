"""v11：把站内“未在 CCI/参考站/手册中逐字找到”的引号短语分三类，写入 data/qfix.json：
  cci = 与 CCI 原文近似（≥90），替换为 CCI 逐字原文（仍保留引号）；
  tr  = 外文或其他译本的本站翻译/转述 → 去引号，标“本站译文”；
  own = 本站自拟用语、标签 → 去引号，标“本站用语”。
用法：python3 tools/audit_all.py *.html | grep ' | ' > /tmp/unm.txt; python3 tools/quotefix.py /tmp/unm.txt"""
import re,json,sys
from rapidfuzz import fuzz
src=[]
c=json.load(open('data/creeds.json',encoding='utf-8'))
for k in ('apostles','nicene','athanasian'): src+=c[k]['paras']
for f,key in (('bc','articles'),):
    for a in json.load(open('data/bc.json',encoding='utf-8'))['articles']: src+=[b['x'] for b in a['blocks'] if b['t'] in('p','h4')]
for l in json.load(open('data/hc.json',encoding='utf-8'))['lds']: src+=[b['x'] for b in l['blocks'] if b['t'] in('p','h4')]
for h in json.load(open('data/dort.json',encoding='utf-8'))['heads']:
    for i in h['items']: src+=[b['x'] for b in i['blocks'] if b['t'] in('p','h4')]
src=[re.sub(r'⟦\d+⟧','',s) for s in src]
P=r'[\s，。；：、！？“”‘’（）()…—·,.;:]'
def norm(s): return re.sub(P,'',s)
qs=[]
for line in open(sys.argv[1],encoding='utf-8'):
    q=line.split(' | ',1)[1].rstrip('\n')
    if q not in qs: qs.append(q)
out={}
for q in qs:
    nq=norm(q); best=(0,None)
    if len(nq)>=6 and '…' not in q and not re.search(r'[A-Za-z]',q):
        for s in src:
            if len(s)<len(nq)*0.8: continue
            al=fuzz.partial_ratio_alignment(nq,norm(s))
            if al and al.score>best[0]: best=(al.score,s,al)
    if best[0]>=90:
        s=best[1]; al=best[2]; ns=norm(s)
        # 把规范化下标映射回原文
        idx=[i for i,ch in enumerate(s) if not re.match(P,ch)]
        a=idx[al.dest_start]; b=idx[al.dest_end-1]+1
        out[q]={'act':'cci','to':s[a:b],'score':round(best[0],1)}
    elif re.search(r'[A-Za-z]',q) or best[0]>=70: out[q]={'act':'tr','score':round(best[0],1)}
    else: out[q]={'act':'own','score':round(best[0],1)}
json.dump(out,open('data/qfix.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
from collections import Counter; print(Counter(v['act'] for v in out.values()))
