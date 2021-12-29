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
            target = get_target_price("KRW-ADA", 0.52)
            price = get_current_price("KRW-ADA")
            buy_price = get_avg_buy_price("KRW-ADA")
            if price < buy_price * 0.98:
                ADA = get_balance("ADA")
                upbit.sell_market_order("KRW-ADA", ADA)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ADA = get_balance("ADA")
                    if ADA < 0.0001:
                        upbit.buy_market_order("KRW-ADA", 20000)
        else:
            ADA = get_balance("ADA")
            if ADA > 0.0001:
                upbit.sell_market_order("KRW-ADA", ADA)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-SBD", 0.52)
            price = get_current_price("KRW-SBD")
            buy_price = get_avg_buy_price("KRW-SBD")
            if price < buy_price * 0.98:
                SBD = get_balance("SBD")
                upbit.sell_market_order("KRW-SBD", SBD)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SBD = get_balance("SBD")
                    if SBD < 0.0001:
                        upbit.buy_market_order("KRW-SBD", 20000)
        else:
            SBD = get_balance("SBD")
            if SBD > 0.0001:
                upbit.sell_market_order("KRW-SBD", SBD)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-POWR", 0.52)
            price = get_current_price("KRW-POWR")
            buy_price = get_avg_buy_price("KRW-POWR")
            if price < buy_price * 0.98:
                POWR = get_balance("POWR")
                upbit.sell_market_order("KRW-POWR", POWR)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    POWR = get_balance("POWR")
                    if POWR < 0.0001:
                        upbit.buy_market_order("KRW-POWR", 20000)
        else:
            POWR = get_balance("POWR")
            if POWR > 0.0001:
                upbit.sell_market_order("KRW-POWR", POWR)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-BTG", 0.52)
            price = get_current_price("KRW-BTG")
            buy_price = get_avg_buy_price("KRW-BTG")
            if price < buy_price * 0.98:
                BTG = get_balance("BTG")
                upbit.sell_market_order("KRW-BTG", BTG)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    BTG = get_balance("BTG")
                    if BTG < 0.0001:
                        upbit.buy_market_order("KRW-BTG", 20000)
        else:
            BTG = get_balance("BTG")
            if BTG > 0.0001:
                upbit.sell_market_order("KRW-BTG", BTG)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-ICX", 0.52)
            price = get_current_price("KRW-ICX")
            buy_price = get_avg_buy_price("KRW-ICX")
            if price < buy_price * 0.98:
                ICX = get_balance("ICX")
                upbit.sell_market_order("KRW-ICX", ICX)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ICX = get_balance("ICX")
                    if ICX < 0.0001:
                        upbit.buy_market_order("KRW-ICX", 20000)
        else:
            ICX = get_balance("ICX")
            if ICX > 0.0001:
                upbit.sell_market_order("KRW-ICX", ICX)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-EOS", 0.52)
            price = get_current_price("KRW-EOS")
            buy_price = get_avg_buy_price("KRW-EOS")
            if price < buy_price * 0.98:
                EOS = get_balance("EOS")
                upbit.sell_market_order("KRW-EOS", EOS)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    EOS = get_balance("EOS")
                    if EOS < 0.0001:
                        upbit.buy_market_order("KRW-EOS", 20000)
        else:
            EOS = get_balance("EOS")
            if EOS > 0.0001:
                upbit.sell_market_order("KRW-EOS", EOS)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-TRX", 0.52)
            price = get_current_price("KRW-TRX")
            buy_price = get_avg_buy_price("KRW-TRX")
            if price < buy_price * 0.98:
                TRX = get_balance("TRX")
                upbit.sell_market_order("KRW-TRX", TRX)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    TRX = get_balance("TRX")
                    if TRX < 0.0001:
                        upbit.buy_market_order("KRW-TRX", 20000)
        else:
            TRX = get_balance("TRX")
            if TRX > 0.0001:
                upbit.sell_market_order("KRW-TRX", TRX)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-SC", 0.52)
            price = get_current_price("KRW-SC")
            buy_price = get_avg_buy_price("KRW-SC")
            if price < buy_price * 0.98:
                SC = get_balance("SC")
                upbit.sell_market_order("KRW-SC", SC)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SC = get_balance("SC")
                    if SC < 0.0001:
                        upbit.buy_market_order("KRW-SC", 20000)
        else:
            SC = get_balance("SC")
            if SC > 0.0001:
                upbit.sell_market_order("KRW-SC", SC)
            
        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-ONT", 0.52)
            price = get_current_price("KRW-ONT")
            buy_price = get_avg_buy_price("KRW-ONT")
            if price < buy_price * 0.98:
                ONT = get_balance("ONT")
                upbit.sell_market_order("KRW-ONT", ONT)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ONT = get_balance("ONT")
                    if ONT < 0.0001:
                        upbit.buy_market_order("KRW-ONT", 20000)
        else:
            ONT = get_balance("ONT")
            if ONT > 0.0001:
                upbit.sell_market_order("KRW-ONT", ONT)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-ZIL", 0.52)
            price = get_current_price("KRW-ZIL")
            buy_price = get_avg_buy_price("KRW-ZIL")
            if price < buy_price * 0.98:
                ZIL = get_balance("ZIL")
                upbit.sell_market_order("KRW-ZIL", ZIL)
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ZIL = get_balance("ZIL")
                    if ZIL < 0.0001:
                        upbit.buy_market_order("KRW-ZIL", 20000)
        else:
            ZIL = get_balance("ZIL")
            if ZIL > 0.0001:
                upbit.sell_market_order("KRW-ZIL", ZIL)

    except Exception as e:
        print(e)
        time.sleep(1)
