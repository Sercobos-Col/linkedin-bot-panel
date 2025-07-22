from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def run_bot(email, password, keywords, ubicacion):
    options = Options()
    options.add_argument("--headless")  # Ejecutar en modo sin interfaz gráfica
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    # Iniciar sesión en LinkedIn
    driver.get("https://www.linkedin.com/login")
    driver.find_element("id", "username").send_keys(email)
    driver.find_element("id", "password").send_keys(password)
    driver.find_element("xpath", "//button[@type='submit']").click()
    time.sleep(3)

    # Buscar empleos
    driver.get("https://www.linkedin.com/jobs")
    driver.find_element("xpath", '//*[@placeholder="Buscar empleos"]').send_keys(keywords)
    driver.find_element("xpath", '//*[@placeholder="Ubicación"]').send_keys(ubicacion)
    driver.find_element("xpath", '//button[@aria-label="Buscar"]').click()
    time.sleep(5)

    # Lógica de aplicar a trabajos (scraping)
    print("✅ Bot ejecutado con éxito 🚀")

    driver.quit()
