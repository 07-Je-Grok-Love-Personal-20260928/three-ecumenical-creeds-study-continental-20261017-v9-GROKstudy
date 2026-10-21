# 三大公教会信经 · 欧陆改革宗深读

**版本标签：three-ecumenical-creeds-study-continental-20261021-v12-GROKstudy**（页脚版本 v20261021-12）

使徒信经、尼西亚信经、亚他那修信经，以及三项联合信条（比利时信条、海德堡要理问答、多特信经）的中文综合学习网站（欧陆改革宗视角）。原文逐字取自 CCI《赞美手册》中文版；CCI 没有的内容用《中国改革宗教会敬拜手册》2015 版补充，逐字摘引并标页码（tools/verify_pdf.py 核对）。

## 当前版本链接（v12）
- GitHub Pages：https://07-je-grok-love-personal-20260928.github.io/three-ecumenical-creeds-study-continental-GROKstudy/
- Netlify：https://three-ecumenical-creeds-continental-20261021-v12-grokstudy.netlify.app/
- Surge：https://three-ecumenical-creeds-continental-20261021-v12-grokstudy.surge.sh/
- 仓库：https://github.com/07-Je-Grok-Love-Personal-20260928/three-ecumenical-creeds-study-continental-GROKstudy

命名：仓库名只含主题（…-GROKstudy，以后不再改名）；Netlify / Surge 域名为“主题-日期-版本-grokstudy”（v12 起后缀由 grokser 改为 grokstudy；这两处只能小写），每个版本一个新域名，旧域名继续在线。**v12 域名去掉了主题里的 study：** 完整写法 three-ecumenical-creeds-study-continental-20261021-v12-grokstudy 有 64 个字符，超过 Netlify / Surge 子域名 63 字符上限，所以用 three-ecumenical-creeds-continental-20261021-v12-grokstudy（study 已含在 grokstudy 里）。

## 发布（Releases）——随时恢复

每个上线版本都在 GitHub 打了固定标签与 Release（时间为台北时间 UTC+8）。恢复：`git checkout <标签>` 后重新部署，或在 Releases 页下载源码包。

| 标签 | 说明 | 链接 |
|---|---|---|
| `v20261021-12` | v12 当前版本（2026-10-21 台北）：记忆图标、干净背诵版、问答分色、四套主题 | https://github.com/07-Je-Grok-Love-Personal-20260928/three-ecumenical-creeds-study-continental-GROKstudy/releases/tag/v20261021-12 |
| `v20261021-0` | 更新前快照（2026-10-21 台北）：t87 改动前的线上 main（0aa6069，与 v11 线上内容一致） | https://github.com/07-Je-Grok-Love-Personal-20260928/three-ecumenical-creeds-study-continental-GROKstudy/releases/tag/v20261021-0 |
| `v20261020-11` | v11：性能、笔记标记系统、引号标注 | https://github.com/07-Je-Grok-Love-Personal-20260928/three-ecumenical-creeds-study-continental-GROKstudy/releases/tag/v20261020-11 |
| `v20261020-10` | v10：CCI 逐字、故事线、思维导图、敬拜手册 2015 补缺 | https://github.com/07-Je-Grok-Love-Personal-20260928/three-ecumenical-creeds-study-continental-GROKstudy/releases/tag/v20261020-10 |

## 版本记录

| 版本 | 更新内容 | 仍可访问的链接 |
|---|---|---|
| **v12 · v20261021-12**（当前） | 目录与正文标题前加记忆图标（52 主日、37 条、多特条目、信经各条各一图）；原文/背诵区的经文参考、原文页链接与学习提示默认折叠（干净背诵版，一键全部展开/收起）；129 问问答分色（金色 Q 条、绿色 A 条）；四套可切换主题（🌌 深夜星空 · 🌅 晨光暖白 · 🏞️ 青绿山水 · 🍇 葡萄紫韵，存在本机，首屏前应用不闪烁）；图标记忆地图、问答结构图；年份蓝色虚线标记；主题对比度检查 tools/contrast.py（WCAG AA）。 | 见上 |
| v11 · v20261020-11 | 性能：IntersectionObserver 滚动高亮、transform 进度条、目录折叠写进 HTML（CLS 约 0.1–0.26 → ≤0.06）、减少毛玻璃、长小节按需渲染、去掉全屏漂移动画；笔记标记系统（同三项联合信条站，图例可关闭）；背诵版按段着色、每行首句加粗（不改原文）；241 个未在 CCI 逐字找到的引号短语去掉引号，标为“本站译文/其他译本措辞”（44）或“本站用语”（197）；记忆页三信经词频图与标记速查表；删去讲解页的抓取/程序说明与重复列。 | 旧版本：[Netlify](https://three-ecumenical-creeds-study-continental-20261020-v11-grokser.netlify.app/) · [Surge](https://three-ecumenical-creeds-study-continental-20261020-v11-grokser.surge.sh/) |
| v10 · v20261020-10 | 用敬拜手册 2015 版补 CCI 缺的内容（主日敬拜中的信经、HC 印刷小标题），并与 CCI 逐字比对，差异列在来源页（正文仍用 CCI）；三信经与 HC、BC、Dort 各加五步动画故事线（每步带出处）与思维导图；按页面区分配色。 | 旧版本：[Netlify](https://three-ecumenical-creeds-study-continental-20261020-v10-grokser.netlify.app/) · [Surge](https://three-ecumenical-creeds-study-continental-20261020-v10-grokser.surge.sh/)（备用镜像：同一版本另有备用镜像：[Netlify](https://three-ecumenical-creeds-study-continental-20261020-v10-ccser.netlify.app/) · [Surge](https://three-ecumenical-creeds-study-continental-20261020-v10-ccser.surge.sh/)） |
| v9 · v20261017-9 | 全站字号体系；三信经页“本页一眼”与导读区块（整本圣经、圣经神学、圣约神学、改革宗读法、六角度）；辅助区块默认折叠；SVG 动画时间轴。 | 旧版本：[Netlify](https://three-ecumenical-creeds-study-continental-20261017-v9-grokstudy.netlify.app/) · [Surge](https://three-ecumenical-creeds-study-continental-20261017-v9-grokstudy.surge.sh/) |
| v8 · v20261014-8 | 各条“核心一句 · 记忆钩 · 为何重要”；核心速记总表；参考站互证；篇幅数据图、环形图与北美地图；亚他那修信经编号差异说明。 | 旧版本：[Netlify](https://three-ecumenical-creeds-study-continental-20261014.netlify.app/) · [Surge](https://three-ecumenical-creeds-study-continental-20261014.surge.sh/)（v1–v8 共用这两个域名，现显示 v8） |
| v7 · v20261014-7 | 使徒、尼西亚信经页加海德堡对应主日的紧凑经文参考行（程序核对）。 | 同上（已被覆盖） |
| v6 · v20261014-6 | 目录可拖拽调宽；背诵版一条一行；经文参考行内编号；参考站互证；数据对比。 | 同上（已被覆盖） |
| v5 · v20261014-5 | 三信经结构目录（12 条、13 节、42 点 11 组）；背诵版与工具栏；三级标题；可勾选速记表。 | 同上（已被覆盖） |
| v4 · v20261014-4 | 改为多页结构；逐字收录三信经与三项联合信条；参考网站转述；威斯敏斯特对照；三圈图、交叉引用图。 | 同上（已被覆盖） |
| v3 · v20261014-3 | 使用 CCI《赞美手册》的信经原文与信条引文。 | 同上（已被覆盖） |
| v2 · v20261014-2 | 中文分组阅读、内容扩充、动画与 SVG 图标。 | 同上（已被覆盖） |
| v1 · v20261014-1 | 首版：三大信经综合学习单页。 | 同上（已被覆盖） |

**GitHub Pages 注意：** 仓库曾多次更名（…-20261014 → …-20261017-v9-GROKstudy → …-20261020-v10-GROKstudy → 现名），旧的 Pages 地址都已失效；GitHub 只转发仓库地址，不转发 Pages。请用上面的 Pages 地址。

## 页面（13 页，共用可隐藏目录与统一编号）
| 页面 | 内容 |
|---|---|
| `index.html` | 首页：十二站学习路径、进度环（localStorage）、视觉工具总览 |
| `bible.html` 一 | 全本圣经视角：四幕救恩史、三约、三一、基督论 |
| `apostles.html` 二 | 使徒信经深读（时间线、地图、逐句、CCI《我属于》主日7–22对照等） |
| `nicene.html` 三 | 尼西亚信经深读（含与改革宗初学者译本对照） |
| `athanasian.html` 四 | 亚他那修信经深读（42点；编号与译本对照；URCNA 脚注） |
| `compare.html` 五 | 比较：异同表、三圈重叠图、分层揭示、信条交叉引用图、各教会陈述 |
| `westminster.html` 六 | 与威斯敏斯特标准的次要对照（WCF 1.10、2、8、31；WLC 9–11…；WSC 6、21…） |
| `creeds.html` 七 | 三信经全文（CCI 逐字）与诵读工具 |
| `bc.html` 八 | 比利时信条全文（37条，CCI 逐字） |
| `hc.html` 九 | 海德堡要理问答全文（129问，52主日，CCI 逐字） |
| `dort.html` 十 | 多特信经全文（63项，CCI 逐字） |
| `memory.html` 十一 | 口诀、思维导图、翻卡、自测 |
| `sources.html` 十二 | 来源与说明：逐字收录 / 转述 / CCI 上没有找到的内容 |

## 文本来源与原则
- 三信经与三项联合信条的中文正文**逐字取自**华人改革宗《赞美手册》（基督教华人网络团契，CCI，https://ccifellowship.org/books/book-of-praise），每条均附原页链接；数据在 `data/*.json`，由 `tools/gen_data.py` 从抓取页面生成，`tools/verify_exact.py` 核对页面与数据一致。
- CCI 的《我属于》、仪文、签署书、《烛台宣言》、《真理的火焰》等其他内容只做转述与短引，并注明出处。
- 其他改革宗网站（ccreformed.org、reformedbeginner.net、canrc.org、urcna.org、heritagereformed.com、prca.org、opc.org、canadianreformedseminary.ca、wts.edu、crts.edu）只转述实际读到的页面内容；PRCA 因站点验证页仅取搜索摘录。
- 不确定处标“约”。以圣经为最高权威。

## 开发
```
python3 build.py            # 生成全部 *.html（需要 Python 3）
python3 tools/check_links.py   # 站内链接/锚点/目录检查
python3 tools/verify_exact.py  # 原文一致性检查
python3 tools/verify_recite.py creeds.html   # 背诵版（一条一行）与 CCI 原文逐字一致
python3 tools/verify_refs.py   # 经文参考行内列表 == CCI 数据
python3 tools/verify_pdf.py    # 敬拜手册 2015 版摘引 == PDF 印刷正文（data/pdf/pdf2015.json，按页）
python3 tools/qa.py [--nojs] [--rm]   # Playwright 五个宽度
python3 tools/perf.py . hc.html memory.html   # 性能：TBT、CLS、长任务、滚动帧（4× CPU 降速）
python3 tools/quotefix.py /tmp/unm.txt   # 未逐字找到的引号短语分类 → data/qfix.json（构建时去引号并标注）
python3 tools/qa_toc.py hc.html --shots   # 目录拖拽/键盘/触摸/持久化
python3 tools/audit_all.py more.py   # 引文核对（需本地爬取缓存）
```
静态站，无需构建；无 JavaScript 时内容全部可见；遵守 `prefers-reduced-motion`。
