import sqlite3
import pathlib
import pandas as pd
from constants import DATABASE_PATH
from sql_queries import *
import inspect
from typing import List

def load_dataset(DATASET_PATH: pathlib.Path) -> pd.DataFrame:
    """
    This function loads the dataset to a pandas dataframe

    Args:
        DATASET_PATH (pathlib.Path): path to csv file

    Returns:
        pd.DataFrame: dataframe containing the dataset
    """
    try:
        df: pd.DataFrame = pd.read_csv(DATASET_PATH)
        return df
    except FileNotFoundError:
        print(f'File not found at {DATASET_PATH}')
    
def csv_to_sqlite(dataframe: pd.DataFrame, database_path: pathlib.Path, table_name: str) -> None:
    """
    This function writes a pandas dataframe to a SQLite database

    Args:
        dataframe (pd.DataFrame): dataframe containing the dataset
        database_path (pathlib.Path): path to SQLite database
        table_name (str): name of the table in the database
    """

    conn: sqlite3.Connection = sqlite3.connect(database_path)
    
    try:
        dataframe.to_sql(table_name, conn, if_exists='replace', index=False)
        print('Dataframe successfully written to SQLite')
    except sqlite3.OperationalError as e:
        print(e)
    finally:
        conn.close()
        
def connect_to_database():
    """
    Establish and return a database connection cursor for SQLite operations.

    Creates a connection to the SQLite database specified by the DATABASE_PATH
    and returns a cursor object for executing SQL commands. The connection
    remains open until explicitly closed by the caller.

    Returns:
        sqlite3.Cursor: A database cursor object used to execute SQL statements
        and fetch results.

    """
    try:
        conn: sqlite3.Connection = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        return cursor
    except sqlite3.Error as e:
        print(e)

def select_products_with_biggest_popularity_return_diff():
    """
    Retrieve products with the largest absolute difference between popularity 
    index and return rate from the database.

    Returns:
        list: A list of tuples representing the selected records, where each 
        tuple corresponds to a row in the result set.
    """
    with connect_to_database() as cursor:
        cursor.execute(biggest_popularity_return_difference_query)
        return cursor.fetchall()

def select_most_popular_category():
    """
    Retrieve the category with the highest number of sells within a specific 
    popularity index range from the database.
    
    Returns:
        tuple: A tuple representing the category with the most products in the 
        specified popularity range, or None if no data is found.
    """

    with connect_to_database() as cursor:
        cursor.execute(most_popular_category_query)
        return cursor.fetchone()

def select_top_supplier_by_net_profit():
    """
    Retrieve the supplier with the highest net profit after consideration of tax and discount 
    from the database.
    
    Returns:
        list: A list of tuples representing the supplier(s) with the highest 
        net profit. Each tuple contains a record for the supplier's net profit.
    """
    with connect_to_database() as cursor:
        cursor.execute(top_supplier_by_net_profit_query)
        return cursor.fetchall()

def select_top_supplier_for_standard_shipping():
    """
    Retrieve the supplier who has shipped the most products via the standard 
    shipping method.

    Returns:
        list: A list of tuples representing the supplier(s) with the highest 
        number of products shipped using the standard shipping method. Each tuple 
        contains a record for the supplier and the total number of products shipped.
    """
    with connect_to_database() as cursor:
        cursor.execute(top_supplier_for_standard_shipping_query)
        return cursor.fetchall()

    
def build_prompt(user_query: str, functions: List = [select_products_with_biggest_popularity_return_diff,
                              select_top_supplier_for_standard_shipping,
                              select_most_popular_category,
                              select_top_supplier_by_net_profit]):
    prompt = ""
    for func in functions:
        prompt += 'Function \n'
        prompt += f'def {func.__name__}{inspect.signature(func)}\n{func.__doc__}\n'
    prompt += f'User Query: {user_query}<human_end>'
    return prompt
    

        
    
    
    
    
