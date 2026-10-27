import base64

import pytest
from pytest_html import extras


# wrapper=True lets this hook run around pytest's own report creation
@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    # Let pytest build the normal report first, then get it back
    report = yield

    # Only act on the test body ("call"), not setup/teardown, and only when it failed
    if report.when == "call" and report.failed:
        # Get the browser tab from the test's "page" fixture (None for non-UI tests)
        page = item.funcargs.get("page")
        if page is not None:
            # Take a screenshot of the visible page as raw PNG bytes
            png_bytes = page.screenshot()
            # Convert to base64 text so the image lives inside the HTML file
            png_base64 = base64.b64encode(png_bytes).decode("utf-8")
            # Attach the image to this test's row in the pytest-html report
            report.extras = getattr(report, "extras", []) + [extras.png(png_base64)]

    # Hand the (possibly updated) report back to pytest
    return report
