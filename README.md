# Python package lbr-trex-client

[Cisco TRex traffic generator](https://trex-tgn.cisco.com/) is distributed as a
[single archive](https://trex-tgn.cisco.com/trex/doc/trex_manual.html#_obtaining_the_trex_package)
containing all external libraries/packages inside. Usage of TRex Client API is then
slightly complicated.

The purpose of this package is to provide client API in form of Python package
which can be easily installed via `pip`. As mentioned, this API is part of
TRex as a [tar.gz archive](https://trex-tgn.cisco.com/trex/doc/cp_docs/index.html#client-package).
It has been extracted and packaged as Python module. Official source code can be also found on
[TRex GitHub](https://github.com/cisco-system-traffic-generator/trex-core).
Current API version of this package is [v3.02](https://trex-tgn.cisco.com/trex/doc/release_notes.html#_release_3_02).
This package uses Python 3.8. Other Python versions are untested, but it is likely they will work as well.


## Hosting and contribution

Package `lbr-trex-client` is hosted publicly on Python Package Index (PyPI)
and internally in GitLab's Package Registry.

This project uses GitLab CI pipeline which is triggered
with every new commit. Pipeline creates .whl package from contents
inside [lbr_trex_client](./lbr_trex_client) folder.

If pipeline triggers on `master` branch, then package is also uploaded into
GitLab Package Registry. Version of package is defined by [git tags](https://pypi.org/project/setuptools-git-versioning/).
It should follow version of TRex.
Additionally, package is also uploaded on PyPI if it has a tag.


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
from lbr_trex_client.v3_02.interactive.trex.stl.api import *
from lbr_trex_client.v3_02.interactive.trex.astf.api import *
...
```

As you can see import above also contains Scapy. TRex is distributed as single archive
and as such contains all external libraries/package inside. This is same with it's API.
Explore [external_libs](./lbr_trex_client/v3_02/external_libs) to see all external packages.

**Note that** if your code already imported given package, then TRex **will replace** it with it's
own version of package. The [replacement method](./lbr_trex_client/v3_02/interactive/trex/__init__.py)
however is not perfect and you can still be left with some local and some TRex version of modules.
This is mostly evident with Scapy, especially with `from scapy.all import *` import.


## Differences compared to official TRex API

Package `lbr-trex-client` has few changes compared to official client package:
 - `stf/examples` directory is removed (examples are not required for API).
 - `interactive/profiles` directory is removed (contains more examples and tests).
 - `interactive/trex/examples` directory is removed (more examples).
 - `interactive/trex/.vscode/tags` file is removed (unimportant).
 - `interactive/trex/wireless` unit tests and Sphinx docs removed.
 - `__pycache__` and `*.pyc` files removed.
 - `sys.path` and `os.environ` are [modified](./lbr_trex_client/__init__.py) on module import for hassle-free usage.

#### Known issues

On import you can get warning messages from Scapy:

```
...lbr_trex_client/v3_02/external_libs/scapy-2.4.3/scapy/layers/ipsec.py:469: CryptographyDeprecationWarning: Blowfish has been deprecated
  cipher=algorithms.Blowfish,
...lbr_trex_client/v3_02/external_libs/scapy-2.4.3/scapy/layers/ipsec.py:483: CryptographyDeprecationWarning: CAST5 has been deprecated
  cipher=algorithms.CAST5,
```

This is related to the fact that TRex uses older Scapy version.

#### Links to official TRex documentation

Here are links to API reference of main components:

[Stateless - trex.stl.api](https://trex-tgn.cisco.com/trex/doc/cp_stl_docs/index.html#api-reference) - API for handling stateless TRex (connection, streams, Field Engine...).

[Advanced Stateful - trex.astf.api](https://trex-tgn.cisco.com/trex/doc/cp_astf_docs/index.html#api-reference) - API for handling advanced stateful TRex (connection, traffic profiles...).

[trex_client (CTRexClient)](https://trex-tgn.cisco.com/trex/doc/cp_docs/index.html#api-reference) - API for communication with TRex daemon (daemon is resposible for starting and terminating TRex instances(both stateless or adv. stateful instances)).

General TRex documentation can be found [here](https://trex-tgn.cisco.com/trex/doc/index.html).

#### Custom TRex API

You can also use `lbr-testsuite` package for custom TRex API that is built on top of this package.
For more information see [testsuite](https://gitlab.liberouter.org/testing/testsuite).


## Repository Maintainer

- Dominik Tran, tran@cesnet.cz

## License

Package is published under [Apache License Version 2.0](./LICENSE), which is [inherited](https://github.com/cisco-system-traffic-generator/trex-core/blob/master/LICENSE) from the TRex traffic generator
source. The TRex client API contains also modified version of Scapy library, which is published under
[GPLv2](./lbr_trex_client/v3_02/external_libs/scapy-2.4.3/LICENSE) license.
