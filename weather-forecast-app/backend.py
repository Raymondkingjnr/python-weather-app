import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("API_KEY")
def get_data(place, days= None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    data = requests.get(url)
    data = data.json()
    filtered_data = data['list']
    nu_values = 8 * days
    filtered_data = filtered_data[:nu_values]

    return filtered_data

if __name__ == "__main__":
    print(get_data(place="London", days=3))
