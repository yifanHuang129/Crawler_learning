import re

html = """
<div><p>www.biancheng.net</p></div>
<div><p>编程帮</p></div>
"""

pattern = re.compile("<div><p>.*</p></div>", re.S)
re_list = pattern.findall(html)

print(re_list)

pattern = re.compile("<div><p>.*?</p></div>", re.S)
re_list = pattern.findall(html)

print(re_list)


website="编程帮 www.biancheng.net"

pattern = re.compile('\w+\s+\w+\.\w+\.\w+')
re_list = pattern.findall(website)
print(re_list)

pattern = re.compile('\w+\.\w+\.\w+')
re_list = pattern.findall(website)
print(re_list)

pattern = re.compile('\w+\s(\w+\.\w+\.\w+)')
re_list = pattern.findall(website)
print(re_list)

pattern = re.compile('(\w+)\s(\w+\.\w+\.\w+)')
re_list = pattern.findall(website)
print(re_list)

html="""
<div class="movie-item-info">
<p class="name">
<a class="title" title="你好，李焕英">你好，李焕英</a>
</p>
<p class="star">
主演：贾玲,张小斐,沈腾
</p>    
</div>
<div class="movie-item-info">
<p class="name">
<a class="title" title="刺杀，小说家">刺杀，小说家</a>
</p>
<p class="star">
主演：雷佳音,杨幂,董子健,于和伟
</p>    
</div> 
"""

pattern = re.compile('<div.*?<a class="title".*?>(.*?)</a>.*?star">\n主演：(.*?)\n</p.*?div>',re.S)
re_list = pattern.findall(html)
print(re_list)

if re_list:
    for element in re_list:
        print("name: ", element[0])
        print("starring: ", element[1])

html = """
<div class="movie-item-info">
        <p class="name"><a href="/films/1200486" title="我不是药神" data-act="boarditem-click" data-val="{movieId:1200486}">我不是药神</a></p>
        <p class="star">
                主演：徐峥,周一围,王传君
        </p>
<p class="releasetime">上映时间:2018-07-05</p>    </div>
"""


pattern = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
re_list = pattern.findall(html)
print(re_list)

for r in re_list:
    name = r[0].strip()
    star = r[1].strip()[3:]
        # 上映时间：2018-07-05
        # 切片截取时间
    time = r[2].strip()[5:15]
    print("name: ", name)
    print("star: ", star)
    print("time", time)