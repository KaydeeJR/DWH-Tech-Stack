import pandas as pd

def read_csv_file(filePath)->pd.DataFrame:
    return pd.read_csv(filepath_or_buffer=filePath)

def get_trajectory_info(row_as_list):
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
    return trajectory_info