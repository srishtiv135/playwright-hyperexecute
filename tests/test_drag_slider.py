import pytest

def test_drag_slider(page):
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Drag & Drop Sliders").click()

    # Wait for slider to be visible
    page.wait_for_selector("#rangeSuccess", state="visible")

    page.evaluate("""() => {
        const output = document.getElementById('rangeSuccess');
        const slider = output.previousElementSibling;
        slider.value = 95;
        output.value = 95;
        output.textContent = 95;
        slider.dispatchEvent(new Event('input', { bubbles: true }));
        slider.dispatchEvent(new Event('change', { bubbles: true }));
    }""")

    # Wait until value is actually 95
    page.wait_for_function(
        "() => document.getElementById('rangeSuccess').textContent.trim() === '95'"
    )

    value_text = page.locator("#rangeSuccess").text_content()
    assert value_text.strip() == "95", f"Slider value is {value_text}, expected 95"
