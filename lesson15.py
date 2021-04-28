import requests

r = requests.get("https://httpbin.org/get")

r2 = requests.post("https://httpbin.org/post", data={'key': "value"})

r3 = requests.patch("https://httpbin.org/patch", data={'key': "value141"})

r4 = requests.put("https://httpbin.org/put", data={'key': "value141124"})

r5 = requests.delete("https://httpbin.org/delete")

r6 = requests.head("https://httpbin.org/head", data={'key': "value14112784"})

r7 = requests.option("https://httpbin.org/option")

r = requests.get("https://httpbin.org/get", params={'k1': 'v1', 'k2': 'v2'})
r = requests.get("https://httpbin.org/get", params={'k1': 'v1', 'k2': ['v2', 'v3']})
r10 = requests.get("https://api.github.com/events")

print(r10.text)


print(r10.url)

print(r10.encoding)

r10.encoding = 'ISO-8859-1'
print(r10.encoding)