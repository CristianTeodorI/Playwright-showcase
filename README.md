# Playwright Showcase — SauceDemo Regression Suite

Automated UI regression tests for [SauceDemo](https://www.saucedemo.com/), built with
Playwright and pytest using the Page Object Model. The suite covers login,
inventory, cart, and the full checkout flow, and produces both pytest-html and
Allure reports.

## Tech stack

Python, Playwright (sync API), pytest, pytest-playwright, pytest-html, allure-pytest.

## Requirements

- Python 3.11 or newer
- Git
- Java 11+ (only for viewing Allure reports — the Allure CLI needs it)

## Setup

```bash
# Clone and enter the project
git clone <repo-url>
cd Playwright-showcase

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate

# Install dependencies and browser binaries
pip install -r requirements.txt
playwright install
```

`pip install` gets the Python packages; `playwright install` downloads the
actual browsers (Chromium, Firefox, WebKit) the tests drive.

## Project structure

```
pages/          Page Objects (locators + actions), one class per page
  base_page.py      shared parent all pages inherit from
  login_page.py
  inventory_page.py
  cart_page.py
  checkout_page.py
  product_page.py
  side_bar.py
tests/          Test cases, one file per group (test_login_*, test_cart_*, ...)
pytest.ini      config: test path, base URL, default report flags
requirements.txt
```

Tests are named `test_*` so pytest discovers them automatically. Page Objects
hold every locator, so the tests express intent (log in, add to cart, check out)
rather than raw selectors.

## Configuration

`pytest.ini` holds the base URL and default options:

```ini
[pytest]
testpaths = tests
base_url = https://www.saucedemo.com/
addopts = --html=report.html --self-contained-html --alluredir=allure-results
```

The base URL means tests navigate with relative paths (e.g. `page.goto("")` for
the login page). The report flags apply on every run, so plain `pytest` already
writes both report formats.

Test credentials are SauceDemo's public practice accounts (`standard_user`,
`locked_out_user`, ... with password `secret_sauce`), so no secrets or `.env`
file are required to run the suite.

## Running the tests

```bash
pytest                              # run the whole suite
pytest tests/test_login_tc01.py     # run one file
pytest -k checkout                  # run tests matching a keyword
pytest -v                           # verbose: show each test name
```

By default tests run on Chromium. To run on another browser, or several:

```bash
pytest --browser firefox
pytest --browser chromium --browser firefox --browser webkit
```

You can also run and watch tests from the VS Code Testing panel (the flask icon)
once the Python and Playwright extensions are installed.

## Reports

Every run writes two reports.

**pytest-html** — a single self-contained file, `report.html`. Open it directly
in any browser; no extra tooling needed. Good for a quick pass/fail glance.

**Allure** — a richer dashboard with graphs, durations, and per-suite breakdowns.
Viewing it needs the Allure command-line tool installed separately (via Scoop,
npm, or a manual download) plus Java:

```bash
# Quick look — generates and opens a temporary report
allure serve allure-results

# Or generate a persistent static report, then open it
allure generate allure-results -o allure-report --clean
allure open allure-report
```

Note: open the generated Allure report with `allure open`, not by
double-clicking `index.html` — browsers block the local file access it needs.

## Test coverage

The suite is a risk-based regression set covering:

- Authentication — valid login, invalid credentials, locked-out user
- Inventory — product presentation, sorting by name and price, add and remove
- Cart — add/remove, cart-inventory data consistency, Continue Shopping preserves cart
- Checkout — field validation (decision table), valid submission, cancel behavior
- Overview — cart-to-overview consistency, payment/shipping info, subtotal
- End-to-end — full purchase flow through order confirmation

Full case specifications (objectives, steps, assertions, requirement traceability)
are in the accompanying regression test documents.

## Notes

- Tests are self-contained: each sets up its own preconditions (login, cart
  contents) rather than depending on another test having run first.
- Locators use SauceDemo's stable `data-test` attributes wherever possible,
  since those are added for automation and survive restyling.
- `allure-results/`, `allure-report/`, `report.html`, and `venv/` are generated
  output and are gitignored.
```
