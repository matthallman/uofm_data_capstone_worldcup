import pandas as pd
import datetime
import time
import pickle
import numpy as np
from sqlalchemy import create_engine, inspect
from sqlite_s3_query import sqlite_s3_query

class SQLHelper():
    def __init__(self):
        self.database_path = "https://jtspingler-bucket.s3.amazonaws.com/knockoutdb2.sqlite"
        # self.conn_string = f"sqlite:///{self.database_path}"

        # Create an engine that can talk to the database
        # self.engine = create_engine(self.conn_string)

    def get_credentials(self, _):
        return (
            "us-east-1",
            "AKIARRD75L6LQVIAAJG7",
            "WQLrB5+eZ8f0pj+TE+Frrd2FfczbbuuqJ5NoRcpt",
            None,  # Only needed for temporary credentials
        )

    def getDataFromDatabase(self, group, team):

        query_inp = f"""
                SELECT 
                    "index",
                    "Match" as match,
                    "Squad 1 Key" as s1_key,
                    "Squad 2 Key" as s2_key,
                    "Group" as "group",
                    "Stage" as "stage",
                    "Squad 1" as squad1,
                    "S1%" as s1_perc,
                    "Squad 1 Seed" as squad1_seed,
                    "Squad 2" as squad2,
                    "S2%" as s2_perc,
                    "Squad 2 Seed" as squad2_seed,
                    "S1_Prob" as s1_prob,
                    "S1_wins" as s1_wins,
                    "Simulation" as simulation,
                    "Match Winner" as match_winner
                FROM
                    knockoutdb
                WHERE
                    match_winner = '{team}' 
                AND "Group" in ({group})
                ;
                """

        print(query_inp)
        with sqlite_s3_query(url=self.database_path,get_credentials=self.get_credentials) as query, query(query_inp) as (columns, rows):

            df = pd.DataFrame(rows, columns=columns)

            return df