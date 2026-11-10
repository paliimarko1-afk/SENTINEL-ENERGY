# Sentinel Energy — сайт

Статичний сайт без збірки й залежностей: завантажте папку на будь-який хостинг (Netlify, Cloudflare Pages, GitHub Pages, Apache, nginx) або відкрийте `index.html` двічі клікнувши.

## Швидкий старт
1. `python set-domain.py ваш-домен.ua` — підставить домен у canonical, Open Graph, `sitemap.xml`, `robots.txt`.
2. Заявки: клієнт надсилає конфігурацію листом зі своєї пошти (Gmail/mailto), готовий лист формується на сайті — див. `GUIDE-FORM.md`. Адреса — `<meta name="form-email">`.
3. Завантажте всю папку на хостинг. Файл `_headers` (Netlify / Cloudflare Pages) або `.htaccess` (Apache) підключить заголовки безпеки; для nginx див. `nginx.conf.example`. GitHub Pages заголовки не підтримує, але CSP вже є в `index.html`.

## Контакти на сайті
Телефон +380 93 941 01 89 і пошта sentinelenerdzi@gmail.com: кнопки «Зв’язатись», «Подзвонити» (tel:), «Написати на Gmail» (mailto:) і є в шапці, у розділі «Контакти», під формою конфігуратора та у вікні після успішної відправки. Міняйте номер і пошту в `index.html` (шукайте `380939410189` і `sentinelenerdzi@gmail.com`) і в JSON-LD.

## Індексація
- Весь контент (текст, таблиця характеристик) є в HTML без JS. Вже додано: title, description, canonical, Open Graph / Twitter-картка (`og-image.png`). Структурованих даних Schema.org (Product/Offer) на сайті немає свідомо: це інформаційний лендінг, а не магазин. `robots.txt`, `sitemap.xml`, `site.webmanifest`, іконки, `404.html` (noindex).
- Після публікації: додайте сайт у Google Search Console і Bing Webmaster Tools, підтвердіть домен і надішліть `https://ваш-домен/sitemap.xml`.

## Піддомен, іконка, індексація
Див. `GUIDE-INDEX.md`.

## Структура
`index.html` · `404.html` · `robots.txt` · `sitemap.xml` · `site.webmanifest` · `favicon.ico` · `apple-touch-icon.png` · `icon-192.png` · `icon-512.png` · `favicon-48.png` · `favicon-96.png` · `favicon.svg` · `og-image.png` · `indexnow.py` · `<ключ>.txt` · `assets/` (логотип, символ, Сенті) · `_headers` · `.htaccess` · `nginx.conf.example` · `set-domain.py`

## Захист
Без сторонніх скриптів; CSP дозволяє лише власний `app.js` (`script-src 'self'`) і Google Fonts — тож редагувати `index.html` чи `app.js` можна вільно, нічого перераховувати не треба. Ніяких мережевих запитів форма не робить (`connect-src 'none'`).
