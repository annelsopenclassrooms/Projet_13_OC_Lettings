from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:8000"

PAGES = [
    "lettings/",
    "profiles/",
    "lettings/2/",
    "profiles/DavWin/"
]

def capture_pages():
    screenshots_dir = Path("oc_lettings_site") / "tests_e2e" / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for path in PAGES:
            url = f"{BASE_URL}/{path.lstrip('/')}"
            print(f"Ouverture de : {url}")
            page.goto(url)

            filename = path.strip("/").replace("/", "_") or "index"
            screenshot_path = screenshots_dir / f"{filename}.png"

            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"Capture sauvegardée dans : {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    capture_pages()
