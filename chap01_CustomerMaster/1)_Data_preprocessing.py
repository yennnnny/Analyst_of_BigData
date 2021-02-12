###[Data]###
# customer_master.csv : 고객 데이터, 이름, 성별 등
# item_master.csv : 취급하는 상품 데이터, 상품명, 가격 등
# transaction_1.csv / transaction_2.csv : 구매내역 데이터
# transaction_detail_1.csv / transaction_detail_2.csv : 구매 내역 상세 데이터

import pandas as pd

# data load
customer_master = pd.read_csv("C:\Data_PT\cahp01\customer_master.csv")
# ['customer_id', 'customer_name', 'registration_date', 'email', 'gender', 'age', 'birth', 'pref']
item_master = pd.read_csv("C:\Data_PT\cahp01\item_master.csv")  # item_id item_name  item_price
transaction_1 = pd.read_csv("C:\\Data_PT\\cahp01\\transaction_1.csv")  # transaction_id  price  payment_date  customer_id
transaction_2 = pd.read_csv("C:\\Data_PT\\cahp01\\transaction_2.csv")
transaction_detail_1 = pd.read_csv("C:\\Data_PT\\cahp01\\transaction_detail_1.csv")  # detail_id  transaction_id  item_id  quantity
transaction_detail_2 = pd.read_csv("C:\\Data_PT\\cahp01\\transaction_detail_2.csv")

# data check
#print(customer_master.head())  # customer_master, item_master, transaction_1, transaction_2, transaction_detail_1, transaction_detail_2)

# data concat
transaction = pd.concat([transaction_1, transaction_2], ignore_index = True)
transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index = True)

# transaction_detail + transaction > + customer_master > + item_master
total_tran = pd.merge(transaction_detail, transaction[["transaction_id", "payment_date", "customer_id"]], on = 'transaction_id', how = "left")
tran_customer = pd.merge(total_tran, customer_master, on = 'customer_id', how = 'left')
data = pd.merge(tran_customer, item_master, on = 'item_id', how = 'left')

# add 'price' columns
data['price'] = data['quantity']*data['item_price']

# check up
checking = sum(data['price']) == sum(transaction['price'])  # True

# save data
data.to_csv('join_data.csv', index=False, encoding='euc-kr')

## summary
#print(data.isnull().sum())  # number of null
#print(data.describe())  # statistic