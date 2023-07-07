import  sqlalchemy as db
import pandas as pd
engine = db.create_engine("mysql://root:root@localhost/mydatabase1")

conn = engine.connect()

query = db.text("insert into customers values ('TestName', 'TestAddress')")
conn.execute(query)
conn.commit()

query = db.text("SELECT * FROM customers")
output = conn.execute(query)
result = output.fetchall()

data = pd.DataFrame(result)
print(data)