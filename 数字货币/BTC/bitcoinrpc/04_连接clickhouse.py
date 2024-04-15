from clickhouse_driver import Client
host='127.0.0.1' #服务器地址
port =29000 #端口
user='default' #用户名
password='' #密码
database='btc' #数据库
send_receive_timeout = 5 #超时时间
conn = Client(host=host, port=port, user=user, password=password,database=database, send_receive_timeout=send_receive_timeout)
sql = 'select count(*) from address '
ans = conn.execute(sql)
print(ans)



insert_query = 'INSERT INTO `address` (`height`,`address`,`p_address`) VALUES (%s,%s,%s) '
sql_distinct_address = 'select distinct(address) from btc.address '
sql_height = 'select max(height) from btc.address '

csv_data = []
csv_data.append([1,'vin_address','vout_address'])
csv_data.append([2,'vin_address2','vout_address2'])
csv_data.append([2,'vin_address3','vout_address3'])
csv_data.append([2,'vin_address3','vout_address3'])

conn.execute('INSERT INTO `address` (`height`,`address`,`p_address`) VALUES', csv_data)


ret_distinct_address = conn.execute(sql_distinct_address)
print(ret_distinct_address)

ret_sql_height = conn.execute(sql_height)
print(ret_sql_height)

# pip install clickhouse_driver