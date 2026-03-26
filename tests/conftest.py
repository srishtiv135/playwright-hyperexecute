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
        use_lt = os.getenv("USE_LT_CLOUD", "false").lower() == "true"

        # Debug prints - remove after fixing
        print(f"\nUSE_LT_CLOUD: {use_lt}")
        print(f"LT_USERNAME set: {bool(lt_username)}")
        print(f"LT_ACCESS_KEY set: {bool(lt_access_key)}")

        if use_lt and lt_username and lt_access_key:
            capabilities = {
                "browserName": "Chrome",
                "browserVersion": "latest",        # FIXED: was "dev"
                "LT:Options": {
                    "username": lt_username,
                    "accessKey": lt_access_key,
                    "visual": True,
                    "video": True,
                    "network": True,
                    "console": True,
                    "platformName": os.getenv("LT_OS", "Windows 10"),  # FIXED: from env
                    "build": "Playwright HyperExecute Build",
                    "project": "TestMu Playwright Assignment",
                    "name": "TestMu AI Playground Tests",
                    "w3c": True,
                    "plugin": "python-pytest"
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

        else:
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
            context.tracing.stop(path="test-results/trace.zip")
            context.close()
            browser.close()
