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

        if now.hour == 21 and now.minute == 0 and 1 <=now.second <= 10:
            op_mode = True
            time.sleep(10)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ETH", 0.51)
            price = get_current_price("KRW-ETH")
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-XEM", 0.51)
            price = get_current_price("KRW-XEM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    XEM = get_balance("XEM")
                    if XEM < 0.0001:
                        upbit.buy_market_order("KRW-XEM", 20000)                   
        else:
            XEM = get_balance("XEM")
            if XEM > 0.0001:
                upbit.sell_market_order("KRW-XEM", XEM)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-QTUM", 0.51)
            price = get_current_price("KRW-QTUM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    QTUM = get_balance("QTUM")
                    if QTUM < 0.0001:
                        upbit.buy_market_order("KRW-QTUM", 20000)                   
        else:
            QTUM = get_balance("QTUM")
            if QTUM > 0.0001:
                upbit.sell_market_order("KRW-QTUM", QTUM)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-LSK", 0.51)
            price = get_current_price("KRW-LSK")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    LSK = get_balance("LSK")
                    if LSK < 0.0001:
                        upbit.buy_market_order("KRW-LSK", 20000)                   
        else:
            LSK = get_balance("LSK")
            if LSK > 0.0001:
                upbit.sell_market_order("KRW-LSK", LSK)               

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-STEEM", 0.51)
            price = get_current_price("KRW-STEEM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    STEEM = get_balance("STEEM")
                    if STEEM < 0.0001:
                        upbit.buy_market_order("KRW-STEEM", 20000)                   
        else:
            STEEM = get_balance("STEEM")
            if STEEM > 0.0001:
                upbit.sell_market_order("KRW-STEEM", STEEM)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-XLM", 0.51)
            price = get_current_price("KRW-XLM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    XLM = get_balance("XLM")
                    if XLM < 0.0001:
                        upbit.buy_market_order("KRW-XLM", 20000)                   
        else:
            XLM = get_balance("XLM")
            if XLM > 0.0001:
                upbit.sell_market_order("KRW-XLM", XLM)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ARDR", 0.51)
            price = get_current_price("KRW-ARDR")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ARDR = get_balance("ARDR")
                    if ARDR < 0.0001:
                        upbit.buy_market_order("KRW-ARDR", 20000)                   
        else:
            ARDR = get_balance("ARDR")
            if ARDR > 0.0001:
                upbit.sell_market_order("KRW-ARDR", ARDR)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ARK", 0.51)
            price = get_current_price("KRW-ARK")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ARK = get_balance("ARK")
                    if ARK < 0.0001:
                        upbit.buy_market_order("KRW-ARK", 20000)                   
        else:
            ARK = get_balance("ARK")
            if ARK > 0.0001:
                upbit.sell_market_order("KRW-ARK", ARK)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-STORJ", 0.51)
            price = get_current_price("KRW-STORJ")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    STORJ = get_balance("STORJ")
                    if STORJ < 0.0001:
                        upbit.buy_market_order("KRW-STORJ", 20000)                   
        else:
            STORJ = get_balance("STORJ")
            if STORJ > 0.0001:
                upbit.sell_market_order("KRW-STORJ", STORJ)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-GRS", 0.51)
            price = get_current_price("KRW-GRS")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    GRS = get_balance("GRS")
                    if GRS < 0.0001:
                        upbit.buy_market_order("KRW-GRS", 20000)                   
        else:
            GRS = get_balance("GRS")
            if GRS > 0.0001:
                upbit.sell_market_order("KRW-GRS", GRS)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-REP", 0.51)
            price = get_current_price("KRW-REP")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    REP = get_balance("REP")
                    if REP < 0.0001:
                        upbit.buy_market_order("KRW-REP", 20000)                   
        else:
            REP = get_balance("REP")
            if REP > 0.0001:
                upbit.sell_market_order("KRW-REP", REP)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ADA", 0.51)
            price = get_current_price("KRW-ADA")
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-SBD", 0.51)
            price = get_current_price("KRW-SBD")
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-POWR", 0.51)
            price = get_current_price("KRW-POWR")
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-BTG", 0.51)
            price = get_current_price("KRW-BTG")
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ICX", 0.51)
            price = get_current_price("KRW-ICX")
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-EOS", 0.51)
            price = get_current_price("KRW-EOS")
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-TRX", 0.51)
            price = get_current_price("KRW-TRX")
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-SC", 0.51)
            price = get_current_price("KRW-SC")
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ONT", 0.51)
            price = get_current_price("KRW-ONT")
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ZIL", 0.51)
            price = get_current_price("KRW-ZIL")
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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-POLY", 0.51)
            price = get_current_price("KRW-POLY")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    POLY = get_balance("POLY")
                    if POLY < 0.0001:
                        upbit.buy_market_order("KRW-POLY", 20000)                   
        else:
            POLY = get_balance("POLY")
            if POLY > 0.0001:
                upbit.sell_market_order("KRW-POLY", POLY)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ZRX", 0.51)
            price = get_current_price("KRW-ZRX")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ZRX = get_balance("ZRX")
                    if ZRX < 0.0001:
                        upbit.buy_market_order("KRW-ZRX", 20000)                   
        else:
            ZRX = get_balance("ZRX")
            if ZRX > 0.0001:
                upbit.sell_market_order("KRW-ZRX", ZRX)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-LOOM", 0.51)
            price = get_current_price("KRW-LOOM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    LOOM = get_balance("LOOM")
                    if LOOM < 0.0001:
                        upbit.buy_market_order("KRW-LOOM", 20000)                   
        else:
            LOOM = get_balance("LOOM")
            if LOOM > 0.0001:
                upbit.sell_market_order("KRW-LOOM", LOOM)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-BCH", 0.51)
            price = get_current_price("KRW-BCH")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    BCH = get_balance("BCH")
                    if BCH < 0.0001:
                        upbit.buy_market_order("KRW-BCH", 20000)                   
        else:
            BCH = get_balance("BCH")
            if BCH > 0.0001:
                upbit.sell_market_order("KRW-BCH", BCH)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-BAT", 0.51)
            price = get_current_price("KRW-BAT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    BAT = get_balance("BAT")
                    if BAT < 0.0001:
                        upbit.buy_market_order("KRW-BAT", 20000)                   
        else:
            BAT = get_balance("BAT")
            if BAT > 0.0001:
                upbit.sell_market_order("KRW-BAT", BAT)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-IOST", 0.51)
            price = get_current_price("KRW-IOST")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    IOST = get_balance("IOST")
                    if IOST < 0.0001:
                        upbit.buy_market_order("KRW-IOST", 20000)                   
        else:
            IOST = get_balance("IOST")
            if IOST > 0.0001:
                upbit.sell_market_order("KRW-IOST", IOST)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-RFR", 0.51)
            price = get_current_price("KRW-RFR")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    RFR = get_balance("RFR")
                    if RFR < 0.0001:
                        upbit.buy_market_order("KRW-RFR", 20000)                   
        else:
            RFR = get_balance("RFR")
            if RFR > 0.0001:
                upbit.sell_market_order("KRW-RFR", RFR)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-CVC", 0.51)
            price = get_current_price("KRW-CVC")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    CVC = get_balance("CVC")
                    if CVC < 0.0001:
                        upbit.buy_market_order("KRW-CVC", 20000)                   
        else:
            CVC = get_balance("CVC")
            if CVC > 0.0001:
                upbit.sell_market_order("KRW-CVC", CVC)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-IQ", 0.51)
            price = get_current_price("KRW-IQ")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    IQ = get_balance("IQ")
                    if IQ < 0.0001:
                        upbit.buy_market_order("KRW-IQ", 20000)                   
        else:
            IQ = get_balance("IQ")
            if IQ > 0.0001:
                upbit.sell_market_order("KRW-IQ", IQ)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-IOTA", 0.51)
            price = get_current_price("KRW-IOTA")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    IOTA = get_balance("IOTA")
                    if IOTA < 0.0001:
                        upbit.buy_market_order("KRW-IOTA", 20000)                   
        else:
            IOTA = get_balance("IOTA")
            if IOTA > 0.0001:
                upbit.sell_market_order("KRW-IOTA", IOTA)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-MFT", 0.51)
            price = get_current_price("KRW-MFT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MFT = get_balance("MFT")
                    if MFT < 0.0001:
                        upbit.buy_market_order("KRW-MFT", 20000)                   
        else:
            MFT = get_balance("MFT")
            if MFT > 0.0001:
                upbit.sell_market_order("KRW-MFT", MFT)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ONG", 0.51)
            price = get_current_price("KRW-ONG")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ONG = get_balance("ONG")
                    if ONG < 0.0001:
                        upbit.buy_market_order("KRW-ONG", 20000)                   
        else:
            ONG = get_balance("ONG")
            if ONG > 0.0001:
                upbit.sell_market_order("KRW-ONG", ONG)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-GAS", 0.51)
            price = get_current_price("KRW-GAS")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    GAS = get_balance("GAS")
                    if GAS < 0.0001:
                        upbit.buy_market_order("KRW-GAS", 20000)                   
        else:
            GAS = get_balance("GAS")
            if GAS > 0.0001:
                upbit.sell_market_order("KRW-GAS", GAS)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-UPP", 0.51)
            price = get_current_price("KRW-UPP")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    UPP = get_balance("UPP")
                    if UPP < 0.0001:
                        upbit.buy_market_order("KRW-UPP", 20000)                   
        else:
            UPP = get_balance("UPP")
            if UPP > 0.0001:
                upbit.sell_market_order("KRW-UPP", UPP)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ELF", 0.51)
            price = get_current_price("KRW-ELF")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ELF = get_balance("ELF")
                    if ELF < 0.0001:
                        upbit.buy_market_order("KRW-ELF", 20000)                   
        else:
            ELF = get_balance("ELF")
            if ELF > 0.0001:
                upbit.sell_market_order("KRW-ELF", ELF)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-KNC", 0.51)
            price = get_current_price("KRW-KNC")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    KNC = get_balance("KNC")
                    if KNC < 0.0001:
                        upbit.buy_market_order("KRW-KNC", 20000)                   
        else:
            KNC = get_balance("KNC")
            if KNC > 0.0001:
                upbit.sell_market_order("KRW-KNC", KNC)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-BSV", 0.51)
            price = get_current_price("KRW-BSV")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    BSV = get_balance("BSV")
                    if BSV < 0.0001:
                        upbit.buy_market_order("KRW-BSV", 20000)                   
        else:
            BSV = get_balance("BSV")
            if BSV > 0.0001:
                upbit.sell_market_order("KRW-BSV", BSV)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-THETA", 0.51)
            price = get_current_price("KRW-THETA")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    THETA = get_balance("THETA")
                    if THETA < 0.0001:
                        upbit.buy_market_order("KRW-THETA", 20000)                   
        else:
            THETA = get_balance("THETA")
            if THETA > 0.0001:
                upbit.sell_market_order("KRW-THETA", THETA)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-QKC", 0.51)
            price = get_current_price("KRW-QKC")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    QKC = get_balance("QKC")
                    if QKC < 0.0001:
                        upbit.buy_market_order("KRW-QKC", 20000)                   
        else:
            QKC = get_balance("QKC")
            if QKC > 0.0001:
                upbit.sell_market_order("KRW-QKC", QKC)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-BTT", 0.51)
            price = get_current_price("KRW-BTT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    BTT = get_balance("BTT")
                    if BTT < 0.0001:
                        upbit.buy_market_order("KRW-BTT", 20000)                   
        else:
            BTT = get_balance("BTT")
            if BTT > 0.0001:
                upbit.sell_market_order("KRW-BTT", BTT)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-MOC", 0.51)
            price = get_current_price("KRW-MOC")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MOC = get_balance("MOC")
                    if MOC < 0.0001:
                        upbit.buy_market_order("KRW-MOC", 20000)                   
        else:
            MOC = get_balance("MOC")
            if MOC > 0.0001:
                upbit.sell_market_order("KRW-MOC", MOC)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ENJ", 0.51)
            price = get_current_price("KRW-ENJ")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ENJ = get_balance("ENJ")
                    if ENJ < 0.0001:
                        upbit.buy_market_order("KRW-ENJ", 20000)                   
        else:
            ENJ = get_balance("ENJ")
            if ENJ > 0.0001:
                upbit.sell_market_order("KRW-ENJ", ENJ)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-TFUEL", 0.51)
            price = get_current_price("KRW-TFUEL")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    TFUEL = get_balance("TFUEL")
                    if TFUEL < 0.0001:
                        upbit.buy_market_order("KRW-TFUEL", 20000)
        else:
            TFUEL = get_balance("TFUEL")
            if TFUEL > 0.0001:
                upbit.sell_market_order("KRW-TFUEL", TFUEL)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-MANA", 0.51)
            price = get_current_price("KRW-MANA")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MANA = get_balance("MANA")
                    if MANA < 0.0001:
                        upbit.buy_market_order("KRW-MANA", 20000)
        else:
            MANA = get_balance("MANA")
            if MANA > 0.0001:
                upbit.sell_market_order("KRW-MANA", MANA)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ANKR", 0.51)
            price = get_current_price("KRW-ANKR")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ANKR = get_balance("ANKR")
                    if ANKR < 0.0001:
                        upbit.buy_market_order("KRW-ANKR", 20000)
        else:
            ANKR = get_balance("ANKR")
            if ANKR > 0.0001:
                upbit.sell_market_order("KRW-ANKR", ANKR)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-AERGO", 0.51)
            price = get_current_price("KRW-AERGO")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    AERGO = get_balance("AERGO")
                    if AERGO < 0.0001:
                        upbit.buy_market_order("KRW-AERGO", 20000)
        else:
            AERGO = get_balance("AERGO")
            if AERGO > 0.0001:
                upbit.sell_market_order("KRW-AERGO", AERGO)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-AERGO", 0.51)
            price = get_current_price("KRW-AERGO")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    AERGO = get_balance("AERGO")
                    if AERGO < 0.0001:
                        upbit.buy_market_order("KRW-AERGO", 20000)
        else:
            AERGO = get_balance("AERGO")
            if AERGO > 0.0001:
                upbit.sell_market_order("KRW-AERGO", AERGO)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ATOM", 0.51)
            price = get_current_price("KRW-ATOM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ATOM = get_balance("ATOM")
                    if ATOM < 0.0001:
                        upbit.buy_market_order("KRW-ATOM", 20000)
        else:
            ATOM = get_balance("ATOM")
            if ATOM > 0.0001:
                upbit.sell_market_order("KRW-ATOM", ATOM)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-TT", 0.51)
            price = get_current_price("KRW-TT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    TT = get_balance("TT")
                    if TT < 0.0001:
                        upbit.buy_market_order("KRW-TT", 20000)
        else:
            TT = get_balance("TT")
            if TT > 0.0001:
                upbit.sell_market_order("KRW-TT", TT)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-CRE", 0.51)
            price = get_current_price("KRW-CRE")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    CRE = get_balance("CRE")
                    if CRE < 0.0001:
                        upbit.buy_market_order("KRW-CRE", 20000)
        else:
            CRE = get_balance("CRE")
            if CRE > 0.0001:
                upbit.sell_market_order("KRW-CRE", CRE)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-MBL", 0.51)
            price = get_current_price("KRW-MBL")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MBL = get_balance("MBL")
                    if MBL < 0.0001:
                        upbit.buy_market_order("KRW-MBL", 20000)
        else:
            MBL = get_balance("MBL")
            if MBL > 0.0001:
                upbit.sell_market_order("KRW-MBL", MBL)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-WAXP", 0.51)
            price = get_current_price("KRW-WAXP")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    WAXP = get_balance("WAXP")
                    if WAXP < 0.0001:
                        upbit.buy_market_order("KRW-WAXP", 20000)
        else:
            WAXP = get_balance("WAXP")
            if WAXP > 0.0001:
                upbit.sell_market_order("KRW-WAXP", WAXP)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-HBAR", 0.51)
            price = get_current_price("KRW-HBAR")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    HBAR = get_balance("HBAR")
                    if HBAR < 0.0001:
                        upbit.buy_market_order("KRW-HBAR", 20000)
        else:
            HBAR = get_balance("HBAR")
            if HBAR > 0.0001:
                upbit.sell_market_order("KRW-HBAR", HBAR)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-MED", 0.51)
            price = get_current_price("KRW-MED")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MED = get_balance("MED")
                    if MED < 0.0001:
                        upbit.buy_market_order("KRW-MED", 20000)
        else:
            MED = get_balance("MED")
            if MED > 0.0001:
                upbit.sell_market_order("KRW-MED", MED)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-MLK", 0.51)
            price = get_current_price("KRW-MLK")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MLK = get_balance("MLK")
                    if MLK < 0.0001:
                        upbit.buy_market_order("KRW-MLK", 20000)
        else:
            MLK = get_balance("MLK")
            if MLK > 0.0001:
                upbit.sell_market_order("KRW-MLK", MLK)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-STPT", 0.51)
            price = get_current_price("KRW-STPT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    STPT = get_balance("STPT")
                    if STPT < 0.0001:
                        upbit.buy_market_order("KRW-STPT", 20000)
        else:
            STPT = get_balance("STPT")
            if STPT > 0.0001:
                upbit.sell_market_order("KRW-STPT", STPT)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ORBS", 0.51)
            price = get_current_price("KRW-ORBS")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    ORBS = get_balance("ORBS")
                    if ORBS < 0.0001:
                        upbit.buy_market_order("KRW-ORBS", 20000)
        else:
            ORBS = get_balance("ORBS")
            if ORBS > 0.0001:
                upbit.sell_market_order("KRW-ORBS", ORBS)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-VET", 0.51)
            price = get_current_price("KRW-VET")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    VET = get_balance("VET")
                    if VET < 0.0001:
                        upbit.buy_market_order("KRW-VET", 20000)
        else:
            VET = get_balance("VET")
            if VET > 0.0001:
                upbit.sell_market_order("KRW-VET", VET)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-CHZ", 0.51)
            price = get_current_price("KRW-CHZ")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    CHZ = get_balance("CHZ")
                    if CHZ < 0.0001:
                        upbit.buy_market_order("KRW-CHZ", 20000)
        else:
            CHZ = get_balance("CHZ")
            if CHZ > 0.0001:
                upbit.sell_market_order("KRW-CHZ", CHZ)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-STMX", 0.51)
            price = get_current_price("KRW-STMX")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    STMX = get_balance("STMX")
                    if STMX < 0.0001:
                        upbit.buy_market_order("KRW-STMX", 20000)
        else:
            STMX = get_balance("STMX")
            if STMX > 0.0001:
                upbit.sell_market_order("KRW-STMX", STMX)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-DKA", 0.51)
            price = get_current_price("KRW-DKA")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    DKA = get_balance("DKA")
                    if DKA < 0.0001:
                        upbit.buy_market_order("KRW-DKA", 20000)
        else:
            DKA = get_balance("DKA")
            if DKA > 0.0001:
                upbit.sell_market_order("KRW-DKA", DKA)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-HIVE", 0.51)
            price = get_current_price("KRW-HIVE")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    HIVE = get_balance("HIVE")
                    if HIVE < 0.0001:
                        upbit.buy_market_order("KRW-HIVE", 20000)
        else:
            HIVE = get_balance("HIVE")
            if HIVE > 0.0001:
                upbit.sell_market_order("KRW-HIVE", HIVE)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-KAVA", 0.51)
            price = get_current_price("KRW-KAVA")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    KAVA = get_balance("KAVA")
                    if KAVA < 0.0001:
                        upbit.buy_market_order("KRW-KAVA", 20000)
        else:
            KAVA = get_balance("KAVA")
            if KAVA > 0.0001:
                upbit.sell_market_order("KRW-KAVA", KAVA)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-AHT", 0.51)
            price = get_current_price("KRW-AHT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    AHT = get_balance("AHT")
                    if AHT < 0.0001:
                        upbit.buy_market_order("KRW-AHT", 20000)
        else:
            AHT = get_balance("AHT")
            if AHT > 0.0001:
                upbit.sell_market_order("KRW-AHT", AHT)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-LINK", 0.51)
            price = get_current_price("KRW-LINK")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    LINK = get_balance("LINK")
                    if LINK < 0.0001:
                        upbit.buy_market_order("KRW-LINK", 20000)
        else:
            LINK = get_balance("LINK")
            if LINK > 0.0001:
                upbit.sell_market_order("KRW-LINK", LINK)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-XTZ", 0.51)
            price = get_current_price("KRW-XTZ")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    XTZ = get_balance("XTZ")
                    if XTZ < 0.0001:
                        upbit.buy_market_order("KRW-XTZ", 20000)
        else:
            XTZ = get_balance("XTZ")
            if XTZ > 0.0001:
                upbit.sell_market_order("KRW-XTZ", XTZ)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-BORA", 0.51)
            price = get_current_price("KRW-BORA")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    BORA = get_balance("BORA")
                    if BORA < 0.0001:
                        upbit.buy_market_order("KRW-BORA", 20000)
        else:
            BORA = get_balance("BORA")
            if BORA > 0.0001:
                upbit.sell_market_order("KRW-BORA", BORA)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-JST", 0.51)
            price = get_current_price("KRW-JST")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    JST = get_balance("JST")
                    if JST < 0.0001:
                        upbit.buy_market_order("KRW-JST", 20000)
        else:
            JST = get_balance("JST")
            if JST > 0.0001:
                upbit.sell_market_order("KRW-JST", JST)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-CRO", 0.51)
            price = get_current_price("KRW-CRO")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    CRO = get_balance("CRO")
                    if CRO < 0.0001:
                        upbit.buy_market_order("KRW-CRO", 20000)
        else:
            CRO = get_balance("CRO")
            if CRO > 0.0001:
                upbit.sell_market_order("KRW-CRO", CRO)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-TON", 0.51)
            price = get_current_price("KRW-TON")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    TON = get_balance("TON")
                    if TON < 0.0001:
                        upbit.buy_market_order("KRW-TON", 20000)
        else:
            TON = get_balance("TON")
            if TON > 0.0001:
                upbit.sell_market_order("KRW-TON", TON)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-SXP", 0.51)
            price = get_current_price("KRW-SXP")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SXP = get_balance("SXP")
                    if SXP < 0.0001:
                        upbit.buy_market_order("KRW-SXP", 20000)
        else:
            SXP = get_balance("SXP")
            if SXP > 0.0001:
                upbit.sell_market_order("KRW-SXP", SXP)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-HUNT", 0.51)
            price = get_current_price("KRW-HUNT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    HUNT = get_balance("HUNT")
                    if HUNT < 0.0001:
                        upbit.buy_market_order("KRW-HUNT", 20000)
        else:
            HUNT = get_balance("HUNT")
            if HUNT > 0.0001:
                upbit.sell_market_order("KRW-HUNT", HUNT)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-PLA", 0.51)
            price = get_current_price("KRW-PLA")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    PLA = get_balance("PLA")
                    if PLA < 0.0001:
                        upbit.buy_market_order("KRW-PLA", 20000)
        else:
            PLA = get_balance("PLA")
            if PLA > 0.0001:
                upbit.sell_market_order("KRW-PLA", PLA)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-DOT", 0.51)
            price = get_current_price("KRW-DOT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    DOT = get_balance("DOT")
                    if DOT < 0.0001:
                        upbit.buy_market_order("KRW-DOT", 20000)
        else:
            DOT = get_balance("DOT")
            if DOT > 0.0001:
                upbit.sell_market_order("KRW-DOT", DOT)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-SRM", 0.51)
            price = get_current_price("KRW-SRM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SRM = get_balance("SRM")
                    if SRM < 0.0001:
                        upbit.buy_market_order("KRW-SRM", 20000)
        else:
            SRM = get_balance("SRM")
            if SRM > 0.0001:
                upbit.sell_market_order("KRW-SRM", SRM)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-MVL", 0.51)
            price = get_current_price("KRW-MVL")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MVL = get_balance("MVL")
                    if MVL < 0.0001:
                        upbit.buy_market_order("KRW-MVL", 20000)
        else:
            MVL = get_balance("MVL")
            if MVL > 0.0001:
                upbit.sell_market_order("KRW-MVL", MVL)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-STRAX", 0.51)
            price = get_current_price("KRW-STRAX")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    STRAX = get_balance("STRAX")
                    if STRAX < 0.0001:
                        upbit.buy_market_order("KRW-STRAX", 20000)
        else:
            STRAX = get_balance("STRAX")
            if STRAX > 0.0001:
                upbit.sell_market_order("KRW-STRAX", STRAX)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-AQT", 0.51)
            price = get_current_price("KRW-AQT")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    AQT = get_balance("AQT")
                    if AQT < 0.0001:
                        upbit.buy_market_order("KRW-AQT", 20000)
        else:
            AQT = get_balance("AQT")
            if AQT > 0.0001:
                upbit.sell_market_order("KRW-AQT", AQT)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-GLM", 0.51)
            price = get_current_price("KRW-GLM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    GLM = get_balance("GLM")
                    if GLM < 0.0001:
                        upbit.buy_market_order("KRW-GLM", 20000)
        else:
            GLM = get_balance("GLM")
            if GLM > 0.0001:
                upbit.sell_market_order("KRW-GLM", GLM)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-SSX", 0.51)
            price = get_current_price("KRW-SSX")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SSX = get_balance("SSX")
                    if SSX < 0.0001:
                        upbit.buy_market_order("KRW-SSX", 20000)
        else:
            SSX = get_balance("SSX")
            if SSX > 0.0001:
                upbit.sell_market_order("KRW-SSX", SSX)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-META", 0.51)
            price = get_current_price("KRW-META")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    META = get_balance("META")
                    if META < 0.0001:
                        upbit.buy_market_order("KRW-META", 20000)
        else:
            META = get_balance("META")
            if META > 0.0001:
                upbit.sell_market_order("KRW-META", META)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-FCT2", 0.51)
            price = get_current_price("KRW-FCT2")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    FCT2 = get_balance("FCT2")
                    if FCT2 < 0.0001:
                        upbit.buy_market_order("KRW-FCT2", 20000)
        else:
            FCT2 = get_balance("FCT2")
            if FCT2 > 0.0001:
                upbit.sell_market_order("KRW-FCT2", FCT2)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-CBK", 0.51)
            price = get_current_price("KRW-CBK")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    CBK = get_balance("CBK")
                    if CBK < 0.0001:
                        upbit.buy_market_order("KRW-CBK", 20000)
        else:
            CBK = get_balance("CBK")
            if CBK > 0.0001:
                upbit.sell_market_order("KRW-CBK", CBK)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-SAND", 0.51)
            price = get_current_price("KRW-SAND")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SAND = get_balance("SAND")
                    if SAND < 0.0001:
                        upbit.buy_market_order("KRW-SAND", 20000)
        else:
            SAND = get_balance("SAND")
            if SAND > 0.0001:
                upbit.sell_market_order("KRW-SAND", SAND)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-HUM", 0.51)
            price = get_current_price("KRW-HUM")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    HUM = get_balance("HUM")
                    if HUM < 0.0001:
                        upbit.buy_market_order("KRW-HUM", 20000)
        else:
            HUM = get_balance("HUM")
            if HUM > 0.0001:
                upbit.sell_market_order("KRW-HUM", HUM)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-DOGE", 0.51)
            price = get_current_price("KRW-DOGE")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    DOGE = get_balance("DOGE")
                    if DOGE < 0.0001:
                        upbit.buy_market_order("KRW-DOGE", 20000)
        else:
            DOGE = get_balance("DOGE")
            if DOGE > 0.0001:
                upbit.sell_market_order("KRW-DOGE", DOGE)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-STRK", 0.51)
            price = get_current_price("KRW-STRK")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    STRK = get_balance("STRK")
                    if STRK < 0.0001:
                        upbit.buy_market_order("KRW-STRK", 20000)
        else:
            STRK = get_balance("STRK")
            if STRK > 0.0001:
                upbit.sell_market_order("KRW-STRK", STRK)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-PUNDIX", 0.51)
            price = get_current_price("KRW-PUNDIX")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    PUNDIX = get_balance("PUNDIX")
                    if PUNDIX < 0.0001:
                        upbit.buy_market_order("KRW-PUNDIX", 20000)
        else:
            PUNDIX = get_balance("PUNDIX")
            if PUNDIX > 0.0001:
                upbit.sell_market_order("KRW-PUNDIX", PUNDIX)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-FLOW", 0.51)
            price = get_current_price("KRW-FLOW")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    FLOW = get_balance("FLOW")
                    if FLOW < 0.0001:
                        upbit.buy_market_order("KRW-FLOW", 20000)
        else:
            FLOW = get_balance("FLOW")
            if FLOW > 0.0001:
                upbit.sell_market_order("KRW-FLOW", FLOW)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-DAWN", 0.51)
            price = get_current_price("KRW-DAWN")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    DAWN = get_balance("DAWN")
                    if DAWN < 0.0001:
                        upbit.buy_market_order("KRW-DAWN", 20000)
        else:
            DAWN = get_balance("DAWN")
            if DAWN > 0.0001:
                upbit.sell_market_order("KRW-DAWN", DAWN)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-AXS", 0.51)
            price = get_current_price("KRW-AXS")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    AXS = get_balance("AXS")
                    if AXS < 0.0001:
                        upbit.buy_market_order("KRW-AXS", 20000)
        else:
            AXS = get_balance("AXS")
            if AXS > 0.0001:
                upbit.sell_market_order("KRW-AXS", AXS)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-STX", 0.51)
            price = get_current_price("KRW-STX")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    STX = get_balance("STX")
                    if STX < 0.0001:
                        upbit.buy_market_order("KRW-STX", 20000)
        else:
            STX = get_balance("STX")
            if STX > 0.0001:
                upbit.sell_market_order("KRW-STX", STX)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-XEC", 0.51)
            price = get_current_price("KRW-XEC")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    XEC = get_balance("XEC")
                    if XEC < 0.0001:
                        upbit.buy_market_order("KRW-XEC", 20000)
        else:
            XEC = get_balance("XEC")
            if XEC > 0.0001:
                upbit.sell_market_order("KRW-XEC", XEC)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-SOL", 0.51)
            price = get_current_price("KRW-SOL")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    SOL = get_balance("SOL")
                    if SOL < 0.0001:
                        upbit.buy_market_order("KRW-SOL", 20000)
        else:
            SOL = get_balance("SOL")
            if SOL > 0.0001:
                upbit.sell_market_order("KRW-SOL", SOL)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-MATIC", 0.51)
            price = get_current_price("KRW-MATIC")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    MATIC = get_balance("MATIC")
                    if MATIC < 0.0001:
                        upbit.buy_market_order("KRW-MATIC", 20000)
        else:
            MATIC = get_balance("MATIC")
            if MATIC > 0.0001:
                upbit.sell_market_order("KRW-MATIC", MATIC)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-NU", 0.51)
            price = get_current_price("KRW-NU")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    NU = get_balance("NU")
                    if NU < 0.0001:
                        upbit.buy_market_order("KRW-NU", 20000)
        else:
            NU = get_balance("NU")
            if NU > 0.0001:
                upbit.sell_market_order("KRW-NU", NU)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-AAVE", 0.51)
            price = get_current_price("KRW-AAVE")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
                    AAVE = get_balance("AAVE")
                    if AAVE < 0.0001:
                        upbit.buy_market_order("KRW-AAVE", 20000)
        else:
            AAVE = get_balance("AAVE")
            if AAVE > 0.0001:
                upbit.sell_market_order("KRW-AAVE", AAVE)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target = get_target_price("KRW-ALGO", 0.51)
            price = get_current_price("KRW-ALGO")
            if target < price and op_mode is True:
                krw = get_balance("KRW")
                if krw > 20000:
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
