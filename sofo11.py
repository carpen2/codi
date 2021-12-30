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
            target = get_target_price("KRW-STX", 0.52)
            price = get_current_price("KRW-STX")
            buy_price = get_avg_buy_price("KRW-STX")
            if price < buy_price * 0.98:
                STX = get_balance("STX")
                upbit.sell_market_order("KRW-STX", STX)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-STX")
                curr_ma10 = get_ticker_ma("KRW-STX")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    STX = get_balance("STX")
                    if STX < 0.0001:
                        upbit.buy_market_order("KRW-STX", 20000)
        else:
            STX = get_balance("STX")
            if STX > 0.0001:
                upbit.sell_market_order("KRW-STX", STX)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-XEC", 0.52)
            price = get_current_price("KRW-XEC")
            buy_price = get_avg_buy_price("KRW-XEC")
            if price < buy_price * 0.98:
                XEC = get_balance("XEC")
                upbit.sell_market_order("KRW-XEC", XEC)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-XEC")
                curr_ma10 = get_ticker_ma("KRW-XEC")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    XEC = get_balance("XEC")
                    if XEC < 0.0001:
                        upbit.buy_market_order("KRW-XEC", 20000)
        else:
            XEC = get_balance("XEC")
            if XEC > 0.0001:
                upbit.sell_market_order("KRW-XEC", XEC)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-SOL", 0.52)
            price = get_current_price("KRW-SOL")
            buy_price = get_avg_buy_price("KRW-SOL")
            if price < buy_price * 0.98:
                SOL = get_balance("SOL")
                upbit.sell_market_order("KRW-SOL", SOL)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-SOL")
                curr_ma10 = get_ticker_ma("KRW-SOL")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    SOL = get_balance("SOL")
                    if SOL < 0.0001:
                        upbit.buy_market_order("KRW-SOL", 20000)
        else:
            SOL = get_balance("SOL")
            if SOL > 0.0001:
                upbit.sell_market_order("KRW-SOL", SOL)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-MATIC", 0.52)
            price = get_current_price("KRW-MATIC")
            buy_price = get_avg_buy_price("KRW-MATIC")
            if price < buy_price * 0.98:
                MATIC = get_balance("MATIC")
                upbit.sell_market_order("KRW-MATIC", MATIC)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-MATIC")
                curr_ma10 = get_ticker_ma("KRW-MATIC")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    MATIC = get_balance("MATIC")
                    if MATIC < 0.0001:
                        upbit.buy_market_order("KRW-MATIC", 20000)
        else:
            MATIC = get_balance("MATIC")
            if MATIC > 0.0001:
                upbit.sell_market_order("KRW-MATIC", MATIC)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-NU", 0.52)
            price = get_current_price("KRW-NU")
            buy_price = get_avg_buy_price("KRW-NU")
            if price < buy_price * 0.98:
                NU = get_balance("NU")
                upbit.sell_market_order("KRW-NU", NU)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-NU")
                curr_ma10 = get_ticker_ma("KRW-NU")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    NU = get_balance("NU")
                    if NU < 0.0001:
                        upbit.buy_market_order("KRW-NU", 20000)
        else:
            NU = get_balance("NU")
            if NU > 0.0001:
                upbit.sell_market_order("KRW-NU", NU)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-AAVE", 0.52)
            price = get_current_price("KRW-AAVE")
            buy_price = get_avg_buy_price("KRW-AAVE")
            if price < buy_price * 0.98:
                AAVE = get_balance("AAVE")
                upbit.sell_market_order("KRW-AAVE", AAVE)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-AAVE")
                curr_ma10 = get_ticker_ma("KRW-AAVE")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    AAVE = get_balance("AAVE")
                    if AAVE < 0.0001:
                        upbit.buy_market_order("KRW-AAVE", 20000)
        else:
            AAVE = get_balance("AAVE")
            if AAVE > 0.0001:
                upbit.sell_market_order("KRW-AAVE", AAVE)

        if start_time < now < end_time - datetime.timedelta(seconds=5):
            target = get_target_price("KRW-ALGO", 0.52)
            price = get_current_price("KRW-ALGO")
            buy_price = get_avg_buy_price("KRW-ALGO")
            if price < buy_price * 0.98:
                ALGO = get_balance("ALGO")
                upbit.sell_market_order("KRW-ALGO", ALGO)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-ALGO")
                curr_ma10 = get_ticker_ma("KRW-ALGO")
                if krw > 20000 and curr_ma5 > curr_ma10:
                    ALGO = get_balance("ALGO")
                    if ALGO < 0.0001:
                        upbit.buy_market_order("KRW-ALGO", 20000)
        else:
            ALGO = get_balance("ALGO")
            if ALGO > 0.0001:
                upbit.sell_market_order("KRW-ALGO", ALGO)

    except Exception as e:
        print(e)
        time.sleep(1)
