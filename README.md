# pybzlquery: Parse Bazel Protobuf query outputs in Python

# Usage

```
!bazel aquery --output proto 'deps(TARGET)' > aquery.protobuf

from pathlib import Path
from pprint import pprint
from pybzlquery import parse_aquery

actions = parse_aquery(Path('aquery.protobuf').read_bytes())
pprint(actions[0])
```

# Building the modules

To build `pybzlquery/analysis_v2_pb2.py` and `pybzlquery/build_pb2.py`, install `nix`, and run:

```
cd gen-mods
nix build
cp --no-preserve=mode result/* ../pybzlquery/
```

# Links to adapted sources

https://github.com/bazelbuild/bazel/blob/master/src/main/protobuf/build.proto
https://github.com/bazelbuild/bazel/blob/master/src/main/protobuf/analysis_v2.proto
