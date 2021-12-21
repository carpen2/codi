import time
import pyupbit
import datetime

access = "123"
secret = "123"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval=day, count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-BTC", 0.51)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-BTC", 20000)
        else:
            btc = get_balance("BTC")
            if btc > 0.00008:              
                upbit.sell_market_order("KRW-BTC", btc)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ETH", 0.51)
            current_price = get_current_price("KRW-ETH")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ETH", 20000)
        else:
            ETH = get_balance("ETH")
            if ETH > 0.00008:              
                upbit.sell_market_order("KRW-ETH", ETH)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
    
    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-NEO", 0.51)
            current_price = get_current_price("KRW-NEO")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-NEO", 20000)
        else:
            NEO = get_balance("NEO")
            if NEO > 0.00008:              
                upbit.sell_market_order("KRW-NEO", NEO)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-MTL", 0.51)
            current_price = get_current_price("KRW-MTL")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-MTL", 20000)
        else:
            MTL = get_balance("MTL")
            if MTL > 0.00008:              
                upbit.sell_market_order("KRW-MTL", MTL)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-LTC", 0.51)
            current_price = get_current_price("KRW-LTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-LTC", 20000)
        else:
            LTC = get_balance("LTC")
            if LTC > 0.00008:              
                upbit.sell_market_order("KRW-LTC", LTC)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-XRP", 0.51)
            current_price = get_current_price("KRW-XRP")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-XRP", 20000)
        else:
            XRP = get_balance("XRP")
            if XRP > 0.00008:              
                upbit.sell_market_order("KRW-XRP", XRP)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ETC", 0.51)
            current_price = get_current_price("KRW-ETC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ETC", 20000)
        else:
            ETC = get_balance("ETC")
            if ETC > 0.00008:              
                upbit.sell_market_order("KRW-ETC", ETC)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-OMG", 0.51)
            current_price = get_current_price("KRW-OMG")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-OMG", 20000)
        else:
            OMG = get_balance("OMG")
            if OMG > 0.00008:              
                upbit.sell_market_order("KRW-OMG", OMG)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-SNT", 0.51)
            current_price = get_current_price("KRW-SNT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-SNT", 20000)
        else:
            SNT = get_balance("SNT")
            if SNT > 0.00008:              
                upbit.sell_market_order("KRW-SNT", SNT)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-WAVES", 0.51)
            current_price = get_current_price("KRW-WAVES")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-WAVES", 20000)
        else:
            WAVES = get_balance("WAVES")
            if WAVES > 0.00008:              
                upbit.sell_market_order("KRW-WAVES", WAVES)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-XEM", 0.51)
            current_price = get_current_price("KRW-XEM")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-XEM", 20000)
        else:
            XEM = get_balance("XEM")
            if XEM > 0.00008:              
                upbit.sell_market_order("KRW-XEM", XEM)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-QTUM", 0.51)
            current_price = get_current_price("KRW-QTUM")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-QTUM", 20000)
        else:
            QTUM = get_balance("QTUM")
            if QTUM > 0.00008:              
                upbit.sell_market_order("KRW-QTUM", QTUM)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-LSK", 0.51)
            current_price = get_current_price("KRW-LSK")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-LSK", 20000)
        else:
            LSK = get_balance("LSK")
            if LSK > 0.00008:              
                upbit.sell_market_order("KRW-LSK", LSK)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-STEEM", 0.51)
            current_price = get_current_price("KRW-STEEM")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-STEEM", 20000)
        else:
            STEEM = get_balance("STEEM")
            if STEEM > 0.00008:              
                upbit.sell_market_order("KRW-STEEM", STEEM)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-XLM", 0.51)
            current_price = get_current_price("KRW-XLM")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-XLM", 20000)
        else:
            XLM = get_balance("XLM")
            if XLM > 0.00008:              
                upbit.sell_market_order("KRW-XLM", XLM)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ARDR", 0.51)
            current_price = get_current_price("KRW-ARDR")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ARDR", 20000)
        else:
            ARDR = get_balance("ARDR")
            if ARDR > 0.00008:              
                upbit.sell_market_order("KRW-ARDR", ARDR)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ARK", 0.51)
            current_price = get_current_price("KRW-ARK")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ARK", 20000)
        else:
            ARK = get_balance("ARK")
            if ARK > 0.00008:              
                upbit.sell_market_order("KRW-ARK", ARK)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-STORJ", 0.51)
            current_price = get_current_price("KRW-STORJ")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-STORJ", 20000)
        else:
            STORJ = get_balance("STORJ")
            if STORJ > 0.00008:              
                upbit.sell_market_order("KRW-STORJ", STORJ)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-GRS", 0.51)
            current_price = get_current_price("KRW-GRS")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-GRS", 20000)
        else:
            GRS = get_balance("GRS")
            if GRS > 0.00008:              
                upbit.sell_market_order("KRW-GRS", GRS)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-REP", 0.51)
            current_price = get_current_price("KRW-REP")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-REP", 20000)
        else:
            REP = get_balance("REP")
            if REP > 0.00008:              
                upbit.sell_market_order("KRW-REP", REP)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ADA", 0.51)
            current_price = get_current_price("KRW-ADA")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ADA", 20000)
        else:
            ADA = get_balance("ADA")
            if ADA > 0.00008:              
                upbit.sell_market_order("KRW-ADA", ADA)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-SBD", 0.51)
            current_price = get_current_price("KRW-SBD")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-SBD", 20000)
        else:
            SBD = get_balance("SBD")
            if SBD > 0.00008:              
                upbit.sell_market_order("KRW-SBD", SBD)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-POWR", 0.51)
            current_price = get_current_price("KRW-POWR")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-POWR", 20000)
        else:
            POWR = get_balance("POWR")
            if POWR > 0.00008:              
                upbit.sell_market_order("KRW-POWR", POWR)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-BTG", 0.51)
            current_price = get_current_price("KRW-BTG")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-BTG", 20000)
        else:
            BTG = get_balance("BTG")
            if BTG > 0.00008:              
                upbit.sell_market_order("KRW-BTG", BTG)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ICX", 0.51)
            current_price = get_current_price("KRW-ICX")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ICX", 20000)
        else:
            ICX = get_balance("ICX")
            if ICX > 0.00008:              
                upbit.sell_market_order("KRW-ICX", ICX)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-EOS", 0.51)
            current_price = get_current_price("KRW-EOS")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-EOS", 20000)
        else:
            EOS = get_balance("EOS")
            if EOS > 0.00008:              
                upbit.sell_market_order("KRW-EOS", EOS)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-TRX", 0.51)
            current_price = get_current_price("KRW-TRX")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-TRX", 20000)
        else:
            TRX = get_balance("TRX")
            if TRX > 0.00008:              
                upbit.sell_market_order("KRW-TRX", TRX)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-SC", 0.51)
            current_price = get_current_price("KRW-SC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-SC", 20000)
        else:
            SC = get_balance("SC")
            if SC > 0.00008:              
                upbit.sell_market_order("KRW-SC", SC)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ONT", 0.51)
            current_price = get_current_price("KRW-ONT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ONT", 20000)
        else:
            ONT = get_balance("ONT")
            if ONT > 0.00008:              
                upbit.sell_market_order("KRW-ONT", ONT)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ZIL", 0.51)
            current_price = get_current_price("KRW-ZIL")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ZIL", 20000)
        else:
            ZIL = get_balance("ZIL")
            if ZIL > 0.00008:              
                upbit.sell_market_order("KRW-ZIL", ZIL)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-POLY", 0.51)
            current_price = get_current_price("KRW-POLY")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-POLY", 20000)
        else:
            POLY = get_balance("POLY")
            if POLY > 0.00008:              
                upbit.sell_market_order("KRW-POLY", POLY)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ZRX", 0.51)
            current_price = get_current_price("KRW-ZRX")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ZRX", 20000)
        else:
            ZRX = get_balance("ZRX")
            if ZRX > 0.00008:              
                upbit.sell_market_order("KRW-ZRX", ZRX)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-LOOM", 0.51)
            current_price = get_current_price("KRW-LOOM")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-LOOM", 20000)
        else:
            LOOM = get_balance("LOOM")
            if LOOM > 0.00008:              
                upbit.sell_market_order("KRW-LOOM", LOOM)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:        
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-BCH", 0.51)
            current_price = get_current_price("KRW-BCH")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-BCH", 20000)
        else:
            BCH = get_balance("BCH")
            if BCH > 0.00008:              
                upbit.sell_market_order("KRW-BCH", BCH)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-BAT", 0.51)
            current_price = get_current_price("KRW-BAT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-BAT", 20000)
        else:
            BAT = get_balance("BAT")
            if BAT > 0.00008:              
                upbit.sell_market_order("KRW-BAT", BAT)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-IOST", 0.51)
            current_price = get_current_price("KRW-IOST")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-IOST", 20000)
        else:
            IOST = get_balance("IOST")
            if IOST > 0.00008:              
                upbit.sell_market_order("KRW-IOST", IOST)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-RFR", 0.51)
            current_price = get_current_price("KRW-RFR")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-RFR", 20000)
        else:
            RFR = get_balance("RFR")
            if RFR > 0.00008:              
                upbit.sell_market_order("KRW-RFR", RFR)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-CVC", 0.51)
            current_price = get_current_price("KRW-CVC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-CVC", 20000)
        else:
            CVC = get_balance("CVC")
            if CVC > 0.00008:              
                upbit.sell_market_order("KRW-CVC", CVC)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-IQ", 0.51)
            current_price = get_current_price("KRW-IQ")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-IQ", 20000)
        else:
            IQ = get_balance("IQ")
            if IQ > 0.00008:              
                upbit.sell_market_order("KRW-IQ", IQ)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-IOTA", 0.51)
            current_price = get_current_price("KRW-IOTA")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-IOTA", 20000)
        else:
            IOTA = get_balance("IOTA")
            if IOTA > 0.00008:              
                upbit.sell_market_order("KRW-IOTA", IOTA)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-MFT", 0.51)
            current_price = get_current_price("KRW-MFT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-MFT", 20000)
        else:
            MFT = get_balance("MFT")
            if MFT > 0.00008:              
                upbit.sell_market_order("KRW-MFT", MFT)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ONG", 0.51)
            current_price = get_current_price("KRW-ONG")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ONG", 20000)
        else:
            ONG = get_balance("ONG")
            if ONG > 0.00008:              
                upbit.sell_market_order("KRW-ONG", ONG)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-GAS", 0.51)
            current_price = get_current_price("KRW-GAS")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-GAS", 20000)
        else:
            GAS = get_balance("GAS")
            if GAS > 0.00008:              
                upbit.sell_market_order("KRW-GAS", GAS)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-UPP", 0.51)
            current_price = get_current_price("KRW-UPP")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-UPP", 20000)
        else:
            UPP = get_balance("UPP")
            if UPP > 0.00008:              
                upbit.sell_market_order("KRW-UPP", UPP)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ELF", 0.51)
            current_price = get_current_price("KRW-ELF")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ELF", 20000)
        else:
            ELF = get_balance("ELF")
            if ELF > 0.00008:              
                upbit.sell_market_order("KRW-ELF", ELF)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-KNC", 0.51)
            current_price = get_current_price("KRW-KNC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-KNC", 20000)
        else:
            KNC = get_balance("KNC")
            if KNC > 0.00008:              
                upbit.sell_market_order("KRW-KNC", KNC)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-BSV", 0.51)
            current_price = get_current_price("KRW-BSV")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-BSV", 20000)
        else:
            BSV = get_balance("BSV")
            if BSV > 0.00008:              
                upbit.sell_market_order("KRW-BSV", BSV)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-THETA", 0.51)
            current_price = get_current_price("KRW-THETA")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-THETA", 20000)
        else:
            THETA = get_balance("THETA")
            if THETA > 0.00008:              
                upbit.sell_market_order("KRW-THETA", THETA)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-QKC", 0.51)
            current_price = get_current_price("KRW-QKC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-QKC", 20000)
        else:
            QKC = get_balance("QKC")
            if QKC > 0.00008:              
                upbit.sell_market_order("KRW-QKC", QKC)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-BTT", 0.51)
            current_price = get_current_price("KRW-BTT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-BTT", 20000)
        else:
            BTT = get_balance("BTT")
            if BTT > 0.00008:              
                upbit.sell_market_order("KRW-BTT", BTT)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-MOC", 0.51)
            current_price = get_current_price("KRW-MOC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-MOC", 20000)
        else:
            MOC = get_balance("MOC")
            if MOC > 0.00008:              
                upbit.sell_market_order("KRW-MOC", MOC)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ENJ", 0.51)
            current_price = get_current_price("KRW-ENJ")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ENJ", 20000)
        else:
            ENJ = get_balance("ENJ")
            if ENJ > 0.00008:              
                upbit.sell_market_order("KRW-ENJ", ENJ)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-TFUEL", 0.51)
            current_price = get_current_price("KRW-TFUEL")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-TFUEL", 20000)
        else:
            TFUEL = get_balance("TFUEL")
            if TFUEL > 0.00008:              
                upbit.sell_market_order("KRW-TFUEL", TFUEL)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-MANA", 0.51)
            current_price = get_current_price("KRW-MANA")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-MANA", 20000)
        else:
            MANA = get_balance("MANA")
            if MANA > 0.00008:              
                upbit.sell_market_order("KRW-MANA", MANA)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ANKR", 0.51)
            current_price = get_current_price("KRW-ANKR")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ANKR", 20000)
        else:
            ANKR = get_balance("ANKR")
            if ANKR > 0.00008:              
                upbit.sell_market_order("KRW-ANKR", ANKR)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-AERGO", 0.51)
            current_price = get_current_price("KRW-AERGO")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-AERGO", 20000)
        else:
            AERGO = get_balance("AERGO")
            if AERGO > 0.00008:              
                upbit.sell_market_order("KRW-AERGO", AERGO)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ATOM", 0.51)
            current_price = get_current_price("KRW-ATOM")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ATOM", 20000)
        else:
            ATOM = get_balance("ATOM")
            if ATOM > 0.00008:              
                upbit.sell_market_order("KRW-ATOM", ATOM)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-TT", 0.51)
            current_price = get_current_price("KRW-TT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-TT", 20000)
        else:
            TT = get_balance("TT")
            if TT > 0.00008:              
                upbit.sell_market_order("KRW-TT", TT)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-CRE", 0.51)
            current_price = get_current_price("KRW-CRE")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-CRE", 20000)
        else:
            CRE = get_balance("CRE")
            if CRE > 0.00008:              
                upbit.sell_market_order("KRW-CRE", CRE)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-MBL", 0.51)
            current_price = get_current_price("KRW-MBL")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-MBL", 20000)
        else:
            MBL = get_balance("MBL")
            if MBL > 0.00008:              
                upbit.sell_market_order("KRW-MBL", MBL)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-WAXP", 0.51)
            current_price = get_current_price("KRW-WAXP")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-WAXP", 20000)
        else:
            WAXP = get_balance("WAXP")
            if WAXP > 0.00008:              
                upbit.sell_market_order("KRW-WAXP", WAXP)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-HBAR", 0.51)
            current_price = get_current_price("KRW-HBAR")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-HBAR", 20000)
        else:
            HBAR = get_balance("HBAR")
            if HBAR > 0.00008:              
                upbit.sell_market_order("KRW-HBAR", HBAR)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-MED", 0.51)
            current_price = get_current_price("KRW-MED")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-MED", 20000)
        else:
            MED = get_balance("MED")
            if MED > 0.00008:              
                upbit.sell_market_order("KRW-MED", MED)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-MLK", 0.51)
            current_price = get_current_price("KRW-MLK")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-MLK", 20000)
        else:
            MLK = get_balance("MLK")
            if MLK > 0.00008:              
                upbit.sell_market_order("KRW-MLK", MLK)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-STPT", 0.51)
            current_price = get_current_price("KRW-STPT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-STPT", 20000)
        else:
            STPT = get_balance("STPT")
            if STPT > 0.00008:              
                upbit.sell_market_order("KRW-STPT", STPT)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ORBS", 0.51)
            current_price = get_current_price("KRW-ORBS")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ORBS", 20000)
        else:
            ORBS = get_balance("ORBS")
            if ORBS > 0.00008:              
                upbit.sell_market_order("KRW-ORBS", ORBS)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-VET", 0.51)
            current_price = get_current_price("KRW-VET")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-VET", 20000)
        else:
            VET = get_balance("VET")
            if VET > 0.00008:              
                upbit.sell_market_order("KRW-VET", VET)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-CHZ", 0.51)
            current_price = get_current_price("KRW-CHZ")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_markett_order("KRW-CHZ", 20000)
        else:
            CHZ = get_balance("CHZ")
            if CHZ > 0.00008:              
                upbit.sell_market_order("KRW-CHZ", CHZ)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-STMX", 0.51)
            current_price = get_current_price("KRW-STMX")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-STMX", 20000)
        else:
            STMX = get_balance("STMX")
            if STMX > 0.00008:              
                upbit.sell_market_order("KRW-STMX", STMX)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-DKA", 0.51)
            current_price = get_current_price("KRW-DKA")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-DKA", 20000)
        else:
            DKA = get_balance("DKA")
            if DKA > 0.00008:              
                upbit.sell_market_order("KRW-DKA", DKA)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-HIVE", 0.51)
            current_price = get_current_price("KRW-HIVE")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-HIVE", 20000)
        else:
            HIVE = get_balance("HIVE")
            if HIVE > 0.00008:              
                upbit.sell_market_order("KRW-HIVE", HIVE)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-KAVA", 0.51)
            current_price = get_current_price("KRW-KAVA")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-KAVA", 20000)
        else:
            KAVA = get_balance("KAVA")
            if KAVA > 0.00008:              
                upbit.sell_market_order("KRW-KAVA", KAVA)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-AHT", 0.51)
            current_price = get_current_price("KRW-AHT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-AHT", 20000)
        else:
            AHT = get_balance("AHT")
            if AHT > 0.00008:              
                upbit.sell_market_order("KRW-AHT", AHT)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-LINK", 0.51)
            current_price = get_current_price("KRW-LINK")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-LINK", 20000)
        else:
            LINK = get_balance("LINK")
            if LINK > 0.00008:              
                upbit.sell_market_order("KRW-LINK", LINK)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-XTZ", 0.51)
            current_price = get_current_price("KRW-XTZ")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-XTZ", 20000)
        else:
            XTZ = get_balance("XTZ")
            if XTZ > 0.00008:              
                upbit.sell_market_order("KRW-XTZ", XTZ)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-BORA", 0.51)
            current_price = get_current_price("KRW-BORA")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-BORA", 20000)
        else:
            BORA = get_balance("BORA")
            if BORA > 0.00008:              
                upbit.sell_market_order("KRW-BORA", BORA)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-JST", 0.51)
            current_price = get_current_price("KRW-JST")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-JST", 20000)
        else:
            JST = get_balance("JST")
            if JST > 0.00008:              
                upbit.sell_market_order("KRW-JST", JST)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-CRO", 0.51)
            current_price = get_current_price("KRW-CRO")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-CRO", 20000)
        else:
            CRO = get_balance("CRO")
            if CRO > 0.00008:              
                upbit.sell_market_order("KRW-CRO", CRO)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-TON", 0.51)
            current_price = get_current_price("KRW-TON")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-TON", 20000)
        else:
            TON = get_balance("TON")
            if TON > 0.00008:              
                upbit.sell_market_order("KRW-TON", TON)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-SXP", 0.51)
            current_price = get_current_price("KRW-SXP")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-SXP", 20000)
        else:
            SXP = get_balance("SXP")
            if SXP > 0.00008:              
                upbit.sell_market_order("KRW-SXP", SXP)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-HUNT", 0.51)
            current_price = get_current_price("KRW-HUNT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-HUNT", 20000)
        else:
            HUNT = get_balance("HUNT")
            if HUNT > 0.00008:              
                upbit.sell_market_order("KRW-HUNT", HUNT)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-PLA", 0.51)
            current_price = get_current_price("KRW-PLA")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-PLA", 20000)
        else:
            PLA = get_balance("PLA")
            if PLA > 0.00008:              
                upbit.sell_market_order("KRW-PLA", PLA)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-DOT", 0.51)
            current_price = get_current_price("KRW-DOT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-DOT", 20000)
        else:
            DOT = get_balance("DOT")
            if DOT > 0.00008:              
                upbit.sell_market_order("KRW-DOT", DOT)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-SRM", 0.51)
            current_price = get_current_price("KRW-SRM")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-SRM", 20000)
        else:
            SRM = get_balance("SRM")
            if SRM > 0.00008:              
                upbit.sell_market_order("KRW-SRM", SRM)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-MVL", 0.51)
            current_price = get_current_price("KRW-MVL")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-MVL", 20000)
        else:
            MVL = get_balance("MVL")
            if MVL > 0.00008:              
                upbit.sell_market_order("KRW-MVL", MVL)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-STRAX", 0.51)
            current_price = get_current_price("KRW-STRAX")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-STRAX", 20000)
        else:
            STRAX = get_balance("STRAX")
            if STRAX > 0.00008:              
                upbit.sell_market_order("KRW-STRAX", STRAX)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)        

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-AQT", 0.51)
            current_price = get_current_price("KRW-AQT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-AQT", 20000)
        else:
            AQT = get_balance("AQT")
            if AQT > 0.00008:              
                upbit.sell_market_order("KRW-AQT", AQT)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-GLM", 0.51)
            current_price = get_current_price("KRW-GLM")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-GLM", 20000)
        else:
            GLM = get_balance("GLM")
            if GLM > 0.00008:              
                upbit.sell_market_order("KRW-GLM", GLM)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-SSX", 0.51)
            current_price = get_current_price("KRW-SSX")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-SSX", 20000)
        else:
            SSX = get_balance("SSX")
            if SSX > 0.00008:              
                upbit.sell_market_order("KRW-SSX", SSX)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-META", 0.51)
            current_price = get_current_price("KRW-META")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-META", 20000)
        else:
            META = get_balance("META")
            if META > 0.00008:              
                upbit.sell_market_order("KRW-META", META)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
    
    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-FCT2", 0.51)
            current_price = get_current_price("KRW-FCT2")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-FCT2", 20000)
        else:
            FCT2 = get_balance("FCT2")
            if FCT2 > 0.00008:              
                upbit.sell_market_order("KRW-FCT2", FCT2)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-CBK", 0.51)
            current_price = get_current_price("KRW-CBK")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-CBK", 20000)
        else:
            CBK = get_balance("CBK")
            if CBK > 0.00008:              
                upbit.sell_market_order("KRW-CBK", CBK)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-SAND", 0.51)
            current_price = get_current_price("KRW-SAND")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-SAND", 20000)
        else:
            SAND = get_balance("SAND")
            if SAND > 0.00008:              
                upbit.sell_market_order("KRW-SAND", SAND)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-HUM", 0.51)
            current_price = get_current_price("KRW-HUM")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-HUM", 20000)
        else:
            HUM = get_balance("HUM")
            if HUM > 0.00008:              
                upbit.sell_market_order("KRW-HUM", HUM)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-DOGE", 0.51)
            current_price = get_current_price("KRW-DOGE")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-DOGE", 20000)
        else:
            DOGE = get_balance("DOGE")
            if DOGE > 0.00008:              
                upbit.sell_market_order("KRW-DOGE", DOGE)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-STRK", 0.51)
            current_price = get_current_price("KRW-STRK")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-STRK", 20000)
        else:
            STRK = get_balance("STRK")
            if STRK > 0.00008:              
                upbit.sell_market_order("KRW-STRK", STRK)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-PUNDIX", 0.51)
            current_price = get_current_price("KRW-PUNDIX")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-PUNDIX", 20000)
        else:
            PUNDIX = get_balance("PUNDIX")
            if PUNDIX > 0.00008:              
                upbit.sell_market_order("KRW-PUNDIX", PUNDIX)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-FLOW", 0.51)
            current_price = get_current_price("KRW-FLOW")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-FLOW", 20000)
        else:
            FLOW = get_balance("FLOW")
            if FLOW > 0.00008:              
                upbit.sell_market_order("KRW-FLOW", FLOW)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-DAWN", 0.51)
            current_price = get_current_price("KRW-DAWN")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-DAWN", 20000)
        else:
            DAWN = get_balance("DAWN")
            if DAWN > 0.00008:              
                upbit.sell_market_order("KRW-DAWN", DAWN)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-AXS", 0.51)
            current_price = get_current_price("KRW-AXS")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-AXS", 20000)
        else:
            AXS = get_balance("AXS")
            if AXS > 0.00008:              
                upbit.sell_market_order("KRW-AXS", AXS)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-STX", 0.51)
            current_price = get_current_price("KRW-STX")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-STX", 20000)
        else:
            STX = get_balance("STX")
            if STX > 0.00008:              
                upbit.sell_market_order("KRW-STX", STX)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-XEC", 0.51)
            current_price = get_current_price("KRW-XEC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-XEC", 20000)
        else:
            XEC = get_balance("XEC")
            if XEC > 0.00008:              
                upbit.sell_market_order("KRW-XEC", XEC)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-SOL", 0.51)
            current_price = get_current_price("KRW-SOL")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-SOL", 20000)
        else:
            SOL = get_balance("SOL")
            if SOL > 0.00008:              
                upbit.sell_market_order("KRW-SOL", SOL)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-MATIC", 0.51)
            current_price = get_current_price("KRW-MATIC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-MATIC", 20000)
        else:
            MATIC = get_balance("MATIC")
            if MATIC > 0.00008:              
                upbit.sell_market_order("KRW-MATIC", MATIC)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-NU", 0.51)
            current_price = get_current_price("KRW-NU")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-NU", 20000)
        else:
            NU = get_balance("NU")
            if NU > 0.00008:              
                upbit.sell_market_order("KRW-NU", NU)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-AAVE", 0.51)
            current_price = get_current_price("KRW-AAVE")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-AAVE", 20000)
        else:
            AAVE = get_balance("AAVE")
            if AAVE > 0.00008:              
                upbit.sell_market_order("KRW-AAVE", AAVE)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-ALGO", 0.51)
            current_price = get_current_price("KRW-ALGO")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-ALGO", 20000)
        else:
            ALGO = get_balance("ALGO")
            if ALGO > 0.00008:              
                upbit.sell_market_order("KRW-ALGO", ALGO)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    try:
        now = datetime.datetime.now()

        if now.minute %  240 == 0: 
            target_price = get_target_price("KRW-NEAR", 0.51)
            current_price = get_current_price("KRW-NEAR")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 20000:
                    upbit.buy_market_order("KRW-NEAR", 20000)
        else:
            NEAR = get_balance("NEAR")
            if NEAR > 0.00008:              
                upbit.sell_market_order("KRW-NEAR", NEAR)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
