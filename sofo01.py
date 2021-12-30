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
            target = get_target_price("KRW-BTC", 0.52)
            price = get_current_price("KRW-BTC")
            buy_price = get_avg_buy_price("KRW-BTC")
            if price < buy_price * 0.98:
                BTC = get_balance("BTC")
                upbit.sell_market_order("KRW-BTC", BTC)
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-BTC")
                curr_ma10 = get_ticker_ma("KRW-BTC")
                if krw > 20000 and curr_ma5 > curr_ma10:
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
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-ETH")
                curr_ma10 = get_ticker_ma("KRW-ETH")
                if krw > 20000 and curr_ma5 > curr_ma10:
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
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-NEO")
                curr_ma10 = get_ticker_ma("KRW-NEO")
                if krw > 20000 and curr_ma5 > curr_ma10:
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
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-MTL")
                curr_ma10 = get_ticker_ma("KRW-MTL")
                if krw > 20000 and curr_ma5 > curr_ma10:
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
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-LTC")
                curr_ma10 = get_ticker_ma("KRW-LTC")
                if krw > 20000 and curr_ma5 > curr_ma10:
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
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-XRP")
                curr_ma10 = get_ticker_ma("KRW-XRP")
                if krw > 20000 and curr_ma5 > curr_ma10:
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
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-ETC")
                curr_ma10 = get_ticker_ma("KRW-ETC")
                if krw > 20000 and curr_ma5 > curr_ma10:
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
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-OMG")
                curr_ma10 = get_ticker_ma("KRW-OMG")
                if krw > 20000 and curr_ma5 > curr_ma10:
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
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-SNT")
                curr_ma10 = get_ticker_ma("KRW-SNT")
                if krw > 20000 and curr_ma5 > curr_ma10:
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
            if target < price < target * 1.01 and op_mode is True:
                krw = get_balance("KRW")
                curr_ma5 = get_ticker_ma("KRW-WAVES")
                curr_ma10 = get_ticker_ma("KRW-WAVES")
                if krw > 20000 and curr_ma5 > curr_ma10:
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
