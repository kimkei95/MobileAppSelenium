import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

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

    # Lihat Siswa
    lihat_siswa = wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.ImageView[@content-desc='Daftar Siswa']")))
    lihat_siswa.click()
    time.sleep(3)


finally:
    # Jangan lupa untuk menutup sesi pengujian jika driver terdefinisi
    if 'driver' in locals():
        driver.quit()
