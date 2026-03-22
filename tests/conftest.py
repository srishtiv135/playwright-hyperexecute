import pytest
from playwright.sync_api import sync_playwright
import os

@pytest.fixture
def page():
    with sync_playwright() as p:
        
        lt_username = os.getenv("LT_USERNAME", "")
        lt_access_key = os.getenv("LT_ACCESS_KEY", "")

        # LambdaTest capabilities with all required options enabled
        capabilities = {
            "browserName": "Chrome",
            "browserVersion": "latest",
            "LT:Options": {
                "username": lt_username,
                "accessKey": lt_access_key,
                "platform": "Windows 10",
                "build": "Playwright Assignment Build",
                "name": "TestMu AI Playground Tests",
                "network": True,        # network logs ✅
                "video": True,          # video recording ✅
                "screenshot": True,     # screenshots ✅
                "console": True,        # console logs ✅
                "tunnel": False,
                "tunnelName": "",
                "geoLocation": "",
            }
        }

        # Connect to LambdaTest cloud if credentials exist
        # otherwise run locally
        if lt_username and lt_access_key:
            browser = p.chromium.connect(
                f"wss://cdp.lambdatest.com/playwright?capabilities="
                f"{__import__('urllib.parse', fromlist=['quote']).quote(__import__('json').dumps(capabilities))}"
            )
            context = browser.new_context()
        else:
            # Local run
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                record_video_dir="test-results/videos/",
            )
            context.tracing.start(
                screenshots=True,
                snapshots=True,
                sources=True
            )

        page = context.new_page()
        yield page

        if lt_username and lt_access_key:
            page.close()
            browser.close()
        else:
            context.tracing.stop(path="test-results/trace.zip")
            context.close()
            browser.close()
