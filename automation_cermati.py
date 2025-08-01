from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

# Ganti ini dengan lokasi file foto KTP kamu (wajib absolute path)
KTP_IMAGE_PATH = os.path.abspath("foto_ktp.jpg")  # pastikan file ini ada

# Setup WebDriver (Chrome)
driver = webdriver.Chrome()  # Pastikan chromedriver sudah di-install
driver.maximize_window()
driver.get("https://www.cermati.com/gabung")

# Isi form pendaftaran
driver.find_element(By.ID, "email").send_keys("tester.cermati@example.com")
driver.find_element(By.ID, "mobilePhone").send_keys("081234567891")
driver.find_element(By.ID, "password").send_keys("Password123!")
driver.find_element(By.ID, "confirmPassword").send_keys("Password123!")
driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Doe")
driver.find_element(By.ID, "idNumber").send_keys("1234567890123456")

# Pilih kota domisili dari dropdown
Select(driver.find_element(By.ID, "cityAndProvince")).select_by_visible_text("KOTA JAKARTA SELATAN")

# Upload foto KTP
driver.find_element(By.ID, "fileKtp").send_keys(KTP_IMAGE_PATH)

# Centang checkbox "Saya menyetujui"
checkbox = driver.find_element(By.XPATH, "//label[@for='agree']")
if not checkbox.is_selected():
    checkbox.click()

# Klik tombol "Daftar"
driver.find_element(By.XPATH, "//button[contains(text(), 'Daftar')]").click()

# Tunggu beberapa detik untuk melihat hasil
time.sleep(5)

# Tutup browser
driver.quit()
