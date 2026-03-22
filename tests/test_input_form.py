import pytest

def test_input_form_submit(page):
    # 1. Open the playground and click "Input Form Submit"
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Input Form Submit").click()
    page.wait_for_load_state("networkidle")

    # Debug: find all buttons and inputs on the page
    elements = page.evaluate("""() => {
        const buttons = [...document.querySelectorAll('button, input[type=submit]')]
            .map(el => ({ tag: el.tagName, id: el.id, type: el.type, text: el.textContent.trim(), name: el.name }))
        const fields = [...document.querySelectorAll('input, select, textarea')]
            .map(el => ({ tag: el.tagName, id: el.id, name: el.name, type: el.type, placeholder: el.placeholder }))
        return { buttons, fields }
    }""")
    print("BUTTONS:", elements['buttons'])
    print("FIELDS:", elements['fields'])

    assert False, "Debug run - check logs"
