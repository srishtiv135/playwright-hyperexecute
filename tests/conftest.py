import pytest
from playwright.sync_api import sync_playwright
import os
import json
import urllib.parse

@pytest.fixture
def page():
    with sync_playwright() as p:

        lt_username = os.getenv("LT_USERNAME", "")
        lt_access_key = os.getenv("LT_ACCESS_KEY", "")

        capabilities = {
            "browserName": "Chrome",
            "browserVersion": "latest",
            "LT:Options": {
                "username": lt_username,
                "accessKey": lt_access_key,
                "platformName": "Windows 10",
                "project": "TestMu Playwright Assignment",
                "build": "Playwright HyperExecute Build",
                "name": "TestMu AI Playground Tests",
                "network": True,
                "video": True,
                "screenshot": True,
                "console": True,
                "w3c": True
            }
        }

        browser = p.chromium.connect(
            f"wss://cdp.lambdatest.com/playwright?capabilities="
            f"{urllib.parse.quote(json.dumps(capabilities))}"
        )

        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
