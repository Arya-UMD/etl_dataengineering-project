from googleapiclient.discovery import build
import requests
import csv
from google.cloud import storage
import google.cloud.bigquery as bigquery


project_id = 'etl-dataengineering-project'
bucket_name = 'bkt-etl-data'
dataset_id = 'cricket_dataset'
table_id = 'icc_odi_batsman_ranking'
#gcs_folder_name

def extract_ranking(cloud_event):
   

    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen'
    headers = {
    'X-RapidAPI-Key': '7c171ec94dmshe598ddd2d1632e5p1ecf63jsnf52812ecc980',
    'X-RapidAPI-Host': 'cricbuzz-cricket.p.rapidapi.com'
    }
    params = {
        'formatType': 'odi'
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get('rank', [])  # Extracting the 'rank' data
        csv_filename = 'batsmen_rankings.csv'

        if data:
            field_names = ['rank', 'name', 'country']  # Specify required field names

            # Write data to CSV file with only specified field names
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                #writer.writeheader()
                for entry in data:
                    writer.writerow({field: entry.get(field) for field in field_names})

            print(f"Data fetched successfully and written to '{csv_filename}'")
                    # Upload the CSV file to GCS
            storage_client = storage.Client()
            bucket = storage_client.bucket(bucket_name)
            destination_blob_name = f'icc_ranking/{csv_filename}'
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_filename(csv_filename)
            print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")
            truncate_table()
            trigger_df_job()
        else:
            print("No data available from the API.")

    else:
        print("Failed to fetch data:", response.status_code)
    return "Data processing completed successfully!"


def trigger_df_job():   
 
    service = build('dataflow', 'v1b3')

    template_path = "gs://dataflow-templates-us-west1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load-icc-ranking",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": f"gs://{bucket_name}/scripts/udf.js",
        "JSONPath": f"gs://{bucket_name}/scripts/bq_ranking.json",
        "javascriptTextTransformFunctionName": "icc_ranking",
        "outputTable": f"{project_id}:cricket_dataset.icc_odi_batsman_ranking",
        "inputFilePattern": f"gs://{bucket_name}/icc_ranking/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": f"gs://{bucket_name}/",
        },
        "environment": {
        # "maxNumWorkers": "1",
        "workerRegion": "us-west1"  
    },
    }


    request = service.projects().templates().launch(projectId=project_id,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
    return response



def truncate_table():
    try:
        # Set the project ID, dataset ID, and table ID

        client = bigquery.Client()
        dataset_ref = client.dataset(dataset_id, project=project_id)
        dataset_exists = bigquery.Client().get_dataset(dataset_ref)
        
        if not dataset_exists:
            print(f"Dataset {project_id}.{dataset_id} does not exist.")
        
        else:
        # Check if the table exists
            table_ref = dataset_ref.table(table_id)
            table_exists = bigquery.Client().get_table(table_ref)

            if not table_exists:
                print(f"Table {project_id}.{dataset_id}.{table_id} does not exist.")

            else:
                # Construct the SQL query to delete all rows from the table
                query = f"DELETE FROM `{project_id}.{dataset_id}.{table_id}` WHERE true;"

                # Run the query
                query_job = client.query(query)

                # Wait for the query to finish
                query_job.result()

                print(f"All rows cleaned from {project_id}.{dataset_id}.{table_id}")
    except Exception as e:
        print(f"Error: {e}")    