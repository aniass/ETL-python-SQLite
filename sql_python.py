import sqlite3
import pandas as pd
from sqlite3 import Error


def sql_connection():
    try:
        db = sqlite3.connect("db.sqlite")
        return db
    except Error:
        print(Error)


def read_excel_file(path):
    df = pd.read_excel(path)
    df = df.rename(columns={"Transaction Datetime": "created_at",
                            "ARN": "acq_tid", "Currnecy": "currency"})
    return df


def read_sql(query, con):
    df = pd.read_sql(query, con)
    return df


def changes_data(df1, df2):
    data = pd.merge(df2, df1[['Masked CCN', 'Amount', 'Card Brans', 'acq_tid']],
                how='left', on='acq_tid')
    
    # fill the missing data
    data['Amount'] = data['Amount'].fillna('0')
    data['Masked CCN'] = data['Masked CCN'].fillna('0')
    data['Amount'] = data['Amount'].astype(str)
   

    # adjust the cb value to whether there is a chargeback or not
    for index in data.index:
        if data.loc[index, 'Amount'] == '0':
            data.loc[index, 'cb'] = 0
        else:
            data.loc[index, 'cb'] = 1

    print(data['cb'].unique())

    # rename of Amount column on Amount_cb
    data = data.rename(columns={"Amount": "Amount_cb"})
    print(data.head())
    
    # put receive file to sql database
    data.to_sql("Transactions_cb", con, if_exists="replace")


if __name__ == "__main__":
    con = sql_connection()
    cur = con.cursor()
    df1 = read_excel_file('Processing Report.xlsx')
    df2 = read_sql('SELECT * FROM Transactions', con)
    changes_data(df1, df2)
    con.close()