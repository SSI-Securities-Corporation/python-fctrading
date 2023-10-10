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
    
@dataclass
class AuditOrderBook:
    account: str

@dataclass
class CashInAdvanceAmount:
    account: str
    
@dataclass
class UnsettleSoldTransaction:
    account: str
    settleDate: str

@dataclass
class CashTransferHistory:
    account: str
    fromDate: str
    toDate: str
@dataclass
class CashInAdvanceHistory:
    account: str
    startDate: str
    endDate: str

@dataclass
class CashInAdvanceEstFee:
    account: str
    ciaAmount: float = 0
    receiveAmount: float = 0
    
@dataclass
class CashTransferVSD:
    account: str
    amount: int
    type: str
    remark: str
    code: str = ""
    
@dataclass
class CashTransfer:
    account: str
    beneficiaryAccount: str
    amount: int
    remark: str
    code: str = ""
    
@dataclass
class CashCIA:
    account: str
    ciaAmount: float = 0
    receiveAmount: float = 0
    code: str = ""
    
@dataclass
class OrsDividend:
    account: str
    
@dataclass
class OrsExercisableQuantity:
    account: str
    
@dataclass
class OrsHistory:
    account: str
    startDate: str
    endDate: str
    
@dataclass
class Ors:
    account: str
    instrumentID: str
    entitlementID: str 
    quantity: int
    amount: float
    code: str = ""   
    
@dataclass
class StockTransferable:
    account: str
    
@dataclass
class StockTransferHistory:
    account: str
    startDate: str
    endDate: str
    
@dataclass
class StockTransfer:
    account: str
    beneficiaryAccount: str
    exchangeID: str
    instrumentID: str
    quantity: int
    code: str = ""