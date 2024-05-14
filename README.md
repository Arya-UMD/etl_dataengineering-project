# etl_dataengineering-project
INST767 Final Project : Here we are bringing 3 Dynamic Cricket APIs to one Model for further analysis.
![IMG-20240510-WA0005](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/d8a368ca-5d08-4575-a123-55e884e6de3a)
Introduction 
This report provides a detailed overview of your cricket data pipeline, which ingests data from the Cricbuzz API, transforms it, stores it in BigQuery, and prepares it for visualization in Looker Studio. This system allows for data-driven insights into cricket statistics, such as player rankings, team performance, and batting averages.

Ingestion
 
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


Transformation 

The transformation step is likely specific to each Cloud Function depending on the data structure retrieved from the API. It might involve: 
● Removing unwanted fields. 
● Renaming or restructuring fields for clarity. 
● Converting data types for consistency. 
● Handling missing or invalid values. 

Storage (Load)

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



Analysis

This section demonstrates how our data model can be used to answer cricket-related questions: 

Question 1

Outstanding Performer

Indian Premier League (IPL) is a sporting league to determine talents and in our first question we would like to see which player has topped his performance in the international stage in batting and as well as Topped the runs chart (top 10) in IPL as well.

Executing query 1 : reference sql file for code

![image](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/65151c5c-7ee5-4b70-bbe3-9922111038d5)

We can see that Virat Kohli is the only player who has topped the runs chart (Highest run getter with 661 runs so IPL rank of 1) and also he is in the top 10 icc rankings (Odi Ranking number 3), we chose ODI format because it is the most defining format of the game and it has the major world cup.

Question 2

Qualification Scenario

Indian Premier League (IPL) is a tough competition among 10 teams, we have done an analysis on May 11, 2024, during the crucial stage of the ongoing tournament because on this day May 14, 2024 most of the qualifications would have been done, so on May 11, 2024 what was the number of wins required by each team to qualify for the knock stages considering 8 wins out of 14 matches as the general cutoff for qualification.

![WhatsApp Image 2024-05-11 at 22 48 03_a4030f1d](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/4f282dae-8666-43f5-84f3-e6c310205d22)

This query shows the number of wins required by each team to qualify for the knockout games but if they have already lost 8 games and there is no scenario where they can win 8 games those teams will be considered eliminated from the playoffs race.

Question 3


