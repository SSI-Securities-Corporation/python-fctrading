from ssi_fctrading import FCTradingClient
from ssi_fctrading.models import fcmodel_requests
from . import fc_config
from typing import Union

from fastapi import FastAPI
app = FastAPI()

import random
client = FCTradingClient(fc_config.Url, fc_config.ConsumerID,
	fc_config.ConsumerSecret, fc_config.PrivateKey, fc_config.TwoFAType)
print('Read token: ' + client.get_access_token())
@app.get("/getOtp")
async def fc_get_otp():
	"""Get OPT if you use SMS OTP or Email OTP

	Returns:
		string: response json string
	"""
	fc_req = fcmodel_requests.GetOTP(fc_config.ConsumerID, fc_config.ConsumerSecret)
	return client.get_otp(fc_req)

@app.get("/verifyCode")
async def fc_get_otp(code: str):
	"""Verify OTP or PIN (with TwoFAType in your config), if you use SMS OTP or Email OTP please get call getOtp to receive OTP before verify.
	 This function auto save OTP and accesstoken for New/Modify/Cancel order

	Returns:
		string: response json string
	"""
	return client.verifyCode(code)

@app.get("/newOrder")
async def fc_new_order(instrument_id: str, market_id: str, side: str, order_type: str
    , price: float, quantity: int, account: str, stop_order: bool = False, stop_price: float = 0, 
      stop_type: str = '', stop_step: float = 0, loss_step: float = 0, profit_step: float = 0, device_id: str = ''):
	
	"""Place new order

	Args:
	```	
	instrument_id (str): Mã chứng khoán
	market_id (str): Thị trường ('VN' hoặc 'VNFE')
	side (str): 'B' or 'S'
	order_type (str): Loại lệnh
	price (float): Giá. Với các lệnh điều kiện price=0
	quantity (int): Khối lượng
	account (str): Tài khoản
	stop_order (bool, optional): Lệnh điều kiện (chỉ áp dụng với phái sinh). Defaults to False.
	stop_price (float, optional): Giá trigger của lệnh điều kiện. Defaults to 0.
	stop_type (str, optional): Loại lệnh điều kiện. Defaults to ''.
	stop_step (float, optional): . Defaults to 0.
	loss_step (float, optional): . Defaults to 0.
	profit_step (float, optional): . Defaults to 0.
	device_id (str, optional): Định danh của thiết bị đặt lệnh
	```
	"""
	fc_req = fcmodel_requests.NewOrder(str(account).upper()
	, str(random.randint(0, 99999999))
	, str(instrument_id).upper(), str(market_id).upper(), str(side).upper(), str(order_type).upper()
	, float(price), int(quantity), bool(stop_order), float(stop_price), str(stop_type), float(stop_step), float(loss_step), float(profit_step),device_id= str(device_id))
	

	res = client.new_order(fc_req)
	return res

@app.get("/modifyOrder")
async def fc_modify_order(order_id: str, instrument_id: str, market_id: str, side: str, order_type: str
    , price: float, quantity: int, account: str):
	"""Modify order

	Args:
		order_id (str): OrderID to modify
		instrument_id (str): Mã chứng khoán
		market_id (str): Thị trường ('VN' for stock 'VNFE' for derviratives)
		side (str): 'B' or 'S'
		order_type (str): Loại lệnh
		price (float): Giá
		quantity (int): Khối lượng
		account (str): Tài khoản

	Returns:
		Str: json string response
	"""
	fc_rq = fcmodel_requests.ModifyOrder(str(account)
	, str(random.randint(0, 99999999)), str(order_id)
	, str(market_id), str(instrument_id), float(price), int(quantity), str(side), str(order_type))

	res = client.modify_order(fc_rq)
	return res

@app.get("/cancelOrder")
async def fc_cancel_order(order_id: str, instrument_id: str, market_id: str, side: str, account: str):
	
	fc_rq = fcmodel_requests.CancelOrder(str(account), str(random.randint(0, 99999999))
	, str(order_id), str(market_id), str(instrument_id), str(side))

	res = client.cancle_order(fc_rq)
	return res


@app.get("/stockAccountBalance")
async def fc_stock_account_balance(account: str):
	"""Get stock account balance

	Args:
		account (str): stock account id

	Returns:
		str: Json str
	"""	
	
	fc_rq = fcmodel_requests.StockAccountBalance(str(account))

	res = client.get_stock_account_balance(fc_rq)
	return res

@app.get("/derivativeAccountBalance")
async def fc_derivative_account_balance(account: str):
	"""Get derivative account balance

	Args:
		account (str): derivative account id

	Returns:
		str: Json str
	"""	
	
	fc_rq = fcmodel_requests.DerivativeAccountBalance(str(account))

	res = client.get_derivative_account_balance(fc_rq)
	return res

@app.get("/ppmmrAccount")
async def fc_pp_mmr_account(account: str):
	"""Get pp and mmr of account

	Args:
		account (str): stock account id

	Returns:
		str: Json str
	"""	
	
	fc_rq = fcmodel_requests.PPMMRAccount(str(account))

	res = client.get_pp_mmr_account(fc_rq)
	return res

@app.get("/stockPosition")
async def fc_stock_position(account: str):
	"""Get stock position of account

	Args:
		account (str): stock account id

	Returns:
		str: Json str
	"""	
	
	fc_rq = fcmodel_requests.StockPosition(str(account))

	res = client.get_stock_position(fc_rq)
	return res

@app.get("/derivativePosition")
async def fc_derivative_position(account: str):
	"""Get derivative position of account

	Args:
		account (str): derivative account id

	Returns:
		str: Json str
	"""	
	
	fc_rq = fcmodel_requests.DerivativePosition(str(account))

	res = client.get_derivative_position(fc_rq)
	return res

@app.get("/maxBuyQty")
async def fc_max_buy_qty(account: str, instrument_id: str, price: float):
	"""Get max buy qty

	Args:
		account (str): account id
		instrument_id (str): buy instrument
		price (float): buy price

	Returns:
		str: json string
	"""
	
	fc_rq = fcmodel_requests.MaxBuyQty(str(account), str(instrument_id), float(price))

	res = client.get_max_buy_qty(fc_rq)
	return res

@app.get("/maxSellQty")
async def fc_max_sell_qty(account: str, instrument_id: str, price: float =0):
	"""Get max sell qty

	Args:
		account (str): account id
		instrument_id (str): sell instrument
		price (float): sell price ( for dervatives exchange )

	Returns:
		str: json string
	"""
	
	fc_rq = fcmodel_requests.MaxSellQty(str(account), str(instrument_id), float(price))

	res = client.get_max_sell_qty(fc_rq)
	return res

@app.get("/orderHistory")
async def fc_order_history(account: str, start_date: str, end_date: str):
	"""Get order history

	Args:
		account (str): account id
		start_date (str): from date (format 'DD/MM/YYYY' ex: 21/05/2021)
		end_date (str): end date (format 'DD/MM/YYYY' ex: 21/05/2021)

	Returns:
		[str]: json string
	"""
	
	fc_rq = fcmodel_requests.OrderHistory(str(account), str(start_date), str(end_date))

	res = client.get_order_history(fc_rq)
	return res

