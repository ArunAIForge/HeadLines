import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

try:
    response = requests.get(URL, headers=HEADERS, timeout=10)

    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        exit()

    soup = BeautifulSoup(response.text, "html.parser")

    # Locate the headline tags identified during page inspection
    headline_elements = soup.find_all("h2", attrs={"data-testid": "card-headline"})

    headlines = []
    seen = set()

    for el in headline_elements:
        text = el.get_text(strip=True)
        # Skip empty strings and duplicate entries
        if text and text not in seen:
            seen.add(text)
            headlines.append(text)
            if len(headlines) == 5:
                break

    # Gracefully handle cases where fewer than 5 headlines are found
    if not headlines:
        print("No headlines found. The page structure or selectors may have changed.")
    else:
        for idx, headline in enumerate(headlines, start=1):
            print(f"{idx}. {headline}")

        if len(headlines) < 5:
            print(f"\nNote: Only {len(headlines)} unique headline(s) were found on the page.")

except requests.exceptions.RequestException as e:
    print(f"Network error encountered: {e}")
    exit()