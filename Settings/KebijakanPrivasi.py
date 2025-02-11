import logging
import random
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
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

    # Menu Pengaturan
    pengaturan = wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.ImageView[@content-desc='Pengaturan']")))
    pengaturan.click()
    time.sleep(4)

    # Kebijakan Privasi
    privacy = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Kebijakan Privasi")'))
    privacy.click()
    time.sleep(4)

    # Scroll Sampai akhir page
    def scroll_to_end(driver):
        while True:
            previous_page_source = driver.page_source
            driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=500, duration=1000)
            time.sleep(2)  # Beri waktu untuk halaman dimuat ulang
            if previous_page_source == driver.page_source:
                break

    scroll_to_end(driver)

finally:
    # Jangan lupa untuk menutup sesi pengujian jika driver terdefinisi
    if 'driver' in locals():
        driver.quit()
        logging.info("Sesi pengujian ditutup")
