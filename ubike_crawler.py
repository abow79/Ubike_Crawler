import requests,json
import pandas as pd
area=input('請輸入您想要查詢ubike資訊的區域: ')
#從url取得資料
url='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
response=requests.get(url)
#使用json()來把原生資料轉換成JSON型態的資料結構,該方法以 Python 字典格式列印 JSON 數據。
json_data=response.json()
#print(json_data) <-這邊可以看一下JSON數據的資料




#先定義好最後資料的欄位名稱
col_names=['站點名稱','區域','可租借數','可歸還數']

#先準備一個空的List等添加json的資料進去
rows=[]

#注意x這時是表示第1個字典,第2個字典而不是0,1,2
for x in json_data:
    if(area in x['sarea']):
        rows.append(x)
df=pd.DataFrame(rows)

#這邊是用來擷取需要的欄位
df=df[['sna','sarea','available_rent_bikes','available_return_bikes']]

#修改欄位標題(下面兩個語法皆可選一個就好)
#df.rename(columns={'sna':'站點名稱','sarea':'區域','available_rent_bikes':'可租借數量','available_return_bikes':'可歸還空位'},inplace=True)  <-若inplace為true直接修改df
df.columns=col_names

#這個語法用來將DataFrame 中的值做slicing並置換
df['站點名稱']=df['站點名稱'].str.slice_replace(stop=11,repl='')
print(df)
