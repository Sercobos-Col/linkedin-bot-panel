from playwright.sync_api import sync_playwright
import time

def run_bot(email, password, keywords, ubicacion):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Iniciar sesión en LinkedIn
        page.goto("https://www.linkedin.com/login")
        page.fill('input[name="session_key"]', email)
        page.fill('input[name="session_password"]', password)
        page.click('button[type="submit"]')

        # Esperar carga
        page.wait_for_load_state('networkidle')
        time.sleep(3)

        # Buscar ofertas
        page.goto("https://www.linkedin.com/jobs")
        page.wait_for_load_state('networkidle')
        page.fill('input[placeholder="Buscar empleos"]', keywords)
        page.fill('input[placeholder="Ubicación"]', ubicacion)
        page.keyboard.press("Enter")
        time.sleep(5)

        # Aquí va tu lógica para aplicar a ofertas (scraping de ofertas)
        print("✅ Bot ejecutado con éxito 🚀")

        browser.close()
