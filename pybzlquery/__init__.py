from __future__ import annotations

from dataclasses import dataclass
from subprocess import check_output
from typing import Any
from enum import Enum

from .analysis_v2_pb2 import ActionGraphContainer, CqueryResult  # type: ignore
# from .build_pb2 import *

# def query(ws: str, target: str) -> QueryResult:
#     output = check_output(['bazel', 'query', '--output', 'proto', target], cwd=ws)
#     r = QueryResult()
#     r.ParseFromString(output)
#     return r

# def cquery(ws: str, target: str) -> CqueryResult:
#     output = check_output(['bazel', 'cquery', '--output', 'proto', target], cwd=ws)
#     r = CqueryResult()
#     r.ParseFromString(output)
#     return r

# def aquery(ws: str, target: str) -> ActionGraphContainer:
#     output = check_output(['bazel', 'aquery', '--output', 'proto', target], cwd=ws)
#     r = ActionGraphContainer()
#     r.ParseFromString(output)
#     return r


@dataclass
class Artifact:
    path: str
    is_tree_artifact: bool


@dataclass
class Target:
    label: str
    rule_class: str


@dataclass
class AspectDescriptor:
    name: str
    parameters: dict[str, str]


@dataclass
class Configuration:
    mnemonic: str
    platform_name: str
    checksum: str
    is_tool: bool


@dataclass
class DepSetOfFiles:
    transitive_dep_sets: list[DepSetOfFiles]
    direct_artifacts: list[Artifact]


@dataclass
class ParamFile:
    exec_path: str
    arguments: list[str]


@dataclass
class Action:
    target: Target
    aspect_descriptors: list[AspectDescriptor]
    action_key: str
    mnemonic: str
    configuration: Configuration
    arguments: list[str]
    environment_variables: dict[str, str]
    input_dep_sets: list[DepSetOfFiles]
    scheduling_dep_dep_sets: list[DepSetOfFiles] | None
    outputs: list[Artifact]
    discovers_inputs: bool
    execution_info: dict[str, str]
    param_files: list[ParamFile]
    primary_output: Artifact
    execution_platform: str
    template_content: str
    substitutions: dict[str, str]
    file_contents: str
    unresolved_symlink_target: str
    is_executable: bool


class Discriminator(Enum):
    RULE = 1
    SOURCE_FILE = 2
    GENERATED_FILE = 3
    PACKAGE_GROUP = 4
    ENVIRONMENT_GROUP = 5



def get_path(path_fragment_id: int, path_fragments: dict[int, Any]) -> str:
    path_fragment = path_fragments[path_fragment_id]
    if path_fragment.parent_id != 0:
        return get_path(path_fragment.parent_id, path_fragments) + '/' + path_fragment.label
    else:
        return path_fragment.label


def parse_aquery(raw: bytes) -> list[Action]:
    aquery = ActionGraphContainer()
    aquery.ParseFromString(raw)

    path_fragments = {x.id: x for x in aquery.path_fragments}
    artifacts = {x.id: Artifact(get_path(x.path_fragment_id, path_fragments), x.is_tree_artifact)
                 for x in aquery.artifacts}
    rule_classes = {x.id: x.name for x in aquery.rule_classes}
    targets = {x.id: Target(x.label, rule_classes[x.rule_class_id]) for x in aquery.targets}
    aspect_descriptors = {x.id: AspectDescriptor(x.name, {p.key: p.value for p in x.parameters})
                          for x in aquery.aspect_descriptors}
    configurations = {x.id: Configuration(x.mnemonic, x.platform_name, x.checksum, x.is_tool)
                      for x in aquery.configuration}
    dep_sets = {}
    for dep_set in aquery.dep_set_of_files:
        dep_sets[dep_set.id] = DepSetOfFiles([dep_sets[i] for i in dep_set.transitive_dep_set_ids], [
                                             artifacts[i] for i in dep_set.direct_artifact_ids])
    actions = [Action(
        target=targets[a.target_id],
        aspect_descriptors=[aspect_descriptors[i] for i in a.aspect_descriptor_ids],
        action_key=a.action_key,
        mnemonic=a.mnemonic,
        configuration=configurations[a.configuration_id],
        arguments=list(a.arguments),
        environment_variables={p.key: p.value for p in a.environment_variables},
        input_dep_sets=[dep_sets[i] for i in a.input_dep_set_ids],
        scheduling_dep_dep_sets=[dep_sets[i] for i in a.scheduling_dep_dep_set_ids] if hasattr(a, 'scheduling_dep_dep_set_ids') else None,
        outputs=[artifacts[i] for i in a.output_ids],
        discovers_inputs=a.discovers_inputs,
        execution_info={p.key: p.value for p in a.execution_info},
        param_files=[ParamFile(p.exec_path, p.arguments) for p in a.param_files],
        primary_output=artifacts[a.primary_output_id],
        execution_platform=a.execution_platform,
        template_content=a.template_content,
        substitutions={p.key: p.value for p in a.substitutions},
        file_contents=a.file_contents,
        unresolved_symlink_target=a.unresolved_symlink_target,
        is_executable=a.is_executable,
    ) for a in aquery.actions]

    return actions


def parse_cquery(raw: bytes) -> list[ConfiguredTarget]:
    pass