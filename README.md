# Python package lbr_trex_client

The purpose of this package is to provide official Cisco
`TRex traffic generator` client API. This API is part of
full TRex package as a [tar.gz archive](https://trex-tgn.cisco.com/trex/doc/cp_docs/index.html#client-package).
It has been extracted and packaged as Python module.
Current API version is [v3.02](https://trex-tgn.cisco.com/trex/doc/release_notes.html#_release_3_02).



## Hosting and contribution

Package `lbr_trex_client` is hosted in GitLab's Package Registry
under PyPI package manager. You can list all available versions
by following this [link](https://gitlab.liberouter.org/testing/trex-client/-/packages).

This project uses GitLab CI pipeline which is triggered
with every new commit. Pipeline creates .whl package from contents
inside [lbr_trex_client](./lbr_trex_client) folder.

If pipeline triggers on `master` branch, then package is also uploaded into
Package Registry. If version of package(defined in [setup.py](./setup.py)) already
exists in Package Registry, then package is rejected.
This means that if you make **changes**, then you also need to **increase version**.


## Installation

You can use following command for installation:

```
python3.6 -m pip install lbr-trex-client --extra-index-url https://trex_client_deploy_token:vyd-dNs7ZnqpUfkm4o-v@gitlab.liberouter.org/api/v4/projects/79/packages/pypi/simple
```


## Usage

#### Method 1
Use standard Python import way:

```
from lbr_trex_client.v3_02.interactive.trex.stl.api import *
from lbr_trex_client.v3_02.interactive.trex.astf.api import *
...
```
This has disadvantage of being relatively long. It also includes version
API, which will change with future TRex updates.

#### Method 2
Import **paths**. This will set system paths that allow for shorter imports.
```
import lbr_trex_client.paths

from trex.stl.api import *
from trex.astf.api import *
from trex_client import CTRexClient
from trex_exceptions import TRexInUseError
from scapy.layers.dns import *
...
```
As you can see import above also contains Scapy. TRex is distributed as single archive
and as such contains all external libraries/package inside. This is same with it's API.
Explore [external_libs](./lbr_trex_client/v3_02/external_libs) to see all external packages.

Here are links to API reference of main components:

[Stateless - trex.stl.api](https://trex-tgn.cisco.com/trex/doc/cp_stl_docs/index.html#api-reference) - API for handling stateless TRex (connection, streams, Field Engine...).

[Advanced Stateful - trex.astf.api](https://trex-tgn.cisco.com/trex/doc/cp_astf_docs/index.html#api-reference) - API for handling advanced stateful TRex (connection, traffic profiles...).

[trex_client (CTRexClient)](https://trex-tgn.cisco.com/trex/doc/cp_docs/index.html#api-reference) - API for communication with TRex daemon (daemon is resposible for starting and terminating TRex instances(both stateless or stateful instances)).

General TRex documentation can be found [here](https://trex-tgn.cisco.com/trex/doc/index.html).

## TRex_tools

You can also use `lbr_testsuite` package for additional TRex tools that are build on top of this API.
TRex tools simplify certain operations. For more information see [testsuite](https://gitlab.liberouter.org/tmc/testsuite).

 ## Repository Maintainer

- Dominik Tran, tran@cesnet.cz
