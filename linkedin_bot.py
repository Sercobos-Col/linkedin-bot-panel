from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def run_bot(email, password, keywords, ubicacion):
    # Configurar opciones para correr sin interfaz gráfica (ideal para la nube)
    options = Options()
    options.add_argument("--headless")  # Modo sin ventana
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # Crear el driver con WebDriver Manager (descarga automática del driver correcto)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    try:
        # Lógica de inicio de sesión, búsqueda y aplicación
        driver.get("https://www.linkedin.com/login")
        time.sleep(2)

        # Autenticación
        driver.find_element("id", "username").send_keys(email)
        driver.find_element("id", "password").send_keys(password)
        driver.find_element("xpath", "//button[@type='submit']").click()
        time.sleep(3)

        # Aquí va tu lógica para búsqueda de empleo, etc.
        print("Bot iniciado correctamente. 🧠🚀")

    except Exception as e:
        print(f"Error al ejecutar el bot: {e}")

    finally:
        driver.quit()
