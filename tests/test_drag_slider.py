import pytest

def test_drag_slider(page):
    # 1. Open the playground and click "Drag & Drop Sliders"
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Drag & Drop Sliders").click()

    # 2. Target the slider whose output id is "rangeSuccess" (Default value 15)
    page.evaluate("""() => {
        const output = document.getElementById('rangeSuccess');
        const slider = output.previousElementSibling;
        slider.value = 95;
        slider.dispatchEvent(new Event('input', { bubbles: true }));
        slider.dispatchEvent(new Event('change', { bubbles: true }));
    }""")

    page.wait_for_timeout(500)

    # 3. Validate the display shows 95
    value_text = page.locator("#rangeSuccess").text_content()
    assert value_text.strip() == "95", f"Slider value is {value_text}, expected 95"
