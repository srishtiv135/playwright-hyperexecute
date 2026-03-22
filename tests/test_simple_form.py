import os
import pytest
from playwright.sync_api import expect

def test_simple_form(page):
    # 1. Open the Selenium Playground page
    page.goto("https://www.testmuai.com/selenium-playground/")

    # 2. Click "Simple Form Demo"
    page.get_by_role("link", name="Simple Form Demo").click()

    # 3. Validate URL contains "simple-form-demo"
    assert "simple-form-demo" in page.url

    # 4. Variable for message
    message = os.getenv("MESSAGE", "Welcome to TestMu AI")

    # 5. Enter value in the text box
    page.wait_for_selector("#user-message")
    page.fill("#user-message", message)

    # 6. Click "Get Checked Value"
    page.wait_for_selector("#showInput")
    page.click("#showInput")

    # 7. Wait for message to appear then validate
    page.wait_for_timeout(1000)
    page.wait_for_selector("#message")
    actual = page.locator("#message").text_content()
    assert actual.strip() == message, f"Expected '{message}', got '{actual}'"
