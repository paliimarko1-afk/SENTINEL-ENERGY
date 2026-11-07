# Використання: python set-domain.py sentinel-energy.com.ua  (підставляє ваш домен в canonical, Open Graph, JSON-LD, sitemap, robots, nginx)
import sys, pathlib
dom = sys.argv[1].replace("https://", "").replace("http://", "").strip("/") if len(sys.argv) > 1 else sys.exit("Вкажіть домен")
d = pathlib.Path(__file__).parent
for n in ("index.html", "robots.txt", "sitemap.xml", "nginx.conf.example"):
    f = d / n
    if f.exists(): f.write_text(f.read_text(encoding="utf-8").replace("YOUR-DOMAIN", dom), encoding="utf-8")
print("OK:", dom)
