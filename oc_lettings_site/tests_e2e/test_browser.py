import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://example.com")
        await page.screenshot(path="example.png", full_page=True)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
