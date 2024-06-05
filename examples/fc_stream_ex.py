from ssi_fctrading import FCTradingStream, fc_stream
from ssi_fctrading import FCTradingClient
from urllib.parse import urlparse, urlunparse, urlencode, quote

import urllib3
from . import fc_config


def on_message(tapi_message):
    print("fc_received: " + tapi_message)


def on_error(tapi_error):
    print("fc_error: " + tapi_error)

def on_open():
    print('Connected to ' + fc_config.StreamURL)

def tapi_data_streaming(on_message, on_error):
    client = FCTradingClient(fc_config.Url, fc_config.ConsumerID,
                             fc_config.ConsumerSecret, fc_config.PrivateKey, fc_config.TwoFAType)
    print("access_token: " + client.get_access_token())
    stream_client = FCTradingStream(client, fc_config.StreamURL, on_message, on_error, fc_config.NotifyId, on_open=on_open)
    stream_client.start()
    message = None
    while message != "exit()":
        message = input(">> ")


# main function
if __name__ == '__main__':
    tapi_data_streaming(on_message, on_error)
