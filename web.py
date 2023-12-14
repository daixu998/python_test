import urllib.request

url = "https://movie.douban.com/top250"

header = {
    "User-Agent""Mozilla/5.0 (Windows NT 10.0; WOW64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/76.0.3809.87 Safari/537.36 SLBrowser/6.0.1.8131"
}

req = urllib.request.Request(url=url,headers=header)

response = urllib.request.urlopen(req)

html = response.read().decode("utf-8")
print(html)