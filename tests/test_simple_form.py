import os
import pytest
from playwright.sync_api import expect

def test_simple_form(page):
    # 1. Open the Selenium Playground page
    page.goto("https://www.testmuai.com/selenium-playground/")

    # 2. Click “Simple Form Demo”
    page.get_by_role("link", name="Simple Form Demo").click()

    # 3. Validate URL contains "simple-form-demo"
    #expect(page).to_have_url(lambda url: "simple-form-demo" in url)
    assert "simple-form-demo" in page.url

    # 4. Variable for message
    message = os.getenv("MESSAGE", "Welcome to TestMu AI")

    # 5. Enter value in the text box
    page.fill("#user-message", message)

    # 6. Click "Get Checked Value"
    page.click("#showInput")

    # 7. Validate the same message is displayed
    expect(page.locator("#message")).to_have_text(message)