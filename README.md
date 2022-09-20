# DWH-Tech-Stack
## :briefcase:Business Understanding

You and your colleagues have joined to create an AI startup that deploys sensors to businesses, collects data from all activities in a business - people’s interaction, traffic flows, smart appliances installed in a company. Your startup helps organisations obtain critical intelligence based on public and private data they collect and organise. 

A city traffic department wants to collect traffic data using swarm UAVs (drones) from a number of locations in the city and use the data collected for improving traffic flow in the city and for a number of other undisclosed projects. Your startup is responsible for creating a scalable data warehouse that will host the vehicle trajectory data extracted by analysing footage taken by swarm drones and static roadside cameras. 

The data warehouse should take into account future needs, organise data such that a number of downstream projects query the data efficiently. You should use the Extract Load Transform (ELT) framework using DBT.  Unlike the Extract, Transform, Load (ETL), the ELT framework helps analytic engineers in the city traffic department setup transformation workflows on a need basis.

## :open_book:About the data

Data is sourced from pNEUMA. pNEUMA is an open large-scale dataset of naturalistic trajectories of half a million vehicles that have been collected by a one-of-a-kind experiment by a swarm of drones in the congested downtown area of Athens, Greece. Each file for a single (area, date, time) is ~87MB data.  To understand how the data is generated from video frames recorded with swarm drones:

Five flight sessions for 2.5 hours per day. From Monday to Friday. Drones hover over a particular location and record vehicle details.  

**For each .csv file the following apply:**

- each row represents the data of a single vehicle. There are 6 types of vehicles. They are: Car, Taxi, Bus, Medium Vehicle, Heavy Vehicle, Motorcycle.
The buses have bus stops. Each vehicle has its dimensions in metres.

- the first 10 columns in the 1st row include the columns’ names

- the first 4 columns include information about the trajectory like the unique trackID, the type of vehicle, the distance traveled in meters and the average speed of the vehicle in km/h

- the last 6 columns are then repeated every 6 columns based on the time frequency. For example, column_5 contains the latitude of the vehicle at time column_10, and column­­­_11 contains the latitude of the vehicle at time column_16.

- Speed is in km/h, Longitudinal and Lateral Acceleration in m/sec2 and time in seconds.

## :toolbox:Tools
1) PostgreSQL
2) DBT
3) Apache Airflow

## :card_file_box:Repo Structure

:file_folder: **data**

<ul>:arrow_up:contains data files in csv format</ul>

:file_folder: **snapshots**

<ul>:arrow_up:contains screenshots of the built data view</ul>

:file_folder: **models**

:file_folder: **tests**

:link: TODO: link to deployed dbt data warehouse documentation
