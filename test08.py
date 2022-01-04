import time
import pyupbit
import datetime

access = "PLHmUf3gpoyKYzAqFzzxJ8vH042arYEQfcfdizx1"
secret = "mqsj8p9QYwd3A1Iich0KctXiz4ZJQrhDPxxA39DF"

#변동성 돌파 전략으로 매수 목표가 조회
def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    target_price = df.iloc[1]['open'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * 0.52
    return target_price

#시작가
def get_open_price(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=2)
    open_price = df.iloc[1]['open']
    return open_price

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

#이동평균선
def get_moving_average(window, ticker):
    try:
        df = pyupbit.get_ohlcv(ticker, interval="minute240")
        ma = df['close'].rolling(window=window).mean()
        return ma[-2]
    except Exception as e:
        time.sleep(1)
        
#최고가 조회
def get_high_price(ticker):
    df2 = pyupbit.get_ohlcv(ticker, interval="minute240", count=1)
    high_price = df2.iloc[0]['high']
    return high_price
    
# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
op_mode = False

ori_tickers = pyupbit.get_tickers(fiat="KRW")

# 자동매매 시작
while True:
    try:
        for ticker in ori_tickers:
            now = datetime.datetime.now()
            if now.hour == 9 and now.minute == 0 and 1 <=now.second <= 10 or \
                now.hour == 13 and now.minute == 0 and 1 <=now.second <= 10 or \
                now.hour == 17 and now.minute == 0 and 1 <=now.second <= 10 or \
                now.hour == 21 and now.minute == 0 and 1 <=now.second <= 10 or \
                now.hour == 1 and now.minute == 0 and 1 <=now.second <= 10 or \
                now.hour == 5 and now.minute == 0 and 1 <=now.second <= 10:
                op_mode = True
                target_p = get_target_price(ticker)
                start_time = get_start_time(ticker)
                time.sleep(10)             
            now = datetime.datetime.now()
            start_time = get_start_time(ticker)
            end_time = start_time + datetime.timedelta(seconds=14400)
            if start_time < now < end_time - datetime.timedelta(seconds=30):
                target_p = get_target_price(ticker)
                open_p = get_open_price(ticker)
                current_p = get_current_price(ticker)
                buy_p = get_avg_buy_price(ticker)
                bct_balances = upbit.get_balance(ticker)
                high_p = get_high_price(ticker)
                if target_p < current_p and op_mode is True:
                    krw = get_balance("KRW")
                    bct_balances = upbit.get_balance(ticker)
                    current_p = get_current_price(ticker)
                    ma5 = get_moving_average(5, ticker)
                    ma10 = get_moving_average(10, ticker)
                    if 15500 < krw and bct_balances < 0.0002 and ma5 > ma10:
                        upbit.buy_market_order(ticker, 15000)
                current_p = get_current_price("KRW-BTC")
                buy_p = get_avg_buy_price("KRW-BTC")
                BTC = get_balance("BTC")
                if buy_p * 1.025 < current_p:
                    if BTC > 0.0002:
                        upbit.sell_market_order("KRW-BTC", BTC)
                if current_p < buy_p * 0.98:
                    upbit.sell_market_order("KRW-BTC", BTC)
                current_p = get_current_price("KRW-ETH")
                buy_p = get_avg_buy_price("KRW-ETH")
                ETH = get_balance("ETH")
                if buy_p * 1.025 < current_p:
                    if ETH > 0.0002:
                        upbit.sell_market_order("KRW-ETH", ETH)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ETH", ETH)
                current_p = get_current_price("KRW-NEO")
                buy_p = get_avg_buy_price("KRW-NEO")
                NEO = get_balance("NEO")
                if buy_p * 1.025 < current_p:
                    if NEO > 0.0002:
                        upbit.sell_market_order("KRW-NEO", NEO)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-NEO", NEO)
                current_p = get_current_price("KRW-MTL")
                buy_p = get_avg_buy_price("KRW-MTL")
                MTL = get_balance("MTL")
                if buy_p * 1.025 < current_p:
                    if MTL > 0.0002:
                        upbit.sell_market_order("KRW-MTL", MTL)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-MTL", MTL)
                current_p = get_current_price("KRW-LTC")
                buy_p = get_avg_buy_price("KRW-LTC")
                LTC = get_balance("LTC")
                if buy_p * 1.025 < current_p:
                    if LTC > 0.0002:
                        upbit.sell_market_order("KRW-LTC", LTC)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-LTC", LTC)
                current_p = get_current_price("KRW-XRP")
                buy_p = get_avg_buy_price("KRW-XRP")
                XRP = get_balance("XRP")
                if buy_p * 1.025 < current_p:
                    if XRP > 0.0002:
                        upbit.sell_market_order("KRW-XRP", XRP)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-XRP", XRP)
                current_p = get_current_price("KRW-ETC")
                buy_p = get_avg_buy_price("KRW-ETC")
                ETC = get_balance("ETC")
                if buy_p * 1.025 < current_p:
                    if ETC > 0.0002:
                        upbit.sell_market_order("KRW-ETC", ETC)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ETC", ETC)
                current_p = get_current_price("KRW-OMG")
                buy_p = get_avg_buy_price("KRW-OMG")
                OMG = get_balance("OMG")
                if buy_p * 1.025 < current_p:
                    if OMG > 0.0002:
                        upbit.sell_market_order("KRW-OMG", OMG)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-OMG", OMG)
                current_p = get_current_price("KRW-SNT")
                buy_p = get_avg_buy_price("KRW-SNT")
                SNT = get_balance("SNT")
                if buy_p * 1.025 < current_p:
                    if SNT > 0.0002:
                        upbit.sell_market_order("KRW-SNT", SNT)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-SNT", SNT)
                current_p = get_current_price("KRW-WAVES")
                buy_p = get_avg_buy_price("KRW-WAVES")
                WAVES = get_balance("WAVES")
                if buy_p * 1.025 < current_p:
                    if WAVES > 0.0002:
                        upbit.sell_market_order("KRW-WAVES", WAVES)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-WAVES", WAVES)
                current_p = get_current_price("KRW-XEM")
                buy_p = get_avg_buy_price("KRW-XEM")
                XEM = get_balance("XEM")
                if buy_p * 1.025 < current_p:
                    if XEM > 0.0002:
                        upbit.sell_market_order("KRW-XEM", XEM)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-XEM", XEM)
                current_p = get_current_price("KRW-QTUM")
                buy_p = get_avg_buy_price("KRW-QTUM")
                QTUM = get_balance("QTUM")
                if buy_p * 1.025 < current_p:
                    if QTUM > 0.0002:
                        upbit.sell_market_order("KRW-QTUM", QTUM)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-QTUM", QTUM)
                current_p = get_current_price("KRW-LSK")
                buy_p = get_avg_buy_price("KRW-LSK")
                LSK = get_balance("LSK")
                if buy_p * 1.025 < current_p:
                    if LSK > 0.0002:
                        upbit.sell_market_order("KRW-LSK", LSK)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-LSK", LSK)
                current_p = get_current_price("KRW-STEEM")
                buy_p = get_avg_buy_price("KRW-STEEM")
                STEEM = get_balance("STEEM")
                if buy_p * 1.025 < current_p:
                    if STEEM > 0.0002:
                        upbit.sell_market_order("KRW-STEEM", STEEM)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-STEEM", STEEM)
                current_p = get_current_price("KRW-XLM")
                buy_p = get_avg_buy_price("KRW-XLM")
                XLM = get_balance("XLM")
                if buy_p * 1.025 < current_p:
                    if XLM > 0.0002:
                        upbit.sell_market_order("KRW-XLM", XLM)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-XLM", XLM)
                current_p = get_current_price("KRW-ARDR")
                buy_p = get_avg_buy_price("KRW-ARDR")
                ARDR = get_balance("ARDR")
                if buy_p * 1.025 < current_p:
                    if ARDR > 0.0002:
                        upbit.sell_market_order("KRW-ARDR", ARDR)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ARDR", ARDR)
                current_p = get_current_price("KRW-ARK")
                buy_p = get_avg_buy_price("KRW-ARK")
                ARK = get_balance("ARK")
                if buy_p * 1.025 < current_p:
                    if ARK > 0.0002:
                        upbit.sell_market_order("KRW-ARK", ARK)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ARK", ARK)
                current_p = get_current_price("KRW-STORJ")
                buy_p = get_avg_buy_price("KRW-STORJ")
                STORJ = get_balance("STORJ")
                if buy_p * 1.025 < current_p:
                    if STORJ > 0.0002:
                        upbit.sell_market_order("KRW-STORJ", STORJ)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-STORJ", STORJ)
                current_p = get_current_price("KRW-GRS")
                buy_p = get_avg_buy_price("KRW-GRS")
                GRS = get_balance("GRS")
                if buy_p * 1.025 < current_p:
                    if GRS > 0.0002:
                        upbit.sell_market_order("KRW-GRS", GRS)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-GRS", GRS)
                current_p = get_current_price("KRW-REP")
                buy_p = get_avg_buy_price("KRW-REP")
                REP = get_balance("REP")
                if buy_p * 1.025 < current_p:
                    if REP > 0.0002:
                        upbit.sell_market_order("KRW-REP", REP)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-REP", REP)
                current_p = get_current_price("KRW-ADA")
                buy_p = get_avg_buy_price("KRW-ADA")
                ADA = get_balance("ADA")
                if buy_p * 1.025 < current_p:
                    if ADA > 0.0002:
                        upbit.sell_market_order("KRW-ADA", ADA)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ADA", ADA)
                current_p = get_current_price("KRW-SBD")
                buy_p = get_avg_buy_price("KRW-SBD")
                SBD = get_balance("SBD")
                if buy_p * 1.025 < current_p:
                    if SBD > 0.0002:
                        upbit.sell_market_order("KRW-SBD", SBD)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-SBD", SBD)
                current_p = get_current_price("KRW-POWR")
                buy_p = get_avg_buy_price("KRW-POWR")
                POWR = get_balance("POWR")
                if buy_p * 1.025 < current_p:
                    if POWR > 0.0002:
                        upbit.sell_market_order("KRW-POWR", POWR)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-POWR", POWR)
                current_p = get_current_price("KRW-BTG")
                buy_p = get_avg_buy_price("KRW-BTG")
                BTG = get_balance("BTG")
                if buy_p * 1.025 < current_p:
                    if BTG > 0.0002:
                        upbit.sell_market_order("KRW-BTG", BTG)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-BTG", BTG)
                current_p = get_current_price("KRW-ICX")
                buy_p = get_avg_buy_price("KRW-ICX")
                ICX = get_balance("ICX")
                if buy_p * 1.025 < current_p:
                    if ICX > 0.0002:
                        upbit.sell_market_order("KRW-ICX", ICX)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ICX", ICX)
                current_p = get_current_price("KRW-EOS")
                buy_p = get_avg_buy_price("KRW-EOS")
                EOS = get_balance("EOS")
                if buy_p * 1.025 < current_p:
                    if EOS > 0.0002:
                        upbit.sell_market_order("KRW-EOS", EOS)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-EOS", EOS)
                current_p = get_current_price("KRW-TRX")
                buy_p = get_avg_buy_price("KRW-TRX")
                TRX = get_balance("TRX")
                if buy_p * 1.025 < current_p:
                    if TRX > 0.0002:
                        upbit.sell_market_order("KRW-TRX", TRX)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-TRX", TRX)
                current_p = get_current_price("KRW-SC")
                buy_p = get_avg_buy_price("KRW-SC")
                SC = get_balance("SC")
                if buy_p * 1.025 < current_p:
                    if SC > 0.0002:
                        upbit.sell_market_order("KRW-SC", SC)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-SC", SC)
                current_p = get_current_price("KRW-ONT")
                buy_p = get_avg_buy_price("KRW-ONT")
                ONT = get_balance("ONT")
                if buy_p * 1.025 < current_p:
                    if ONT > 0.0002:
                        upbit.sell_market_order("KRW-ONT", ONT)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ONT", ONT)
                current_p = get_current_price("KRW-ZIL")
                buy_p = get_avg_buy_price("KRW-ZIL")
                ZIL = get_balance("ZIL")
                if buy_p * 1.025 < current_p:
                    if ZIL > 0.0002:
                        upbit.sell_market_order("KRW-ZIL", ZIL)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ZIL", ZIL)
                current_p = get_current_price("KRW-POLY")
                buy_p = get_avg_buy_price("KRW-POLY")
                POLY = get_balance("POLY")
                if buy_p * 1.025 < current_p:
                    if POLY > 0.0002:
                        upbit.sell_market_order("KRW-POLY", POLY)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-POLY", POLY)
                current_p = get_current_price("KRW-ZRX")
                buy_p = get_avg_buy_price("KRW-ZRX")
                ZRX = get_balance("ZRX")
                if buy_p * 1.025 < current_p:
                    if ZRX > 0.0002:
                        upbit.sell_market_order("KRW-ZRX", ZRX)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ZRX", ZRX)
                current_p = get_current_price("KRW-LOOM")
                buy_p = get_avg_buy_price("KRW-LOOM")
                LOOM = get_balance("LOOM")
                if buy_p * 1.025 < current_p:
                    if LOOM > 0.0002:
                        upbit.sell_market_order("KRW-LOOM", LOOM)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-LOOM", LOOM)
                current_p = get_current_price("KRW-BCH")
                buy_p = get_avg_buy_price("KRW-BCH")
                BCH = get_balance("BCH")
                if buy_p * 1.025 < current_p:
                    if BCH > 0.0002:
                        upbit.sell_market_order("KRW-BCH", BCH)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-BCH", BCH)
                current_p = get_current_price("KRW-BAT")
                buy_p = get_avg_buy_price("KRW-BAT")
                BAT = get_balance("BAT")
                if buy_p * 1.025 < current_p:
                    if BAT > 0.0002:
                        upbit.sell_market_order("KRW-BAT", BAT)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-BAT", BAT)
                current_p = get_current_price("KRW-IOST")
                buy_p = get_avg_buy_price("KRW-IOST")
                IOST = get_balance("IOST")
                if buy_p * 1.025 < current_p:
                    if IOST > 0.0002:
                        upbit.sell_market_order("KRW-IOST", IOST)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-IOST", IOST)
                current_p = get_current_price("KRW-RFR")
                buy_p = get_avg_buy_price("KRW-RFR")
                RFR = get_balance("RFR")
                if buy_p * 1.025 < current_p:
                    if RFR > 0.0002:
                        upbit.sell_market_order("KRW-RFR", RFR)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-RFR", RFR)
                current_p = get_current_price("KRW-CVC")
                buy_p = get_avg_buy_price("KRW-CVC")
                CVC = get_balance("CVC")
                if buy_p * 1.025 < current_p:
                    if CVC > 0.0002:
                        upbit.sell_market_order("KRW-CVC", CVC)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-CVC", CVC)
                current_p = get_current_price("KRW-IQ")
                buy_p = get_avg_buy_price("KRW-IQ")
                IQ = get_balance("IQ")
                if buy_p * 1.025 < current_p:
                    if IQ > 0.0002:
                        upbit.sell_market_order("KRW-IQ", IQ)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-IQ", IQ)
                current_p = get_current_price("KRW-IOTA")
                buy_p = get_avg_buy_price("KRW-IOTA")
                IOTA = get_balance("IOTA")
                if buy_p * 1.025 < current_p:
                    if IOTA > 0.0002:
                        upbit.sell_market_order("KRW-IOTA", IOTA)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-IOTA", IOTA)
                current_p = get_current_price("KRW-MFT")
                buy_p = get_avg_buy_price("KRW-MFT")
                MFT = get_balance("MFT")
                if buy_p * 1.025 < current_p:
                    if MFT > 0.0002:
                        upbit.sell_market_order("KRW-MFT", MFT)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-MFT", MFT)
                current_p = get_current_price("KRW-ONG")
                buy_p = get_avg_buy_price("KRW-ONG")
                ONG = get_balance("ONG")
                if buy_p * 1.025 < current_p:
                    if ONG > 0.0002:
                        upbit.sell_market_order("KRW-ONG", ONG)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ONG", ONG)
                current_p = get_current_price("KRW-GAS")
                buy_p = get_avg_buy_price("KRW-GAS")
                GAS = get_balance("GAS")
                if buy_p * 1.025 < current_p:
                    if GAS > 0.0002:
                        upbit.sell_market_order("KRW-GAS", GAS)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-GAS", GAS)
                current_p = get_current_price("KRW-UPP")
                buy_p = get_avg_buy_price("KRW-UPP")
                UPP = get_balance("UPP")
                if buy_p * 1.025 < current_p:
                    if UPP > 0.0002:
                        upbit.sell_market_order("KRW-UPP", UPP)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-UPP", UPP)
                current_p = get_current_price("KRW-ELF")
                buy_p = get_avg_buy_price("KRW-ELF")
                ELF = get_balance("ELF")
                if buy_p * 1.025 < current_p:
                    if ELF > 0.0002:
                        upbit.sell_market_order("KRW-ELF", ELF)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ELF", ELF)
                current_p = get_current_price("KRW-KNC")
                buy_p = get_avg_buy_price("KRW-KNC")
                KNC = get_balance("KNC")
                if buy_p * 1.025 < current_p:
                    if KNC > 0.0002:
                        upbit.sell_market_order("KRW-KNC", KNC)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-KNC", KNC)
                current_p = get_current_price("KRW-BSV")
                buy_p = get_avg_buy_price("KRW-BSV")
                BSV = get_balance("BSV")
                if buy_p * 1.025 < current_p:
                    if BSV > 0.0002:
                        upbit.sell_market_order("KRW-BSV", BSV)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-BSV", BSV)
                current_p = get_current_price("KRW-THETA")
                buy_p = get_avg_buy_price("KRW-THETA")
                THETA = get_balance("THETA")
                if buy_p * 1.025 < current_p:
                    if THETA > 0.0002:
                        upbit.sell_market_order("KRW-THETA", THETA)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-THETA", THETA)
                current_p = get_current_price("KRW-QKC")
                buy_p = get_avg_buy_price("KRW-QKC")
                QKC = get_balance("QKC")
                if buy_p * 1.025 < current_p:
                    if QKC > 0.0002:
                        upbit.sell_market_order("KRW-QKC", QKC)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-QKC", QKC)
                current_p = get_current_price("KRW-BTT")
                buy_p = get_avg_buy_price("KRW-BTT")
                BTT = get_balance("BTT")
                if buy_p * 1.025 < current_p:
                    if BTT > 0.0002:
                        upbit.sell_market_order("KRW-BTT", BTT)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-BTT", BTT)
                current_p = get_current_price("KRW-MOC")
                buy_p = get_avg_buy_price("KRW-MOC")
                MOC = get_balance("MOC")
                if buy_p * 1.025 < current_p:
                    if MOC > 0.0002:
                        upbit.sell_market_order("KRW-MOC", MOC)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-MOC", MOC)
                current_p = get_current_price("KRW-ENJ")
                buy_p = get_avg_buy_price("KRW-ENJ")
                ENJ = get_balance("ENJ")
                if buy_p * 1.025 < current_p:
                    if ENJ > 0.0002:
                        upbit.sell_market_order("KRW-ENJ", ENJ)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ENJ", ENJ)
                current_p = get_current_price("KRW-TFUEL")
                buy_p = get_avg_buy_price("KRW-TFUEL")
                TFUEL = get_balance("TFUEL")
                if buy_p * 1.025 < current_p:
                    if TFUEL > 0.0002:
                        upbit.sell_market_order("KRW-TFUEL", TFUEL)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-TFUEL", TFUEL)
                current_p = get_current_price("KRW-MANA")
                buy_p = get_avg_buy_price("KRW-MANA")
                MANA = get_balance("MANA")
                if buy_p * 1.025 < current_p:
                    if MANA > 0.0002:
                        upbit.sell_market_order("KRW-MANA", MANA)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-MANA", MANA)
                current_p = get_current_price("KRW-ANKR")
                buy_p = get_avg_buy_price("KRW-ANKR")
                ANKR = get_balance("ANKR")
                if buy_p * 1.025 < current_p:
                    if ANKR > 0.0002:
                        upbit.sell_market_order("KRW-ANKR", ANKR)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ANKR", ANKR)
                current_p = get_current_price("KRW-AERGO")
                buy_p = get_avg_buy_price("KRW-AERGO")
                AERGO = get_balance("AERGO")
                if buy_p * 1.025 < current_p:
                    if AERGO > 0.0002:
                        upbit.sell_market_order("KRW-AERGO", AERGO)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-AERGO", AERGO)
                current_p = get_current_price("KRW-ATOM")
                buy_p = get_avg_buy_price("KRW-ATOM")
                ATOM = get_balance("ATOM")
                if buy_p * 1.025 < current_p:
                    if ATOM > 0.0002:
                        upbit.sell_market_order("KRW-ATOM", ATOM)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ATOM", ATOM)
                current_p = get_current_price("KRW-TT")
                buy_p = get_avg_buy_price("KRW-TT")
                TT = get_balance("TT")
                if buy_p * 1.025 < current_p:
                    if TT > 0.0002:
                        upbit.sell_market_order("KRW-TT", TT)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-TT", TT)
                current_p = get_current_price("KRW-CRE")
                buy_p = get_avg_buy_price("KRW-CRE")
                CRE = get_balance("CRE")
                if buy_p * 1.025 < current_p:
                    if CRE > 0.0002:
                        upbit.sell_market_order("KRW-CRE", CRE)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-CRE", CRE)
                current_p = get_current_price("KRW-MBL")
                buy_p = get_avg_buy_price("KRW-MBL")
                MBL = get_balance("MBL")
                if buy_p * 1.025 < current_p:
                    if MBL > 0.0002:
                        upbit.sell_market_order("KRW-MBL", MBL)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-MBL", MBL)
                current_p = get_current_price("KRW-WAXP")
                buy_p = get_avg_buy_price("KRW-WAXP")
                WAXP = get_balance("WAXP")
                if buy_p * 1.025 < current_p:
                    if WAXP > 0.0002:
                        upbit.sell_market_order("KRW-WAXP", WAXP)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-WAXP", WAXP)
                current_p = get_current_price("KRW-HBAR")
                buy_p = get_avg_buy_price("KRW-HBAR")
                HBAR = get_balance("HBAR")
                if buy_p * 1.025 < current_p:
                    if HBAR > 0.0002:
                        upbit.sell_market_order("KRW-HBAR", HBAR)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-HBAR", HBAR)
                current_p = get_current_price("KRW-MED")
                buy_p = get_avg_buy_price("KRW-MED")
                MED = get_balance("MED")
                if buy_p * 1.025 < current_p:
                    if MED > 0.0002:
                        upbit.sell_market_order("KRW-MED", MED)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-MED", MED)
                current_p = get_current_price("KRW-MLK")
                buy_p = get_avg_buy_price("KRW-MLK")
                MLK = get_balance("MLK")
                if buy_p * 1.025 < current_p:
                    if MLK > 0.0002:
                        upbit.sell_market_order("KRW-MLK", MLK)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-MLK", MLK)
                current_p = get_current_price("KRW-STPT")
                buy_p = get_avg_buy_price("KRW-STPT")
                STPT = get_balance("STPT")
                if buy_p * 1.025 < current_p:
                    if STPT > 0.0002:
                        upbit.sell_market_order("KRW-STPT", STPT)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-STPT", STPT)
                current_p = get_current_price("KRW-ORBS")
                buy_p = get_avg_buy_price("KRW-ORBS")
                ORBS = get_balance("ORBS")
                if buy_p * 1.025 < current_p:
                    if ORBS > 0.0002:
                        upbit.sell_market_order("KRW-ORBS", ORBS)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ORBS", ORBS)
                current_p = get_current_price("KRW-CHZ")
                buy_p = get_avg_buy_price("KRW-CHZ")
                CHZ = get_balance("CHZ")
                if buy_p * 1.025 < current_p:
                    if CHZ > 0.0002:
                        upbit.sell_market_order("KRW-CHZ", CHZ)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-CHZ", CHZ)
                current_p = get_current_price("KRW-VET")
                buy_p = get_avg_buy_price("KRW-VET")
                VET = get_balance("VET")
                if buy_p * 1.025 < current_p:
                    if VET > 0.0002:
                        upbit.sell_market_order("KRW-VET", VET)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-VET", VET)
                current_p = get_current_price("KRW-STMX")
                buy_p = get_avg_buy_price("KRW-STMX")
                STMX = get_balance("STMX")
                if buy_p * 1.025 < current_p:
                    if STMX > 0.0002:
                        upbit.sell_market_order("KRW-STMX", STMX)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-STMX", STMX)
                current_p = get_current_price("KRW-DKA")
                buy_p = get_avg_buy_price("KRW-DKA")
                DKA = get_balance("DKA")
                if buy_p * 1.025 < current_p:
                    if DKA > 0.0002:
                        upbit.sell_market_order("KRW-DKA", DKA)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-DKA", DKA)
                current_p = get_current_price("KRW-HIVE")
                buy_p = get_avg_buy_price("KRW-HIVE")
                HIVE = get_balance("HIVE")
                if buy_p * 1.025 < current_p:
                    if HIVE > 0.0002:
                        upbit.sell_market_order("KRW-HIVE", HIVE)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-HIVE", HIVE)
                current_p = get_current_price("KRW-KAVA")
                buy_p = get_avg_buy_price("KRW-KAVA")
                KAVA = get_balance("KAVA")
                if buy_p * 1.025 < current_p:
                    if KAVA > 0.0002:
                        upbit.sell_market_order("KRW-KAVA", KAVA)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-KAVA", KAVA)
                current_p = get_current_price("KRW-AHT")
                buy_p = get_avg_buy_price("KRW-AHT")
                AHT = get_balance("AHT")
                if buy_p * 1.025 < current_p:
                    if AHT > 0.0002:
                        upbit.sell_market_order("KRW-AHT", AHT)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-AHT", AHT)
                current_p = get_current_price("KRW-LINK")
                buy_p = get_avg_buy_price("KRW-LINK")
                LINK = get_balance("LINK")
                if buy_p * 1.025 < current_p:
                    if LINK > 0.0002:
                        upbit.sell_market_order("KRW-LINK", LINK)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-LINK", LINK)
                current_p = get_current_price("KRW-XTZ")
                buy_p = get_avg_buy_price("KRW-XTZ")
                XTZ = get_balance("XTZ")
                if buy_p * 1.025 < current_p:
                    if XTZ > 0.0002:
                        upbit.sell_market_order("KRW-XTZ", XTZ)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-XTZ", XTZ)
                current_p = get_current_price("KRW-BORA")
                buy_p = get_avg_buy_price("KRW-BORA")
                BORA = get_balance("BORA")
                if buy_p * 1.025 < current_p:
                    if BORA > 0.0002:
                        upbit.sell_market_order("KRW-BORA", BORA)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-BORA", BORA)
                current_p = get_current_price("KRW-JST")
                buy_p = get_avg_buy_price("KRW-JST")
                JST = get_balance("JST")
                if buy_p * 1.025 < current_p:
                    if JST > 0.0002:
                        upbit.sell_market_order("KRW-JST", JST)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-JST", JST)
                current_p = get_current_price("KRW-CRO")
                buy_p = get_avg_buy_price("KRW-CRO")
                CRO = get_balance("CRO")
                if buy_p * 1.025 < current_p:
                    if CRO > 0.0002:
                        upbit.sell_market_order("KRW-CRO", CRO)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-CRO", CRO)
                current_p = get_current_price("KRW-TON")
                buy_p = get_avg_buy_price("KRW-TON")
                TON = get_balance("TON")
                if buy_p * 1.025 < current_p:
                    if TON > 0.0002:
                        upbit.sell_market_order("KRW-TON", TON)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-TON", TON)
                current_p = get_current_price("KRW-SXP")
                buy_p = get_avg_buy_price("KRW-SXP")
                SXP = get_balance("SXP")
                if buy_p * 1.025 < current_p:
                    if SXP > 0.0002:
                        upbit.sell_market_order("KRW-SXP", SXP)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-SXP", SXP)
                current_p = get_current_price("KRW-HUNT")
                buy_p = get_avg_buy_price("KRW-HUNT")
                HUNT = get_balance("HUNT")
                if buy_p * 1.025 < current_p:
                    if HUNT > 0.0002:
                        upbit.sell_market_order("KRW-HUNT", HUNT)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-HUNT", HUNT)
                current_p = get_current_price("KRW-PLA")
                buy_p = get_avg_buy_price("KRW-PLA")
                PLA = get_balance("PLA")
                if buy_p * 1.025 < current_p:
                    if PLA > 0.0002:
                        upbit.sell_market_order("KRW-PLA", PLA)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-PLA", PLA)
                current_p = get_current_price("KRW-DOT")
                buy_p = get_avg_buy_price("KRW-DOT")
                DOT = get_balance("DOT")
                if buy_p * 1.025 < current_p:
                    if DOT > 0.0002:
                        upbit.sell_market_order("KRW-DOT", DOT)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-DOT", DOT)
                current_p = get_current_price("KRW-SRM")
                buy_p = get_avg_buy_price("KRW-SRM")
                SRM = get_balance("SRM")
                if buy_p * 1.025 < current_p:
                    if SRM > 0.0002:
                        upbit.sell_market_order("KRW-SRM", SRM)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-SRM", SRM)
                current_p = get_current_price("KRW-MVL")
                buy_p = get_avg_buy_price("KRW-MVL")
                MVL = get_balance("MVL")
                if buy_p * 1.025 < current_p:
                    if MVL > 0.0002:
                        upbit.sell_market_order("KRW-MVL", MVL)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-MVL", MVL)
                current_p = get_current_price("KRW-STRAX")
                buy_p = get_avg_buy_price("KRW-STRAX")
                STRAX = get_balance("STRAX")
                if buy_p * 1.025 < current_p:
                    if STRAX > 0.0002:
                        upbit.sell_market_order("KRW-STRAX", STRAX)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-STRAX", STRAX)
                current_p = get_current_price("KRW-AQT")
                buy_p = get_avg_buy_price("KRW-AQT")
                AQT = get_balance("AQT")
                if buy_p * 1.025 < current_p:
                    if AQT > 0.0002:
                        upbit.sell_market_order("KRW-AQT", AQT)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-AQT", AQT)
                current_p = get_current_price("KRW-GLM")
                buy_p = get_avg_buy_price("KRW-GLM")
                GLM = get_balance("GLM")
                if buy_p * 1.025 < current_p:
                    if GLM > 0.0002:
                        upbit.sell_market_order("KRW-GLM", GLM)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-GLM", GLM)
                current_p = get_current_price("KRW-SSX")
                buy_p = get_avg_buy_price("KRW-SSX")
                SSX = get_balance("SSX")
                if buy_p * 1.025 < current_p:
                    if SSX > 0.0002:
                        upbit.sell_market_order("KRW-SSX", SSX)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-SSX", SSX)
                current_p = get_current_price("KRW-META")
                buy_p = get_avg_buy_price("KRW-META")
                META = get_balance("META")
                if buy_p * 1.025 < current_p:
                    if META > 0.0002:
                        upbit.sell_market_order("KRW-META", META)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-META", META)
                current_p = get_current_price("KRW-FCT2")
                buy_p = get_avg_buy_price("KRW-FCT2")
                FCT2 = get_balance("FCT2")
                if buy_p * 1.025 < current_p:
                    if FCT2 > 0.0002:
                        upbit.sell_market_order("KRW-FCT2", FCT2)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-FCT2", FCT2)
                current_p = get_current_price("KRW-CBK")
                buy_p = get_avg_buy_price("KRW-CBK")
                CBK = get_balance("CBK")
                if buy_p * 1.025 < current_p:
                    if CBK > 0.0002:
                        upbit.sell_market_order("KRW-CBK", CBK)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-CBK", CBK)
                current_p = get_current_price("KRW-SAND")
                buy_p = get_avg_buy_price("KRW-SAND")
                SAND = get_balance("SAND")
                if buy_p * 1.025 < current_p:
                    if SAND > 0.0002:
                        upbit.sell_market_order("KRW-SAND", SAND)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-SAND", SAND)
                current_p = get_current_price("KRW-HUM")
                buy_p = get_avg_buy_price("KRW-HUM")
                HUM = get_balance("HUM")
                if buy_p * 1.025 < current_p:
                    if HUM > 0.0002:
                        upbit.sell_market_order("KRW-HUM", HUM)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-HUM", HUM)
                current_p = get_current_price("KRW-DOGE")
                buy_p = get_avg_buy_price("KRW-DOGE")
                DOGE = get_balance("DOGE")
                if buy_p * 1.025 < current_p:
                    if DOGE > 0.0002:
                        upbit.sell_market_order("KRW-DOGE", DOGE)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-DOGE", DOGE)
                current_p = get_current_price("KRW-STRK")
                buy_p = get_avg_buy_price("KRW-STRK")
                STRK = get_balance("STRK")
                if buy_p * 1.025 < current_p:
                    if STRK > 0.0002:
                        upbit.sell_market_order("KRW-STRK", STRK)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-STRK", STRK)
                current_p = get_current_price("KRW-PUNDIX")
                buy_p = get_avg_buy_price("KRW-PUNDIX")
                PUNDIX = get_balance("PUNDIX")
                if buy_p * 1.025 < current_p:
                    if PUNDIX > 0.0002:
                        upbit.sell_market_order("KRW-PUNDIX", PUNDIX)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-PUNDIX", PUNDIX)
                current_p = get_current_price("KRW-FLOW")
                buy_p = get_avg_buy_price("KRW-FLOW")
                FLOW = get_balance("FLOW")
                if buy_p * 1.025 < current_p:
                    if FLOW > 0.0002:
                        upbit.sell_market_order("KRW-FLOW", FLOW)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-FLOW", FLOW)
                current_p = get_current_price("KRW-DAWN")
                buy_p = get_avg_buy_price("KRW-DAWN")
                DAWN = get_balance("DAWN")
                if buy_p * 1.025 < current_p:
                    if DAWN > 0.0002:
                        upbit.sell_market_order("KRW-DAWN", DAWN)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-DAWN", DAWN)
                current_p = get_current_price("KRW-AXS")
                buy_p = get_avg_buy_price("KRW-AXS")
                AXS = get_balance("AXS")
                if buy_p * 1.025 < current_p:
                    if AXS > 0.0002:
                        upbit.sell_market_order("KRW-AXS", AXS)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-AXS", AXS)
                current_p = get_current_price("KRW-STX")
                buy_p = get_avg_buy_price("KRW-STX")
                STX = get_balance("STX")
                if buy_p * 1.025 < current_p:
                    if STX > 0.0002:
                        upbit.sell_market_order("KRW-STX", STX)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-STX", STX)
                current_p = get_current_price("KRW-XEC")
                buy_p = get_avg_buy_price("KRW-XEC")
                XEC = get_balance("XEC")
                if buy_p * 1.025 < current_p:
                    if XEC > 0.0002:
                        upbit.sell_market_order("KRW-XEC", XEC)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-XEC", XEC)
                current_p = get_current_price("KRW-SOL")
                buy_p = get_avg_buy_price("KRW-SOL")
                SOL = get_balance("SOL")
                if buy_p * 1.025 < current_p:
                    if SOL > 0.0002:
                        upbit.sell_market_order("KRW-SOL", SOL)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-SOL", SOL)
                current_p = get_current_price("KRW-MATIC")
                buy_p = get_avg_buy_price("KRW-MATIC")
                MATIC = get_balance("MATIC")
                if buy_p * 1.025 < current_p:
                    if MATIC > 0.0002:
                        upbit.sell_market_order("KRW-MATIC", MATIC)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-MATIC", MATIC)
                current_p = get_current_price("KRW-NU")
                buy_p = get_avg_buy_price("KRW-NU")
                NU = get_balance("NU")
                if buy_p * 1.025 < current_p:
                    if NU > 0.0002:
                        upbit.sell_market_order("KRW-NU", NU)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-NU", NU)
                current_p = get_current_price("KRW-AAVE")
                buy_p = get_avg_buy_price("KRW-AAVE")
                AAVE = get_balance("AAVE")
                if buy_p * 1.025 < current_p:
                    if AAVE > 0.0002:
                        upbit.sell_market_order("KRW-AAVE", AAVE)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-AAVE", AAVE)
                current_p = get_current_price("KRW-ALGO")
                buy_p = get_avg_buy_price("KRW-ALGO")
                ALGO = get_balance("ALGO")
                if buy_p * 1.025 < current_p:
                    if ALGO > 0.0002:
                        upbit.sell_market_order("KRW-ALGO", ALGO)
                if buy_p * 0.98 > current_p:
                    upbit.sell_market_order("KRW-ALGO", ALGO)
            else:
                bct_balances = upbit.get_balance(ticker)
                if bct_balances > 0.0002:
                    upbit.sell_market_order(ticker, bct_balances)
                    time.sleep(1)  
    except Exception as e:
        print(e)
        time.sleep(1)
