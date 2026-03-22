import pytest

def test_drag_slider(page):
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Drag & Drop Sliders").click()

    # Debug: find the correct display element
    result = page.evaluate("""() => {
        const slider = document.querySelectorAll("input[type='range']")[0];
        const parent = slider.parentElement;
        return {
            sliderValue: slider.value,
            parentHTML: parent.outerHTML
        }
    }""")
    print("DEBUG:", result)

    # Set slider value to 95
    page.evaluate("""() => {
        const slider = document.querySelectorAll("input[type='range']")[0];
        slider.value = 95;
        slider.dispatchEvent(new Event('input', { bubbles: true }));
        slider.dispatchEvent(new Event('change', { bubbles: true }));
    }""")

    page.wait_for_timeout(1000)

    # Debug: find all IDs with short text
    ids = page.evaluate("""() => {
        return [...document.querySelectorAll('[id]')]
            .map(el => ({ id: el.id, text: el.textContent.trim() }))
            .filter(el => el.text.length < 10)
    }""")
    print("ALL IDs:", ids)

    assert False, "Debug run - check logs"
