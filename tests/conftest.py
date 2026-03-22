# tests/conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        page.close()
        browser.close()
```

**What this does in simple words:**
- It tells pytest *"when a test asks for `page`, here's how to create it"*
- It opens a Chrome browser (headless = invisible, no screen needed)
- It gives the browser page to your test
- After the test finishes, it closes everything cleanly

---

## Your folder should now look like this
```
tests/
├── conftest.py          ← NEW file you just created
├── test_simple_form.py
├── test_slider.py
├── test_input_form.py
```

---

## Also check your `requirements.txt`

Can you paste what's inside it? It needs to have these lines at minimum:
```
pytest
playwright
pytest-playwright
