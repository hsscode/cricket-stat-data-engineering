
import os
import requests
import csv
 
from google.cloud import storage



url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

params = {
    'formatType': 'odi'

}

headers = {
	"X-RapidAPI-Key": "caafe0ee3emsh6a2410f997a8340p11119fjsn3e343652f67e",
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=params)


print(response)



if response.status_code == 200:  ### 200 mean request is successful  (HTTP status code)


    data = response.json().get('rank', [])  # Extracting the 'rank' data from json, if didnt get the data rank then empty list []

    csv_filename = 'batsmen_rankings.csv'

    if data:
        field_names = ['rank', 'name', 'country']  # Specify required field names

        # Write data to CSV file with only specified field names
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:   ## this will open the csv in write mode 
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            #writer.writeheader()
            for entry in data:
                """ Here i am using dictionary comprensive  this dictinary will passed to the writer.writerow() method to write a row to the CSV file."""
                writer.writerow({field: entry.get(field) for field in field_names}) #For each entry, it writes a row to the CSV file with values corresponding to the specified field names.

        print(f"Data fetched successfully and written to '{csv_filename}'")

                #upload the csv file to the bucket
        bucket_name="bkt-cricket"
        storage_client= storage.Client()
        bucket=storage_client.bucket(bucket_name)
        destination_blob_name=f'{csv_filename}'
        blob= bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)
        print("Done uplading")


    else:
        print("No data available from the API.")

else:
    print("Failed to fetch data:", response.status_code)

