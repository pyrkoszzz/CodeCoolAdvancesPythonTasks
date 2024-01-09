import requests
from bs4 import BeautifulSoup


class NewsScraper:
    def __init__(self, url):
        self.url = url

    def get_headlines(self) -> list | None:
        try:
            response = requests.get(self.url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            headline_divs = soup.find_all('a', class_='wp-block-latest-posts__post-title')
            return [headline.text.strip() for headline in headline_divs]
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None


if __name__ == "__main__":
    try:
        news_scraper = NewsScraper("https://wmp.uksw.edu.pl/aktualnosci/")
        headlines = news_scraper.get_headlines()

        if headlines:
            print("Headlines:")
            for idx, headline in enumerate(headlines, start=1):
                print(f"{idx}. {headline}")
        else:
            print("Unable to fetch headlines.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
