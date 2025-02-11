import logging
import random
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

    #Akses Tagihan
    tagihan = wait.until(EC.presence_of_element_located((By.XPATH,"(//android.widget.ImageView[@content-desc='Tagihan'])[2]")))
    tagihan.click()
    time.sleep(5)

    #Pilih Tagihan yang akan dibayarkan
    ui_selectors = [
        "new UiSelector().className(\"android.widget.CheckBox\").instance(2)",
        "new UiSelector().className(\"android.widget.CheckBox\").instance(3)",
        "new UiSelector().className(\"android.widget.CheckBox\").instance(4)",
        "new UiSelector().className(\"android.widget.CheckBox\").instance(5)",

    ]

    # Pilih elemen secara acak
    selected_ui_selectors = random.sample(ui_selectors, random.randint(1, 3))

    for ui_selector in selected_ui_selectors:
        try:
            element = driver.find_element(By.ANDROID_UIAUTOMATOR, ui_selector)
            element.click()
            time.sleep(4)
        except Exception as e:
            print(f"Failed to click on element with UiSelector '{ui_selector}': {e}")

    # Klik Lanjut Bayar
    button_bayar = wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='Bayar']")))
    button_bayar.click()
    time.sleep(4)

    #pop up lanjutkan pembayaran

    lanjut_bayar = wait.until(lambda d: d.find_element(
        By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Lanjut Bayar")'
    ))
    lanjut_bayar.click()
    time.sleep(4)

    #random choice pilih bank

    selector_bank = ["new UiSelector().className(\"android.widget.RadioButton\").instance(1)",
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

    time.sleep(5)


    #Klik Bayar

    bayar_tagihan = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Bayar")'))
    bayar_tagihan.click()
    time.sleep(5)


finally:
    # Jangan lupa untuk menutup sesi pengujian jika driver terdefinisi
    if 'driver' in locals():
        driver.quit()

