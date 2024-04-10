# Python package lbr-trex-client

[Cisco TRex traffic generator](https://trex-tgn.cisco.com/) is distributed as a
single [.tar.gz archive](https://trex-tgn.cisco.com/trex/doc/trex_manual.html#_obtaining_the_trex_package)
and contains all external libraries/packages for running TRex.
This means trying to use or import TRex Client Python API in your code is relatively complicated, especially
if your code runs on different machine than TRex itself.

The purpose of this package is to provide client API in form of Python package
which can be easily installed via `pip`. This API is part of
TRex as another [tar.gz archive](https://trex-tgn.cisco.com/trex/doc/cp_docs/index.html#client-package).
It was repackaged as standard Python module.
Versions of this package follow TRex [version scheme](https://trex-tgn.cisco.com/trex/doc/release_notes.html)
(also see [special versions](#special-versions)).
Although module was tested only on Python 3.8, it is likely that newer Python versions will work as well.
Official source code can be also found on [TRex GitHub](https://github.com/cisco-system-traffic-generator/trex-core).

## Installation

You can use following command for installation:

```
python3.8 -m pip install lbr-trex-client
```

## Usage

Importing `lbr_trex_client` automatically sets paths and environment variables
for hassle-free usage of TRex Client API. Imports used in, for example,
[TRex Cookbook](https://github.com/cisco-system-traffic-generator/trex-core/blob/master/doc/trex_cookbook.asciidoc)
will then work as well.

```
import lbr_trex_client

from trex.stl.api import *
from trex.astf.api import *
from trex_stl_lib.api import *
from trex_client import CTRexClient
from trex_exceptions import TRexInUseError
from scapy.layers.dns import *
...
```

Alternatively you can use

```
from lbr_trex_client.interactive.trex.stl.api import *
from lbr_trex_client.interactive.trex.astf.api import *
...
```

You can notice that imports above also contain [Scapy](https://scrapy.org/).
As mentioned, TRex archive contains all dependencies, including modified Scapy.
Explore [external_libs](./lbr_trex_client/external_libs) to see all external packages.

**Note that** if your code already imported given package, then TRex **will replace** it with it's
own version of package. The [replacement method](./lbr_trex_client/interactive/trex/__init__.py)
however is not perfect and you can still be left with some local and some TRex version of modules.
This is mostly evident with Scapy, especially with `from scapy.all import *` import.
It can then lead to strange errors.

## Differences compared to official TRex API

Package `lbr-trex-client` has few changes compared to official client package:
 - `stf/examples` directory is removed (examples are not required for API).
 - `interactive/profiles` directory is removed (contains more examples and tests).
 - `interactive/trex/examples` directory is removed (more examples).
 - `interactive/trex/.vscode/tags` file is removed (unimportant).
 - `interactive/trex/wireless` unit tests, examples and Sphinx docs removed.
 - `__pycache__` and `*.pyc` files removed.
 - `sys.path` and `os.environ` are [modified](./lbr_trex_client/__init__.py) on module import for hassle-free usage.

#### Special versions

Some versions might have `.dev311` suffix. These versions are used in our Python3.11 environment.
There are some breaking changes when moving from Python3.8 to Python3.11. Since we want to keep
official version, we release our Python3.11 version with this special suffix.

#### Known issues

On import you can get warning messages from Scapy:

```
...lbr_trex_client/external_libs/scapy-2.4.3/scapy/layers/ipsec.py:469: CryptographyDeprecationWarning: Blowfish has been deprecated
  cipher=algorithms.Blowfish,
...lbr_trex_client/external_libs/scapy-2.4.3/scapy/layers/ipsec.py:483: CryptographyDeprecationWarning: CAST5 has been deprecated
  cipher=algorithms.CAST5,
```

This is related to the fact that TRex uses older Scapy version.

#### Links to official TRex documentation

Here are links to API reference of main components:

 - [Stateless\[trex.stl.api\]](https://trex-tgn.cisco.com/trex/doc/cp_stl_docs/index.html#api-reference) - API for stateless mode.
 - [Advanced Stateful\[trex.astf.api\]](https://trex-tgn.cisco.com/trex/doc/cp_astf_docs/index.html#api-reference) - API for advanced stateful mode.
 - [trex_client\[CTRexClient\]](https://trex-tgn.cisco.com/trex/doc/cp_docs/index.html#api-reference) - API for communication with TRex daemon.

General TRex documentation can be found [here](https://trex-tgn.cisco.com/trex/doc/index.html).

#### Custom TRex API

You can also use `lbr-testsuite` package for custom TRex API that is built on top of this package.
For more information see [testsuite](https://pypi.org/project/lbr-testsuite/).

## Hosting and contribution

Package `lbr-trex-client` is hosted publicly on Python Package Index (PyPI)
and internally in GitLab's Package Registry.

This project uses GitLab CI pipeline which is triggered
with every new commit. Pipeline creates .whl package from contents
inside [lbr_trex_client](./lbr_trex_client) folder.

If pipeline triggers on `master` branch, then package is also uploaded into
GitLab Package Registry. Version of package is defined by [git tags](https://pypi.org/project/setuptools-git-versioning/).
Additionally, package is also uploaded on PyPI if it has a tag.

## Repository Maintainer

- Dominik Tran, tran@cesnet.cz

## License

Package is published under [Apache License Version 2.0](./LICENSE), which is [inherited](https://github.com/cisco-system-traffic-generator/trex-core/blob/master/LICENSE) from the TRex traffic generator
source. The TRex client API contains also modified version of Scapy library, which is published under
[GPLv2](./lbr_trex_client/external_libs/scapy-2.4.3/LICENSE) license.
