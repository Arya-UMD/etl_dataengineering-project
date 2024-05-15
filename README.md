# etl_dataengineering-project
**INST767 Final Project**

Initially, our focus was on utilizing the APIs and data sources from Cricbuzz. However, as we delved into our other project involving Football APIs, we realized the potential for completing the Cricbuzz project as well. Although our data pipeline was only halfway implemented initially, we have made significant strides and gained valuable insights, particularly in the implementation of Looker Studio.

Note: The recent commits indicate the files which were committed as part of a feature branch in the repository (https://github.com/hramac/INST767_Big-Data-Infrastructure/tree/harshitha/cricbuzz_data).


![IMG-20240510-WA0005](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/d8a368ca-5d08-4575-a123-55e884e6de3a)
**Introduction** 

This report provides a detailed overview of our cricket data pipeline, which ingests data from three dynamic Cricbuzz APIs, transforms it, stores it in BigQuery, and prepares it for visualization in Looker Studio. This system allows for data-driven insights into cricket statistics, such as player rankings, team performance, and batting averages.

**Ingestion**
 
The data pipeline utilizes three Cloud Functions: 

● cf-icc-rankings: Extracts data related to ICC ODI batting rankings.

● cf-ipl-pointstable: Extracts data on IPL points tables.

● cf-ipl-battingstats: Extracts data on IPL batting statistics.

![WhatsApp Image 2024-05-14 at 19 34 26_cb10e5ae](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/c91821db-a965-4544-b2e8-53bc4e87296a)

![image](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/8583af7e-2ed8-4c42-b964-009340605df2)
These cloud functions are scheduled by the Cloud scheduler in a specific interval. Each Cloud Function performs the following tasks: 

a. Extract: Calls the respective Cricbuzz API endpoint to retrieve data.

b. Transform: Cleans, filters, and formats the extracted data as needed.

c. Store in CSV: Saves the transformed data as a CSV file to the Cloud Storage bucket "bkt-etl-data". 


**Transformation** 

The transformation step is likely specific to each Cloud Function depending on the data structure retrieved from the API. It might involve: 

● Removing unwanted fields. 

● Renaming or restructuring fields for clarity. 

● Converting data types for consistency. 

● Handling missing or invalid values. 

**Storage (Load)**

After transformation, each Cloud Function triggers a Dataflow job using a GCS-to-BigQuery template. This template loads the corresponding CSV file from the "bkt-etl-data" bucket into a specific BigQuery table:

● bq-load-icc-ranking: Stores ICC ODI batting ranking data.

● bq-load-points-table: Stores IPL points table data. 

● bq-load-ipl-batting-stat: Stores IPL batting statistics data.

![WhatsApp Image 2024-05-11 at 22 51 00_f4750190](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/29021374-d5b8-4fee-bf1d-52d0073ed84e)

![WhatsApp Image 2024-05-11 at 22 51 21_ed923ec8](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/08f85844-eb7a-4d4d-a1f7-1ee5c13681df)

![WhatsApp Image 2024-05-11 at 22 51 55_4a27d997](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/099ee876-e8ed-4895-a328-d7c9e2053331)

Here we can see all the three are under one model "Cricket Dataset"
![image](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/43d0f9b8-b818-48e1-b5bc-6eb5392cced9)


Cloud Scheduler 

Now we schedule it run at regular intervals

![WhatsApp Image 2024-05-14 at 19 32 28_dd4392bd](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/c2773a27-1283-4d31-9dc5-182a65ca2732)



**Analysis**

This section demonstrates how our data model can be used to answer cricket-related questions: 

Question 1

Outstanding Performer

Indian Premier League (IPL) is a sporting league to determine talents and in our first question we would like to see which player has topped his performance in the international stage in batting and as well as Topped the runs chart (top 10) in IPL as well.

Executing query 1 : reference sql file for code

![image](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/65151c5c-7ee5-4b70-bbe3-9922111038d5)

We can see that Virat Kohli is the only player who has topped the runs chart (Highest run getter with 661 runs so IPL rank of 1) and also he is in the top 10 icc rankings (Odi Ranking number 3), we chose ODI format because it is the most defining format of the game and it has the major world cup.

Question 2

Qualification Scenario

Executing query 2 : reference sql file for code

Indian Premier League (IPL) is a tough competition among 10 teams, we have done an analysis on May 11, 2024, during the crucial stage of the ongoing tournament because on this day May 14, 2024 most of the qualifications would have been done, so on May 11, 2024 what was the number of wins required by each team to qualify for the knock stages considering 8 wins out of 14 matches as the general cutoff for qualification.

![WhatsApp Image 2024-05-11 at 22 48 03_a4030f1d](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/4f282dae-8666-43f5-84f3-e6c310205d22)

This query shows the number of wins required by each team to qualify for the knockout games but if they have already lost 8 games and there is no scenario where they can win 8 games those teams will be considered eliminated from the playoffs race.

Question 3

Best Batters vs Other Batters

Executing query 3 : reference sql file for code

In this question, we will compare the runs and average of top 5 run getters in the ongoing IPL and compare them with average runs and batting average of all other batsman combined, this would tell us how much better the top run getters are better than the rest of the batsman in the league.

![image](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/d28b820c-15b0-49c0-a5b5-1657ed91a29a)

Now we have a side by side comparison of top 5 run getters with the rest of the batsman

Question 4

Top Records for Busy People

Executing query 4 : reference sql file for code

A simple query that joins all the three tables and presents the the top record, this can be useful for people who particularly do not have time to follow cricket but are interested to be updated with the latest news.

![WhatsApp Image 2024-05-14 at 17 39 26_942d91a0](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/22ae9f14-57e4-478a-a2c1-a487245b5389)

![WhatsApp Image 2024-05-14 at 17 39 43_184ab9b9](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/71852244-dd9b-4636-89ed-47abc7d03293)


Kolkata Knight Riders stand top of the IPL points table, Babar Azam tops the ICC rankings and Virat Kohli is the highest run getter in the IPL as of May 14, 2024

Question 5

Percentage of Indians in ICC rankings

Executing query 5 : reference sql file for code

IPL is a tournament specifically designed to find cricketing talents in India. Now Board of Control for Cricket in India (BCCI) is concerned about the number of Indians in the Rankings, which would help them to know whether IPL is really helping for Indian players if yes, they can invest more in the league.

![image](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/149049bb-4792-4242-834b-07505e242131)

We can clearly see that there are 26.67% Indians in the Top 15 ICC rankings and now BCCI has good reason to go ahead and invest more in the IPL. 

**Future Scope**

As a further extension of the Query and out of the scope of the project we visualized the final query on Looker Studio

![image](https://github.com/Arya-UMD/etl_dataengineering-project/assets/152458007/adc08568-871d-4ee2-8afe-e2782ec65cc0)




