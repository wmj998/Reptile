from relation_mysql import action_table

action = action_table(host="localhost", user="root", password="w_f1216570180",
                      port=3306, db='test')

# 创建数据表
# information = 'id INT NOT NULL, ' \
#               'name VARCHAR(45) NOT NULL, ' \
#               'age VARCHAR(45) NOT NULL, ' \
#               'PRIMARY KEY (id)'
# action.create(table='information', information=information)

# 删除数据表
# action.drop(table='information')

# 查询数据
# action.query(table='students', what='*')

# 插入数据
# action.insert(table='students', keys=('id', 'name', 'age'), values=(2, 'Tom', '22'))

# 修改数据
# action.update(table='students', set='age=21', where='age=20')

# 删除数据
# action.delete(table='students', where='id=2')
