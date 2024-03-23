#! /usr/local/bin/env python3
#! encode : -*- utf-8 -*-
# author : osada (http://ossa2019.stars.ne.jp/)
#% sitemapの生成（URL, priority, lastmod）


import os
import pathlib
import datetime
import pprint

os.chdir("/Users/osadamasashi/Desktop/ossa2019.stars.ne.jp")
# os.chdir("C:\\Users\\81806\\Desktop\\ossa2019.stars.ne.jp")
SITE_NAME = "http://ossa2019.stars.ne.jp/"
PROFILE_PATH = "programs/sitemap_profile.txt"
OUTPUT_PATH = "sitemap.xml"
top_data = ["", ""]


#### sitemap_profileの読み込み

with open(PROFILE_PATH, "r", encoding="utf8") as f:
    input_txt = f.read().split("\n")[1:]
profile = dict()
for i in input_txt:
    if(len(i) != 0) and (i[0] != "#") and (i[0] != ":"):
        bf = i.split(":")
        bf[0] = bf[0].replace(" ", "")
        bf[1] = bf[1].replace(" ", "")
        profile[bf[0]] = bf[1]
    elif(i[0] == ":"):
        top_data[0] = i[1:]


#### sitemapの生成

result = """\
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

<!--  created with Python program (made by osada http://ossa2019.stars.ne.jp)  -->"""

for p in profile.keys():
    result += f"\n<url>\n  <loc>{SITE_NAME}{p}.html</loc>\n  <priority>{profile[p]}</priority>\n  <lastmod>"
    file = pathlib.Path(p+".html")
    dt = datetime.datetime.fromtimestamp(file.stat().st_mtime)
    dt_str = dt.strftime("%Y-%m-%dT%H:%M:%S+09:00")
    if(p == "index"):
        top_data[1] = dt_str
    result += dt_str + "</lastmod>\n  </url>"

result += """
<url>
  <loc>https://ossa2019.stars.ne.jp/</loc>
  <priority>%s</priority>
  <lastmod>%s</lastmod>
</url>

</urlset>
"""%(top_data[0], top_data[1])


#### 書き込み

with open(OUTPUT_PATH, "w", encoding="utf8") as f:
    f.write(result)


#### 最後の出力

pprint.pprint(profile)
print(f"\n{OUTPUT_PATH}に書き込みました。\n")
