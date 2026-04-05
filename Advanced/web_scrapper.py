import csv
import json
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def main() -> None:
    all_quotes = []
    base_url = "https://quotes.toscrape.com/page/{}/"

    print("Starting to scrape all 10 pages...\n")

    for page in range(1, 11):  # pages 1 to 10
        url = base_url.format(page)
        print(f"Scraping page {page}/10...")

        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to load page {page}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            quote_text = quote.find("span", class_="text")
            text = (
                quote_text.get_text(strip=True).strip("“”") if quote_text else "Unknown"
            )

            author_tag = quote.find("small", class_="author")
            author = author_tag.get_text(strip=True) if author_tag else "Unknown"

            tags_div = quote.find("div", class_="tags")
            tags = (
                [
                    tag.get_text(strip=True)
                    for tag in tags_div.find_all("a", class_="tag")
                ]
                if tags_div
                else []
            )

            all_quotes.append(
                {
                    "quote": text,
                    "author": author,
                    "tags": tags,
                    "page": page,  # bonus: track which page it came from
                }
            )

        time.sleep(1)  # Be polite - 1 second delay between pages

    print(f"\n Finished! Total quotes scraped: {len(all_quotes)}\n")

    # Save to JSON
    with open("quotes_all.json", "w", encoding="utf-8") as f:
        json.dump(all_quotes, f, indent=4, ensure_ascii=False)

    # Save to CSV
    with open("quotes_all.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["quote", "author", "tags", "page"])
        writer.writeheader()
        for q in all_quotes:
            row = q.copy()
            row["tags"] = ", ".join(q["tags"])
            writer.writerow(row)

    print(" Files saved:")
    print("   → quotes_all.json")
    print("   → quotes_all.csv")

    # Preview
    print("\nFirst 3 quotes preview:")
    for q in all_quotes[:3]:
        print(f"• {q['quote'][:90]}{'...' if len(q['quote']) > 90 else ''}")
        print(f"  — {q['author']}")
        print(f"  Tags: {', '.join(q['tags'])}")
        print()


# Add proper headers (User-Agent) so the site doesn't suspect you're a bot
# Better error handling (what if a page fails to load?)
# Make the script more reusable (add functions, arguments)
# Add a progress bar


if __name__ == "__main__":
    main()
