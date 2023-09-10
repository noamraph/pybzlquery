# pybzlquery: Parse Bazel Protobuf query outputs in Python

# Building the modules

To build `pybzlquery/analysis_v2_pb2.py` and `pybzlquery/build_pb2.py`, install `nix`, and run:

```
cd gen-mods
nix build
cp --no-preserve=mode result/* ../pybzlquery/
```
