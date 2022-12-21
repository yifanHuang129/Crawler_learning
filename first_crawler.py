# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response)


from urllib import request

response = request.urlopen('http://www.baidu.com')
print(response)

html = response.read().decode('utf-8')
print(html)