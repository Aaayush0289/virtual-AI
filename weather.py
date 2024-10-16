import requests

url = "https://current-affairs-of-india.p.rapidapi.com/recent"

headers = {
	"X-RapidAPI-Key": "08c7795a32mshe3a9c4179b4f08dp1fcf29jsnd641d1111616",
	"X-RapidAPI-Host": "current-affairs-of-india.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())