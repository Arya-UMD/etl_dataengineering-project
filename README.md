# etl_dataengineering-project
INST767 Final Project : Here we are bringing 3 Dynamic Cricket APIs to one Model for further analysis.
![IMG-20240510-WA0005](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/d8a368ca-5d08-4575-a123-55e884e6de3a)
Introduction 
This report provides a detailed overview of your cricket data pipeline, which ingests data from the Cricbuzz API, transforms it, stores it in BigQuery, and prepares it for visualization in Looker Studio. This system allows for data-driven insights into cricket statistics, such as player rankings, team performance, and batting averages.

1. Ingestion 
The data pipeline utilizes three Cloud Functions: 
● cf-extract-icc-ranking: Extracts data related to ICC ODI batting rankings.
● cf-extract-ipl-points-table: Extracts data on IPL points tables.
● cf-extract-ipl-batting-stats: Extracts data on IPL batting statistics.
![WhatsApp Image 2024-05-14 at 19 34 26_cb10e5ae](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/c91821db-a965-4544-b2e8-53bc4e87296a)

![image](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/8583af7e-2ed8-4c42-b964-009340605df2)
These cloud functions are scheduled by the Cloud scheduler in a specific interval. Each Cloud Function performs the following tasks: 
a. Extract: Calls the respective Cricbuzz API endpoint to retrieve data.
b. Transform: Cleans, filters, and formats the extracted data as needed.
c. Store in CSV: Saves the transformed data as a CSV file to the Cloud Storage bucket "bkt-etl-data". 


2.Transformation 
The transformation step is likely specific to each Cloud Function depending on the data structure retrieved from the API. It might involve: 
● Removing unwanted fields. 
● Renaming or restructuring fields for clarity. 
● Converting data types for consistency. 
● Handling missing or invalid values. 

3. Storage (Load)
After transformation, each Cloud Function triggers a Dataflow job using a GCS-to-BigQuery template. This template loads the corresponding CSV file from the "bkt-etl-data" bucket into a specific BigQuery table: 
● icc-odi-batting-ranking: Stores ICC ODI batting ranking data.
● ipl-points-table: Stores IPL points table data. 
● ipl-batting-stats: Stores IPL batting statistics data.
![WhatsApp Image 2024-05-11 at 22 51 00_f4750190](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/29021374-d5b8-4fee-bf1d-52d0073ed84e)

![WhatsApp Image 2024-05-11 at 22 51 21_ed923ec8](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/08f85844-eb7a-4d4d-a1f7-1ee5c13681df)

![WhatsApp Image 2024-05-11 at 22 51 55_4a27d997](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/099ee876-e8ed-4895-a328-d7c9e2053331)

Here we can see all the three are under one model "Cricket Dataset"
![image](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/43d0f9b8-b818-48e1-b5bc-6eb5392cced9)


Cloud Scheduler 
![WhatsApp Image 2024-05-14 at 19 32 28_dd4392bd](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/c2773a27-1283-4d31-9dc5-182a65ca2732)



4.Analysis
This section demonstrates how our data model can be used to answer cricket-related questions: 
