import os
import platform
from pathlib import Path
from playwright.sync_api import sync_playwright

# Détection OS
OS_NAME = platform.system()
print(f"Exécution sur : {OS_NAME}")

# URL configurable via variable d'environnement ou valeur par défaut
BASE_URL = os.getenv("TEST_URL", "http://localhost:8000/")

def capture_homepage_reference():
    # Chemin fixe vers oc_lettings_site/tests_e2e/screenshots
    screenshots_dir = Path("oc_lettings_site") / "tests_e2e" / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    screenshot_path = screenshots_dir / "homepage_reference.png"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"Ouverture de : {BASE_URL}")
        page.goto(BASE_URL)

        page.screenshot(path=str(screenshot_path), full_page=True)
        print(f"Capture sauvegardée dans : {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    capture_homepage_reference()
