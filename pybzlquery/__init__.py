from __future__ import annotations

from subprocess import check_output

from .analysis_v2_pb2 import *
from .build_pb2 import *

def query(ws: str, target: str) -> QueryResult:
    output = check_output(['bazel', 'query', '--output', 'proto', target], cwd=ws)
    r = QueryResult()
    r.ParseFromString(output)
    return r

def cquery(ws: str, target: str) -> CqueryResult:
    output = check_output(['bazel', 'cquery', '--output', 'proto', target], cwd=ws)
    r = CqueryResult()
    r.ParseFromString(output)
    return r

def aquery(ws: str, target: str) -> ActionGraphContainer:
    output = check_output(['bazel', 'aquery', '--output', 'proto', target], cwd=ws)
    r = ActionGraphContainer()
    r.ParseFromString(output)
    return r
