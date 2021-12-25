import time
import pyupbit
import datetime

access = "your-access"
secret = "your-secret"

#변동성 돌파 전략으로 매수 목표가 조회
def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

#시작 시간 조회"""
def get_start_time(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=1)
    start_time = df.index[0]
    return start_time
    
#잔고 조회
def get_balance(ticker):
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0
    
#현재가 조회
def get_current_price(ticker):
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

#hold = False
op_mode = False

#자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(seconds=14400)

        if now.hour == 9 and now.minute == 0 and 1 <=now.second <= 10:
            op_mode = True
            time.sleep(10)
            
        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-BTC", 0.51)
            price = get_current_price("KRW-BTC")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    BTC = get_balance("BTC")
                    if BTC < 0.0001:
                        upbit.buy_market_order("KRW-BTC", 20000)                   
        else:
            BTC = get_balance("BTC")
            if BTC > 0.0001:
                upbit.sell_market_order("KRW-BTC", BTC)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ETH", 0.51)
            price = get_current_price("KRW-ETH")
            if target < price  and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ETH = get_balance("ETH")
                    if ETH < 0.0001:
                        upbit.buy_market_order("KRW-ETH", 20000)                   
        else:
            ETH = get_balance("ETH")
            if ETH > 0.0001:
                upbit.sell_market_order("KRW-ETH", ETH)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-NEO", 0.51)
            price = get_current_price("KRW-NEO")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    NEO = get_balance("NEO")
                    if NEO < 0.0001:
                        upbit.buy_market_order("KRW-NEO", 20000)                   
        else:
            NEO = get_balance("NEO")
            if NEO > 0.0001:
                upbit.sell_market_order("KRW-NEO", NEO)               

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-MTL", 0.51)
            price = get_current_price("KRW-MTL")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MTL = get_balance("MTL")
                    if MTL < 0.0001:
                        upbit.buy_market_order("KRW-MTL", 20000)                   
        else:
            MTL = get_balance("MTL")
            if MTL > 0.0001:
                upbit.sell_market_order("KRW-MTL", MTL)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-LTC", 0.51)
            price = get_current_price("KRW-LTC")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    LTC = get_balance("LTC")
                    if LTC < 0.0001:
                        upbit.buy_market_order("KRW-LTC", 20000)                   
        else:
            LTC = get_balance("LTC")
            if LTC > 0.0001:
                upbit.sell_market_order("KRW-LTC", LTC)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-XRP", 0.51)
            price = get_current_price("KRW-XRP")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    XRP = get_balance("XRP")
                    if XRP < 0.0001:
                        upbit.buy_market_order("KRW-XRP", 20000)                   
        else:
            XRP = get_balance("XRP")
            if XRP > 0.0001:
                upbit.sell_market_order("KRW-XRP", XRP)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-ETC", 0.51)
            price = get_current_price("KRW-ETC")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ETC = get_balance("ETC")
                    if ETC < 0.0001:
                        upbit.buy_market_order("KRW-ETC", 20000)                   
        else:
            ETC = get_balance("ETC")
            if ETC > 0.0001:
                upbit.sell_market_order("KRW-ETC", ETC) 

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-OMG", 0.51)
            price = get_current_price("KRW-OMG")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    OMG = get_balance("OMG")
                    if OMG < 0.0001:
                        upbit.buy_market_order("KRW-OMG", 20000)                   
        else:
            OMG = get_balance("OMG")
            if OMG > 0.0001:
                upbit.sell_market_order("KRW-OMG", OMG)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-SNT", 0.51)
            price = get_current_price("KRW-SNT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SNT = get_balance("SNT")
                    if SNT < 0.0001:
                        upbit.buy_market_order("KRW-SNT", 20000)                   
        else:
            SNT = get_balance("SNT")
            if SNT > 0.0001:
                upbit.sell_market_order("KRW-SNT", SNT)

        if start_time < now < end_time - datetime.timedelta(seconds=20):
            target = get_target_price("KRW-WAVES", 0.51)
            price = get_current_price("KRW-WAVES")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    WAVES = get_balance("WAVES")
                    if WAVES < 0.0001:
                        upbit.buy_market_order("KRW-WAVES", 20000)                   
        else:
            WAVES = get_balance("WAVES")
            if WAVES > 0.0001:
                upbit.sell_market_order("KRW-WAVES", WAVES)

    except Exception as e:
        print(e)
        time.sleep(1)