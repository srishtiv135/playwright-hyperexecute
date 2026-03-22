import pytest
from playwright.sync_api import expect

def test_input_form_submit(page):
    # 1. Open the playground and click "Input Form Submit"
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Input Form Submit").click()

    # 2. Wait for the form to appear
    form = page.locator("form").first
    form.wait_for(state="visible")

    # 3. Click Submit without filling any info to trigger validation
    form.get_by_role("button", name="Submit").click()

    # 4. Assert that at least one input shows validation error
    required_input = form.locator("input:invalid").first
    assert required_input, "Expected validation error message"

    # 5. Fill in all required fields
    form.locator("input[name='name']").fill("John Doe")
    form.locator("input[name='email']").fill("johndoe@example.com")
    form.locator("input[name='password']").fill("Password123")
    form.locator("input[name='company']").fill("TestMu AI")
    form.locator("input[name='website']").fill("www.example.com")

    # 6. Select Country: United States
    form.locator("select[name='country']").select_option(label="United States")

    # 7. Fill Comment
    form.locator("textarea[name='comment']").fill("This is a test")

    # 8. Click Submit
    form.get_by_role("button", name="Submit").click()

    # 9. Validate the success message
    success_msg = page.locator("div.success").text_content()
    assert "Thanks for contacting us" in success_msg