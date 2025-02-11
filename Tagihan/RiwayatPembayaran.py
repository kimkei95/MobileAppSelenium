import random
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import logging

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
    logging.info("Terhubung ke server Appium")

    # Tunggu Sampai Bisa Berinteraksi Dengan Elemen
    wait = WebDriverWait(driver, 20)

    # Landing Page
    kliklanjut1 = wait.until(
        EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
    logging.info("Elemen pertama 'Lanjut' ditemukan")
    kliklanjut1.click()
    logging.info("Klik 'Lanjut' pertama berhasil")
    time.sleep(3)

    kliklanjut2 = wait.until(
        EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
    logging.info("Elemen kedua 'Lanjut' ditemukan")
    kliklanjut2.click()
    logging.info("Klik 'Lanjut' kedua berhasil")
    time.sleep(3)

    kliklanjut3 = wait.until(
        EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
    logging.info("Elemen ketiga 'Lanjut' ditemukan")
    kliklanjut3.click()
    logging.info("Klik 'Lanjut' ketiga berhasil")
    time.sleep(3)

    # Pilih Sekolah
    Pilih_sekolah = wait.until(
        EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
    logging.info("Elemen 'Pilih sekolah' ditemukan")
    Pilih_sekolah.click()
    logging.info("Klik 'Pilih sekolah' berhasil")
    time.sleep(3)

    # Temukan elemen menggunakan UiSelector
    value_sekolah = wait.until(lambda d: d.find_element(
        By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
    ))
    logging.info("Elemen sekolah 'PT Aigen Global Teknologi' ditemukan")
    value_sekolah.click()
    logging.info("Klik sekolah 'PT Aigen Global Teknologi' berhasil")
    time.sleep(3)

    # Klik Lanjut
    tombol_lanjut = wait.until(
        EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
    logging.info("Elemen 'Lanjut' untuk tombol lanjut ditemukan")
    tombol_lanjut.click()
    logging.info("Klik tombol 'Lanjut' berhasil")
    time.sleep(3)

    # Klik Kolom Email
    field_email = wait.until(EC.presence_of_element_located((By.XPATH,
                                                             "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
    logging.info("Elemen kolom email ditemukan")
    field_email.click()
    logging.info("Klik kolom email berhasil")
    os.system('adb shell input text "akmalalhaqi123@gmail.com"')
    logging.info("Input teks email berhasil")
    time.sleep(3)

    # Klik Kolom Password
    field_password = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
    logging.info("Elemen kolom password ditemukan")
    field_password.click()
    logging.info("Klik kolom password berhasil")
    os.system('adb shell input text "Test12345"')
    logging.info("Input teks password berhasil")
    time.sleep(3)

    # Klik Tombol Login
    login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
    logging.info("Elemen tombol login 'Masuk' ditemukan")
    login.click()
    logging.info("Klik tombol login 'Masuk' berhasil")
    time.sleep(10)

    # Akses Tagihan
    tagihan = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//android.widget.ImageView[@content-desc='Tagihan'])[2]")))
    logging.info("Elemen akses 'Tagihan' ditemukan")
    tagihan.click()
    logging.info("Klik akses 'Tagihan' berhasil")
    time.sleep(5)

    # Akses Riwayat Pembayaran
    try:
        time.sleep(2)  # Penundaan tambahan sebelum mencari elemen
        riwayat_pembayaran = wait.until(
            lambda d: d.find_element(By.ACCESSIBILITY_ID, "Riwayat Pembayaran\nTab 3 dari 3"))
        logging.info("Elemen 'Riwayat Pembayaran' ditemukan")
        riwayat_pembayaran.click()
        logging.info("Klik 'Riwayat Pembayaran' berhasil")
    except Exception as e:
        logging.error(f"Error menemukan elemen 'Riwayat Pembayaran': {e}")
    time.sleep(5)


    # Scroll Sampai Dapat Yang Lunas
    def scroll_until_element_found(driver, ui_selector, max_scroll_attempts=10):
        scroll_attempts = 0
        while scroll_attempts < max_scroll_attempts:
            try:
                element = driver.find_element(By.ANDROID_UIAUTOMATOR, ui_selector)
                return element
            except:
                driver.swipe(500, 1500, 500, 500, 1000)  # Gunakan driver.swipe untuk menggulir layar
                time.sleep(2)
                scroll_attempts += 1
        raise Exception(f"Element with UiSelector '{ui_selector}' not found after {max_scroll_attempts} attempts.")


    ui_selector = 'new UiSelector().descriptionContains("Lunas")'
    elemen_lunas = scroll_until_element_found(driver, ui_selector)
    elemen_lunas.click()
    time.sleep(7)
    logging.info("Elemen 'Lunas' ditemukan")
finally:
    # Jangan lupa untuk menutup sesi pengujian jika driver terdefinisi
    if 'driver' in locals():
        driver.quit()
        logging.info("Sesi pengujian ditutup")
