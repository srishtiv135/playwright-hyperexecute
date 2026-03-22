import pytest
from playwright.sync_api import expect

def test_drag_slider(page):
    # 1. Open the playground and click "Drag & Drop Sliders"
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Drag & Drop Sliders").click()

    # 2. Get the first slider (Default value 15)
    slider = page.locator("input[type='range']").nth(0)

    # 3. Set value to 95 using JavaScript (most reliable way)
    page.evaluate("""
        const slider = document.querySelectorAll("input[type='range']")[0];
        slider.value = 95;
        slider.dispatchEvent(new Event('input', { bubbles: true }));
        slider.dispatchEvent(new Event('change', { bubbles: true }));
    """)

    # 4. Wait for the display to update
    page.wait_for_timeout(500)

    # 5. Validate the range value shows 95
    value_text = page.locator("#rangeSuccess").text_content()
    assert value_text.strip() == "95", f"Slider value is {value_text}, expected 95"
