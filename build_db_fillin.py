import pathlib
import sqlite3
import pandas as pd


path = pathlib.Path().cwd() # use pathlib to get current working directory


def create_db(db_name, filename, table_name):
    file_path = path / filename # create a path to the data file

    con = sqlite3.connect(db_name) # create a connection to the database
    cursor = con.cursor() # create a cursor

    students = pd.read_csv(file_path) # read in the data 
    
    # insert the data into the specified table 
    students.to_sql(table_name, con, if_exists='replace', index = False)
    
    # execute a select statement as f-string and print results to verify insertion
    results = cursor.execute(f'SELECT * FROM {table_name}').fetchall()
    print(results)
    
    # commit the changes to the database
    con.commit()
    
    # close the connection
    con.close()

if __name__=="__main__":
    db_name = "School.db"
    filename = "students_1.csv"
    table_name = "students"
    create_db(db_name, filename, table_name)
