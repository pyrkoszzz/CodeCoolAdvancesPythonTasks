import os
import requests


class WeatherFetcher:
    def __init__(self):
        self.api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
        if not self.api_key:
            raise ValueError("OpenWeatherMap API key not found")

        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str) -> dict:
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    @staticmethod
    def display_weather(weather_data) -> None:
            try:
                if not weather_data:
                    raise ValueError("Unable to display weather information.")
                city_name = weather_data['name']
                temperature = weather_data['main']['temp']
                description = weather_data['weather'][0]['description']

                print(f"Weather in {city_name}:")
                print(f"Temperature: {temperature}°C")
                print(f"Description: {description}")
            except KeyError as e:
                print(f"Error parsing weather data: {e}")


if __name__ == "__main__":
    try:
        weather_fetcher = WeatherFetcher()
        city = input("Enter the city name: ")

        weather_data = weather_fetcher.get_weather(city)
        weather_fetcher.display_weather(weather_data)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
