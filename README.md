# sinergiunesa.or.id

Website resmi Sinergiunesa - Siap untuk hosting online dan dapat diakses melalui Google.

## 📋 Deskripsi

Website ini dibuat untuk organisasi Sinergiunesa dan siap untuk di-hosting secara online dengan domain sinergiunesa.or.id.

## 🚀 Cara Deploy ke Hosting Online

### Opsi 1: GitHub Pages (Gratis)

1. Buka repository di GitHub
2. Pergi ke **Settings** > **Pages**
3. Di bagian **Source**, pilih branch `main` atau `master`
4. Klik **Save**
5. Website akan tersedia di `https://yogaariganggoro.github.io/sinergiunesa.or.id/`
6. Untuk custom domain:
   - Di **Settings** > **Pages** > **Custom domain**, masukkan `sinergiunesa.or.id`
   - Tambahkan DNS record di registrar domain Anda:
     - Type: `A` atau `CNAME`
     - Name: `@` atau `www`
     - Value: Lihat dokumentasi GitHub Pages untuk IP address terbaru

### Opsi 2: Netlify (Gratis)

1. Buka [https://netlify.com](https://netlify.com)
2. Klik **Add new site** > **Import an existing project**
3. Hubungkan dengan GitHub dan pilih repository ini
4. Deploy settings:
   - Build command: (kosongkan)
   - Publish directory: `/`
5. Klik **Deploy site**
6. Untuk custom domain:
   - Pergi ke **Domain settings**
   - Klik **Add custom domain**
   - Masukkan `sinergiunesa.or.id`
   - Ikuti instruksi untuk setup DNS

### Opsi 3: Vercel (Gratis)

1. Buka [https://vercel.com](https://vercel.com)
2. Klik **Add New** > **Project**
3. Import repository dari GitHub
4. Klik **Deploy**
5. Untuk custom domain:
   - Pergi ke **Settings** > **Domains**
   - Tambahkan `sinergiunesa.or.id`
   - Update DNS record di registrar domain

### Opsi 4: Hosting Tradisional (cPanel, dll)

1. Download atau clone repository ini
2. Upload semua file ke folder `public_html` atau `www` di hosting
3. Pastikan file `index.html` berada di root directory
4. Website akan otomatis tersedia di domain yang sudah dikonfigurasi

## 📁 Struktur File

```
sinergiunesa.or.id/
├── index.html          # Halaman utama website
├── style.css           # File styling CSS
├── robots.txt          # File untuk SEO dan crawler Google
├── sitemap.xml         # Sitemap untuk indexing Google
├── CNAME               # File untuk custom domain
├── vercel.json         # Konfigurasi untuk Vercel
├── _redirects          # Konfigurasi untuk Netlify
└── README.md           # Dokumentasi
```

## 🔍 SEO & Google Indexing

Website ini sudah dilengkapi dengan:

- ✅ **robots.txt** - Mengizinkan semua search engine untuk crawl website
- ✅ **sitemap.xml** - Memudahkan Google untuk index semua halaman
- ✅ **Meta tags** - Description, keywords, dan author untuk SEO
- ✅ **Semantic HTML** - Struktur HTML yang baik untuk SEO
- ✅ **Responsive design** - Mobile-friendly (penting untuk ranking Google)

### Cara Submit ke Google

1. Buka [Google Search Console](https://search.google.com/search-console)
2. Tambahkan property baru dengan domain `sinergiunesa.or.id`
3. Verifikasi kepemilikan domain
4. Submit sitemap: `https://sinergiunesa.or.id/sitemap.xml`
5. Minta Google untuk index: klik **URL Inspection** dan masukkan URL website

## 🛠️ Pengembangan Lokal

Untuk melihat website di komputer lokal:

1. Clone repository:
   ```bash
   git clone https://github.com/YogaAriAnggoro/sinergiunesa.or.id.git
   cd sinergiunesa.or.id
   ```

2. Buka file `index.html` di browser, atau gunakan live server:
   ```bash
   # Dengan Python
   python -m http.server 8000
   
   # Dengan Node.js (install http-server dulu)
   npx http-server
   ```

3. Buka browser dan akses `http://localhost:8000`

## 📝 Kustomisasi

- Edit `index.html` untuk mengubah konten website
- Edit `style.css` untuk mengubah tampilan dan warna
- Tambahkan gambar di folder baru (misal: `images/`)
- Update `sitemap.xml` jika menambah halaman baru

## 📞 Support

Jika ada pertanyaan atau butuh bantuan, silakan buat issue di repository ini.

## 📄 License

© 2026 Sinergiunesa. All rights reserved.
