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

    def create_table(self, tableName, session):
        """create table with different names but with the same schema"""
        command = f"CREATE TABLE IF NOT EXISTS {tableName} (track_id INTEGER PRIMARY KEY, vehicle_type VARCHAR(50),travelled_dist FLOAT, avg_speed FLOAT, latitude VARCHAR(50), longitude VARCHAR(50), speed FLOAT, long_accel FLOAT,lati_accel FLOAT,duration FLOAT);"
        try:
            session.execute(command)
            session.commit()
        except Exception as ex:
            print(ex)
    
    def add_trajectory_data_to_table(self, session, tableName, path_to_file):
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
            values = tuple(read_csv.get_trajectory_info(elements),)
            command = f"INSERT INTO {tableName} (track_id, vehicle_type, travelled_dist, avg_speed) VALUES {values};"
            session.execute(command)
            session.commit()
        # close the db session
        session.close()

if __name__ == '__main__':
    # initatialize engine to connect to DB
    # syntax -> //username:password@host:port/database
    db_engine = create_engine('postgresql://postgres:PG13#Njogu@localhost:5432/pNeuma_Traffic_DB')
    db_connect = ConnectToDB(engine=db_engine)
    db_session = db_connect.start_DB_session()
    # TODO: CHANGE TABLE NAME
    table_name = "d5_2018_10_24_0830_0900"
    # CREATE TABLE (IF NOT EXIST)
    db_connect.create_table(table_name, db_session)
    # INSERT INTO TABLE
    db_connect.add_trajectory_data_to_table(db_session, table_name, os.getcwd()+'\\data\\20181024_d5_0830_0900.csv')