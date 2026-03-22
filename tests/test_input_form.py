import pytest

def test_input_form_submit(page):
    # 1. Open the playground and click "Input Form Submit"
    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_role("link", name="Input Form Submit").click()
    page.wait_for_load_state("networkidle")

    # 2. Click Submit without filling any info
    page.get_by_role("button", name="Submit").click()

    # 3. Assert validation error on first required field
    validation = page.locator("#name").evaluate(
        "el => el.validationMessage"
    )
    assert validation != "", f"Expected validation message, got: {validation}"
    assert "fill in this field" in validation.lower(), \
        f"Expected 'fill in this field', got: {validation}"

    # 4. Fill all required fields
    page.locator("#name").fill("John Doe")
    page.locator("#inputEmail4").fill("johndoe@example.com")
    page.locator("#inputPassword4").fill("Password123")
    page.locator("#company").fill("TestMu AI")
    page.locator("#websitename").fill("www.example.com")

    # 5. Select Country: United States by text
    page.locator("select[name='country']").select_option(label="United States")

    # 6. Fill remaining fields
    page.locator("#inputCity").fill("San Jose")
    page.locator("#inputAddress1").fill("123 Main Street")
    page.locator("#inputAddress2").fill("Suite 400")
    page.locator("#inputState").fill("California")
    page.locator("#inputZip").fill("95101")

    # 7. Click Submit
    page.get_by_role("button", name="Submit").click()

    # 8. Validate success message
    page.wait_for_timeout(2000)
    success_m
