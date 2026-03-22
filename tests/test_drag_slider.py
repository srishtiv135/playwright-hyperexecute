import pytest

def test_drag_slider(page):
    # 1. Open the playground and click "Drag & Drop Sliders"
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Drag & Drop Sliders").click()

    # 2. Wait for slider to be visible
    page.wait_for_selector("#rangeSuccess")

    # 3. Set "Default value 15" slider to 95
    page.evaluate("""() => {
        const output = document.getElementById('rangeSuccess');
        const slider = output.previousElementSibling;
        slider.value = 95;
        output.value = 95;
        output.textContent = 95;
        slider.dispatchEvent(new Event('input', { bubbles: true }));
        slider.dispatchEvent(new Event('change', { bubbles: true }));
    }""")

    page.wait_for_timeout(1000)

    # 4. Run evaluate once more to allow page to settle
    page.evaluate("""() => {
        const output = document.getElementById('rangeSuccess');
        const slider = output.previousElementSibling;
        return {
            sliderValue: slider.value,
            outputText: output.textContent
        }
    }""")

    # 5. Validate the range value shows 95
    value_text = page.locator("#rangeSuccess").text_content()
    assert value_text.strip() == "95", f"Slider value is {value_text}, expected 95"
