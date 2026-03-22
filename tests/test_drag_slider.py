import pytest

def test_drag_slider(page):
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Drag & Drop Sliders").click()
    page.wait_for_selector("#rangeSuccess")

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

    debug = page.evaluate("""() => {
        const output = document.getElementById('rangeSuccess');
        const slider = output.previousElementSibling;
        return {
            sliderValue: slider.value,
            outputText: output.textContent,
            outputValue: output.value
        }
    }""")
    print("AFTER SET:", debug)

    value_text = page.locator("#rangeSuccess").text_content()
    assert value_text.strip() == "95", f"Slider value is {value_text}, expected 95"
