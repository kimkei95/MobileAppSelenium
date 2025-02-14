import json
import os
import shutil
import subprocess
from appium.options.android import UiAutomator2Options
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure
import logging
import time
import os
from conftest import driver

# Konfigurasi Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

screenshot_dir = "ReportMobile/Reports/screenshots"
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)


def capture_screenshot(driver, request, step_name, attempt):
    test_name = request.node.name
    iteration_screenshot_dir = os.path.join(screenshot_dir, f"attempt_{attempt}")

    if not os.path.exists(iteration_screenshot_dir):
        os.makedirs(iteration_screenshot_dir)

    screenshot_path = os.path.join(
        iteration_screenshot_dir, f"{test_name}_{step_name}.png"
    )

    # Menyimpan screenshot dan log path
    print(f"Taking screenshot for {step_name} (Attempt {attempt})...")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

    # Lampirkan screenshot ke laporan Allure
    allure.attach.file(
        screenshot_path,
        name=f"{step_name} (Attempt {attempt})",
        attachment_type=allure.attachment_type.PNG,
    )


@allure.feature('Login Feature')
@allure.story('Test Login on Mobile App')
def test_login(driver, request):
    try:
        wait = WebDriverWait(driver, 40)
        logging.info("Test Login")

        # Landing Page
        with allure.step("Klik Lanjut 1"):
            kliklanjut1 = wait.until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']"))
            )
            kliklanjut1.click()
            capture_screenshot(driver, request, "Klik Lanjut 1", attempt=1)
            time.sleep(3)

        with allure.step("Klik Lanjut 2"):
            kliklanjut2 = wait.until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']"))
            )
            kliklanjut2.click()
            capture_screenshot(driver, request, "Klik Lanjut 2", attempt=1)
            time.sleep(3)

        with allure.step("Klik Lanjut 3"):
            kliklanjut3 = wait.until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']"))
            )
            kliklanjut3.click()
            capture_screenshot(driver, request, "Klik Lanjut 3", attempt=1)
            time.sleep(3)

        # Pilih Sekolah
        with allure.step("Pilih Sekolah"):
            Pilih_sekolah = wait.until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']"))
            )
            Pilih_sekolah.click()
            capture_screenshot(driver, request, "Pilih Sekolah", attempt=1)
            time.sleep(3)

        # Value Sekolah
        with allure.step("Value Sekolah Terpilih"):
            value_sekolah = wait.until(lambda d: d.find_element(
                By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
            ))
            value_sekolah.click()
            capture_screenshot(driver, request, "Value Sekolah Terpilih", attempt=1)
            time.sleep(3)

        # Klik Lanjut
        with allure.step("Klik lanjut"):
            tombol_lanjut = wait.until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']"))
            )
            tombol_lanjut.click()
            capture_screenshot(driver, request, "Klik lanjut", attempt=1)
            time.sleep(3)

        # Klik Kolom Email
        with allure.step("Klik Field Email"):
            field_email = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
            field_email.click()
            capture_screenshot(driver, request, "Klik Field Email", attempt=1)
            os.system('adb shell input text "akmalalhaqi123@gmail.com"')
            capture_screenshot(driver, request, "Isi Value Email", attempt=1)
            time.sleep(5)

        # Klik field Password
        with allure.step("Klik Field Password"):
            field_password = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                        "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
            field_password.click()
            capture_screenshot(driver, request, "Klik Field Password", attempt=1)
            os.system('adb shell input text "Test12345"')
            capture_screenshot(driver, request, "Value Password", attempt=1)
            time.sleep(5)

        # Klik Tombol login
        with allure.step("Klik Login"):
            login = wait.until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
            login.click()
            capture_screenshot(driver, request, "Klik Login", attempt=1)
            time.sleep(10)

        with allure.step("User Berhasil Login"):
            capture_screenshot(driver, request, "User Berhasil Login", attempt=1)

    except Exception as e:
        logging.error(f"Error dalam pengujian login: {e}")
        raise

# @allure.feature('Tambah Siswa')
# @allure.story('Test Tambah Siswa In Mobile App')
# def test_lihat_siswa(driver):
#     try:
#         wait = WebDriverWait(driver, 40)
#         logging.info("Test Lihat Siswa")
#         # Landing Page
#         kliklanjut1 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut1.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 1 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut2 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut2.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 2 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut3 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut3.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 3 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Pilih Sekolah
#         Pilih_sekolah = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
#         Pilih_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Pilih Sekolah Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Temukan elemen menggunakan UiSelector
#         value_sekolah = wait.until(lambda d: d.find_element(
#             By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
#         ))
#         value_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Value Sekolah Berhasil DiTemukan",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Lanjut
#         tombol_lanjut = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         tombol_lanjut.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Email
#         field_email = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                  "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
#         field_email.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Email Berhasil DiKlik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "akmalalhaqi123@gmail.com"')
#         allure.attach(driver.get_screenshot_as_png(), name="Email Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Password
#         field_password = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
#         field_password.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Password Berhasil DiKlik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "Test12345"')
#         allure.attach(driver.get_screenshot_as_png(), name="Password Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Tombol Login
#         login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
#         login.click()
#         allure.attach(driver.get_screenshot_as_png(), name="User Berhasil Login",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(10)
#
#         # Lihat Siswa
#         lihat_siswa = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='Daftar Siswa']")))
#         lihat_siswa.click()
#         allure.attach(driver.get_screenshot_as_png(), name="User Berhasil Melihat List Siswa",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#     except Exception as e:
#         logging.error(f"Error dalam pengujian lihat siswa: {e}")
#         raise
#
# @allure.feature('Akses Breadcrums')
# @allure.story('Test Akses Breadcrums')
# def test_akses_breadcrums(driver):
#     try:
#         wait = WebDriverWait(driver, 40)
#         logging.info("Test Breadcrums")
#         # Landing Page
#         kliklanjut1 = wait.until(
#         EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut1.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 1 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut2 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut2.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 2 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut3 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut3.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 3 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Pilih Sekolah
#         Pilih_sekolah = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
#         Pilih_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Pilih Sekolah Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Temukan elemen menggunakan UiSelector
#         value_sekolah = wait.until(lambda d: d.find_element(
#             By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
#         ))
#         value_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Value Sekolah Berhasil DiTemukan",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Lanjut
#         tombol_lanjut = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         tombol_lanjut.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Email
#         field_email = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                  "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
#         field_email.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Field Email Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "akmalalhaqi123@gmail.com"')
#         allure.attach(driver.get_screenshot_as_png(), name="Email Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Password
#         field_password = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
#         field_password.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Password Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "Test12345"')
#         allure.attach(driver.get_screenshot_as_png(), name="Password Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Tombol Login
#         login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
#         login.click()
#         allure.attach(driver.get_screenshot_as_png(), name="User Berhasil Login",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(10)
#
#         # Akses  Menu Pengumuman
#
#         br_pengumuman = wait.until(lambda d: d.find_element(By.ACCESSIBILITY_ID, "Pengumuman"))
#         br_pengumuman.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Menu Pengumuman Berhasil Dipilih",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(5)
#
#         # Akses breadcrums Pengumuman
#         ngumumin = wait.until(lambda d: d.find_element(By.ACCESSIBILITY_ID, "Pengumuman"))
#         ngumumin.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Breadcrums Pengumuman Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # akses breadcrums Event
#
#         br_event = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Event")'))
#         br_event.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Breadcrums Event Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(5)
#
#     except Exception as e:
#         logging.error(f"Error dalam pengujian breadcrums: {e}")
#         raise
#
# @allure.feature('Akses Menu Event')
# @allure.story('Test Akses Menu Event')
# def test_akses_event(driver):
#     try:
#         wait = WebDriverWait(driver, 40)
#         logging.info("Test Akses Event")
#         kliklanjut1 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut1.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 1 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut2 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut2.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 2 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut3 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut3.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 3 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Pilih Sekolah
#         Pilih_sekolah = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
#         Pilih_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Pilih Sekolah Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Temukan elemen menggunakan UiSelector
#         value_sekolah = wait.until(lambda d: d.find_element(
#             By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
#         ))
#         value_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Value Sekolah Berhasil DiTemukan",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Lanjut
#         tombol_lanjut = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         tombol_lanjut.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Email
#         field_email = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                  "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
#         field_email.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Email Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "akmalalhaqi123@gmail.com"')
#         allure.attach(driver.get_screenshot_as_png(), name="Email Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Password
#         field_password = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
#         field_password.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Password Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "Test12345"')
#         allure.attach(driver.get_screenshot_as_png(), name="Password Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Tombol Login
#         login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
#         login.click()
#         allure.attach(driver.get_screenshot_as_png(), name="User Berhasil Login",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(10)
#         # Event
#         menu_event = wait.until(
#             lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Event")'))
#         menu_event.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Menu Event Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(5)
#
#         # Pilih Breadcrums Event
#         event = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Event")'))
#         event.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Breadcrums Event Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(4)
#
#         # Daftar UiSelector untuk Event
#         event_selectors = [
#             'new UiSelector().description("Workshop Pengembangan Diri untuk Siswa\nEvent\nDiterbitkan 28 January 2025")',
#             'new UiSelector().description("Lomba Debat Bahasa Inggris\nEvent\nDiterbitkan 28 January 2025").instance(0)',
#             'new UiSelector().description("Workshop Teknologi: Mengenal AI dan Robotika\nEvent\nDiterbitkan 28 January 2025")',
#             'new UiSelector().description("Lomba Debat Bahasa Inggris\nEvent\nDiterbitkan 28 January 2025").instance(1)',
#             'new UiSelector().description("Pelatihan Menulis Kreatif untuk Siswa\nEvent\nDiterbitkan 23 January 2025")',
#             'new UiSelector().description("UMP DKI Jakarta 2025 naik 6, 5 persen\nEvent\nDiterbitkan 17 December 2024")',
#             'new UiSelector().description("Ini Judul\nEvent\nDiterbitkan 16 December 2024")',
#             'new UiSelector().description("Cari gweh coba\nEvent\nDiterbitkan 16 December 2024")'
#         ]
#
#         # Pilih salah satu event acak dan klik elemen tersebut
#         selected_event = random.choice(event_selectors)
#         allure.attach(driver.get_screenshot_as_png(), name="Event Berhasil Dipiilih",
#                       attachment_type=allure.attachment_type.PNG)
#
#         # Tunggu dan temukan elemen yang dipilih
#         try:
#             logging.info(f"Menunggu dan mengklik event dengan selector: {selected_event}")
#             event_element = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, selected_event))
#             event_element.click()
#             allure.attach(driver.get_screenshot_as_png(), name="User Berhasil Memilih Event",
#                           attachment_type=allure.attachment_type.PNG)
#             logging.info(f"Klik event berhasil: {selected_event}")
#             time.sleep(5)
#         except TimeoutException:
#             logging.error(f"Gagal menemukan event dengan selector: {selected_event}")
#     except Exception as e:
#         logging.error(f"Error dalam pengujian akses event: {e}")
#         raise
# @allure.feature('Akses Menu Pengumuman')
# @allure.story('Test Akses Menu Pengumuman')
# def test_akses_pengumuman(driver):
#     try:
#         wait = WebDriverWait(driver, 40)
#         logging.info("Test Akses Pengumuman")
#
#         kliklanjut1 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut1.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 1 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut2 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut2.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 2 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut3 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut3.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 3 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Pilih Sekolah
#         Pilih_sekolah = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
#         Pilih_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Sekolah Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Temukan elemen menggunakan UiSelector
#         value_sekolah = wait.until(lambda d: d.find_element(
#             By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
#         ))
#         value_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Value Sekolah Berhasil Ditemukan",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Lanjut
#         tombol_lanjut = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         tombol_lanjut.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Email
#         field_email = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                  "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
#         field_email.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Email Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "akmalalhaqi123@gmail.com"')
#         allure.attach(driver.get_screenshot_as_png(), name="Email Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Password
#         field_password = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
#         field_password.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Password Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "Test12345"')
#         allure.attach(driver.get_screenshot_as_png(), name="Password Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Tombol Login
#         login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
#         login.click()
#         allure.attach(driver.get_screenshot_as_png(), name="User Berhasil Login",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(10)
#
#         # Event
#         menu_event = wait.until(
#             lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Event")'))
#         menu_event.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Menu Event Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(5)
#
#         # Pengumuman
#         pengumuman = wait.until(
#             lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Pengumuman")'))
#         pengumuman.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Breadcrums Pengumuman Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(4)
#
#         # Pilih pengumuman secara acak berdasarkan accessibility-id
#         random_pengumuman = [
#             'Pendaftaran Ekstrakurikuler Dibuka!\nPengumuman\nDiterbitkan 28 January 2025',
#             'Penggalangan Dana untuk Korban Bencana\nPengumuman\nDiterbitkan 28 January 2025',
#             'Hari Guru Nasional: Acara dan Perayaan\nPengumuman\nDiterbitkan 28 January 2025',
#             'Kegiatan Study Tour ke Museum Nasional\nPengumuman\nDiterbitkan 23 December 2024'
#         ]
#
#         # Pilih pengumuman secara acak
#         selected_pengumuman_desc = random.choice(random_pengumuman)
#         allure.attach(driver.get_screenshot_as_png(), name="Memilih Random Pengumuman",
#                       attachment_type=allure.attachment_type.PNG)
#
#         # Tunggu dan temukan elemen berdasarkan accessibility-id
#         try:
#             selected_pengumuman_element = wait.until(
#                 EC.presence_of_element_located(
#                     (By.ACCESSIBILITY_ID, selected_pengumuman_desc)
#                 )
#             )
#             logging.info(f"Pengumuman yang dipilih: {selected_pengumuman_desc}")
#             selected_pengumuman_element.click()
#             allure.attach(driver.get_screenshot_as_png(), name="Pengumuman Berhasil DiPilih",
#                           attachment_type=allure.attachment_type.PNG)
#             logging.info("Pengumuman berhasil dipilih dan diklik.")
#             time.sleep(7)
#
#         except TimeoutException:
#             logging.error(f"Gagal menemukan pengumuman dengan accessibility-id: {selected_pengumuman_desc}")
#
#     except Exception as e:
#         logging.error(f"Error dalam pengujian akses pengumuman: {e}")
#         raise
#
# @allure.feature('Akses FAQ')
# @allure.story('Test Akses FAQ')
# def test_akses_faq(driver):
#     try:
#         wait = WebDriverWait(driver, 40)
#         logging.info("Test FAQ")
#         kliklanjut1 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut1.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 1 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut2 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut2.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 2 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut3 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut3.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 3 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Pilih Sekolah
#         Pilih_sekolah = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
#         Pilih_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Sekolah Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Temukan elemen menggunakan UiSelector
#         value_sekolah = wait.until(lambda d: d.find_element(
#             By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
#         ))
#         value_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Value Sekolah Berhasil Dipilih",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Lanjut
#         tombol_lanjut = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         tombol_lanjut.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Email
#         field_email = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                  "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
#         field_email.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Email Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "akmalalhaqi123@gmail.com"')
#         allure.attach(driver.get_screenshot_as_png(), name="Email Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Password
#         field_password = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
#         field_password.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Password Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "Test12345"')
#         allure.attach(driver.get_screenshot_as_png(), name="Password Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Tombol Login
#         login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
#         login.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Login Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(10)
#         allure.attach(driver.get_screenshot_as_png(), name="User Berhasil Login",
#                       attachment_type=allure.attachment_type.PNG)
#         # Menu Pengaturan
#         pengaturan = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='Pengaturan']")))
#         pengaturan.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Menu Pengaturan Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(4)
#
#         # FAQ
#         FAQ = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='FAQ']")))
#         FAQ.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Menu FAQ Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(4)
#
#         # List of UiSelectors
#         uiselectors = [
#             'new UiSelector().description("Bagaimana cara membayarkan tagihan sekolah?")',
#             'new UiSelector().description("Bagaimana cara mendownload nota pembayaran?")',
#             'new UiSelector().description("Bagaimana cara mengubah data siswa?")',
#             'new UiSelector().description("Apa yang harus dilakukan jika pembayaran gagal?")',
#             'new UiSelector().description("Apakah ada biaya tambahan untuk setiap transaksi?")'
#         ]
#
#         # Klik setiap elemen secara acak dengan jeda setidaknya 10 detik
#         random.shuffle(uiselectors)
#
#         for uiselector in uiselectors:
#             clicked = False
#             attempts = 0
#             while not clicked and attempts < 3:
#                 try:
#                     element = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, uiselector))
#                     element.click()
#                     logging.info(
#                         f"Klik berhasil pada elemen dengan deskripsi: {element.get_attribute('contentDescription')}")
#                     clicked = True
#                     time.sleep(10)
#                     allure.attach(driver.get_screenshot_as_png(), name="Mengklik Setiap Elemen",
#                                   attachment_type=allure.attachment_type.PNG)
#                     # Jeda setidaknya 10 detik
#                 except StaleElementReferenceException:
#                     logging.warning(
#                         f"StaleElementReferenceException: Elemen tidak lagi dalam DOM, mencoba lagi... (percobaan {attempts + 1})")
#                     attempts += 1
#                 except Exception as e:
#                     logging.error(f"Gagal mengklik elemen: {e}")
#                     break
#     except Exception as e:
#         logging.error(f"Error dalam pengujian akses FAQ: {e}")
#         raise
# @allure.feature('Akses Kebijakan Privasi')
# @allure.story('Test Akses Kebijakan Privasi')
# def test_kebijakan_privasi(driver):
#     try:
#         wait = WebDriverWait(driver, 40)
#         logging.info("Test Kebijakan Privasi")
#         kliklanjut1 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut1.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 1 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut2 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut2.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 2 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut3 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut3.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 3 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Pilih Sekolah
#         Pilih_sekolah = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
#         Pilih_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Pilih Sekolah Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Temukan elemen menggunakan UiSelector
#         value_sekolah = wait.until(lambda d: d.find_element(
#             By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
#         ))
#         value_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Value Sekolah Berhasil Dipilih",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Lanjut
#         tombol_lanjut = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         tombol_lanjut.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Email
#         field_email = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                  "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
#         field_email.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Email Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "akmalalhaqi123@gmail.com"')
#         allure.attach(driver.get_screenshot_as_png(), name="Email Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Password
#         field_password = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
#         field_password.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Password Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "Test12345"')
#         allure.attach(driver.get_screenshot_as_png(), name="Password Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Tombol Login
#         login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
#         login.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Login Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(10)
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 1 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#
#         # Menu Pengaturan
#         pengaturan = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='Pengaturan']")))
#         pengaturan.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Menu Pengaturan Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(4)
#
#         # Kebijakan Privasi
#         privacy = wait.until(
#             lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Kebijakan Privasi")'))
#         privacy.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Kebijakan Privasi Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(4)
#
#         # Scroll Sampai akhir page
#         def scroll_to_end(driver):
#             while True:
#                 previous_page_source = driver.page_source
#                 driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=500, duration=1000)
#                 time.sleep(2)  # Beri waktu untuk halaman dimuat ulang
#                 if previous_page_source == driver.page_source:
#                     break
#
#         scroll_to_end(driver)
#     except Exception as e:
#         logging.error(f"Error dalam pengujian kebijakan privasi: {e}")
#         raise
# @allure.feature('Akses Ubah Password')
# @allure.story('Test Akses Ubah Password')
# def test_ubah_password(driver):
#     try:
#         wait = WebDriverWait(driver, 40)
#         logging.info("Test Ubah Password")
#         kliklanjut1 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut1.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 1 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut2 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut2.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 2 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut3 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut3.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 3 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Pilih Sekolah
#         Pilih_sekolah = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
#         Pilih_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Pilih Sekolah Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Temukan elemen menggunakan UiSelector
#         value_sekolah = wait.until(lambda d: d.find_element(
#             By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
#         ))
#         value_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Value Sekolah Berhasil Dipilih",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Lanjut
#         tombol_lanjut = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         tombol_lanjut.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Email
#         field_email = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                  "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
#         field_email.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Email Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "akmalalhaqi123@gmail.com"')
#         allure.attach(driver.get_screenshot_as_png(), name="Email Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Password
#         field_password = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
#         field_password.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Password Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "Test12345"')
#         allure.attach(driver.get_screenshot_as_png(), name="Password Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Tombol Login
#         login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
#         login.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Login Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(10)
#         allure.attach(driver.get_screenshot_as_png(), name="User Berhasil Login",
#                       attachment_type=allure.attachment_type.PNG)
#
#         # Menu Pengaturan
#         pengaturan = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='Pengaturan']")))
#         pengaturan.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Menu Pengaturan Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(4)
#
#         # Ubah Password
#         ubah_password = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='Ubah Password']")))
#         ubah_password.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Ubah Password Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(4)
#
#         # field password lama
#         field_lama = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR,
#                                                          'new UiSelector().className("android.widget.EditText").instance(0)'))
#         field_lama.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Field Password Lama Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "Test12345"')
#         allure.attach(driver.get_screenshot_as_png(), name="Password Lama Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # field pass baru
#         pass_baru = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR,
#                                                         'new UiSelector().className("android.widget.EditText").instance(1)'))
#         pass_baru.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Field Password Baru Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "Test123456"')
#         allure.attach(driver.get_screenshot_as_png(), name="Password Baru Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # konfirmasi pass baru
#         konf_pass = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR,
#                                                         'new UiSelector().className("android.widget.EditText").instance(2)'))
#         konf_pass.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Field Konfirmasi Password Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "Test123456"')
#         allure.attach(driver.get_screenshot_as_png(), name="Kofrimasi Password Baru Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#     except Exception as e:
#         logging.error(f"Error dalam pengujian ubah password: {e}")
#         raise
#
# @allure.feature('Bayar Sumbangan')
# @allure.story('Test Bayar Sumbangan')
# def test_bayar_sumbangan(driver):
#     try:
#         wait = WebDriverWait(driver, 40)
#         logging.info("Test Bayar Sumbangan")
#         kliklanjut1 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut1.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 1 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut2 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut2.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 2 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut3 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut3.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 3 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Pilih Sekolah
#         Pilih_sekolah = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
#         Pilih_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Pilih Sekolah Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Temukan elemen menggunakan UiSelector
#         value_sekolah = wait.until(lambda d: d.find_element(
#             By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
#         ))
#         value_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Value Sekolah Berhasil Dipilih",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Lanjut
#         tombol_lanjut = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         tombol_lanjut.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Email
#         field_email = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                  "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
#         field_email.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Email Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "akmalalhaqi123@gmail.com"')
#         allure.attach(driver.get_screenshot_as_png(), name="Email Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Password
#         field_password = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
#         field_password.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Password Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "Test12345"')
#         allure.attach(driver.get_screenshot_as_png(), name="Value Password Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Tombol Login
#         login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
#         login.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Login Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(10)
#         allure.attach(driver.get_screenshot_as_png(), name="User Berhasil Login",
#                       attachment_type=allure.attachment_type.PNG)
#
#         # Akses Tagihan
#         tagihan = wait.until(
#             EC.presence_of_element_located((By.XPATH, "(//android.widget.ImageView[@content-desc='Tagihan'])[2]")))
#         tagihan.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Menu Tagihan Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(5)
#
#         # Akses Bayar Sumbangan
#         try:
#             time.sleep(2)
#             sumbangan = wait.until(lambda d: d.find_element(By.ACCESSIBILITY_ID, "Sumbangan\nTab 2 dari 3"))
#             logging.info("Elemen 'Sumbangan' ditemukan")
#             sumbangan.click()
#             logging.info("Klik 'Sumbangan' berhasil")
#             allure.attach(driver.get_screenshot_as_png(), name="BreadCrums Sumbangan Berhasil Diklik",
#                           attachment_type=allure.attachment_type.PNG)
#
#             # Randomize Bayar Sumbangan
#             nama_sumbangan = [
#                 "(//android.widget.Button[@content-desc='Bayar'])[1]",  # Sumbangan Buku
#                 "(//android.widget.Button[@content-desc='Bayar'])[2]",  # Sumbangan Fasilitas
#                 "(//android.widget.Button[@content-desc='Bayar'])[3]",  # Sumbangan Seragam
#                 "(//android.widget.Button[@content-desc='Bayar'])[4]",  # Alat Musik
#                 "(//android.widget.Button[@content-desc='Bayar'])[5]",  # Bencana Alam
#                 "(//android.widget.Button[@content-desc='Bayar'])[6]",  # Teknologi Digital
#                 "(//android.widget.Button[@content-desc='Bayar'])[7]",  # Bencana Alam (2)
#                 "(//android.widget.Button[@content-desc='Bayar'])[8]",  # Orang Meninggal
#                 "(//android.widget.Button[@content-desc='Bayar'])[9]",  # Baru New
#                 "(//android.widget.Button[@content-desc='Bayar'])[10]"  # Baru
#             ]
#
#             # Pilih salah satu elemen secara acak
#             selected_sumbangan = random.choice(nama_sumbangan)
#
#             # Klik elemen yang dipilih secara acak
#             elemen_sumbangan = wait.until(EC.presence_of_element_located((By.XPATH, selected_sumbangan)))
#             elemen_sumbangan.click()
#             allure.attach(driver.get_screenshot_as_png(), name="Sumbangan Berhasil Diklik",
#                           attachment_type=allure.attachment_type.PNG)
#             time.sleep(3)
#
#             # Pop-up Sumbangan
#             field_nominal = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText")))
#             field_nominal.click()
#             allure.attach(driver.get_screenshot_as_png(), name="Field Sumbangan Berhasil Diklik",
#                           attachment_type=allure.attachment_type.PNG)
#             time.sleep(4)
#
#             # Menghasilkan Angka Acak antara 10.000 dan 10 juta
#             nominal = random.randint(10000, 10000000)
#             logging.info(f"Nominal acak yang dihasilkan: {nominal}")
#
#             # Memasukkan Angka Acak ke dalam Field Nominal
#             os.system(f'adb shell input text "{nominal}"')
#             allure.attach(driver.get_screenshot_as_png(), name="Nominal Sumbangan Berhasil Diinput",
#                           attachment_type=allure.attachment_type.PNG)
#             logging.info(f"Nominal {nominal} telah dimasukkan ke dalam field")
#             time.sleep(4)
#
#             # Lanjutkan Bayar Sumbangan
#             logging.info("Mencoba untuk klik 'Lanjutkan'")
#             bayar_sumbangan = wait.until(
#                 lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Lanjutkan")'))
#             bayar_sumbangan.click()
#             allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjutkan Berhasil",
#                           attachment_type=allure.attachment_type.PNG)
#             logging.info("Klik 'Lanjutkan' berhasil")
#             time.sleep(5)
#
#         except Exception as e:
#             logging.error(f"Error dalam eksekusi skrip: {e}")
#
#         # Pilih Random Metode Pembayaran
#         selector_bank = [
#             "new UiSelector().className(\"android.widget.RadioButton\").instance(1)",
#             "new UiSelector().className(\"android.widget.RadioButton\").instance(2)",
#             "new UiSelector().className(\"android.widget.RadioButton\").instance(3)",
#             "new UiSelector().className(\"android.widget.RadioButton\").instance(4)",
#             "new UiSelector().className(\"android.widget.RadioButton\").instance(5)",
#             "new UiSelector().className(\"android.widget.RadioButton\").instance(6)"
#         ]
#
#         selected_bank_selector = random.choice(selector_bank)
#         bank_element = driver.find_element(By.ANDROID_UIAUTOMATOR, selected_bank_selector)
#         bank_element.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Bank Berhasil Dipilih",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(2)
#
#         # Klik Bayar
#         bayar_tagihan = wait.until(
#             lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Bayar")'))
#         bayar_tagihan.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Bayar Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(5)
#     except Exception as e:
#         logging.error(f"Error dalam pengujian bayar sumbangan: {e}")
#         raise
#
# @allure.feature('Bayar Tagihan')
# @allure.story('Test Bayar Tagihan')
# def test_bayar_tagihan(driver):
#     try:
#         wait = WebDriverWait(driver, 40)
#         logging.info("Test Bayar Tagihan")
#             # Landing Page
#         kliklanjut1 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut1.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 1 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut2 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut2.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 2 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         kliklanjut3 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         kliklanjut3.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 3 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Pilih Sekolah
#         Pilih_sekolah = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
#         Pilih_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Pilih Sekolah Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Temukan elemen menggunakan UiSelector
#         value_sekolah = wait.until(lambda d: d.find_element(
#             By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
#         ))
#         value_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Value Sekolah Berhasil Dipilih",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Lanjut
#         tombol_lanjut = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         tombol_lanjut.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Email
#         field_email = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                  "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
#         field_email.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Email Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "akmalalhaqi123@gmail.com"')
#         allure.attach(driver.get_screenshot_as_png(), name="Email Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Kolom Password
#         field_password = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
#         field_password.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Password Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         os.system('adb shell input text "Test12345"')
#         allure.attach(driver.get_screenshot_as_png(), name="Passsword Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(3)
#
#         # Klik Tombol Login
#         login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
#         login.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Tombol Login Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(10)
#         allure.attach(driver.get_screenshot_as_png(), name="User Berhasil Login",
#                       attachment_type=allure.attachment_type.PNG)
#
#         # Akses Tagihan
#         tagihan = wait.until(
#             EC.presence_of_element_located((By.XPATH, "(//android.widget.ImageView[@content-desc='Tagihan'])[2]")))
#         tagihan.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Menu Tagihan Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(5)
#
#         # Pilih Tagihan yang akan dibayarkan
#         ui_selectors = [
#             "new UiSelector().className(\"android.widget.CheckBox\").instance(2)",
#             "new UiSelector().className(\"android.widget.CheckBox\").instance(3)",
#             "new UiSelector().className(\"android.widget.CheckBox\").instance(4)",
#             "new UiSelector().className(\"android.widget.CheckBox\").instance(5)",
#
#         ]
#
#         # Pilih elemen secara acak
#         selected_ui_selectors = random.sample(ui_selectors, random.randint(1, 3))
#
#         for ui_selector in selected_ui_selectors:
#             try:
#                 element = driver.find_element(By.ANDROID_UIAUTOMATOR, ui_selector)
#                 element.click()
#                 allure.attach(driver.get_screenshot_as_png(), name="Tagihan Terpilih",
#                               attachment_type=allure.attachment_type.PNG)
#                 time.sleep(4)
#             except Exception as e:
#                 print(f"Failed to click on element with UiSelector '{ui_selector}': {e}")
#
#         # Klik Lanjut Bayar
#         button_bayar = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Bayar']")))
#         button_bayar.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Tombol Bayar Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(4)
#
#         # pop up lanjutkan pembayaran
#
#         lanjut_bayar = wait.until(lambda d: d.find_element(
#             By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Lanjut Bayar")'
#         ))
#         lanjut_bayar.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Tombol Lanjut Bayar Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(4)
#
#         # random choice pilih bank
#
#         selector_bank = ["new UiSelector().className(\"android.widget.RadioButton\").instance(1)",
#                          "new UiSelector().className(\"android.widget.RadioButton\").instance(2)",
#                          "new UiSelector().className(\"android.widget.RadioButton\").instance(3)",
#                          "new UiSelector().className(\"android.widget.RadioButton\").instance(4)",
#                          "new UiSelector().className(\"android.widget.RadioButton\").instance(5)",
#                          "new UiSelector().className(\"android.widget.RadioButton\").instance(6)"
#                          ]
#
#         selected_bank_selector = random.choice(selector_bank)
#         bank_element = driver.find_element(By.ANDROID_UIAUTOMATOR, selected_bank_selector)
#         bank_element.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Bank Berhasil Dipilih",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(2)
#
#         time.sleep(5)
#
#         # Klik Bayar
#
#         bayar_tagihan = wait.until(
#             lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Bayar")'))
#         bayar_tagihan.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Tombol Bayar Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(5)
#
#     except Exception as e:
#         logging.error(f"Error dalam pengujian bayar tagihan: {e}")
#         raise
# @allure.feature('Check Riwayat Pembayaran')
# @allure.story('Test Check Riwayat Pembayaran')
# def test_riwayat_pembayaran(driver):
#     try:
#         wait = WebDriverWait(driver, 40)
#         logging.info("Test Riwayat Pembayaran")
#         # Landing Page
#         kliklanjut1 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         logging.info("Elemen pertama 'Lanjut' ditemukan")
#         kliklanjut1.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 1 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         logging.info("Klik 'Lanjut' pertama berhasil")
#         time.sleep(3)
#
#         kliklanjut2 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         logging.info("Elemen kedua 'Lanjut' ditemukan")
#         kliklanjut2.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 2 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         logging.info("Klik 'Lanjut' kedua berhasil")
#         time.sleep(3)
#
#         kliklanjut3 = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         logging.info("Elemen ketiga 'Lanjut' ditemukan")
#         kliklanjut3.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut 3 Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         logging.info("Klik 'Lanjut' ketiga berhasil")
#         time.sleep(3)
#
#         # Pilih Sekolah
#         Pilih_sekolah = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
#         logging.info("Elemen 'Pilih sekolah' ditemukan")
#         Pilih_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Pilih Sekolah Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         logging.info("Klik 'Pilih sekolah' berhasil")
#         time.sleep(3)
#
#         # Temukan elemen menggunakan UiSelector
#         value_sekolah = wait.until(lambda d: d.find_element(
#             By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
#         ))
#         logging.info("Elemen sekolah 'PT Aigen Global Teknologi' ditemukan")
#         value_sekolah.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Value Sekolah Berhasil Dipilih",
#                       attachment_type=allure.attachment_type.PNG)
#         logging.info("Klik sekolah 'PT Aigen Global Teknologi' berhasil")
#         time.sleep(3)
#
#         # Klik Lanjut
#         tombol_lanjut = wait.until(
#             EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
#         logging.info("Elemen 'Lanjut' untuk tombol lanjut ditemukan")
#         tombol_lanjut.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Klik Lanjut Berhasil",
#                       attachment_type=allure.attachment_type.PNG)
#         logging.info("Klik tombol 'Lanjut' berhasil")
#         time.sleep(3)
#
#         # Klik Kolom Email
#         field_email = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                  "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
#         logging.info("Elemen kolom email ditemukan")
#         field_email.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Email Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         logging.info("Klik kolom email berhasil")
#         os.system('adb shell input text "akmalalhaqi123@gmail.com"')
#         allure.attach(driver.get_screenshot_as_png(), name="Email Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         logging.info("Input teks email berhasil")
#         time.sleep(3)
#
#         # Klik Kolom Password
#         field_password = wait.until(EC.presence_of_element_located((By.XPATH,
#                                                                     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
#         logging.info("Elemen kolom password ditemukan")
#         field_password.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Field Password Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         logging.info("Klik kolom password berhasil")
#         os.system('adb shell input text "Test12345"')
#         allure.attach(driver.get_screenshot_as_png(), name="Password Berhasil Diinput",
#                       attachment_type=allure.attachment_type.PNG)
#         logging.info("Input teks password berhasil")
#         time.sleep(3)
#
#         # Klik Tombol Login
#         login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
#         logging.info("Elemen tombol login 'Masuk' ditemukan")
#         login.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Login Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         logging.info("Klik tombol login 'Masuk' berhasil")
#         time.sleep(10)
#         allure.attach(driver.get_screenshot_as_png(), name="User Berhasil Login",
#                       attachment_type=allure.attachment_type.PNG)
#
#         # Akses Tagihan
#         tagihan = wait.until(
#             EC.presence_of_element_located((By.XPATH, "(//android.widget.ImageView[@content-desc='Tagihan'])[2]")))
#         logging.info("Elemen akses 'Tagihan' ditemukan")
#         tagihan.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Tagihan Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         logging.info("Klik akses 'Tagihan' berhasil")
#         time.sleep(5)
#
#         # Akses Riwayat Pembayaran
#         try:
#             time.sleep(2)  # Penundaan tambahan sebelum mencari elemen
#             riwayat_pembayaran = wait.until(
#                 lambda d: d.find_element(By.ACCESSIBILITY_ID, "Riwayat Pembayaran\nTab 3 dari 3"))
#             logging.info("Elemen 'Riwayat Pembayaran' ditemukan")
#             riwayat_pembayaran.click()
#             allure.attach(driver.get_screenshot_as_png(), name="Riwayat Pembayaran Berhasil Diklik",
#                           attachment_type=allure.attachment_type.PNG)
#             logging.info("Klik 'Riwayat Pembayaran' berhasil")
#         except Exception as e:
#             logging.error(f"Error menemukan elemen 'Riwayat Pembayaran': {e}")
#         time.sleep(5)
#
#         # Scroll Sampai Dapat Yang Lunas
#         def scroll_until_element_found(driver, ui_selector, max_scroll_attempts=5):
#             scroll_attempts = 0
#             while scroll_attempts < max_scroll_attempts:
#                 try:
#                     element = driver.find_element(By.ANDROID_UIAUTOMATOR, ui_selector)
#                     return element
#                 except:
#                     driver.swipe(500, 1500, 500, 500, 1000)  # Gunakan driver.swipe untuk menggulir layar
#                     time.sleep(2)
#                     scroll_attempts += 1
#             raise Exception(f"Element with UiSelector '{ui_selector}' not found after {max_scroll_attempts} attempts.")
#
#         ui_selector = 'new UiSelector().descriptionContains("Lunas")'
#         elemen_lunas = scroll_until_element_found(driver, ui_selector)
#         elemen_lunas.click()
#         allure.attach(driver.get_screenshot_as_png(), name="Tagihan Lunas Berhasil Diklik",
#                       attachment_type=allure.attachment_type.PNG)
#         time.sleep(7)
#         logging.info("Elemen 'Lunas' ditemukan")
#     except Exception as e:
#         logging.error(f"Error dalam pengujian bayar tagihan: {e}")
#         raise

def run_regression_test():
    driver = driver()

    try:
        test_login(driver)
        driver.quit()

        # driver = driver()
        # test_lihat_siswa(driver)
        # driver.quit()
        #
        # driver = driver()
        # test_akses_breadcrums(driver)
        # driver.quit()
        #
        #
        # driver= driver()
        # test_bayar_tagihan(driver)
        # driver.quit()
        #
        # driver = driver()
        # test_bayar_sumbangan(driver)
        # driver.quit()
        #
        #
        # driver = driver()
        # test_riwayat_pembayaran(driver)
        # driver.quit()
        #
        # driver = driver()
        # test_akses_event(driver)
        # driver.quit()
        #
        # driver = driver()
        # test_akses_pengumuman(driver)
        # driver.quit()
        #
        # driver = driver()
        # test_akses_faq(driver)
        # driver.quit()
        #
        # driver = driver()
        # test_ubah_password(driver)
        # driver.quit()
        #
        # driver = driver()
        # test_kebijakan_privasi(driver)
        # driver.quit()

        logging.info("Semua Test Regresi Berhasil")

    except Exception as e:
        logging.error(f"Pengujian Gagal: {e}")


    finally:
        # Pastikan driver ditutup jika ada error
        if 'driver' in locals():
            driver.quit()


if __name__ == "__main__":
    run_regression_test()

