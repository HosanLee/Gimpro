import pyupbit

# 티커 '거래통화 - 코인명' => list 반환
def get_ticker(input=""):
    return pyupbit.get_tickers(fiat=input)

def get_price(input):
    return pyupbit.get_current_price(input)


ticker = get_ticker('KRW')

usdt_btc = get_price('USDT-BTC')
# coins_price = get_price(ticker)
# print(coins_price)

btc_krw = get_price('KRW-BTC')
print(btc_krw)
print(usdt_btc)
usdt = btc_krw / usdt_btc
print(usdt)

