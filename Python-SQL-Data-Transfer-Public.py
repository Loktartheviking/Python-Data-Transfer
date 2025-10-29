from sqlalchemy import create_engine, inspect, select
import pandas as pd

# Create two engines to connect to the both SQL database tables you are looking to use, help creating the connection string: https://www.connectionstrings.com/
#  Plugin used ODBC Driver 17 for SQL Server.
#  Trusted connection is used for Windows Authentication, can replace with username and password if needed.
engine = create_engine('mssql+pyodbc://Server\\Typeofinstance/Database?driver=ODBC Driver 17 for SQL Server&Trusted_Connection=yes')
engine2 = create_engine('mssql+pyodbc://Server\\Typeofinstance/Database?driver=ODBC Driver 17 for SQL Server&Trusted_Connection=yes')



#Confirm that the connection is made by inspecting the database tables
inspection = inspect(engine)
inspection2 = inspect(engine2)

#Query to retrieve data from the first database
with engine.connect() as conn:
    rtrv = """SELECT * FROM Datatablename"""
    result_df = pd.read_sql(rtrv, conn)
    #To print the dataframe extracted from the database for testing purposes
    #print(result_df)
    conn.close()
#Adding the retrieved data to the second database
with engine2.connect() as conn2:
  result_df.to_sql(name = "Datatablename", con=conn2, if_exists='replace', index=False)
  final_df = pd.read_sql("""SELECT * FROM Datatablename2""", conn2) 
  #To print the final dataframe after transfer for testing purposes 
  #print(final_df)
  conn2.close()

#Closes connections to both databases
engine.dispose()
engine2.dispose()