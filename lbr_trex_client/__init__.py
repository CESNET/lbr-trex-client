import os
import sys

# Set TREX_EXT_LIBS which is used by some TRex modules
os.environ['TREX_EXT_LIBS'] = os.path.join(os.path.dirname(__file__), "v3_02/external_libs")
