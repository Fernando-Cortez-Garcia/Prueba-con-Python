import mysql.connector
import json
import pandas as pd

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database=""
)

cursor = db.cursor()
cursor.execute("SELECT * FROM usuarios")
result = cursor.fetchall()


#analizar el resultado con pandas
df = pd.DataFrame.abs(result)
print(df)





    