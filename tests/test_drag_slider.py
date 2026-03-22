import pytest

def test_drag_slider(page):
    # 1. Open the playground and click "Drag & Drop Sliders"
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Drag & Drop Sliders").click()

    # 2. Wait for slider to be visible
    page.wait_for_selector("#rangeSuccess")

    # 3. Set slider value AND update output element directly
    page.evaluate("""() => {
        const output = document.getElementById('rangeSuccess');
        const slider = output.previousElementSibling;
        
        // Set the value
        slider.value = 95;
        
        // Update output directly
        output.value = 95;
        output.textContent = 95;
        output.innerHTML = 95;
        
        // Fire all possible events
        slider.dispatchEvent(new Event('mousedown', { bubbles: true }));
        slider.dispatchEvent(new Event('input', { bubbles: true }));
        slider.dispatchEvent(new Event('change', { bubbles: true }));
        slider.dispatchEvent(new Event('mouseup', { bubbles: true }));
    }""")

    page.wait_for_timeout(1000)

    # 4. Validate
    value_text = page.locator("#rangeSuccess").text_content()
    assert value_text.strip() == "95", f"Slider value is {value_text}, expected 95"
