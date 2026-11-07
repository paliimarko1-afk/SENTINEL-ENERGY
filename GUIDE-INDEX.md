# Піддомен, іконка бренду та швидка індексація

## 1. Піддомен
Приклад: `energy.ваш-домен.ua`.
1. Розмістіть папку на Cloudflare Pages / Netlify (Drop) — у налаштуваннях проєкту додайте Custom domain `energy.ваш-домен.ua`.
2. У DNS вашого домену створіть запис **CNAME**: `energy` → адреса проєкту (`назва.pages.dev` або `назва.netlify.app`). HTTPS-сертифікат хостинг видасть сам.
3. Локально виконайте `python set-domain.py energy.ваш-домен.ua` **до** завантаження — він підставить адресу в canonical, Open Graph, JSON-LD, sitemap і robots. Потім завантажте папку.

## 2. Іконка бренду в браузері та в Google
Усе вже в `<head>`: `favicon.ico` (16/32/48), `favicon.svg`, `favicon-48.png`, `favicon-96.png`, `icon-192.png`, `apple-touch-icon.png`, `site.webmanifest`. Google показує іконку в результатах пошуку лише після того, як сам її пересканує: це займає від кількох днів до пари тижнів, прискорити можна кроками нижче. Іконка має бути доступна без авторизації, а головна сторінка — не закрита в robots (так і є).

## 3. Прискорення індексації
1. **Google Search Console** → Додати ресурс → «Префікс URL» `https://energy.ваш-домен.ua/` → підтвердіть (HTML-тег: вставте в `<head>` `index.html`, або через DNS TXT).
2. «Sitemaps» → додайте `sitemap.xml`.
3. «Перевірка URL» → вставте головну адресу → **Запросити індексацію**.
4. **Bing Webmaster Tools**: імпортуйте сайт із Search Console, додайте sitemap.
5. **IndexNow** (Bing, Yandex): після публікації `python indexnow.py energy.ваш-домен.ua` (файл ключа `70d7c0c4e07944564e6195023f4b0e83.txt` має лежати в корені сайту — він уже в папці).
6. Поставте посилання на сайт із профілів, де ви є (Instagram, Facebook, Google Business, Telegram): зовнішні посилання сильно прискорюють сканування.
