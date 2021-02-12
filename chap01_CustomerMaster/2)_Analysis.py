import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("join_data.csv", encoding='euc-kr')
# print(data.dtypes)

# 날짜 데이터 형식 변환
data['payment_date'] = pd.to_datetime(data["payment_date"])  # type 변환 : object -> datetime
data['payment_month'] = data['payment_date'].dt.strftime('%Y%m')  # dt : 년·월 추출, time.strftime() : 형태에 맞게 날짜반환
#print(data[['payment_month', 'payment_date']].head())

# monthly price
monthly_price = data.groupby('payment_month').sum()['price']  # groupby(집계하고싶은 컬럼).집계방법()[특정컬럼만 추출하고싶을 경우]
monthly_pivot = pd.pivot_table(data, index = 'payment_month', columns = 'item_name', values = 'price', aggfunc = 'sum')
# pd.pivot_table(data, index = 행으로 표현할 속성, columns = 열로 표현할 속성, values = 집계하고 싶은 속성, aggfunc = 집계방법)

# monthly item price
monthly_item_price = data.groupby(['payment_month', 'item_name']).sum()[['price', 'quantity']]
monthly_item_pivot = pd.pivot_table(data, index = 'item_name', columns = 'payment_month', values = ['price', 'quantity'], aggfunc = 'sum')

# visualization
plt.plot(list(monthly_pivot.index), monthly_pivot["PC-A"], label='PC-A')
plt.plot(list(monthly_pivot.index), monthly_pivot["PC-B"], label='PC-B')
plt.plot(list(monthly_pivot.index), monthly_pivot["PC-C"], label='PC-C')
plt.plot(list(monthly_pivot.index), monthly_pivot["PC-D"], label='PC-D')
plt.plot(list(monthly_pivot.index), monthly_pivot["PC-E"], label='PC-E')
plt.legend()
plt.show()
