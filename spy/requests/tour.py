import http.client

conn = http.client.HTTPSConnection("api.github.com")

headers = {
    'cache-control': "no-cache",
    'postman-token': "09386baa-7088-1caa-029f-009364cf7e73",
    'User-Agent': 'xxx'
    }

conn.request("GET", "/events", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
