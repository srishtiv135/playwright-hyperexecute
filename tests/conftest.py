import pytest
from playwright.sync_api import sync_playwright
import os

@pytest.fixture
def page():
    with sync_playwright() as p:
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
