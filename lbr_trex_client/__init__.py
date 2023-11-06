import os
import sys

# Set TREX_EXT_LIBS which is used by some TRex modules
os.environ["TREX_EXT_LIBS"] = os.path.join(
    os.path.dirname(__file__), "v3_02/external_libs"
)

# Provide TRex paths.
# Some TRex modules use imports like "from trex import ..."
# but "trex" module isn't found in standard sys.path.
# This leads to errors like
#
#  File "...interactive/trex/utils/parsing_opts.py", line 5, in <module>
#    from trex.emu.trex_emu_validator import Ipv4, Ipv6, Mac
#  ModuleNotFoundError: No module named 'trex'
#
# Adding correct paths to sys.path fixes the issue.
sys.path.append(os.path.join(os.path.dirname(__file__), "v3_02/interactive"))
sys.path.append(os.path.join(os.path.dirname(__file__), "v3_02/stf/trex_stf_lib"))
