import pytest

def test_input_form_submit(page):
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Input Form Submit").click()
    page.wait_for_load_state("networkidle")

    # Wait for form to be visible
    page.wait_for_selector("#name", state="visible")

    page.get_by_role("button", name="Submit").click()

    validation = page.locator("#name").evaluate(
        "el => el.validationMessage"
    )
    assert validation != "", f"Expected validation message, got: {validation}"
    assert "fill out this field" in validation.lower()

    page.locator("#name").fill("John Doe")
    page.locator("#inputEmail4").fill("johndoe@example.com")
    page.locator("#inputPassword4").fill("Password123")
    page.locator("#company").fill("TestMu AI")
    page.locator("#websitename").fill("www.example.com")
    page.locator("select[name='country']").select_option(label="United States")
    page.locator("#inputCity").fill("San Jose")
    page.locator("#inputAddress1").fill("123 Main Street")
    page.locator("#inputAddress2").fill("Suite 400")
    page.locator("#inputState").fill("California")
    page.locator("#inputZip").fill("95101")

    page.get_by_role("button", name="Submit").click()

    # Wait until success message appears
    page.wait_for_selector(".success-msg", state="visible")
    success_msg = page.locator(".success-msg").text_content()
    assert "Thanks for contacting us, we will get back to you shortly." in success_msg, \
        f"Unexpected message: {success_msg}"
