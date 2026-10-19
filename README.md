# News Headlines Scraper

A lightweight Python command-line tool that scrapes real-time headlines from BBC News (or any target news site) and outputs them cleanly to your terminal or an export file.

Built with `requests` and `BeautifulSoup4`.

---

## Features

- **Direct DOM Inspection:** Targets headline elements using attribute-level selectors (`data-testid="card-headline"`).
- **Clean Output:** Automatically strips extraneous whitespace and deduplicates repeat items.
- **Resilient Networking:** Custom `User-Agent` headers and HTTP status validation to prevent blocks.
- **Section Filtering:** Supports scraping specific categories (`world`, `business`, `technology`, `science`, `entertainment`).
- **File Export:** Save formatted headlines straight to a text file with a single flag.
- **Graceful Error Handling:** Catches timeouts, request failures, and shortages of page headlines without crashing.

---

## Project Structure

```text
.
├── headlines.py       # Main script containing scraper and CLI logic
├── requirements.txt   # Project dependencies
├── .gitignore         # Git ignore rules for Python / virtual environments
└── README.md          # Documentation
