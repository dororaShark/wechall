import urllib.request
import webbrowser

url1 = "http://www.wechall.net/challenge/training/programming1/index.php?action=request"
url2 = "http://www.wechall.net/challenge/training/programming1/index.php?answer="

ck = "Cookie: WC=13891189-57177-MfCZesJA2jJQNb4V"
hd = {}

req1 = urllib.request.Request(url=url1,headers=hd)
req1.add_header('Cookie','WC=13891189-57177-MfCZesJA2jJQNb4V')

resp = urllib.request.urlopen(req1)
result = resp.read().decode('utf8')
print(result)

resp2 = urllib.request.urlopen(url2+result)
print(url2+result)
# print(resp2.read().decode())
webbrowser.open(url2+result)

