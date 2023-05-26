from dataclasses import dataclass
@dataclass
class AccessToken:
    consumerID: str
    consumerSecret: str
    twoFactorType: int
    code: str
    isSave: bool = True
@dataclass
class GetOTP:
    consumerID: str
    consumerSecret: str
@dataclass
class NewOrder:
    account: str
    requestID: str
    instrumentID: str
    market: str
    buySell: str
    orderType: str
    price: float
    quantity: int
    stopOrder: bool = False
    stopPrice: float = 0.0
    stopType: str = ''
    stopStep: float = 0.0
    lossStep: float = 0.0
    profitStep: float = 0.0
    channelID: str = 'TA'
    code: str = ''
    deviceId: str = ''
    userAgent: str = ''

@dataclass
class CancelOrder:
    account: str
    requestID: str
    orderID: str
    marketID: str
    instrumentID: str
    buySell: str
    code: str = ''
    deviceId: str = ''
    userAgent: str = ''

@dataclass
class ModifyOrder:
    account: str
    requestID: str
    orderID: str
    marketID: str
    instrumentID: str
    price: float
    quantity: int
    buySell: str
    orderType: str
    code: str = ''
    deviceId: str = ''
    userAgent: str = ''

@dataclass
class StockAccountBalance:
    account: str

@dataclass
class DerivativeAccountBalance:
    account: str

@dataclass
class PPMMRAccount:
    account: str

@dataclass
class StockPosition:
    account: str

@dataclass
class DerivativePosition:
    account: str
    querySummary: bool = True

@dataclass
class MaxBuyQty:
    account: str
    instrumentID: str
    price: float

@dataclass
class MaxSellQty:
    account: str
    instrumentID : str
    price: str

@dataclass
class OrderHistory:
    account: str
    startDate: str
    endDate: str
    
@dataclass
class OrderBook:
    account: str
