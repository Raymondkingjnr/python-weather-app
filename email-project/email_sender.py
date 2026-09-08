import requests
from send_email import send_email

topic = "Ai Hackathons"


api_key = "aa15640c4b6149b4a67fc925aee56b21"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2026-08-08&sortBy=publishedAt&apiKey=aa15640c4b6149b4a67fc925aee56b21&language=en"

request = requests.get(url)
content = request.json()

body =""

for article in content["articles"][:20]:
    if article["title"] is not None:
        body += article["title"] + "\n" \
                + article["description"] + "\n" \
                + article["url"] + "\n\n"

body = "Subject: Today's news\n\n" + body
body = body.encode("utf-8")
send_email(body)