import logging
import random
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Konfigurasi Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Konfigurasi UiAutomatorOptions
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "HapeTesting"
options.app = "C:\\Users\\akmal\\Downloads\\SiprusEdu SIT Debug v0.24.49 (1).apk"

# Connect ke Server Appium
try:
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", options=options)

    # Tunggu Sampai Bisa Berinteraksi Dengan Elemen
    wait = WebDriverWait(driver, 20)

    # Landing Page
    kliklanjut1 = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
    kliklanjut1.click()
    time.sleep(3)

    kliklanjut2 = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
    kliklanjut2.click()
    time.sleep(3)

    kliklanjut3 = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
    kliklanjut3.click()
    time.sleep(3)

    # Pilih Sekolah
    Pilih_sekolah = wait.until(EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
    Pilih_sekolah.click()
    time.sleep(3)

    # Temukan elemen menggunakan UiSelector
    value_sekolah = wait.until(lambda d: d.find_element(
        By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
    ))
    value_sekolah.click()
    time.sleep(3)

    # Klik Lanjut
    tombol_lanjut = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
    tombol_lanjut.click()
    time.sleep(3)

    # Klik Kolom Email
    field_email = wait.until(EC.presence_of_element_located((By.XPATH,
        "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
    field_email.click()
    os.system('adb shell input text "akmalalhaqi123@gmail.com"')
    time.sleep(3)

    # Klik Kolom Password
    field_password = wait.until(EC.presence_of_element_located((By.XPATH,
        "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
    field_password.click()
    os.system('adb shell input text "Test12345"')
    time.sleep(3)

    # Klik Tombol Login
    login = wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='Masuk']")))
    login.click()
    time.sleep(10)

    # Akses Tagihan
    tagihan = wait.until(EC.presence_of_element_located((By.XPATH,"(//android.widget.ImageView[@content-desc='Tagihan'])[2]")))
    tagihan.click()
    time.sleep(5)

    # Akses Bayar Sumbangan
    try:
        time.sleep(2)
        sumbangan = wait.until(lambda d: d.find_element(By.ACCESSIBILITY_ID, "Sumbangan\nTab 2 dari 3"))
        logging.info("Elemen 'Sumbangan' ditemukan")
        sumbangan.click()
        logging.info("Klik 'Sumbangan' berhasil")

        # Randomize Bayar Sumbangan
        nama_sumbangan = [
            "(//android.widget.Button[@content-desc='Bayar'])[1]",  # Sumbangan Buku
            "(//android.widget.Button[@content-desc='Bayar'])[2]",  # Sumbangan Fasilitas
            "(//android.widget.Button[@content-desc='Bayar'])[3]",  # Sumbangan Seragam
            "(//android.widget.Button[@content-desc='Bayar'])[4]",  # Alat Musik
            "(//android.widget.Button[@content-desc='Bayar'])[5]",  # Bencana Alam
            "(//android.widget.Button[@content-desc='Bayar'])[6]",  # Teknologi Digital
            "(//android.widget.Button[@content-desc='Bayar'])[7]",  # Bencana Alam (2)
            "(//android.widget.Button[@content-desc='Bayar'])[8]",  # Orang Meninggal
            "(//android.widget.Button[@content-desc='Bayar'])[9]",  # Baru New
            "(//android.widget.Button[@content-desc='Bayar'])[10]"  # Baru
        ]

        # Pilih salah satu elemen secara acak
        selected_sumbangan = random.choice(nama_sumbangan)

        # Klik elemen yang dipilih secara acak
        elemen_sumbangan = wait.until(EC.presence_of_element_located((By.XPATH, selected_sumbangan)))
        elemen_sumbangan.click()
        time.sleep(3)

        # Pop-up Sumbangan
        field_nominal = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText")))
        field_nominal.click()
        time.sleep(4)

        # Menghasilkan Angka Acak antara 10.000 dan 10 juta
        nominal = random.randint(10000, 10000000)
        logging.info(f"Nominal acak yang dihasilkan: {nominal}")

        # Memasukkan Angka Acak ke dalam Field Nominal
        os.system(f'adb shell input text "{nominal}"')
        logging.info(f"Nominal {nominal} telah dimasukkan ke dalam field")
        time.sleep(4)

        # Lanjutkan Bayar Sumbangan
        logging.info("Mencoba untuk klik 'Lanjutkan'")
        bayar_sumbangan = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Lanjutkan")'))
        bayar_sumbangan.click()
        logging.info("Klik 'Lanjutkan' berhasil")
        time.sleep(5)

    except Exception as e:
        logging.error(f"Error dalam eksekusi skrip: {e}")

    # Pilih Random Metode Pembayaran
    selector_bank = [
        "new UiSelector().className(\"android.widget.RadioButton\").instance(1)",
        "new UiSelector().className(\"android.widget.RadioButton\").instance(2)",
        "new UiSelector().className(\"android.widget.RadioButton\").instance(3)",
        "new UiSelector().className(\"android.widget.RadioButton\").instance(4)",
        "new UiSelector().className(\"android.widget.RadioButton\").instance(5)",
        "new UiSelector().className(\"android.widget.RadioButton\").instance(6)"
    ]

    selected_bank_selector = random.choice(selector_bank)
    bank_element = driver.find_element(By.ANDROID_UIAUTOMATOR, selected_bank_selector)
    bank_element.click()
    time.sleep(2)

    # Klik Bayar
    bayar_tagihan = wait.until(
        lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Bayar")'))
    bayar_tagihan.click()
    time.sleep(5)

finally:
    # Jangan lupa untuk menutup sesi pengujian jika driver terdefinisi
    if 'driver' in locals():
        driver.quit()
        logging.info("Sesi pengujian ditutup")
