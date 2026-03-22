import pytest
from playwright.sync_api import expect

def test_input_form_submit(page):
    # 1. Open the playground and click "Input Form Submit"
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Input Form Submit").click()

    # 2. Wait for page to load
    page.wait_for_load_state("networkidle")

    # 3. Click Submit without filling any info
    page.locator("#submit").click()

    # 4. Assert validation error on first required field
    validation = page.locator("#inputFirstName").evaluate(
        "el => el.validationMessage"
    )
    assert "fill in this field" in validation.lower() or validation != "", \
        f"Expected validation message, got: {validation}"

    # 5. Fill all required fields
    page.locator("#inputFirstName").fill("John")
    page.locator("#inputLastName").fill("Doe")
    page.locator("#inputEmail").fill("johndoe@example.com")
    page.locator("#mobileid").fill("9876543210")
    page.locator("#inputCity").fill("San Jose")
    page.locator("#inputAddress1").fill("123 Main Street")
    page.locator("#inputAddress2").fill("Suite 400")
    page.locator("#inputState").fill("California")
    page.locator("#inputZip").fill("95101")

    # 6. Select Country: United States by text
    page.locator("select[name='country']").select_option(label="United States")

    # 7. Click Submit
    page.locator("#submit").click()

    # 8. Validate success message
    success_msg = page.locator(".success-msg").text_content()
    assert "Thanks for contacting us, we will get back to you shortly." in success_msg, \
        f"Unexpected message: {success_msg}"
