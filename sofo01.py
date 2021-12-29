import time
import pyupbit
import datetime

access = "123"
secret = "123"

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

#매수평균가
def get_avg_buy_price(ticker):
    buy_price = upbit.get_avg_buy_price(ticker)
    return buy_price

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

op_mode = False

#자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(seconds=14400)

        if now.hour == 21 and now.minute == 0 and 1 <=now.second <= 10:
            op_mode = True
            time.sleep(10)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-BTC", 0.52)
            price = get_current_price("KRW-BTC")
            buy_price = get_avg_buy_price("KRW-BTC")
            if price < buy_price * 0.98:
                BTC = get_balance("BTC")
                upbit.sell_market_order("KRW-BTC", BTC)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-ETH", 0.52)
            price = get_current_price("KRW-ETH")
            buy_price = get_avg_buy_price("KRW-ETH")
            if price < buy_price * 0.98:
                ETH = get_balance("ETH")
                upbit.sell_market_order("KRW-ETH", ETH)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ETH = get_balance("ETH")
                    if ETH < 0.0001:
                        upbit.buy_market_order("KRW-ETH", 20000)
        else:
            ETH = get_balance("ETH")
            if ETH > 0.0001:
                upbit.sell_market_order("KRW-ETH", ETH)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-NEO", 0.52)
            price = get_current_price("KRW-NEO")
            buy_price = get_avg_buy_price("KRW-NEO")
            if price < buy_price * 0.98:
                NEO = get_balance("NEO")
                upbit.sell_market_order("KRW-NEO", NEO)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-MTL", 0.52)
            price = get_current_price("KRW-MTL")
            buy_price = get_avg_buy_price("KRW-MTL")
            if price < buy_price * 0.98:
                MTL = get_balance("MTL")
                upbit.sell_market_order("KRW-MTL", MTL)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-LTC", 0.52)
            price = get_current_price("KRW-LTC")
            buy_price = get_avg_buy_price("KRW-LTC")
            if price < buy_price * 0.98:
                LTC = get_balance("LTC")
                upbit.sell_market_order("KRW-LTC", LTC)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-XRP", 0.52)
            price = get_current_price("KRW-XRP")
            buy_price = get_avg_buy_price("KRW-XRP")
            if price < buy_price * 0.98:
                XRP = get_balance("XRP")
                upbit.sell_market_order("KRW-XRP", XRP)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-ETC", 0.52)
            price = get_current_price("KRW-ETC")
            buy_price = get_avg_buy_price("KRW-ETC")
            if price < buy_price * 0.98:
                ETC = get_balance("ETC")
                upbit.sell_market_order("KRW-ETC", ETC)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-OMG", 0.52)
            price = get_current_price("KRW-OMG")
            buy_price = get_avg_buy_price("KRW-OMG")
            if price < buy_price * 0.98:
                OMG = get_balance("OMG")
                upbit.sell_market_order("KRW-OMG", OMG)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-SNT", 0.52)
            price = get_current_price("KRW-SNT")
            buy_price = get_avg_buy_price("KRW-SNT")
            if price < buy_price * 0.98:
                SNT = get_balance("SNT")
                upbit.sell_market_order("KRW-SNT", SNT)
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

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-WAVES", 0.52)
            price = get_current_price("KRW-WAVES")
            buy_price = get_avg_buy_price("KRW-WAVES")
            if price < buy_price * 0.98:
                WAVES = get_balance("WAVES")
                upbit.sell_market_order("KRW-WAVES", WAVES)
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
