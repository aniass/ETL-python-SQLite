import sqlite3
import pandas as pd

# create SQL connecting with database
conn = sqlite3.connect("db.sqlite")
cur = conn.cursor()

# read Excel report
df1 = pd.read_excel('Processing Report.xlsx')

# load the data into a DataFrame
df2 = pd.read_sql('SELECT * FROM Transactions', conn)

# rename columns
trans = df1.rename(columns={"Transaction Datetime": "created_at", "ARN": "acq_tid", "Currnecy": "currency"})

# combine the tables
data = pd.merge(df2, trans[['Masked CCN', 'Amount', 'Card Brans', 'acq_tid']], how='left', on='acq_tid')

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
data.to_sql("Transactions_cb", conn, if_exists="replace")

# close the connection
conn.close()
