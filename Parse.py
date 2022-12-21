from urllib import parse

query_string = {
    'wd' : '爬虫'
}

result = parse.urlencode(query_string)
url = 'https://www.google.com/s?{}'.format(result)

print(url)

# url="http://www.baidu.com/s?wd={}"
# word=input('请输入想要的内容：')
# query_string=parse.quote(word)
# print(url.format(query_string))

string = "%E7%88%AC%E8%99%AB"
result = parse.unquote(string)
print(result)