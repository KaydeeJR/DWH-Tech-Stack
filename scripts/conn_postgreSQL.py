import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import read_csv

class ConnectToDB:
    """
    Class that:
    Connects to PostgreSQL database server using Docker
    Opens a session to communicate with database
    Creates table in database
    Inserts data into table
    """
    def __init__(self, engine):
        self.engine = engine


    def start_DB_session(self):
        # create a DB session
        db_session = scoped_session(sessionmaker(bind=self.engine))
        return db_session

    def create_table(self, session, schema_file_path):
        """create 2 tables:
        1) Trajectories table 
        2) Time frequencies table
        """
        # access file in path
        sqlFile = schema_file_path
        # open and read file
        fd = open(sqlFile, 'r')
        readSqlFile = fd.read()
        fd.close()
        # retrieving SQL commands
        sqlCommands = readSqlFile.split(';')
        for command in sqlCommands:
            try:
                if (len(command)>0):
                    session.execute(command.strip())
                    session.commit()
            except Exception as ex:
                print("Command skipped: ", command)
                print(ex)
    
    def load_trajectory_data(self, session, tableName, path_to_file):
        """
        for loop to insert data
        trajectory information includes: track_id, vehicle type, traveled distance, avg_speed in km/h
        """
        # read from CSV file 
        df = read_csv.read_csv_file(filePath=path_to_file)

        # access dataframe values
        for data_index in range(len(df.values)):
            # list of data elements
            elements = str(df.values[data_index]).split(';')
            traj_info = read_csv.get_trajectory_info(elements)
            file_info = read_csv.get_file_details(path_to_file)
            values = traj_info+file_info
            command = f"INSERT INTO {tableName} (track_id, vehicle_type, travelled_dist, avg_speed, drone_number, date, time_range) VALUES {values};"
            session.execute(command)
            session.commit()
        # close the db session
        session.close()

    #def load_time_frequency_data():

if __name__ == '__main__':
    # initatialize engine to connect to DB
    # syntax -> //username:password@host:port/database
    db_engine = create_engine('postgresql://postgres:PG13#Njogu@localhost:5432/pNeuma_Traffic_DB')
    db_connect = ConnectToDB(engine=db_engine)
    db_session = db_connect.start_DB_session()
    # CREATE TABLES (IF NOT EXIST)
    db_connect.create_table(db_session, "D:\\10XAcademy\\DWH-Tech-Stack\\postgresql\\db_schema.sql")
    # INSERT INTO TABLE
    path = "D:\\10XAcademy\\DWH-Tech-Stack\\postgresql\\data\\20181024_d5_0830_0900.csv"
    db_connect.load_trajectory_data(db_session, "trajectories_data",path)