import requests

url = "https://www.binance.info/api/v3/uiKlines?limit=3&symbol=AVAXUSDT&interval=15m"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())

# Given data
data = response.json()

# Extract the value based on the index within the sub-array
try:
    value_vol_0 = int(float(data[0][5]))
# value_vol_1 = int(float(data[1][5]))
    print(value_vol_0)
except:
    print("error")
#count the volume percent increase
# increase_vol = value_vol_1 - value_vol_0
# percent_inc_vol = increase_vol/value_vol_0

# Print the extracted value
# print(f"Volume 1: {value_vol_0} and volume 2: {value_vol_1}, percent increase: {percent_inc_vol}" )


