import dataclasses
from .models import fcmodel_requests
from .models import fcmodel_responses
from .models import AccessTokenModel
from .core.core_crypto import core_crypto
from .constant import api
from dataclasses import asdict
import requests
import json
from datetime import date, datetime, timedelta


class FCTradingClient(object):

    def __init__(self, url: str, consumer_id:str, consumer_secret: str, private_key: str, twoFAType: int):
        self.url = url
        self.consumer_id = consumer_id
        self.consumer_secret = consumer_secret
        self.rsa_key = core_crypto.getRSAKey(private_key)
        self._headers = {'Content-Type': 'application/json'}
        self._last_login: datetime = datetime.now()
        self._token_expire_at:  datetime = datetime.now()
        self._twoFAType: int = twoFAType
        self._write_access_token: AccessTokenModel = None
        self._read_access_token: AccessTokenModel = None
        self.get_access_token()

    def _fc_make_request_get(self, _api_url: str, _request_object: object):
        _headers = self._headers
        _headers["Authorization"] = "Bearer " + self.get_access_token()
        tapi_response = requests.get(self.url + _api_url , asdict(_request_object), 
            headers=_headers)

        return tapi_response.json()
        

    def _fc_make_request_post(self, _api_url: str, _request_object: object):
        payload = json.dumps(dataclasses.asdict(_request_object))
        sign_payload = core_crypto.sign(payload, self.rsa_key)
        _headers = self._headers
        _headers["Authorization"] = "Bearer " + self.get_writer_access_token()
        _headers["X-Signature"] = sign_payload
        tapi_response = requests.post(self.url + _api_url , data=payload, 
            headers=_headers)
        return tapi_response.json()

    def get_access_token(self):
        if self._read_access_token == None or self._read_access_token.is_expired():
            req = fcmodel_requests.AccessToken(self.consumer_id, self.consumer_secret, self._twoFAType, '1', False)
            payload = json.dumps(dataclasses.asdict( req))
            res = requests.post(self.url + api.FC_GET_ACCESS_TOKEN , payload, headers=self._headers)
            res_obj = fcmodel_responses.Response(**(res.json()))
            if res_obj.status == 200:
                model = fcmodel_responses.AccessToken(**res_obj.data)
                self._read_access_token = AccessTokenModel(model)
                return self._read_access_token.get_access_token()
            else:
                raise NameError(res_obj.message)
        else:
            return self._read_access_token.get_access_token()

    def get_writer_access_token(self):
        assert self._write_access_token != None, 'Please verify code to get writer token before get it!'
        assert self._write_access_token.is_expired() == False, 'Writer token is expired! Please verify code again to get new one!'
        return self._write_access_token.get_access_token()
    
    def verifyCode(self, code: str):
        req = fcmodel_requests.AccessToken(self.consumer_id, self.consumer_secret, self._twoFAType, code, True)
        payload = json.dumps(dataclasses.asdict( req))
        res = requests.post(self.url + api.FC_GET_ACCESS_TOKEN , payload, headers=self._headers)
        res_obj = fcmodel_responses.Response(**(res.json()))
        if res_obj.status == 200:
            model = fcmodel_responses.AccessToken(**res_obj.data)
            self._write_access_token = AccessTokenModel(model)
            return self._write_access_token.get_access_token()
        else:
            raise NameError(res_obj.message)
    
    def new_order(self, model: fcmodel_requests.NewOrder):
        return self._fc_make_request_post(api.FC_NEW_ORDER, model)

    def modify_order(self, model: fcmodel_requests.ModifyOrder):
        return self._fc_make_request_post(api.FC_MODIFY_ORDER, model)

    def cancle_order(self, model: fcmodel_requests.CancelOrder):
        return self._fc_make_request_post(api.FC_CANCEL_ORDER, model)

    def get_stock_account_balance(self, model: fcmodel_requests.StockAccountBalance):
        return self._fc_make_request_get(api.FC_GET_ACCOUNT_BALANCE, model)

    def get_derivative_account_balance(self, model: fcmodel_requests.DerivativeAccountBalance):
        return self._fc_make_request_get(api.FC_GET_DER_ACCOUNT_BALANCE, model)

    def get_pp_mmr_account(self, model: fcmodel_requests.PPMMRAccount):
        return self._fc_make_request_get(api.FC_GET_PP_MMR_ACCOUNT, model)

    def get_stock_position(self, model: fcmodel_requests.StockPosition):
        return self._fc_make_request_get(api.FC_GET_STOCK_POSITION, model)

    def get_derivative_position(self, model: fcmodel_requests.DerivativePosition):
        return self._fc_make_request_get(api.FC_GET_DER_POSITION, model)

    def get_max_buy_qty(self, model: fcmodel_requests.MaxBuyQty):
        return self._fc_make_request_get(api.FC_GET_MAX_BUY_QUANTITY, model)

    def get_max_sell_qty(self, model: fcmodel_requests.MaxSellQty):
        return self._fc_make_request_get(api.FC_GET_MAX_SELL_QUANTITY, model)

    def get_order_history(self, model: fcmodel_requests.OrderHistory):
        return self._fc_make_request_get(api.FC_GET_ORDER_HISTORY, model)

    def get_otp(self, model: fcmodel_requests.GetOTP):
        payload = json.dumps(dataclasses.asdict(model))
        _headers = self._headers
        tapi_response = requests.post(self.url + api.FC_GET_OTP , data=payload, 
            headers=_headers)
        return tapi_response.json()
    
    def der_new_order(self, model: fcmodel_requests.NewOrder):
        return self._fc_make_request_post(api.FC_DER_NEW_ORDER, model)

    def der_modify_order(self, model: fcmodel_requests.ModifyOrder):
        return self._fc_make_request_post(api.FC_DER_MODIFY_ORDER, model)

    def der_cancle_order(self, model: fcmodel_requests.CancelOrder):
        return self._fc_make_request_post(api.FC_DER_CANCEL_ORDER, model)
    
    def get_order_book(self, model: fcmodel_requests.OrderBook):
        return self._fc_make_request_get(api.FC_GET_ORDER_BOOK, model)