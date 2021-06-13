import pyupbit

# 티커 '거래통화 - 코인명' => list 반환
def get_ticker(input=""):
    return pyupbit.get_tickers(fiat=input)

def get_price(input):
    return pyupbit.get_current_price(input)


ticker = get_ticker('KRW')

# usdt_btc = get_price('USDT-BTC')
coins_price = get_price(ticker)
coin_list = {}
for k, v in coins_price.items():
    coin_list[k[4:]] = [v,0 ,0,0,0]
    
print(coin_list)
    
    
# btc_krw = get_price('KRW-BTC')


