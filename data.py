import sqlalchemy as db
from sqlalchemy import create_engine
import pandas as pd

# Creating 
def connectDB():
    db_config = {
    'host':  #host,
    'database': #database,
    'user': #user,
    'password': #password,
    'port': #port
    }
    engine = create_engine(f'postgresql+psycopg2://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["database"]}')
    return engine

def createTable():
    

# Add info in table
def addTable(engine):
    table = 'data_censo_escolar'
    file = pd.read_excel(r'data_censo_escolar.xlsx', engine='openpyxl')
    file.to_sql(table, engine, if_exists='replace', index=False)
    

    
engine = connectDB()
addTable(engine)

    
    
    
    