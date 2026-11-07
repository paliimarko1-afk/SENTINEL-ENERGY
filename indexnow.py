# Прискорює індексацію в Bing/Yandex (IndexNow). Запуск ПІСЛЯ публікації сайту: python indexnow.py ваш-піддомен.example.com
import sys, json, urllib.request
host = sys.argv[1].replace("https://", "").strip("/") if len(sys.argv) > 1 else sys.exit("Вкажіть домен")
KEY = "70d7c0c4e07944564e6195023f4b0e83"
body = json.dumps({"host": host, "key": KEY, "keyLocation": f"https://{host}/{KEY}.txt", "urlList": [f"https://{host}/"]}).encode()
r = urllib.request.urlopen(urllib.request.Request("https://api.indexnow.org/indexnow", body, {"Content-Type": "application/json; charset=utf-8"}))
print("IndexNow:", r.status)
