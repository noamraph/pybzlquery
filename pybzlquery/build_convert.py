from __future__ import annotations
from .build_proto import (
    Target, Rule, SourceFile, License, GeneratedFile, PackageGroup, EnvironmentGroup, Attribute, AttributeDiscriminator, Value,
    Label, Output, DistributionSet, Tristate, FilesetEntry, SymlinkBehavior, SelectorList, Selector, SelectorEntry,
    ConfiguredRuleInput,
)
from . import build_pb2

"""
Convert the ugly classes produced by build_pb2.py into the nice classes in build_proto.py
"""
from typing import Any

build_pb2: Any


def convert_license(src: Any) -> License:
    return License(src.license_type, src.exception)


def convert_fileset_entry(src: Any) -> FilesetEntry:
    return FilesetEntry(
        src.source, src.destination_directory, src.files_present, src.file, src.exclude,
        SymlinkBehavior(src.symlink_behavior) if src.symlink_behavior is not None else None,
        src.strip_prefix,
    )


def convert_selector_entry(src: Any, typ: AttributeDiscriminator) -> SelectorEntry:
    return SelectorEntry(src.label, src.is_default_value, convert_value(src, typ))


def convert_selector(src: Any, typ: AttributeDiscriminator) -> Selector:
    return Selector([convert_selector_entry(x, typ) for x in src.entries], src.has_default_value, src.no_match_error)


def convert_selector_list(src: Any) -> SelectorList:
    if src.type is None:
        raise NotImplementedError("I'm not sure what should be done if the type is None")
    typ = AttributeDiscriminator(src.type)
    return SelectorList(typ, [convert_selector(x, typ) for x in src.elements])


def convert_value(src: Any, typ: AttributeDiscriminator) -> Value:
    if typ == AttributeDiscriminator.INTEGER:
        return src.int_value
    elif typ == AttributeDiscriminator.STRING:
        return src.string_value
    elif typ == AttributeDiscriminator.LABEL:
        return Label(src.string_value)
    elif typ == AttributeDiscriminator.OUTPUT:
        return Output(src.string_value)
    elif typ == AttributeDiscriminator.STRING_LIST:
        return src.string_list_value
    elif typ == AttributeDiscriminator.LABEL_LIST:
        return [Label(x) for x in src.string_list_value]
    elif typ == AttributeDiscriminator.OUTPUT_LIST:
        return [Output(x) for x in src.string_list_value]
    elif typ == AttributeDiscriminator.DISTRIBUTION_SET:
        return DistributionSet(set(src.string_list_value))
    elif typ == AttributeDiscriminator.LICENSE:
        return convert_license(src.license)
    elif typ == AttributeDiscriminator.STRING_DICT:
        return {x.key: x.value for x in src.string_dict_value}
    elif typ == AttributeDiscriminator.FILESET_ENTRY_LIST:
        return [convert_fileset_entry(x) for x in src.fileset_list_value]
    elif typ == AttributeDiscriminator.LABEL_LIST_DICT:
        return {x.key: [Label(v) for v in x.value] for x in src.label_list_dict}
    elif typ == AttributeDiscriminator.STRING_LIST_DICT:
        return {x.key: x.value for x in src.string_list_dict}
    elif typ == AttributeDiscriminator.BOOLEAN:
        return src.boolean_value
    elif typ == AttributeDiscriminator.TRISTATE:
        return Tristate(src.tristate_value)
    elif typ == AttributeDiscriminator.INTEGER_LIST:
        return src.int_list_value
    elif typ == AttributeDiscriminator.UNKNOWN:
        raise NotImplementedError
    elif typ == AttributeDiscriminator.LABEL_DICT_UNARY:
        return {x.key: Label(x.value) for x in src.label_dict_unary}
    elif typ == AttributeDiscriminator.SELECTOR_LIST:
        return convert_selector_list(src.selector_list)
    elif typ == AttributeDiscriminator.LABEL_KEYED_STRING_DICT:
        return {Label(x.key): x.value for x in src.label_keyed_string_dict_value}
    elif typ == AttributeDiscriminator.DEPRECATED_STRING_DICT_UNARY:
        raise NotImplementedError
    else:
        assert False


def convert_attribute(src: Any) -> Attribute:
    typ = AttributeDiscriminator(src.type)
    value = convert_value(src, typ)
    return Attribute(
        src.name,
        src.explicitly_specified,
        src.nodep,
        src.source_aspect_name,
        typ,
        value,
    )


def convert_configured_rule_input(src: Any) -> ConfiguredRuleInput:
    return ConfiguredRuleInput(src.label, src.configuration_checksum, src.configuration_id)


def convert_rule(src: Any) -> Rule:
    return Rule(
        src.name,
        src.rule_class,
        src.location,
        [convert_attribute(attribute) for attribute in src.attribute],
        src.rule_input,
        [convert_configured_rule_input(x) for x in src.configured_rule_input],
        src.rule_outputs,
        src.default_setting,
        src.skylark_environment_hash_code,
        src.instantiation_stack,
        src.definition_stack,
    )


def convert_source_file(src: Any) -> SourceFile:
    return SourceFile(
        src.name,
        src.location,
        src.subinclude,
        src.package_group,
        src.visibility_label,
        src.feature,
        convert_license(src.license) if src.license is not None else None,
        src.package_contains_errors,
    )


def convert_generated_file(src: Any) -> GeneratedFile:
    raise NotImplementedError


def convert_package_group(src: Any) -> PackageGroup:
    raise NotImplementedError


def convert_environment_group(src: Any) -> EnvironmentGroup:
    raise NotImplementedError


def convert_target(src: Any) -> Target:
    D = build_pb2.Target.Discriminator
    if src.type == D.RULE:
        return convert_rule(src.rule)
    elif src.type == D.SOURCE_FILE:
        return convert_source_file(src.source_file)
    elif src.type == D.GENERATED_FILE:
        return convert_generated_file(src.generated_file)
    elif src.type == D.PACKAGE_GROUP:
        return convert_package_group(src.package_group)
    elif src.type == D.ENVIRONMENT_GROUP:
        return convert_environment_group(src.environment_group)
    else:
        assert False


def parse_query(raw: bytes) -> list[Target]:
    query = build_pb2.QueryResult()
    query.ParseFromString(raw)
    return [convert_target(target) for target in query.target]
