import os
import sys

# Set TRex paths
# TRex modules then can be imported like this:
# import lbr_trex_client.paths
# from trex.stl.api import *
# from trex_exceptions import TRexInUseError
# from scapy.layers.dns import *
# ...
# Without it, you will need to use long paths like
# from lbr_trex_client.v3_02.interactive.trex.stl.api import *
sys.path.append(os.path.join(os.path.dirname(__file__), "../v3_02/interactive"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../v3_02/stf/trex_stf_lib"))
