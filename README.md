# Cermati Registration Automation

Skrip otomatisasi menggunakan **Selenium (Python)** untuk mengisi form pendaftaran di [Cermati.com](https://www.cermati.com/gabung).
---
## Purpose
Melakukan automation testing untuk positive case pada form pendaftaran pengguna Cermati.
---
## Tools & Framework
- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- Chrome WebDriver
---
## Form Field yang Diisi (Positive Case)
- Email
- Nomor Handphone
- Password & Konfirmasi Password
- Nama Depan & Belakang
- Kota Domisili (dropdown)
- Nomor KTP
- Foto KTP (upload file)
- Checkbox persetujuan
---
## Cara Menjalankan
### 1. Clone repository ini:
```bash
git clone https://github.com/USERNAME/cermati-automation.git
cd cermati-automation

### 2. Install dependencies:
pip install selenium

### 3. Pastikan kamu punya:
- chromedriver sesuai dengan versi Google Chrome kamu
- File foto_ktp.jpg di folder yang sama (dummy file untuk upload)

### 4. Jalankan script:
python automation_cermati.py


