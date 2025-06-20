import requests
from bs4 import BeautifulSoup


def fetch_homepage():
    url = "https://www.ifood.com.br"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text


def parse_homepage(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.text.strip() if soup.title else "No title found"
    return {"title": title}


def main():
    html = fetch_homepage()
    data = parse_homepage(html)
    print("Page title:", data["title"])


if __name__ == "__main__":
    main()
