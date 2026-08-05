*[English](#english) | [Deutsch](#deutsch)*

---

# English

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





---

# Deutsch

# Playwright Showcase — SauceDemo Regressionssuite

Automatisierte UI-Regressionstests für [SauceDemo](https://www.saucedemo.com/),
umgesetzt mit Playwright und pytest nach dem Page-Object-Model. Die Suite deckt
Login, Inventar, Warenkorb und den kompletten Checkout-Ablauf ab und erzeugt
Reports sowohl mit pytest-html als auch mit Allure.

## Technologien

Python, Playwright (Sync-API), pytest, pytest-playwright, pytest-html, allure-pytest.

## Voraussetzungen

- Python 3.11 oder neuer
- Git
- Java 11+ (nur zum Anzeigen der Allure-Reports — die Allure-CLI benötigt es)

## Einrichtung

```bash
# Projekt klonen und hineinwechseln
git clone <repo-url>
cd Playwright-showcase

# Virtuelle Umgebung erstellen und aktivieren
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate

# Abhängigkeiten und Browser-Binaries installieren
pip install -r requirements.txt
playwright install
```

`pip install` holt die Python-Pakete; `playwright install` lädt die eigentlichen
Browser (Chromium, Firefox, WebKit), die von den Tests gesteuert werden.

## Projektstruktur

```
pages/          Page Objects (Locators + Aktionen), eine Klasse pro Seite
  base_page.py      gemeinsame Elternklasse, von der alle Seiten erben
  login_page.py
  inventory_page.py
  cart_page.py
  checkout_page.py
  product_page.py
  side_bar.py
tests/          Testfälle, eine Datei pro Gruppe (test_login_*, test_cart_*, ...)
pytest.ini      Konfiguration: Testpfad, Basis-URL, Standard-Report-Flags
requirements.txt
```

Tests sind nach dem Muster `test_*` benannt, damit pytest sie automatisch findet.
Die Page Objects enthalten alle Locators, sodass die Tests die Absicht ausdrücken
(einloggen, in den Warenkorb legen, zur Kasse gehen) statt roher Selektoren.

## Konfiguration

`pytest.ini` enthält die Basis-URL und die Standardoptionen:

```ini
[pytest]
testpaths = tests
base_url = https://www.saucedemo.com/
addopts = --html=report.html --self-contained-html --alluredir=allure-results
```

Durch die Basis-URL navigieren die Tests mit relativen Pfaden (z. B. `page.goto("")`
für die Login-Seite). Die Report-Flags gelten bei jedem Lauf, daher schreibt schon
ein einfaches `pytest` beide Report-Formate.

Die Test-Zugangsdaten sind die öffentlichen Übungskonten von SauceDemo
(`standard_user`, `locked_out_user`, ... mit Passwort `secret_sauce`), sodass zum
Ausführen der Suite keine Geheimnisse oder eine `.env`-Datei nötig sind.

## Tests ausführen

```bash
pytest                              # gesamte Suite ausführen
pytest tests/test_login_tc01.py     # eine einzelne Datei ausführen
pytest -k checkout                  # Tests mit passendem Schlüsselwort ausführen
pytest -v                           # ausführlich: jeden Testnamen anzeigen
```

Standardmäßig laufen die Tests auf Chromium. Für einen anderen Browser oder mehrere:

```bash
pytest --browser firefox
pytest --browser chromium --browser firefox --browser webkit
```

Tests lassen sich außerdem über das VS-Code-Testing-Panel (das Kolben-Symbol)
ausführen und beobachten, sobald die Python- und Playwright-Erweiterungen
installiert sind.

## Reports

Jeder Lauf schreibt zwei Reports.

**pytest-html** — eine einzelne, in sich geschlossene Datei `report.html`. Lässt
sich direkt in jedem Browser öffnen; keine zusätzlichen Werkzeuge nötig. Gut für
einen schnellen Überblick über Erfolg/Fehlschlag.

**Allure** — ein umfangreicheres Dashboard mit Diagrammen, Laufzeiten und
Aufschlüsselung nach Testgruppen. Zum Anzeigen wird das separat zu installierende
Allure-Kommandozeilenwerkzeug (via Scoop, npm oder manueller Download) sowie Java
benötigt:

```bash
# Schneller Blick — erzeugt und öffnet einen temporären Report
allure serve allure-results

# Oder einen dauerhaften statischen Report erzeugen und dann öffnen
allure generate allure-results -o allure-report --clean
allure open allure-report
```

Hinweis: Den erzeugten Allure-Report mit `allure open` öffnen, nicht per
Doppelklick auf `index.html` — Browser blockieren den dafür nötigen lokalen
Dateizugriff.

## Testabdeckung

Die Suite ist ein risikobasiertes Regressionsset und deckt ab:

- Authentifizierung — gültiger Login, ungültige Zugangsdaten, gesperrter Benutzer
- Inventar — Produktdarstellung, Sortierung nach Name und Preis, Hinzufügen und Entfernen
- Warenkorb — Hinzufügen/Entfernen, Datenkonsistenz Inventar-Warenkorb, "Continue Shopping" erhält den Warenkorb
- Checkout — Feldvalidierung (Entscheidungstabelle), gültige Übermittlung, Abbruchverhalten
- Übersicht — Konsistenz Warenkorb-Übersicht, Zahlungs-/Versandinfo, Zwischensumme
- End-to-End — kompletter Kaufablauf bis zur Bestellbestätigung

Die vollständigen Fallspezifikationen (Ziele, Schritte, Prüfungen,
Anforderungs-Rückverfolgbarkeit) befinden sich in den beiliegenden
Regressionstest-Dokumenten.

## Hinweise

- Tests sind eigenständig: Jeder Test richtet seine eigenen Vorbedingungen ein
  (Login, Warenkorbinhalt), statt sich darauf zu verlassen, dass ein anderer Test
  zuvor gelaufen ist.
- Locators nutzen wo möglich die stabilen `data-test`-Attribute von SauceDemo, da
  diese eigens für die Automatisierung gesetzt sind und ein Redesign überstehen.
- `allure-results/`, `allure-report/`, `report.html` und `venv/` sind erzeugte
  Ausgaben und werden per gitignore ausgeschlossen.

