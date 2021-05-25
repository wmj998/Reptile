import pandas as pd
from pd_mysql import action

action = action(user='root', password='w_f1216570180',
                host='localhost', port=3306, db='test')

data = action.read(table='students')
print(data)

information = [[1, 'Tom', 20], [2, 'Bob', 22], [3, 'Allon', 23]]
columns = ['id', 'name', 'age']
data = pd.DataFrame(information, columns=columns)

action.save(table='information', data=data)
