import configparser
import os
# READ CONFIG
config = configparser.SafeConfigParser(os.environ)
config.read(os.path.dirname(os.path.abspath(__file__)) + "/config.ini")

ConsumerID     = config.get("DEFAULT", "ConsumerID", fallback="")
ConsumerSecret = config.get("DEFAULT", "ConsumerSecret", fallback="")
PrivateKey     = config.get("DEFAULT", "PrivateKey", fallback="")
Url            = config.get("DEFAULT", "Url", fallback="https://fc-tradeapi.ssi.com.vn/") 
StreamURL      = config.get("DEFAULT", "StreamURL", fallback="https://fc-tradehub.ssi.com.vn/")
TwoFAType      = int(config.get("DEFAULT", "TwoFAType", fallback="0")) # 0-PIN, 1-OTP
NotifyId       = config.get("DEFAULT", "NotifyId", fallback="-1")
