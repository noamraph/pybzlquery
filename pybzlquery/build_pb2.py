# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/main/protobuf/build.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsrc/main/protobuf/build.proto\x12\x0b\x62laze_query\"2\n\x07License\x12\x14\n\x0clicense_type\x18\x01 \x03(\t\x12\x11\n\texception\x18\x02 \x03(\t\"-\n\x0fStringDictEntry\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"1\n\x13LabelDictUnaryEntry\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"0\n\x12LabelListDictEntry\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x03(\t\"7\n\x19LabelKeyedStringDictEntry\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"1\n\x13StringListDictEntry\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x03(\t\"\x82\x02\n\x0c\x46ilesetEntry\x12\x0e\n\x06source\x18\x01 \x02(\t\x12\x1d\n\x15\x64\x65stination_directory\x18\x02 \x02(\t\x12\x15\n\rfiles_present\x18\x07 \x01(\x08\x12\x0c\n\x04\x66ile\x18\x03 \x03(\t\x12\x0f\n\x07\x65xclude\x18\x04 \x03(\t\x12I\n\x10symlink_behavior\x18\x05 \x01(\x0e\x32).blaze_query.FilesetEntry.SymlinkBehavior:\x04\x43OPY\x12\x14\n\x0cstrip_prefix\x18\x06 \x01(\t\",\n\x0fSymlinkBehavior\x12\x08\n\x04\x43OPY\x10\x01\x12\x0f\n\x0b\x44\x45REFERENCE\x10\x02\"\xc4\x11\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1c\n\x14\x65xplicitly_specified\x18\r \x01(\x08\x12\r\n\x05nodep\x18\x14 \x01(\x08\x12\x1a\n\x12source_aspect_name\x18\x17 \x01(\t\x12\x32\n\x04type\x18\x02 \x02(\x0e\x32$.blaze_query.Attribute.Discriminator\x12\x11\n\tint_value\x18\x03 \x01(\x05\x12\x14\n\x0cstring_value\x18\x05 \x01(\t\x12\x15\n\rboolean_value\x18\x0e \x01(\x08\x12\x37\n\x0etristate_value\x18\x0f \x01(\x0e\x32\x1f.blaze_query.Attribute.Tristate\x12\x19\n\x11string_list_value\x18\x06 \x03(\t\x12%\n\x07license\x18\x07 \x01(\x0b\x32\x14.blaze_query.License\x12\x37\n\x11string_dict_value\x18\x08 \x03(\x0b\x32\x1c.blaze_query.StringDictEntry\x12\x35\n\x12\x66ileset_list_value\x18\t \x03(\x0b\x32\x19.blaze_query.FilesetEntry\x12>\n\x15label_list_dict_value\x18\n \x03(\x0b\x32\x1f.blaze_query.LabelListDictEntry\x12@\n\x16string_list_dict_value\x18\x0b \x03(\x0b\x32 .blaze_query.StringListDictEntry\x12\x16\n\x0eint_list_value\x18\x11 \x03(\x05\x12@\n\x16label_dict_unary_value\x18\x13 \x03(\x0b\x32 .blaze_query.LabelDictUnaryEntry\x12M\n\x1dlabel_keyed_string_dict_value\x18\x16 \x03(\x0b\x32&.blaze_query.LabelKeyedStringDictEntry\x12:\n\rselector_list\x18\x15 \x01(\x0b\x32#.blaze_query.Attribute.SelectorList\x12*\n\"DEPRECATED_string_dict_unary_value\x18\x12 \x03(\x0c\x1a\xc0\x05\n\rSelectorEntry\x12\r\n\x05label\x18\x01 \x01(\t\x12\x18\n\x10is_default_value\x18\x10 \x01(\x08\x12\x11\n\tint_value\x18\x02 \x01(\x05\x12\x14\n\x0cstring_value\x18\x03 \x01(\t\x12\x15\n\rboolean_value\x18\x04 \x01(\x08\x12\x37\n\x0etristate_value\x18\x05 \x01(\x0e\x32\x1f.blaze_query.Attribute.Tristate\x12\x19\n\x11string_list_value\x18\x06 \x03(\t\x12%\n\x07license\x18\x07 \x01(\x0b\x32\x14.blaze_query.License\x12\x37\n\x11string_dict_value\x18\x08 \x03(\x0b\x32\x1c.blaze_query.StringDictEntry\x12\x35\n\x12\x66ileset_list_value\x18\t \x03(\x0b\x32\x19.blaze_query.FilesetEntry\x12>\n\x15label_list_dict_value\x18\n \x03(\x0b\x32\x1f.blaze_query.LabelListDictEntry\x12@\n\x16string_list_dict_value\x18\x0b \x03(\x0b\x32 .blaze_query.StringListDictEntry\x12\x16\n\x0eint_list_value\x18\r \x03(\x05\x12@\n\x16label_dict_unary_value\x18\x0f \x03(\x0b\x32 .blaze_query.LabelDictUnaryEntry\x12M\n\x1dlabel_keyed_string_dict_value\x18\x11 \x03(\x0b\x32&.blaze_query.LabelKeyedStringDictEntry\x12*\n\"DEPRECATED_string_dict_unary_value\x18\x0e \x03(\x0cJ\x04\x08\x0c\x10\r\x1at\n\x08Selector\x12\x35\n\x07\x65ntries\x18\x01 \x03(\x0b\x32$.blaze_query.Attribute.SelectorEntry\x12\x19\n\x11has_default_value\x18\x02 \x01(\x08\x12\x16\n\x0eno_match_error\x18\x03 \x01(\t\x1au\n\x0cSelectorList\x12\x32\n\x04type\x18\x01 \x01(\x0e\x32$.blaze_query.Attribute.Discriminator\x12\x31\n\x08\x65lements\x18\x02 \x03(\x0b\x32\x1f.blaze_query.Attribute.Selector\"\x8a\x03\n\rDiscriminator\x12\x0b\n\x07INTEGER\x10\x01\x12\n\n\x06STRING\x10\x02\x12\t\n\x05LABEL\x10\x03\x12\n\n\x06OUTPUT\x10\x04\x12\x0f\n\x0bSTRING_LIST\x10\x05\x12\x0e\n\nLABEL_LIST\x10\x06\x12\x0f\n\x0bOUTPUT_LIST\x10\x07\x12\x14\n\x10\x44ISTRIBUTION_SET\x10\x08\x12\x0b\n\x07LICENSE\x10\t\x12\x0f\n\x0bSTRING_DICT\x10\n\x12\x16\n\x12\x46ILESET_ENTRY_LIST\x10\x0b\x12\x13\n\x0fLABEL_LIST_DICT\x10\x0c\x12\x14\n\x10STRING_LIST_DICT\x10\r\x12\x0b\n\x07\x42OOLEAN\x10\x0e\x12\x0c\n\x08TRISTATE\x10\x0f\x12\x10\n\x0cINTEGER_LIST\x10\x10\x12\x0b\n\x07UNKNOWN\x10\x12\x12\x14\n\x10LABEL_DICT_UNARY\x10\x13\x12\x11\n\rSELECTOR_LIST\x10\x14\x12\x1b\n\x17LABEL_KEYED_STRING_DICT\x10\x15\x12 \n\x1c\x44\x45PRECATED_STRING_DICT_UNARY\x10\x11\"%\n\x08Tristate\x12\x06\n\x02NO\x10\x00\x12\x07\n\x03YES\x10\x01\x12\x08\n\x04\x41UTO\x10\x02J\x04\x08\x0c\x10\rJ\x04\x08\x10\x10\x11\"\x97\x03\n\x04Rule\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x12\n\nrule_class\x18\x02 \x02(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12)\n\tattribute\x18\x04 \x03(\x0b\x32\x16.blaze_query.Attribute\x12\x12\n\nrule_input\x18\x05 \x03(\t\x12?\n\x15\x63onfigured_rule_input\x18\x0f \x03(\x0b\x32 .blaze_query.ConfiguredRuleInput\x12\x13\n\x0brule_output\x18\x06 \x03(\t\x12\x17\n\x0f\x64\x65\x66\x61ult_setting\x18\x07 \x03(\t\x12$\n\x1c\x44\x45PRECATED_public_by_default\x18\t \x01(\x08\x12\x1d\n\x15\x44\x45PRECATED_is_skylark\x18\n \x01(\x08\x12%\n\x1dskylark_environment_hash_code\x18\x0c \x01(\t\x12\x1b\n\x13instantiation_stack\x18\r \x03(\t\x12\x18\n\x10\x64\x65\x66inition_stack\x18\x0e \x03(\tJ\x04\x08\x08\x10\tJ\x04\x08\x0b\x10\x0c\"^\n\x13\x43onfiguredRuleInput\x12\r\n\x05label\x18\x01 \x01(\t\x12\x1e\n\x16\x63onfiguration_checksum\x18\x02 \x01(\t\x12\x18\n\x10\x63onfiguration_id\x18\x03 \x01(\r\"g\n\x0bRuleSummary\x12\x1f\n\x04rule\x18\x01 \x02(\x0b\x32\x11.blaze_query.Rule\x12%\n\ndependency\x18\x02 \x03(\x0b\x32\x11.blaze_query.Rule\x12\x10\n\x08location\x18\x03 \x01(\t\"]\n\x0cPackageGroup\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x19\n\x11\x63ontained_package\x18\x02 \x03(\t\x12\x1e\n\x16included_package_group\x18\x03 \x03(\tJ\x04\x08\x04\x10\x05\"F\n\x10\x45nvironmentGroup\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x13\n\x0b\x65nvironment\x18\x02 \x03(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x03 \x03(\t\"\xd0\x01\n\nSourceFile\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x12\n\nsubinclude\x18\x03 \x03(\t\x12\x15\n\rpackage_group\x18\x04 \x03(\t\x12\x18\n\x10visibility_label\x18\x05 \x03(\t\x12\x0f\n\x07\x66\x65\x61ture\x18\x06 \x03(\t\x12%\n\x07license\x18\x08 \x01(\x0b\x32\x14.blaze_query.License\x12\x1f\n\x17package_contains_errors\x18\t \x01(\x08J\x04\x08\x07\x10\x08\"H\n\rGeneratedFile\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x17\n\x0fgenerating_rule\x18\x02 \x02(\t\x12\x10\n\x08location\x18\x03 \x01(\t\"\x92\x03\n\x06Target\x12/\n\x04type\x18\x01 \x02(\x0e\x32!.blaze_query.Target.Discriminator\x12\x1f\n\x04rule\x18\x02 \x01(\x0b\x32\x11.blaze_query.Rule\x12,\n\x0bsource_file\x18\x03 \x01(\x0b\x32\x17.blaze_query.SourceFile\x12\x32\n\x0egenerated_file\x18\x04 \x01(\x0b\x32\x1a.blaze_query.GeneratedFile\x12\x30\n\rpackage_group\x18\x05 \x01(\x0b\x32\x19.blaze_query.PackageGroup\x12\x38\n\x11\x65nvironment_group\x18\x06 \x01(\x0b\x32\x1d.blaze_query.EnvironmentGroup\"h\n\rDiscriminator\x12\x08\n\x04RULE\x10\x01\x12\x0f\n\x0bSOURCE_FILE\x10\x02\x12\x12\n\x0eGENERATED_FILE\x10\x03\x12\x11\n\rPACKAGE_GROUP\x10\x04\x12\x15\n\x11\x45NVIRONMENT_GROUP\x10\x05\"2\n\x0bQueryResult\x12#\n\x06target\x18\x01 \x03(\x0b\x32\x13.blaze_query.Target\"\xa6\x01\n\x14\x41llowedRuleClassInfo\x12\x44\n\x06policy\x18\x01 \x02(\x0e\x32\x34.blaze_query.AllowedRuleClassInfo.AllowedRuleClasses\x12\x1a\n\x12\x61llowed_rule_class\x18\x02 \x03(\t\",\n\x12\x41llowedRuleClasses\x12\x07\n\x03\x41NY\x10\x01\x12\r\n\tSPECIFIED\x10\x02\"\xee\x02\n\x13\x41ttributeDefinition\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x32\n\x04type\x18\x02 \x02(\x0e\x32$.blaze_query.Attribute.Discriminator\x12\x11\n\tmandatory\x18\x03 \x01(\x08\x12?\n\x14\x61llowed_rule_classes\x18\x04 \x01(\x0b\x32!.blaze_query.AllowedRuleClassInfo\x12\x15\n\rdocumentation\x18\x05 \x01(\t\x12\x13\n\x0b\x61llow_empty\x18\x06 \x01(\x08\x12\x19\n\x11\x61llow_single_file\x18\x07 \x01(\x08\x12,\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x0b\x32\x1b.blaze_query.AttributeValue\x12\x12\n\nexecutable\x18\n \x01(\x08\x12\x14\n\x0c\x63onfigurable\x18\x0b \x01(\x08\x12\r\n\x05nodep\x18\x0c \x01(\x08\x12\x13\n\x0b\x63\x66g_is_host\x18\r \x01(\x08\"\xe1\x01\n\x0e\x41ttributeValue\x12\x0b\n\x03int\x18\x01 \x01(\x05\x12\x0e\n\x06string\x18\x02 \x01(\t\x12\x0c\n\x04\x62ool\x18\x03 \x01(\x08\x12)\n\x04list\x18\x04 \x03(\x0b\x32\x1b.blaze_query.AttributeValue\x12\x33\n\x04\x64ict\x18\x05 \x03(\x0b\x32%.blaze_query.AttributeValue.DictEntry\x1a\x44\n\tDictEntry\x12\x0b\n\x03key\x18\x01 \x02(\t\x12*\n\x05value\x18\x02 \x02(\x0b\x32\x1b.blaze_query.AttributeValue\"y\n\x0eRuleDefinition\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x33\n\tattribute\x18\x02 \x03(\x0b\x32 .blaze_query.AttributeDefinition\x12\x15\n\rdocumentation\x18\x03 \x01(\t\x12\r\n\x05label\x18\x04 \x01(\t\":\n\rBuildLanguage\x12)\n\x04rule\x18\x01 \x03(\x0b\x32\x1b.blaze_query.RuleDefinitionB6\n4com.google.devtools.build.lib.query2.proto.proto2api')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.main.protobuf.build_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n4com.google.devtools.build.lib.query2.proto.proto2api'
  _LICENSE._serialized_start=46
  _LICENSE._serialized_end=96
  _STRINGDICTENTRY._serialized_start=98
  _STRINGDICTENTRY._serialized_end=143
  _LABELDICTUNARYENTRY._serialized_start=145
  _LABELDICTUNARYENTRY._serialized_end=194
  _LABELLISTDICTENTRY._serialized_start=196
  _LABELLISTDICTENTRY._serialized_end=244
  _LABELKEYEDSTRINGDICTENTRY._serialized_start=246
  _LABELKEYEDSTRINGDICTENTRY._serialized_end=301
  _STRINGLISTDICTENTRY._serialized_start=303
  _STRINGLISTDICTENTRY._serialized_end=352
  _FILESETENTRY._serialized_start=355
  _FILESETENTRY._serialized_end=613
  _FILESETENTRY_SYMLINKBEHAVIOR._serialized_start=569
  _FILESETENTRY_SYMLINKBEHAVIOR._serialized_end=613
  _ATTRIBUTE._serialized_start=616
  _ATTRIBUTE._serialized_end=2860
  _ATTRIBUTE_SELECTORENTRY._serialized_start=1471
  _ATTRIBUTE_SELECTORENTRY._serialized_end=2175
  _ATTRIBUTE_SELECTOR._serialized_start=2177
  _ATTRIBUTE_SELECTOR._serialized_end=2293
  _ATTRIBUTE_SELECTORLIST._serialized_start=2295
  _ATTRIBUTE_SELECTORLIST._serialized_end=2412
  _ATTRIBUTE_DISCRIMINATOR._serialized_start=2415
  _ATTRIBUTE_DISCRIMINATOR._serialized_end=2809
  _ATTRIBUTE_TRISTATE._serialized_start=2811
  _ATTRIBUTE_TRISTATE._serialized_end=2848
  _RULE._serialized_start=2863
  _RULE._serialized_end=3270
  _CONFIGUREDRULEINPUT._serialized_start=3272
  _CONFIGUREDRULEINPUT._serialized_end=3366
  _RULESUMMARY._serialized_start=3368
  _RULESUMMARY._serialized_end=3471
  _PACKAGEGROUP._serialized_start=3473
  _PACKAGEGROUP._serialized_end=3566
  _ENVIRONMENTGROUP._serialized_start=3568
  _ENVIRONMENTGROUP._serialized_end=3638
  _SOURCEFILE._serialized_start=3641
  _SOURCEFILE._serialized_end=3849
  _GENERATEDFILE._serialized_start=3851
  _GENERATEDFILE._serialized_end=3923
  _TARGET._serialized_start=3926
  _TARGET._serialized_end=4328
  _TARGET_DISCRIMINATOR._serialized_start=4224
  _TARGET_DISCRIMINATOR._serialized_end=4328
  _QUERYRESULT._serialized_start=4330
  _QUERYRESULT._serialized_end=4380
  _ALLOWEDRULECLASSINFO._serialized_start=4383
  _ALLOWEDRULECLASSINFO._serialized_end=4549
  _ALLOWEDRULECLASSINFO_ALLOWEDRULECLASSES._serialized_start=4505
  _ALLOWEDRULECLASSINFO_ALLOWEDRULECLASSES._serialized_end=4549
  _ATTRIBUTEDEFINITION._serialized_start=4552
  _ATTRIBUTEDEFINITION._serialized_end=4918
  _ATTRIBUTEVALUE._serialized_start=4921
  _ATTRIBUTEVALUE._serialized_end=5146
  _ATTRIBUTEVALUE_DICTENTRY._serialized_start=5078
  _ATTRIBUTEVALUE_DICTENTRY._serialized_end=5146
  _RULEDEFINITION._serialized_start=5148
  _RULEDEFINITION._serialized_end=5269
  _BUILDLANGUAGE._serialized_start=5271
  _BUILDLANGUAGE._serialized_end=5329
# @@protoc_insertion_point(module_scope)