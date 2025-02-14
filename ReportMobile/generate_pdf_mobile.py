import json
import os
import shutil
import subprocess
import sys

import allure
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
import zipfile

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from RegressionMobile.Test_Regression import screenshot_dir

# Path configurations
ALLURE_REPORT_DATA = "allure-report/data/test-cases"
ATTACHMENTS_PATH = "allure-report/data/attachments"
ALLURE_RESULTS = "allure-results"
ALLURE_REPORT = "allure-report"
OUTPUT_PDF = "allure_steps_report1.pdf"
ZIP_FILE = "regression_report1.zip"
SCREENSHOT_DIR = "screenshots"  # Path for storing screenshots

# Mengubah directory screenshot sesuai dengan struktur yang diinginkan
screenshot_dir = os.path.join(os.getcwd(), "ReportMobile/Reports/screenshots")

def run_tests():
    """ Menjalankan pytest dan generate report allure """
    print("Menjalankan pytest...")
    try:
        result = subprocess.run(
            ["pytest", f"--alluredir={ALLURE_RESULTS}","C:\\Users\\akmal\\PycharmProjects\\PythonProject5\\RegressionMobile\\Test_Regression.py"],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        print("Pytest berhasil dijalankan.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Pytest failed with exit code {e.returncode}")
        print(e.stderr)
        raise SystemExit("Pytest gagal dijalankan.")

    print("Menghasilkan laporan Allure...")
    allure_executable = shutil.which("allure")
    if not allure_executable:
        print("Allure executable not found. Please install Allure CLI.")
        return

    try:
        subprocess.run(
            [allure_executable, "generate", ALLURE_RESULTS, "-o", ALLURE_REPORT, "--clean"],
            check=True
        )
        print("Laporan Allure berhasil dibuat.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Allure report generation: {e}")
        raise SystemExit("Gagal membuat laporan Allure.")

def extract_steps_and_screenshots():
    test_cases = []

    if not os.path.exists(ALLURE_REPORT_DATA):
        print(f"Error: Folder tidak ditemukan: {ALLURE_REPORT_DATA}")
        return test_cases

    for filename in os.listdir(ALLURE_REPORT_DATA):
        if filename.endswith(".json"):
            with open(os.path.join(ALLURE_REPORT_DATA, filename), "r", encoding="utf-8") as file:
                data = json.load(file)
                print(f"Membaca file: {filename}")  # Debug

                test_name = data.get("name", "Unknown Test")
                steps = []

                stages = data.get("beforeStages", []) + [data.get("testStage", {})] + data.get("afterStages", [])

                for stage in stages:
                    for step in stage.get("steps", []):
                        step_name = step.get("name", "Unknown Step")
                        status = step.get("status", "Unknown Status")
                        attachments = step.get("attachments", [])

                        screenshots = []
                        for attachment in attachments:
                            if attachment["name"] == "Screenshot" or attachment["type"] == "image/png":
                                screenshot_path = os.path.join(ATTACHMENTS_PATH, attachment["source"])
                                print(f"Memeriksa screenshot di path: {screenshot_path}")  # Log tambahan
                                if os.path.exists(screenshot_path):
                                    screenshots.append(screenshot_path)
                                    print(f"Screenshot ditemukan: {screenshot_path}")
                                else:
                                    print(f"Screenshot tidak ditemukan: {screenshot_path}")

                        steps.append({"name": step_name, "status": status, "screenshots": screenshots})

                test_cases.append({"name": test_name, "steps": steps})

    return test_cases


def create_pdf(test_cases):
    c = canvas.Canvas(OUTPUT_PDF, pagesize=letter)
    width, height = letter
    y_position = height - 40

    for test in test_cases:
        c.setFont("Helvetica-Bold", 12)
        c.drawString(40, y_position, f"Test: {test['name']}")
        y_position -= 20

        if not test["steps"]:
            c.drawString(60, y_position, "Tidak ada langkah ditemukan!")
            y_position -= 20

        for step in test["steps"]:
            c.setFont("Helvetica", 10)
            c.drawString(60, y_position, f"Step: {step['name']} - Status: {step['status']}")
            y_position -= 30

            if step["screenshots"]:
                for screenshot in step["screenshots"]:
                    screenshot_path = screenshot  # Use screenshot directly, as it is already the full path
                    if os.path.exists(screenshot_path):
                        try:
                            img = ImageReader(screenshot_path)
                            img_width, img_height = img.getSize()
                            aspect_ratio = img_width / img_height
                            max_width = 300
                            max_height = 200

                            # Sesuaikan ukuran gambar jika terlalu besar
                            if img_width > max_width or img_height > max_height:
                                if img_width > img_height:
                                    img_width = max_width
                                    img_height = img_width / aspect_ratio
                                else:
                                    img_height = max_height
                                    img_width = img_height * aspect_ratio

                            # Jika gambar terlalu besar, buat halaman baru
                            if img_height > (y_position - 40):
                                c.showPage()
                                y_position = height - 40

                            c.drawImage(img, 80, y_position - img_height, width=img_width, height=img_height)
                            y_position -= img_height + 20
                        except Exception as e:
                            c.drawString(60, y_position, f"Gambar gagal ditampilkan: {e}")
                            y_position -= 20
                    else:
                        c.drawString(60, y_position, "Screenshot tidak ditemukan!")
                        y_position -= 20

            y_position -= 10

        y_position -= 20
        if y_position < 100:
            c.showPage()
            y_position = height - 80

    c.save()

def create_zip():
    with zipfile.ZipFile(ZIP_FILE, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(OUTPUT_PDF, OUTPUT_PDF)

        for root, dirs, files in os.walk("allure-report"):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, "allure-report")
                zipf.write(file_path, arcname)

def main():
    try:
        run_tests()
        test_cases = extract_steps_and_screenshots()
        create_pdf(test_cases)
        create_zip()
        print("Laporan PDF dan ZIP berhasil dibuat.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        raise SystemExit("Program dihentikan karena kesalahan.")

if __name__ == "__main__":
    main()
