import pandas as pd
import datetime
import time
import pickle
import numpy as np
from sqlalchemy import create_engine, inspect

class SQLHelper():
    def __init__(self):
        self.database_path = "worldcupdb.sqlite"
        self.conn_string = f"sqlite:///{self.database_path}"

        # Create an engine that can talk to the database
        self.engine = create_engine(self.conn_string)

    def getDataFromDatabase(self, team1, group):

        query = f"""
                SELECT
                    *
                FROM
                    titanic
                WHERE
                    Squad1 = 'United States'
                    AND Squad2 in ({team1})
                    AND Groups in ({group})
                    """

        print(query)

        df = pd.read_sql(query, con=self.engine)

        return df
