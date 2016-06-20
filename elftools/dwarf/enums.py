#-------------------------------------------------------------------------------
# elftools: dwarf/enums.py
#
# Mappings of enum names to values
#
# Eli Bendersky (eliben@gmail.com)
# This code is in the public domain
#-------------------------------------------------------------------------------
from construct import Pass
from ..common.py3compat import iteritems


ENUM_DW_TAG = dict(
    DW_TAG_null                     = 0x00,
    DW_TAG_array_type               = 0x01,
    DW_TAG_class_type               = 0x02,
    DW_TAG_entry_point              = 0x03,
    DW_TAG_enumeration_type         = 0x04,
    DW_TAG_formal_parameter         = 0x05,
    DW_TAG_imported_declaration     = 0x08,
    DW_TAG_label                    = 0x0a,
    DW_TAG_lexical_block            = 0x0b,
    DW_TAG_member                   = 0x0d,
    DW_TAG_pointer_type             = 0x0f,
    DW_TAG_reference_type           = 0x10,
    DW_TAG_compile_unit             = 0x11,
    DW_TAG_string_type              = 0x12,
    DW_TAG_structure_type           = 0x13,
    DW_TAG_subroutine_type          = 0x15,
    DW_TAG_typedef                  = 0x16,
    DW_TAG_union_type               = 0x17,
    DW_TAG_unspecified_parameters   = 0x18,
    DW_TAG_variant                  = 0x19,
    DW_TAG_common_block             = 0x1a,
    DW_TAG_common_inclusion         = 0x1b,
    DW_TAG_inheritance              = 0x1c,
    DW_TAG_inlined_subroutine       = 0x1d,
    DW_TAG_module                   = 0x1e,
    DW_TAG_ptr_to_member_type       = 0x1f,
    DW_TAG_set_type                 = 0x20,
    DW_TAG_subrange_type            = 0x21,
    DW_TAG_with_stmt                = 0x22,
    DW_TAG_access_declaration       = 0x23,
    DW_TAG_base_type                = 0x24,
    DW_TAG_catch_block              = 0x25,
    DW_TAG_const_type               = 0x26,
    DW_TAG_constant                 = 0x27,
    DW_TAG_enumerator               = 0x28,
    DW_TAG_file_type                = 0x29,
    DW_TAG_friend                   = 0x2a,
    DW_TAG_namelist                 = 0x2b,
    DW_TAG_namelist_item            = 0x2c,
    DW_TAG_namelist_items           = 0x2c,
    DW_TAG_packed_type              = 0x2d,
    DW_TAG_subprogram               = 0x2e,

    # The DWARF standard defines these as _parameter, not _param, but we
    # maintain compatibility with readelf.
    DW_TAG_template_type_param      = 0x2f,
    DW_TAG_template_value_param     = 0x30,

    DW_TAG_thrown_type              = 0x31,
    DW_TAG_try_block                = 0x32,
    DW_TAG_variant_part             = 0x33,
    DW_TAG_variable                 = 0x34,
    DW_TAG_volatile_type            = 0x35,
    DW_TAG_dwarf_procedure          = 0x36,
    DW_TAG_restrict_type            = 0x37,
    DW_TAG_interface_type           = 0x38,
    DW_TAG_namespace                = 0x39,
    DW_TAG_imported_module          = 0x3a,
    DW_TAG_unspecified_type         = 0x3b,
    DW_TAG_partial_unit             = 0x3c,
    DW_TAG_imported_unit            = 0x3d,
    DW_TAG_mutable_type             = 0x3e,
    DW_TAG_condition                = 0x3f,
    DW_TAG_shared_type              = 0x40,
    DW_TAG_type_unit                = 0x41,
    DW_TAG_rvalue_reference_type    = 0x42,

    DW_TAG_lo_user                  = 0x4080,
    DW_TAG_GNU_call_site            = 0x4109,
    DW_TAG_GNU_call_site_parameter  = 0x410a,
    DW_TAG_hi_user                  = 0xffff,

    _default_                       = Pass,
)


ENUM_DW_CHILDREN = dict(
    DW_CHILDREN_no  = 0x00,
    DW_CHILDREN_yes = 0x01,
)


ENUM_DW_AT = dict(
    DW_AT_null                  = 0x00,
    DW_AT_sibling               = 0x01,
    DW_AT_location              = 0x02,
    DW_AT_name                  = 0x03,
    DW_AT_ordering              = 0x09,
    DW_AT_subscr_data           = 0x0a,
    DW_AT_byte_size             = 0x0b,
    DW_AT_bit_offset            = 0x0c,
    DW_AT_bit_size              = 0x0d,
    DW_AT_element_list          = 0x0f,
    DW_AT_stmt_list             = 0x10,
    DW_AT_low_pc                = 0x11,
    DW_AT_high_pc               = 0x12,
    DW_AT_language              = 0x13,
    DW_AT_member                = 0x14,
    DW_AT_discr                 = 0x15,
    DW_AT_discr_value           = 0x16,
    DW_AT_visibility            = 0x17,
    DW_AT_import                = 0x18,
    DW_AT_string_length         = 0x19,
    DW_AT_common_reference      = 0x1a,
    DW_AT_comp_dir              = 0x1b,
    DW_AT_const_value           = 0x1c,
    DW_AT_containing_type       = 0x1d,
    DW_AT_default_value         = 0x1e,
    DW_AT_inline                = 0x20,
    DW_AT_is_optional           = 0x21,
    DW_AT_lower_bound           = 0x22,
    DW_AT_producer              = 0x25,
    DW_AT_prototyped            = 0x27,
    DW_AT_return_addr           = 0x2a,
    DW_AT_start_scope           = 0x2c,
    DW_AT_bit_stride            = 0x2e,
    DW_AT_stride_size           = 0x2e,
    DW_AT_upper_bound           = 0x2f,
    DW_AT_abstract_origin       = 0x31,
    DW_AT_accessibility         = 0x32,
    DW_AT_address_class         = 0x33,
    DW_AT_artificial            = 0x34,
    DW_AT_base_types            = 0x35,
    DW_AT_calling_convention    = 0x36,
    DW_AT_count                 = 0x37,
    DW_AT_data_member_location  = 0x38,
    DW_AT_decl_column           = 0x39,
    DW_AT_decl_file             = 0x3a,
    DW_AT_decl_line             = 0x3b,
    DW_AT_declaration           = 0x3c,
    DW_AT_discr_list            = 0x3d,
    DW_AT_encoding              = 0x3e,
    DW_AT_external              = 0x3f,
    DW_AT_frame_base            = 0x40,
    DW_AT_friend                = 0x41,
    DW_AT_identifier_case       = 0x42,
    DW_AT_macro_info            = 0x43,
    DW_AT_namelist_item         = 0x44,
    DW_AT_priority              = 0x45,
    DW_AT_segment               = 0x46,
    DW_AT_specification         = 0x47,
    DW_AT_static_link           = 0x48,
    DW_AT_type                  = 0x49,
    DW_AT_use_location          = 0x4a,
    DW_AT_variable_parameter    = 0x4b,
    DW_AT_virtuality            = 0x4c,
    DW_AT_vtable_elem_location  = 0x4d,
    DW_AT_allocated             = 0x4e,
    DW_AT_associated            = 0x4f,
    DW_AT_data_location         = 0x50,
    DW_AT_byte_stride           = 0x51,
    DW_AT_stride                = 0x51,
    DW_AT_entry_pc              = 0x52,
    DW_AT_use_UTF8              = 0x53,
    DW_AT_extension             = 0x54,
    DW_AT_ranges                = 0x55,
    DW_AT_trampoline            = 0x56,
    DW_AT_call_column           = 0x57,
    DW_AT_call_file             = 0x58,
    DW_AT_call_line             = 0x59,
    DW_AT_description           = 0x5a,
    DW_AT_binary_scale          = 0x5b,
    DW_AT_decimal_scale         = 0x5c,
    DW_AT_small                 = 0x5d,
    DW_AT_decimal_sign          = 0x5e,
    DW_AT_digit_count           = 0x5f,
    DW_AT_picture_string        = 0x60,
    DW_AT_mutable               = 0x61,
    DW_AT_threads_scaled        = 0x62,
    DW_AT_explicit              = 0x63,
    DW_AT_object_pointer        = 0x64,
    DW_AT_endianity             = 0x65,
    DW_AT_elemental             = 0x66,
    DW_AT_pure                  = 0x67,
    DW_AT_recursive             = 0x68,
    DW_AT_signature             = 0x69,
    DW_AT_main_subprogram       = 0x6a,
    DW_AT_data_bit_offset       = 0x6b,
    DW_AT_const_expr            = 0x6c,
    DW_AT_enum_class            = 0x6d,
    DW_AT_linkage_name          = 0x6e,

    DW_AT_MIPS_fde                      = 0x2001,
    DW_AT_MIPS_loop_begin               = 0x2002,
    DW_AT_MIPS_tail_loop_begin          = 0x2003,
    DW_AT_MIPS_epilog_begin             = 0x2004,
    DW_AT_MIPS_loop_unroll_factor       = 0x2005,
    DW_AT_MIPS_software_pipeline_depth  = 0x2006,
    DW_AT_MIPS_linkage_name             = 0x2007,
    DW_AT_MIPS_stride                   = 0x2008,
    DW_AT_MIPS_abstract_name            = 0x2009,
    DW_AT_MIPS_clone_origin             = 0x200a,
    DW_AT_MIPS_has_inlines              = 0x200b,
    DW_AT_MIPS_stride_byte              = 0x200c,
    DW_AT_MIPS_stride_elem              = 0x200d,
    DW_AT_MIPS_ptr_dopetype             = 0x200e,
    DW_AT_MIPS_allocatable_dopetype     = 0x200f,
    DW_AT_MIPS_assumed_shape_dopetype   = 0x2010,
    DW_AT_MIPS_assumed_size             = 0x2011,

    DW_AT_sf_names                      = 0x2101,
    DW_AT_src_info                      = 0x2102,
    DW_AT_mac_info                      = 0x2103,
    DW_AT_src_coords                    = 0x2104,
    DW_AT_body_begin                    = 0x2105,
    DW_AT_body_end                      = 0x2106,
    DW_AT_GNU_vector                    = 0x2107,
    DW_AT_GNU_template_name             = 0x2110,

    DW_AT_GNU_call_site_value               = 0x2111,
    DW_AT_GNU_call_site_data_value          = 0x2112,
    DW_AT_GNU_call_site_target              = 0x2113,
    DW_AT_GNU_call_site_target_clobbered    = 0x2114,
    DW_AT_GNU_tail_call                     = 0x2115,
    DW_AT_GNU_all_tail_call_sites           = 0x2116,
    DW_AT_GNU_all_call_sites                = 0x2117,
    DW_AT_GNU_all_source_call_sites         = 0x2118,

    DW_AT_APPLE_optimized               = 0x3fe1,
    DW_AT_APPLE_flags                   = 0x3fe2,
    DW_AT_APPLE_isa                     = 0x3fe3,
    DW_AT_APPLE_block                   = 0x3fe4,
    DW_AT_APPLE_major_runtime_vers      = 0x3fe5,
    DW_AT_APPLE_runtime_class           = 0x3fe6,
    DW_AT_APPLE_omit_frame_ptr          = 0x3fe7,
    DW_AT_APPLE_property_name           = 0x3fe8,
    DW_AT_APPLE_property_getter         = 0x3fe9,
    DW_AT_APPLE_property_setter         = 0x3fea,
    DW_AT_APPLE_property_attribute      = 0x3feb,
    DW_AT_APPLE_objc_complete_type      = 0x3fec,
    DW_AT_APPLE_property                = 0x3fed,

    _default_ = Pass,
)


ENUM_DW_FORM = dict(
    DW_FORM_null            = 0x00,
    DW_FORM_addr            = 0x01,
    DW_FORM_block2          = 0x03,
    DW_FORM_block4          = 0x04,
    DW_FORM_data2           = 0x05,
    DW_FORM_data4           = 0x06,
    DW_FORM_data8           = 0x07,
    DW_FORM_string          = 0x08,
    DW_FORM_block           = 0x09,
    DW_FORM_block1          = 0x0a,
    DW_FORM_data1           = 0x0b,
    DW_FORM_flag            = 0x0c,
    DW_FORM_sdata           = 0x0d,
    DW_FORM_strp            = 0x0e,
    DW_FORM_udata           = 0x0f,
    DW_FORM_ref_addr        = 0x10,
    DW_FORM_ref1            = 0x11,
    DW_FORM_ref2            = 0x12,
    DW_FORM_ref4            = 0x13,
    DW_FORM_ref8            = 0x14,
    DW_FORM_ref_udata       = 0x15,
    DW_FORM_indirect        = 0x16,
    DW_FORM_sec_offset      = 0x17,
    DW_FORM_exprloc         = 0x18,
    DW_FORM_flag_present    = 0x19,
    DW_FORM_ref_sig8        = 0x20,

    DW_FORM_GNU_strp_alt    = 0x1f21,
    DW_FORM_GNU_ref_alt     = 0x1f20,
    _default_               = Pass,
)

# Inverse mapping for ENUM_DW_FORM
DW_FORM_raw2name = dict((v, k) for k, v in iteritems(ENUM_DW_FORM))

