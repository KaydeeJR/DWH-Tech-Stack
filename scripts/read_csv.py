from fileinput import filename
import pandas as pd
import os

def read_csv_file(filePath)->pd.DataFrame:
    return pd.read_csv(filepath_or_buffer=filePath)

def get_trajectory_info(row_as_list)->tuple:
    """
    parameter: list
    
    split the string using ';'
    
    extract trajectory information available at index:
    0 -> track_id
    1 -> vehicle type
    2 -> traveled distance in m
    3 -> avg_speed in km/h
    """
    trajectory_info = []
    trajectory_info.append(row_as_list[0][2:]) # substring
    trajectory_info.append(row_as_list[1])
    trajectory_info.append(row_as_list[2])
    trajectory_info.append(row_as_list[3])
    return tuple(trajectory_info)

def get_vehicle_data():
    """
    the last 6/10 columns are repeated every 6 columns based on the time frequency.
    For example, column_5 contains the latitude of the vehicle at time column_9, and column­­­_11 contains the latitude of the vehicle at time column_15
    """
  
    df = read_csv_file(filePath="D:\\10XAcademy\\DWH-Tech-Stack\\postgresql\\db_schema.sql")
    for data_index in range(len(df.values)):
        if data_index==0:
            track_data = str(df.values[data_index]).split(';')
            # fetch time data in repeated columns
            time_index = 9 # first index of time data
            while time_index < len(track_data):
                # time frequencies -> every .04 s
                print(time_index , track_data[time_index])
                time_index = time_index + 6

def get_file_details(filePath)->tuple:
    fileName = os.path.basename(filePath).split('/')[-1]
    drone_no = fileName.split("_")[1]
    date=fileName.split("_")[0]
    time=fileName.split("_")[2]+(fileName.split("_")[3])
    return (drone_no, date, time)

#if __name__ == '__main__':
 #   get_file_details("D:\\10XAcademy\\DWH-Tech-Stack\\postgresql\\data\\20181024_d5_0830_0900")