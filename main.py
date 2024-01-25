import requests
import schedule
import time


def get_coin_list():
    url = "https://www.tokocrypto.com/v1/market/trading-pairs?quoteAsset=USDT&offset=0&limit=1000"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    return data["data"]["list"]

def get_coin_data(coin):
    base_asset = coin["baseAsset"]
    url2 = "https://www.binance.info/api/v3/uiKlines?limit=3&symbol=" + base_asset + "USDT&interval=15m"

    payload = {} 
    headers = {}

    response2 = requests.request("GET", url2, headers=headers, data=payload)

    return response2.json()

def calculate_volume_change(data):
    value_vol_0 = int(float(data[0][5]))
    value_vol_1 = int(float(data[1][5]))
    
    increase_vol = value_vol_1 - value_vol_0
    percent_inc_vol = increase_vol/value_vol_0
    return percent_inc_vol

def print_volume_change(coin, percent_change):
    if percent_change > 5: 
        print(f"Coin: {coin}; vol change: {percent_change}")

def main():
    # Display start time
    start_time = time.time()
    print("Script started at: ", time.ctime(start_time)) 
    coin_list = get_coin_list()

    for coin in coin_list:
        data = get_coin_data(coin)
        try:
            percent_change = calculate_volume_change(data)
            print_volume_change(coin["baseAsset"], percent_change)
        except:
            print(coin["baseAsset"])


# def run_script():
#     main() 

# def schedule_job():
#     schedule.every(5).minutes.do(run_script)
    
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

if __name__ == "__main__":
    main()
