import pytest
from playwright.sync_api import sync_playwright
import os
import json
import urllib.parse


@pytest.fixture
def page():
    with sync_playwright() as p:

        # ✅ DEFINE VARIABLES FIRST
        lt_username = os.getenv("LT_USERNAME", "")
        lt_access_key = os.getenv("LT_ACCESS_KEY", "")
        use_lt = os.getenv("USE_LT_CLOUD", "false").lower() == "true"

        if use_lt and lt_username and lt_access_key:

            # ✅ CAPABILITIES INSIDE FIXTURE
            capabilities = {
                "browserName": "Chrome",
                "browserVersion": "latest",
                "LT:Options": {
                    "user": lt_username,
                    "accessKey": lt_access_key,
                    "platformName": "Windows 10",

                    # 🔥 REQUIRED FOR EXAM
                    "network": True,
                    "video": True,
                    "console": True,
                    "visual": True,

                    "build": "Playwright HyperExecute Build",
                    "project": "TestMu Playwright Assignment",
                    "name": "TestMu AI Playground Tests"
                }
            }

            ws_url = f"wss://cdp.testmuai.com/playwright?capabilities={urllib.parse.quote(json.dumps(capabilities))}"

            print("Connecting to cloud...")  # debug

            browser = p.chromium.connect(ws_url)
            context = browser.new_context()
            page = context.new_page()

            yield page

            context.close()
            browser.close()

        else:
            print("Running locally...")  # debug

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
