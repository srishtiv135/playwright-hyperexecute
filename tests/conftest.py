import urllib.parse
import json

capabilities = {
    "browserName": "Chrome",
    "browserVersion": "latest",
    "LT:Options": {
        "user": lt_username,   # ✅ IMPORTANT (not username)
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

browser = p.chromium.connect(ws_url)
