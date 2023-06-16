__version__ = '2.1.0'

# This is a property
# of SSI company
import gevent
from gevent import monkey

monkey.patch_all()
import warnings

warnings.filterwarnings("ignore")
import sys
from .fc_client import FCTradingClient
from .fc_stream import FCTradingStream
