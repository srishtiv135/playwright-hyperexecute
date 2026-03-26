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

        # Debug prints
        print(f"\nUSE_LT_CLOUD: {use_lt}")
        print(f"LT_USERNAME set: {bool(lt_username)}")
        print(f"LT_ACCESS_KEY set: {bool(lt_access_key)}")
        print(f"USERNAME first 4 chars: {lt_username[:4]}")
        print(f"ACCESS KEY first 4 chars: {lt_access_key[:4]}")

        if use_lt and lt_username and lt_access_key:
            capabilities = {
                "browserName": "Chrome",
                "browserVersion": "latest",
                "LT:Options": {
                    "username": lt_username,
                    "accessKey": lt_access_key,
                    "visual": True,
                    "video": True,
                    "network": True,
                    "console": True,
                    "platformName": os.getenv("LT_OS", "Windows 10"),
                    "build": "Playwright HyperExecute Build",
                    "project": "TestMu Playwright Assignment",
                    "name": "TestMu AI Playground Tests",
                    "w3c": True,
                    "plugin": "python-pytest"
                }
            }

            ws_url = f"wss://cdp.lambdatest.com/playwright?capabilities={urllib.parse.quote(json.dumps(capabilities))}"

            print(f"Connecting to: wss://cdp.lambdatest.com/playwright")
            print(f"Username: {lt_username[:4]}***")

            browser = p.chromium.connect(ws_url)
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
