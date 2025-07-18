from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run_bot(email, password, keywords, ubicacion):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # 🔧 AQUÍ la corrección definitiva:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
