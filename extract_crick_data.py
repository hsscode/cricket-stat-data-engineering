import requests
import csv

# API endpoint and parameters
url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"
querystring = {"formatType": "test"}

# Headers including the API key
headers = {
    "x-rapidapi-key": "0afd98f16amsh24c7c82912b7be6p154cb8jsn50bbe566195f",
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

# Make the API request
response = requests.get(url, headers=headers, params=querystring)

# Check if the response is successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Open a new CSV file to write the data
    with open('batsmen_rankings.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write headers to the CSV file
        writer.writerow(['Position', 'Player', 'Country', 'Rating'])

        # Iterate through the data and write to the CSV file
        for player in data.get('rankings', []):
            writer.writerow([player['position'], player['name'], player['country'], player['rating']])

    print("Data has been written to batsmen_rankings.csv")
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
