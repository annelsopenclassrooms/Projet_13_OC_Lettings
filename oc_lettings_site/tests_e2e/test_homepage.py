def test_homepage_visual(page):
    page.goto("http://localhost:8000/")
    assert page.title() == "Welcome"  # vérifie le <title>
    page.screenshot(path="tests_e2e/screenshots/homepage.png")
    assert page.locator("h1").inner_text() == "Welcome"
