import time
import pyupbit
import datetime

access = "PLHmUf3gpoyKYzAqFzzxJ8vH042arYEQfcfdizx1"
secret = "mqsj8p9QYwd3A1Iich0KctXiz4ZJQrhDPxxA39DF"

#변동성 돌파 전략으로 매수 목표가 조회
def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    target_price = df.iloc[0]['close'] + ((df.iloc[0]['high'] - df.iloc[0]['low']) * k)
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

# 코인 심볼 하나씩 받아와서 이동평균선 구한 후 매수 조건 탐색
def get_ticker_ma(ticker):  
    '''get_ohlcv 함수는 고가/시가/저가/종가/거래량을 DataFrame으로 반환합니다'''
    df = pyupbit.get_ohlcv(ticker, interval="minute240") # 일봉 데이터 프레임 생성
    ma5.extend(df['close'])    # ma7 변수에 종가 넣기
    ma10.extend(df['close'])    # ma15 변수에 종가 넣기
    curr_ma5 = sum(ma5) / len(ma5)       # ma5값 더해서 나누기 = 5일선 이동평균
    curr_ma10 = sum(ma10) / len(ma10)       # ma10값 더해서 나누기 = 10일선 이동평균

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
        time.sleep(0.5)

        if now.hour == 9 and now.minute == 0 and 1 <=now.second <= 10:
            op_mode = True
            time.sleep(10)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-FCT2", 0.52)
            price = get_current_price("KRW-FCT2")
            buy_price = get_avg_buy_price("KRW-FCT2")
            if price < buy_price * 0.98:
                FCT2 = get_balance("FCT2")
                upbit.sell_market_order("KRW-FCT2", FCT2)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-FCT2")
                curr_ma10 = get_ticker_ma("KRW-FCT2")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    FCT2 = get_balance("FCT2")
                    if FCT2 < 0.0001:
                        upbit.buy_market_order("KRW-FCT2", 20000)
        else:
            FCT2 = get_balance("FCT2")
            if FCT2 > 0.0001:
                upbit.sell_market_order("KRW-FCT2", FCT2)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-CBK", 0.52)
            price = get_current_price("KRW-CBK")
            buy_price = get_avg_buy_price("KRW-CBK")
            if price < buy_price * 0.98:
                CBK = get_balance("CBK")
                upbit.sell_market_order("KRW-CBK", CBK)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-CBK")
                curr_ma10 = get_ticker_ma("KRW-CBK")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    CBK = get_balance("CBK")
                    if CBK < 0.0001:
                        upbit.buy_market_order("KRW-CBK", 20000)
        else:
            CBK = get_balance("CBK")
            if CBK > 0.0001:
                upbit.sell_market_order("KRW-CBK", CBK)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-SAND", 0.52)
            price = get_current_price("KRW-SAND")
            buy_price = get_avg_buy_price("KRW-SAND")
            if price < buy_price * 0.98:
                SAND = get_balance("SAND")
                upbit.sell_market_order("KRW-SAND", SAND)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-SAND")
                curr_ma10 = get_ticker_ma("KRW-SAND")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    SAND = get_balance("SAND")
                    if SAND < 0.0001:
                        upbit.buy_market_order("KRW-SAND", 20000)
        else:
            SAND = get_balance("SAND")
            if SAND > 0.0001:
                upbit.sell_market_order("KRW-SAND", SAND)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-HUM", 0.52)
            price = get_current_price("KRW-HUM")
            buy_price = get_avg_buy_price("KRW-HUM")
            if price < buy_price * 0.98:
                HUM = get_balance("HUM")
                upbit.sell_market_order("KRW-HUM", HUM)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-HUM")
                curr_ma10 = get_ticker_ma("KRW-HUM")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    HUM = get_balance("HUM")
                    if HUM < 0.0001:
                        upbit.buy_market_order("KRW-HUM", 20000)
        else:
            HUM = get_balance("HUM")
            if HUM > 0.0001:
                upbit.sell_market_order("KRW-HUM", HUM)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-DOGE", 0.52)
            price = get_current_price("KRW-DOGE")
            buy_price = get_avg_buy_price("KRW-DOGE")
            if price < buy_price * 0.98:
                DOGE = get_balance("DOGE")
                upbit.sell_market_order("KRW-DOGE", DOGE)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-DOGE")
                curr_ma10 = get_ticker_ma("KRW-DOGE")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    DOGE = get_balance("DOGE")
                    if DOGE < 0.0001:
                        upbit.buy_market_order("KRW-DOGE", 20000)
        else:
            DOGE = get_balance("DOGE")
            if DOGE > 0.0001:
                upbit.sell_market_order("KRW-DOGE", DOGE)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-STRK", 0.52)
            price = get_current_price("KRW-STRK")
            buy_price = get_avg_buy_price("KRW-STRK")
            if price < buy_price * 0.98:
                STRK = get_balance("STRK")
                upbit.sell_market_order("KRW-STRK", STRK)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-STRK")
                curr_ma10 = get_ticker_ma("KRW-STRK")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    STRK = get_balance("STRK")
                    if STRK < 0.0001:
                        upbit.buy_market_order("KRW-STRK", 20000)
        else:
            STRK = get_balance("STRK")
            if STRK > 0.0001:
                upbit.sell_market_order("KRW-STRK", STRK)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-PUNDIX", 0.52)
            price = get_current_price("KRW-PUNDIX")
            buy_price = get_avg_buy_price("KRW-PUNDIX")
            if price < buy_price * 0.98:
                PUNDIX = get_balance("PUNDIX")
                upbit.sell_market_order("KRW-PUNDIX", PUNDIX)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-PUNDIX")
                curr_ma10 = get_ticker_ma("KRW-PUNDIX")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    PUNDIX = get_balance("PUNDIX")
                    if PUNDIX < 0.0001:
                        upbit.buy_market_order("KRW-PUNDIX", 20000)
        else:
            PUNDIX = get_balance("PUNDIX")
            if PUNDIX > 0.0001:
                upbit.sell_market_order("KRW-PUNDIX", PUNDIX)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-FLOW", 0.52)
            price = get_current_price("KRW-FLOW")
            buy_price = get_avg_buy_price("KRW-FLOW")
            if price < buy_price * 0.98:
                FLOW = get_balance("FLOW")
                upbit.sell_market_order("KRW-FLOW", FLOW)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-FLOW")
                curr_ma10 = get_ticker_ma("KRW-FLOW")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    FLOW = get_balance("FLOW")
                    if FLOW < 0.0001:
                        upbit.buy_market_order("KRW-FLOW", 20000)
        else:
            FLOW = get_balance("FLOW")
            if FLOW > 0.0001:
                upbit.sell_market_order("KRW-FLOW", FLOW)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-DAWN", 0.52)
            price = get_current_price("KRW-DAWN")
            buy_price = get_avg_buy_price("KRW-DAWN")
            if price < buy_price * 0.98:
                DAWN = get_balance("DAWN")
                upbit.sell_market_order("KRW-DAWN", DAWN)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-DAWN")
                curr_ma10 = get_ticker_ma("KRW-DAWN")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    DAWN = get_balance("DAWN")
                    if DAWN < 0.0001:
                        upbit.buy_market_order("KRW-DAWN", 20000)
        else:
            DAWN = get_balance("DAWN")
            if DAWN > 0.0001:
                upbit.sell_market_order("KRW-DAWN", DAWN)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-AXS", 0.52)
            price = get_current_price("KRW-AXS")
            buy_price = get_avg_buy_price("KRW-AXS")
            if price < buy_price * 0.98:
                AXS = get_balance("AXS")
                upbit.sell_market_order("KRW-AXS", AXS)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-AXS")
                curr_ma10 = get_ticker_ma("KRW-AXS")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    AXS = get_balance("AXS")
                    if AXS < 0.0001:
                        upbit.buy_market_order("KRW-AXS", 20000)
        else:
            AXS = get_balance("AXS")
            if AXS > 0.0001:
                upbit.sell_market_order("KRW-AXS", AXS)

    except Exception as e:
        print(e)
        time.sleep(1)
