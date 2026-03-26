import os
import pytest

def test_simple_form(page):
    page.goto("https://www.testmuai.com/selenium-playground/")

    page.get_by_role("link", name="Simple Form Demo").click()

    assert "simple-form-demo" in page.url
    message = os.getenv("MESSAGE", "Welcome to TestMu AI")

    page.wait_for_selector("#user-message", state="visible")
    page.fill("#user-message", message)
    page.wait_for_selector("#showInput", state="visible")
    page.click("#showInput")

    page.wait_for_timeout(3000)

    actual = page.locator("#message").text_content()
    assert actual.strip() == message, f"Expected '{message}', got '{actual}'"
