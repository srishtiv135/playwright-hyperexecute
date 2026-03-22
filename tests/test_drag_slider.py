import pytest
from playwright.sync_api import expect

def test_drag_slider(page):
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Drag & Drop Sliders").click()

    # Debug: print all text content around sliders
    result = page.evaluate("""
        const slider = document.querySelectorAll("input[type='range']")[0];
        const parent = slider.closest('.sp__range') || slider.parentElement;
        return {
            sliderValue: slider.value,
            sliderMin: slider.min,
            sliderMax: slider.max,
            parentHTML: parent.outerHTML
        }
    """)
    print("DEBUG:", result)

    # Set value
    page.evaluate("""
        const slider = document.querySelectorAll("input[type='range']")[0];
        slider.value = 95;
        slider.dispatchEvent(new Event('input', { bubbles: true }));
        slider.dispatchEvent(new Event('change', { bubbles: true }));
    """)

    page.wait_for_timeout(1000)

    # Debug: check all elements with IDs near the slider
    ids = page.evaluate("""
        return [...document.querySelectorAll('[id]')]
            .map(el => ({ id: el.id, text: el.textContent.trim() }))
            .filter(el => el.text.length < 10)
    """)
    print("ALL IDs with short text:", ids)

    assert False, "Debug run - check logs for element IDs"
