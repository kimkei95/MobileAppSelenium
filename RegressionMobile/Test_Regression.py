import logging
import random
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os


# Konfigurasi Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def setup_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "HapeTesting"
    options.app = "C:\\Users\\akmal\\Downloads\\SiprusEdu SIT Debug v0.24.49 (1).apk"
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    return driver

def test_login(driver):
    try:
        wait = WebDriverWait(driver, 20)
        logging.info("Test Login")
        # Landing Page
        kliklanjut1 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut1.click()
        time.sleep(3)

        kliklanjut2 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut2.click()
        time.sleep(3)

        kliklanjut3 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut3.click()
        time.sleep(3)

        # Pilih Sekolah
        Pilih_sekolah = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
        Pilih_sekolah.click()
        time.sleep(3)

        # cari pakai uiAutomator By Xpath udah coba dia ngedetect 2 choice bukan 1
        value_sekolah = wait.until(lambda d: d.find_element(
            By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
        ))
        value_sekolah.click()
        time.sleep(3)

        # Klik Lanjut
        tombol_lanjut = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        tombol_lanjut.click()
        time.sleep(3)

        # klik Kolom Email

        # Pakai os supaya langsung interact sama operating sistemnya (udah coba make send_keys dan mobileBy ga bisa)
        field_email = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                 "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
        field_email.click()
        os.system('adb shell input text "akmalalhaqi123@gmail.com"')
        time.sleep(5)

        # klik field Password
        field_password = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                    "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")))
        field_password.click()
        os.system('adb shell input text "Test12345"')
        time.sleep(5)

        # Klik Tombol login
        login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
        login.click()
        time.sleep(10)
    except Exception as e:
        logging.error(f"Error dalam pengujian login: {e}")
        raise

def test_lihat_siswa(driver):
    try:
        wait = WebDriverWait(driver, 20)
        logging.info("Test Lihat Siswa")
        # Landing Page
        kliklanjut1 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut1.click()
        time.sleep(3)

        kliklanjut2 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut2.click()
        time.sleep(3)

        kliklanjut3 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut3.click()
        time.sleep(3)

        # Pilih Sekolah
        Pilih_sekolah = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
        Pilih_sekolah.click()
        time.sleep(3)

        # Temukan elemen menggunakan UiSelector
        value_sekolah = wait.until(lambda d: d.find_element(
            By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
        ))
        value_sekolah.click()
        time.sleep(3)

        # Klik Lanjut
        tombol_lanjut = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
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
        login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
        login.click()
        time.sleep(10)

        # Lihat Siswa
        lihat_siswa = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='Daftar Siswa']")))
        lihat_siswa.click()
        time.sleep(3)
    except Exception as e:
        logging.error(f"Error dalam pengujian lihat siswa: {e}")
        raise

def test_akses_breadcrums(driver):
    try:
        wait = WebDriverWait(driver, 20)
        logging.info("Test Breadcrums")
        # Landing Page
        kliklanjut1 = wait.until(
        EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut1.click()
        time.sleep(3)

        kliklanjut2 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut2.click()
        time.sleep(3)

        kliklanjut3 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut3.click()
        time.sleep(3)

        # Pilih Sekolah
        Pilih_sekolah = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
        Pilih_sekolah.click()
        time.sleep(3)

        # Temukan elemen menggunakan UiSelector
        value_sekolah = wait.until(lambda d: d.find_element(
            By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
        ))
        value_sekolah.click()
        time.sleep(3)

        # Klik Lanjut
        tombol_lanjut = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
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
        login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
        login.click()
        time.sleep(10)

        # Akses  Menu Pengumuman

        br_pengumuman = wait.until(lambda d: d.find_element(By.ACCESSIBILITY_ID, "Pengumuman"))
        br_pengumuman.click()
        time.sleep(5)

        # Akses breadcrums Pengumuman
        ngumumin = wait.until(lambda d: d.find_element(By.ACCESSIBILITY_ID, "Pengumuman"))
        ngumumin.click()
        time.sleep(3)

        # akses breadcrums Event

        br_event = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Event")'))
        br_event.click()
        time.sleep(5)

    except Exception as e:
        logging.error(f"Error dalam pengujian breadcrums: {e}")
        raise

def test_akses_event(driver):
    try:
        wait = WebDriverWait(driver, 20)
        logging.info("Test Akses Event")
        kliklanjut1 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut1.click()
        time.sleep(3)

        kliklanjut2 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut2.click()
        time.sleep(3)

        kliklanjut3 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut3.click()
        time.sleep(3)

        # Pilih Sekolah
        Pilih_sekolah = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
        Pilih_sekolah.click()
        time.sleep(3)

        # Temukan elemen menggunakan UiSelector
        value_sekolah = wait.until(lambda d: d.find_element(
            By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
        ))
        value_sekolah.click()
        time.sleep(3)

        # Klik Lanjut
        tombol_lanjut = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
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
        login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
        login.click()
        time.sleep(10)
        # Event
        menu_event = wait.until(
            lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Event")'))
        menu_event.click()
        time.sleep(5)

        # Pilih Breadcrums Event
        event = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Event")'))
        event.click()
        time.sleep(4)

        # Daftar UiSelector untuk Event
        event_selectors = [
            'new UiSelector().description("Workshop Pengembangan Diri untuk Siswa\nEvent\nDiterbitkan 28 January 2025")',
            'new UiSelector().description("Lomba Debat Bahasa Inggris\nEvent\nDiterbitkan 28 January 2025").instance(0)',
            'new UiSelector().description("Workshop Teknologi: Mengenal AI dan Robotika\nEvent\nDiterbitkan 28 January 2025")',
            'new UiSelector().description("Lomba Debat Bahasa Inggris\nEvent\nDiterbitkan 28 January 2025").instance(1)',
            'new UiSelector().description("Pelatihan Menulis Kreatif untuk Siswa\nEvent\nDiterbitkan 23 January 2025")',
            'new UiSelector().description("UMP DKI Jakarta 2025 naik 6, 5 persen\nEvent\nDiterbitkan 17 December 2024")',
            'new UiSelector().description("Ini Judul\nEvent\nDiterbitkan 16 December 2024")',
            'new UiSelector().description("Cari gweh coba\nEvent\nDiterbitkan 16 December 2024")'
        ]

        # Pilih salah satu event acak dan klik elemen tersebut
        selected_event = random.choice(event_selectors)

        # Tunggu dan temukan elemen yang dipilih
        try:
            logging.info(f"Menunggu dan mengklik event dengan selector: {selected_event}")
            event_element = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, selected_event))
            event_element.click()
            logging.info(f"Klik event berhasil: {selected_event}")
            time.sleep(5)
        except TimeoutException:
            logging.error(f"Gagal menemukan event dengan selector: {selected_event}")
    except Exception as e:
        logging.error(f"Error dalam pengujian akses event: {e}")
        raise

def test_akses_pengumuman(driver):
    try:
        wait = WebDriverWait(driver, 20)
        logging.info("Test Akses Pengumuman")

        kliklanjut1 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut1.click()
        time.sleep(3)

        kliklanjut2 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut2.click()
        time.sleep(3)

        kliklanjut3 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut3.click()
        time.sleep(3)

        # Pilih Sekolah
        Pilih_sekolah = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
        Pilih_sekolah.click()
        time.sleep(3)

        # Temukan elemen menggunakan UiSelector
        value_sekolah = wait.until(lambda d: d.find_element(
            By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
        ))
        value_sekolah.click()
        time.sleep(3)

        # Klik Lanjut
        tombol_lanjut = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
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
        login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
        login.click()
        time.sleep(10)

        # Event
        menu_event = wait.until(
            lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Event")'))
        menu_event.click()
        time.sleep(5)

        # Pengumuman
        pengumuman = wait.until(
            lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Pengumuman")'))
        pengumuman.click()
        time.sleep(4)

        # Pilih pengumuman secara acak berdasarkan accessibility-id
        random_pengumuman = [
            'Pendaftaran Ekstrakurikuler Dibuka!\nPengumuman\nDiterbitkan 28 January 2025',
            'Penggalangan Dana untuk Korban Bencana\nPengumuman\nDiterbitkan 28 January 2025',
            'Hari Guru Nasional: Acara dan Perayaan\nPengumuman\nDiterbitkan 28 January 2025',
            'Kegiatan Study Tour ke Museum Nasional\nPengumuman\nDiterbitkan 23 December 2024'
        ]

        # Pilih pengumuman secara acak
        selected_pengumuman_desc = random.choice(random_pengumuman)

        # Tunggu dan temukan elemen berdasarkan accessibility-id
        try:
            selected_pengumuman_element = wait.until(
                EC.presence_of_element_located(
                    (By.ACCESSIBILITY_ID, selected_pengumuman_desc)
                )
            )
            logging.info(f"Pengumuman yang dipilih: {selected_pengumuman_desc}")
            selected_pengumuman_element.click()
            logging.info("Pengumuman berhasil dipilih dan diklik.")
            time.sleep(7)

        except TimeoutException:
            logging.error(f"Gagal menemukan pengumuman dengan accessibility-id: {selected_pengumuman_desc}")

    except Exception as e:
        logging.error(f"Error dalam pengujian akses pengumuman: {e}")
        raise

def test_akses_faq(driver):
    try:
        wait = WebDriverWait(driver, 20)
        logging.info("Test FAQ")
        kliklanjut1 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut1.click()
        time.sleep(3)

        kliklanjut2 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut2.click()
        time.sleep(3)

        kliklanjut3 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut3.click()
        time.sleep(3)

        # Pilih Sekolah
        Pilih_sekolah = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
        Pilih_sekolah.click()
        time.sleep(3)

        # Temukan elemen menggunakan UiSelector
        value_sekolah = wait.until(lambda d: d.find_element(
            By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
        ))
        value_sekolah.click()
        time.sleep(3)

        # Klik Lanjut
        tombol_lanjut = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
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
        login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
        login.click()
        time.sleep(10)

        # Menu Pengaturan
        pengaturan = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='Pengaturan']")))
        pengaturan.click()
        time.sleep(4)

        # FAQ
        FAQ = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='FAQ']")))
        FAQ.click()
        time.sleep(4)

        # List of UiSelectors
        uiselectors = [
            'new UiSelector().description("Bagaimana cara membayarkan tagihan sekolah?")',
            'new UiSelector().description("Bagaimana cara mendownload nota pembayaran?")',
            'new UiSelector().description("Bagaimana cara mengubah data siswa?")',
            'new UiSelector().description("Apa yang harus dilakukan jika pembayaran gagal?")',
            'new UiSelector().description("Apakah ada biaya tambahan untuk setiap transaksi?")'
        ]

        # Klik setiap elemen secara acak dengan jeda setidaknya 10 detik
        random.shuffle(uiselectors)

        for uiselector in uiselectors:
            clicked = False
            attempts = 0
            while not clicked and attempts < 3:
                try:
                    element = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, uiselector))
                    element.click()
                    logging.info(
                        f"Klik berhasil pada elemen dengan deskripsi: {element.get_attribute('contentDescription')}")
                    clicked = True
                    time.sleep(10)  # Jeda setidaknya 10 detik
                except StaleElementReferenceException:
                    logging.warning(
                        f"StaleElementReferenceException: Elemen tidak lagi dalam DOM, mencoba lagi... (percobaan {attempts + 1})")
                    attempts += 1
                except Exception as e:
                    logging.error(f"Gagal mengklik elemen: {e}")
                    break
    except Exception as e:
        logging.error(f"Error dalam pengujian akses FAQ: {e}")
        raise

def test_kebijakan_privasi(driver):
    try:
        wait = WebDriverWait(driver, 20)
        logging.info("Test Kebijakan Privasi")
        kliklanjut1 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut1.click()
        time.sleep(3)

        kliklanjut2 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut2.click()
        time.sleep(3)

        kliklanjut3 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut3.click()
        time.sleep(3)

        # Pilih Sekolah
        Pilih_sekolah = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
        Pilih_sekolah.click()
        time.sleep(3)

        # Temukan elemen menggunakan UiSelector
        value_sekolah = wait.until(lambda d: d.find_element(
            By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
        ))
        value_sekolah.click()
        time.sleep(3)

        # Klik Lanjut
        tombol_lanjut = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
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
        login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
        login.click()
        time.sleep(10)

        # Menu Pengaturan
        pengaturan = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='Pengaturan']")))
        pengaturan.click()
        time.sleep(4)

        # Kebijakan Privasi
        privacy = wait.until(
            lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Kebijakan Privasi")'))
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
    except Exception as e:
        logging.error(f"Error dalam pengujian kebijakan privasi: {e}")
        raise
def test_ubah_password(driver):
    try:
        wait = WebDriverWait(driver, 20)
        logging.info("Test Ubah Password")
        kliklanjut1 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut1.click()
        time.sleep(3)

        kliklanjut2 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut2.click()
        time.sleep(3)

        kliklanjut3 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut3.click()
        time.sleep(3)

        # Pilih Sekolah
        Pilih_sekolah = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
        Pilih_sekolah.click()
        time.sleep(3)

        # Temukan elemen menggunakan UiSelector
        value_sekolah = wait.until(lambda d: d.find_element(
            By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
        ))
        value_sekolah.click()
        time.sleep(3)

        # Klik Lanjut
        tombol_lanjut = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
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
        login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
        login.click()
        time.sleep(10)

        # Menu Pengaturan
        pengaturan = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='Pengaturan']")))
        pengaturan.click()
        time.sleep(4)

        # Ubah Password
        ubah_password = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc='Ubah Password']")))
        ubah_password.click()
        time.sleep(4)

        # field password lama
        field_lama = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR,
                                                         'new UiSelector().className("android.widget.EditText").instance(0)'))
        field_lama.click()
        os.system('adb shell input text "Test12345"')
        time.sleep(3)

        # field pass baru
        pass_baru = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR,
                                                        'new UiSelector().className("android.widget.EditText").instance(1)'))
        pass_baru.click()
        os.system('adb shell input text "Test123456"')
        time.sleep(3)

        # konfirmasi pass baru
        konf_pass = wait.until(lambda d: d.find_element(By.ANDROID_UIAUTOMATOR,
                                                        'new UiSelector().className("android.widget.EditText").instance(2)'))
        konf_pass.click()
        os.system('adb shell input text "Test123456"')
        time.sleep(3)
    except Exception as e:
        logging.error(f"Error dalam pengujian ubah password: {e}")
        raise

def test_bayar_sumbangan(driver):
    try:
        wait = WebDriverWait(driver, 20)
        logging.info("Test Bayar Sumbangan")
        kliklanjut1 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut1.click()
        time.sleep(3)

        kliklanjut2 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut2.click()
        time.sleep(3)

        kliklanjut3 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut3.click()
        time.sleep(3)

        # Pilih Sekolah
        Pilih_sekolah = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
        Pilih_sekolah.click()
        time.sleep(3)

        # Temukan elemen menggunakan UiSelector
        value_sekolah = wait.until(lambda d: d.find_element(
            By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
        ))
        value_sekolah.click()
        time.sleep(3)

        # Klik Lanjut
        tombol_lanjut = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
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
        login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
        login.click()
        time.sleep(10)

        # Akses Tagihan
        tagihan = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//android.widget.ImageView[@content-desc='Tagihan'])[2]")))
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
            bayar_sumbangan = wait.until(
                lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Lanjutkan")'))
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
    except Exception as e:
        logging.error(f"Error dalam pengujian bayar sumbangan: {e}")
        raise

def test_bayar_tagihan(driver):
    try:
        wait = WebDriverWait(driver, 20)
        logging.info("Test Bayar Tagihan")
            # Landing Page
        kliklanjut1 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut1.click()
        time.sleep(3)

        kliklanjut2 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut2.click()
        time.sleep(3)

        kliklanjut3 = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
        kliklanjut3.click()
        time.sleep(3)

        # Pilih Sekolah
        Pilih_sekolah = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Pilih sekolah']")))
        Pilih_sekolah.click()
        time.sleep(3)

        # Temukan elemen menggunakan UiSelector
        value_sekolah = wait.until(lambda d: d.find_element(
            By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("PT Aigen Global Teknologi")'
        ))
        value_sekolah.click()
        time.sleep(3)

        # Klik Lanjut
        tombol_lanjut = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Lanjut']")))
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
        login = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Masuk']")))
        login.click()
        time.sleep(10)

        # Akses Tagihan
        tagihan = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//android.widget.ImageView[@content-desc='Tagihan'])[2]")))
        tagihan.click()
        time.sleep(5)

        # Pilih Tagihan yang akan dibayarkan
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
        button_bayar = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Bayar']")))
        button_bayar.click()
        time.sleep(4)

        # pop up lanjutkan pembayaran

        lanjut_bayar = wait.until(lambda d: d.find_element(
            By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Lanjut Bayar")'
        ))
        lanjut_bayar.click()
        time.sleep(4)

        # random choice pilih bank

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

        # Klik Bayar

        bayar_tagihan = wait.until(
            lambda d: d.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Bayar")'))
        bayar_tagihan.click()
        time.sleep(5)

    except Exception as e:
        logging.error(f"Error dalam pengujian bayar tagihan: {e}")
        raise

def test_riwayat_pembayaran(driver):
    try:
        wait = WebDriverWait(driver, 20)
        logging.info("Test Riwayat Pembayaran")
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
    except Exception as e:
        logging.error(f"Error dalam pengujian bayar tagihan: {e}")
        raise

def run_regression_test():
    driver = setup_driver()

    try:
        test_login(driver)
        driver.quit()

        driver = setup_driver()
        test_lihat_siswa(driver)
        driver.quit()

        driver = setup_driver()
        test_akses_breadcrums(driver)
        driver.quit()


        driver= setup_driver()
        test_bayar_tagihan(driver)
        driver.quit()

        driver = setup_driver()
        test_bayar_sumbangan(driver)
        driver.quit()


        driver = setup_driver()
        test_riwayat_pembayaran(driver)
        driver.quit()

        driver = setup_driver()
        test_akses_event(driver)
        driver.quit()

        driver = setup_driver()
        test_akses_pengumuman(driver)
        driver.quit()

        driver = setup_driver()
        test_akses_faq(driver)
        driver.quit()

        driver = setup_driver()
        test_ubah_password(driver)
        driver.quit()

        driver = setup_driver()
        test_kebijakan_privasi(driver)
        driver.quit()

        logging.info("Semua Test Regresi Berhasil")

    except Exception as e:
        logging.error(f"Pengujian Gagal: {e}")


    finally:
        # Pastikan driver ditutup jika ada error
        if 'driver' in locals():
            driver.quit()


if __name__ == "__main__":
    run_regression_test()

