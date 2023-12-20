from __future__ import annotations

"""
Python-native classes for build.proto
"""

from dataclasses import dataclass
from enum import Enum
from typing import Union


@dataclass
class License:
    license_types: list[str]
    exceptions: list[str]


class SymlinkBehavior(Enum):
    """Indicates what to do when a source file is actually a symlink."""
    COPY = 1
    DEREFERENCE = 2


@dataclass
class FilesetEntry:
    """Represents an entry attribute of a Fileset rule in a build file."""

    # The label pointing to the source target where files are copied from.
    source: str

    # The relative path within the fileset rule where files will be mapped.
    destination_directory: str

    # Whether the files= attribute was specified. This is necessary because
    # no files= attribute and files=[] mean different things.
    files_present: bool | None

    # A list of file labels to include from the source directory.
    files: list[str]

    # If this is a fileset entry representing files within the rule
    # package, this lists relative paths to files that should be excluded from
    # the set.  This cannot contain values if 'file' also has values.
    excludes: list[str]

    # This field is optional because there will be some time when the new
    # PB is used by tools depending on blaze query, but the new blaze version
    # is not yet released.
    symlink_behavior: SymlinkBehavior | None

    # The prefix to strip from the path of the files in this FilesetEntry. Note
    # that no value and the empty string as the value mean different things here.
    strip_prefix: str | None


class AttributeDiscriminator(Enum):
    """Indicates the type of attribute."""
    INTEGER = 1              # int_value
    STRING = 2               # string_value
    LABEL = 3                # string_value
    OUTPUT = 4               # string_value
    STRING_LIST = 5          # string_list_value
    LABEL_LIST = 6           # string_list_value
    OUTPUT_LIST = 7          # string_list_value
    DISTRIBUTION_SET = 8     # string_list_value - order is unimportant
    LICENSE = 9              # license
    STRING_DICT = 10         # string_dict_value
    FILESET_ENTRY_LIST = 11  # fileset_list_value
    LABEL_LIST_DICT = 12     # label_list_dict_value
    STRING_LIST_DICT = 13    # string_list_dict_value
    BOOLEAN = 14             # int, bool and string value
    TRISTATE = 15            # tristate, int and string value
    INTEGER_LIST = 16        # int_list_value
    UNKNOWN = 18             # unknown type, use only for build extensions
    LABEL_DICT_UNARY = 19    # label_dict_unary_value
    SELECTOR_LIST = 20       # selector_list
    LABEL_KEYED_STRING_DICT = 21  # label_keyed_string_dict

    DEPRECATED_STRING_DICT_UNARY = 17


@dataclass(frozen=True)
class Label:
    value: str


@dataclass(frozen=True)
class Output:
    value: str


@dataclass
class DistributionSet:
    value: set[str]


class Tristate(Enum):
    """Values for the TriState field type."""
    NO = 0
    YES = 1
    AUTO = 2


@dataclass
class SelectorEntry:
    # The key of the selector entry. At this time, this is the label of a
    # config_setting rule, or the pseudo-label "//conditions:default".
    label: str | None

    # True if the entry's value is the default value for the type as a
    # result of the condition value being specified as None (ie:
    # {"//condition": None}).
    is_default_value: bool | None

    value: Value


@dataclass
class Selector:
    # The list of (label, value) pairs in the map that defines the selector.
    # At this time, this cannot be empty, i.e. a selector has at least one
    # entry.
    entries: list[SelectorEntry]

    # Whether or not this has any default values.
    has_default_value: bool | None

    # The error message when no condition matches.
    no_match_error: str | None


@dataclass
class SelectorList:
    # The type that this selector list evaluates to, and the type that each
    # selector in the list evaluates to. At this time, this cannot be
    # SELECTOR_LIST, i.e. selector lists do not nest.
    type: AttributeDiscriminator | None

    # The list of selector elements in this selector list. At this time, this
    # cannot be empty, i.e. a selector list is never empty.
    elements: list[Selector]


# An Attribute value or a SelectorEntry value
Value = Union[
    int,
    str,
    Label,
    Output,
    list[str],
    list[Label],
    list[Output],
    DistributionSet,
    License,
    dict[str, str],
    list[FilesetEntry],
    dict[str, list[Label]],
    bool,
    Tristate,
    list[int],
    dict[str, Label],  # LABEL_DICT_UNARY
    SelectorList,
    dict[Label, str],  # LABEL_KEYED_STRING_DICT
]


@dataclass
class Attribute:
    """
    A rule attribute. Each attribute must have a type and one of the various
    value fields populated - for the most part.
    """
    # The name of the attribute
    name: str

    # Whether the attribute was explicitly specified
    explicitly_specified: bool | None

    # If this attribute has a string value or a string list value, then this
    # may be set to indicate that the value may be treated as a label that
    # isn't a dependency of this attribute's rule.
    nodep: bool | None

    # Represents the aspect that this attribute comes from. It is set to an
    # empty string if it does not come from an aspect.
    source_aspect_name: str | None

    # The type of attribute.  This message is used for all of the different
    # attribute types so the discriminator helps for figuring out what is
    # stored in the message.
    type: AttributeDiscriminator

    value: Value


@dataclass
class Rule:
    """A rule instance (e.g., cc_library foo, java_binary bar)."""
    # The name of the rule (formatted as an absolute label, e.g. //foo/bar:baz).
    name: str

    # The rule class (e.g., java_library)
    rule_class: str

    # The BUILD file and line number of the location (formatted as
    # <absolute_path>:<line_number>:<column_number>) in the rule's package's
    # BUILD file where the rule instance was instantiated. The line number will
    # be that of a rule invocation or macro call (that in turn invoked a
    # rule). See
    # https://bazel.build/rules/macros#macro-creation
    location: str | None

    # All of the attributes that describe the rule.
    attributes: list[Attribute]

    # All of the inputs to the rule (formatted as absolute labels). These are
    # predecessors in the dependency graph.
    rule_inputs: list[str]

    configured_rule_inputs: list[ConfiguredRuleInput]

    # All of the outputs of the rule (formatted as absolute labels). These are
    # successors in the dependency graph.
    rule_outputs: list[str]

    # The set of all "features" inherited from the rule's package declaration.
    default_settings: list[str]

    # Hash encapsulating the behavior of this Starlark rule. Any change to this
    # rule's definition that could change its behavior will be reflected here.
    skylark_environment_hash_code: str | None

    # The Starlark call stack at the moment the rule was instantiated.
    # Each entry has the form "file:line:col: function".
    # The outermost stack frame ("<toplevel>", the BUILD file) appears first;
    # the frame for the rule function itself is omitted.
    # The file name may be relative to package's source root directory.
    #
    # Requires --proto:instantiation_stack=true.
    instantiation_stack: list[str]

    # The Starlark call stack for the definition of the rule class of this
    # particular rule instance. If empty, either populating the field was not
    # enabled on the command line with the --proto:definition_stack flag or the
    # rule is a native one.
    definition_stack: list[str]


@dataclass
class ConfiguredRuleInput:
    label: str | None
    configuration_checksum: str | None
    configuration_id: int


@dataclass
class PackageGroup:
    """
    A package group. Aside from the name, it contains the list of packages
    present in the group (as specified in the BUILD file).
    """
    # The name of the package group
    name: str

    # The list of packages as specified in the BUILD file. Currently this is
    # only a list of packages, but some time in the future, there might be
    # some type of wildcard mechanism.
    contained_packages: list[str]

    # The list of sub package groups included in this one.
    included_package_groups: list[str]


@dataclass
class EnvironmentGroup:
    """
    An environment group.
    """
    # The name of the environment group.
    name: str

    # The environments that belong to this group (as labels).
    environmnet: list[str]

    # The member environments that rules implicitly support if not otherwise
    # specified.
    default: list[str]


@dataclass
class SourceFile:
    """A file that is an input into the build system."""

    # The name of the source file (a label).
    name: str

    # The location of the source file.  This is a path with a line number and a
    # column number not a label in the build system.
    location: str | None

    # Labels of .bzl (Starlark) files that are transitively loaded in this BUILD
    # file. This is present only when the SourceFile represents a BUILD file that
    # loaded .bzl files.
    subincludes: list[str]

    # Labels of package groups that are mentioned in the visibility declaration
    # for this source file.
    package_groups: list[str]

    # Labels mentioned in the visibility declaration (including :__pkg__ and
    # //visibility: ones)
    visibility_labels: list[str]

    # The package-level features enabled for this package. Only present if the
    # SourceFile represents a BUILD file.
    features: list[str]

    # License attribute for the file.
    license: License | None

    # True if the package contains an error. Only present if the SourceFile
    # represents a BUILD file.
    package_contains_errors: bool | None


@dataclass
class GeneratedFile:
    """A file that is the output of a build rule."""

    # The name of the generated file (a label).
    name: str

    # The label of the target that generates the file.
    generating_rule: str

    # The path, line number, and column number of the output file (not a label).
    location: str | None


Target = Union[Rule, SourceFile, GeneratedFile, PackageGroup, EnvironmentGroup]
