import pytest
from playwright.sync_api import expect

def test_drag_slider(page):
    # 1. Open the playground and click "Drag & Drop Sliders"
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Drag & Drop Sliders").click()

    slider = page.locator("input[type='range']").nth(0)  # first slider on page
    slider.fill("95")                                  # set value directly
    slider.dispatch_event("change")                    # trigger JS update      

    # Validate the range value shows 95
    value_text = page.locator("#range").text_content()
    assert value_text == "95", f"Slider value is {value_text}, expected 95"