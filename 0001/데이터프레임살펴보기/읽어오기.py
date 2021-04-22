#데이터를 2차원 데이터의 형태인 테이블로 읽어오려면 PANDAS라이브러리 필요

import pandas as pd
import  numpy as np

df= pd.read_csv("../데이터분석1/2010.csv", encoding="utf-8")
print(df)

