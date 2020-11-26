import pandas as pd
import requests
import json

pd.options.display.max_columns = 30
# print(a)
api_key = "f01f7fafa5b6217e2c04cbc143a334ab"
basic_url = "https://api.themoviedb.org/3/movie/550"

json_list = []

m_result = requests.get("https://api.themoviedb.org/3/movie/550?api_key=f01f7fafa5b6217e2c04cbc143a334ab")
m_result = m_result.json()

for r in m_result:
    print(r)



