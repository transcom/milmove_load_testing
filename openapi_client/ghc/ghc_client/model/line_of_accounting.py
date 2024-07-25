"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ghc_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from ghc_client.exceptions import ApiAttributeError



class LineOfAccounting(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('loa_sys_id',): {
            'max_length': 20,
        },
        ('loa_dpt_id',): {
            'max_length': 2,
        },
        ('loa_tnsfr_dpt_nm',): {
            'max_length': 4,
        },
        ('loa_baf_id',): {
            'max_length': 4,
        },
        ('loa_trsy_sfx_tx',): {
            'max_length': 4,
        },
        ('loa_maj_clm_nm',): {
            'max_length': 4,
        },
        ('loa_op_agncy_id',): {
            'max_length': 4,
        },
        ('loa_allt_sn_id',): {
            'max_length': 5,
        },
        ('loa_pgm_elmnt_id',): {
            'max_length': 12,
        },
        ('loa_tsk_bdgt_sbln_tx',): {
            'max_length': 8,
        },
        ('loa_df_agncy_alctn_rcpnt_id',): {
            'max_length': 4,
        },
        ('loa_jb_ord_nm',): {
            'max_length': 10,
        },
        ('loa_sbaltmt_rcpnt_id',): {
            'max_length': 1,
        },
        ('loa_wk_cntr_rcpnt_nm',): {
            'max_length': 6,
        },
        ('loa_maj_rmbsmt_src_id',): {
            'max_length': 1,
        },
        ('loa_dtl_rmbsmt_src_id',): {
            'max_length': 3,
        },
        ('loa_cust_nm',): {
            'max_length': 6,
        },
        ('loa_obj_cls_id',): {
            'max_length': 6,
        },
        ('loa_srv_src_id',): {
            'max_length': 1,
        },
        ('loa_spcl_intr_id',): {
            'max_length': 2,
        },
        ('loa_bdgt_acnt_cls_nm',): {
            'max_length': 8,
        },
        ('loa_doc_id',): {
            'max_length': 15,
        },
        ('loa_cls_ref_id',): {
            'max_length': 2,
        },
        ('loa_instl_acntg_act_id',): {
            'max_length': 6,
        },
        ('loa_lcl_instl_id',): {
            'max_length': 18,
        },
        ('loa_fms_trnsactn_id',): {
            'max_length': 12,
        },
        ('loa_fnct_prs_nm',): {
            'max_length': 255,
        },
        ('loa_stat_cd',): {
            'max_length': 1,
        },
        ('loa_hist_stat_cd',): {
            'max_length': 1,
        },
        ('loa_hs_gds_cd',): {
            'max_length': 2,
        },
        ('org_grp_dfas_cd',): {
            'max_length': 2,
        },
        ('loa_uic',): {
            'max_length': 6,
        },
        ('loa_trnsn_id',): {
            'max_length': 3,
        },
        ('loa_sub_acnt_id',): {
            'max_length': 3,
        },
        ('loa_bet_cd',): {
            'max_length': 4,
        },
        ('loa_fnd_ty_fg_cd',): {
            'max_length': 1,
        },
        ('loa_bgt_ln_itm_id',): {
            'max_length': 8,
        },
        ('loa_scrty_coop_impl_agnc_cd',): {
            'max_length': 1,
        },
        ('loa_scrty_coop_dsgntr_cd',): {
            'max_length': 4,
        },
        ('loa_scrty_coop_ln_itm_id',): {
            'max_length': 3,
        },
        ('loa_agnc_dsbr_cd',): {
            'max_length': 6,
        },
        ('loa_agnc_acntng_cd',): {
            'max_length': 6,
        },
        ('loa_fnd_cntr_id',): {
            'max_length': 12,
        },
        ('loa_cst_cntr_id',): {
            'max_length': 16,
        },
        ('loa_prj_id',): {
            'max_length': 12,
        },
        ('loa_actvty_id',): {
            'max_length': 11,
        },
        ('loa_cst_cd',): {
            'max_length': 16,
        },
        ('loa_wrk_ord_id',): {
            'max_length': 16,
        },
        ('loa_fncl_ar_id',): {
            'max_length': 6,
        },
        ('loa_scrty_coop_cust_cd',): {
            'max_length': 2,
        },
        ('loa_bgt_rstr_cd',): {
            'max_length': 1,
        },
        ('loa_bgt_sub_act_cd',): {
            'max_length': 4,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'id': (str,),  # noqa: E501
            'loa_sys_id': (str, none_type,),  # noqa: E501
            'loa_dpt_id': (str, none_type,),  # noqa: E501
            'loa_tnsfr_dpt_nm': (str, none_type,),  # noqa: E501
            'loa_baf_id': (str, none_type,),  # noqa: E501
            'loa_trsy_sfx_tx': (str, none_type,),  # noqa: E501
            'loa_maj_clm_nm': (str, none_type,),  # noqa: E501
            'loa_op_agncy_id': (str, none_type,),  # noqa: E501
            'loa_allt_sn_id': (str, none_type,),  # noqa: E501
            'loa_pgm_elmnt_id': (str, none_type,),  # noqa: E501
            'loa_tsk_bdgt_sbln_tx': (str, none_type,),  # noqa: E501
            'loa_df_agncy_alctn_rcpnt_id': (str, none_type,),  # noqa: E501
            'loa_jb_ord_nm': (str, none_type,),  # noqa: E501
            'loa_sbaltmt_rcpnt_id': (str, none_type,),  # noqa: E501
            'loa_wk_cntr_rcpnt_nm': (str, none_type,),  # noqa: E501
            'loa_maj_rmbsmt_src_id': (str, none_type,),  # noqa: E501
            'loa_dtl_rmbsmt_src_id': (str, none_type,),  # noqa: E501
            'loa_cust_nm': (str, none_type,),  # noqa: E501
            'loa_obj_cls_id': (str, none_type,),  # noqa: E501
            'loa_srv_src_id': (str, none_type,),  # noqa: E501
            'loa_spcl_intr_id': (str, none_type,),  # noqa: E501
            'loa_bdgt_acnt_cls_nm': (str, none_type,),  # noqa: E501
            'loa_doc_id': (str, none_type,),  # noqa: E501
            'loa_cls_ref_id': (str, none_type,),  # noqa: E501
            'loa_instl_acntg_act_id': (str, none_type,),  # noqa: E501
            'loa_lcl_instl_id': (str, none_type,),  # noqa: E501
            'loa_fms_trnsactn_id': (str, none_type,),  # noqa: E501
            'loa_dsc_tx': (str, none_type,),  # noqa: E501
            'loa_bgn_dt': (date, none_type,),  # noqa: E501
            'loa_end_dt': (date, none_type,),  # noqa: E501
            'loa_fnct_prs_nm': (str, none_type,),  # noqa: E501
            'loa_stat_cd': (str, none_type,),  # noqa: E501
            'loa_hist_stat_cd': (str, none_type,),  # noqa: E501
            'loa_hs_gds_cd': (str, none_type,),  # noqa: E501
            'org_grp_dfas_cd': (str, none_type,),  # noqa: E501
            'loa_uic': (str, none_type,),  # noqa: E501
            'loa_trnsn_id': (str, none_type,),  # noqa: E501
            'loa_sub_acnt_id': (str, none_type,),  # noqa: E501
            'loa_bet_cd': (str, none_type,),  # noqa: E501
            'loa_fnd_ty_fg_cd': (str, none_type,),  # noqa: E501
            'loa_bgt_ln_itm_id': (str, none_type,),  # noqa: E501
            'loa_scrty_coop_impl_agnc_cd': (str, none_type,),  # noqa: E501
            'loa_scrty_coop_dsgntr_cd': (str, none_type,),  # noqa: E501
            'loa_scrty_coop_ln_itm_id': (str, none_type,),  # noqa: E501
            'loa_agnc_dsbr_cd': (str, none_type,),  # noqa: E501
            'loa_agnc_acntng_cd': (str, none_type,),  # noqa: E501
            'loa_fnd_cntr_id': (str, none_type,),  # noqa: E501
            'loa_cst_cntr_id': (str, none_type,),  # noqa: E501
            'loa_prj_id': (str, none_type,),  # noqa: E501
            'loa_actvty_id': (str, none_type,),  # noqa: E501
            'loa_cst_cd': (str, none_type,),  # noqa: E501
            'loa_wrk_ord_id': (str, none_type,),  # noqa: E501
            'loa_fncl_ar_id': (str, none_type,),  # noqa: E501
            'loa_scrty_coop_cust_cd': (str, none_type,),  # noqa: E501
            'loa_end_fy_tx': (int, none_type,),  # noqa: E501
            'loa_bg_fy_tx': (int, none_type,),  # noqa: E501
            'loa_bgt_rstr_cd': (str, none_type,),  # noqa: E501
            'loa_bgt_sub_act_cd': (str, none_type,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'valid_loa_for_tac': (bool, none_type,),  # noqa: E501
            'valid_hhg_program_code_for_loa': (bool, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'loa_sys_id': 'loaSysId',  # noqa: E501
        'loa_dpt_id': 'loaDptID',  # noqa: E501
        'loa_tnsfr_dpt_nm': 'loaTnsfrDptNm',  # noqa: E501
        'loa_baf_id': 'loaBafID',  # noqa: E501
        'loa_trsy_sfx_tx': 'loaTrsySfxTx',  # noqa: E501
        'loa_maj_clm_nm': 'loaMajClmNm',  # noqa: E501
        'loa_op_agncy_id': 'loaOpAgncyID',  # noqa: E501
        'loa_allt_sn_id': 'loaAlltSnID',  # noqa: E501
        'loa_pgm_elmnt_id': 'loaPgmElmntID',  # noqa: E501
        'loa_tsk_bdgt_sbln_tx': 'loaTskBdgtSblnTx',  # noqa: E501
        'loa_df_agncy_alctn_rcpnt_id': 'loaDfAgncyAlctnRcpntID',  # noqa: E501
        'loa_jb_ord_nm': 'loaJbOrdNm',  # noqa: E501
        'loa_sbaltmt_rcpnt_id': 'loaSbaltmtRcpntID',  # noqa: E501
        'loa_wk_cntr_rcpnt_nm': 'loaWkCntrRcpntNm',  # noqa: E501
        'loa_maj_rmbsmt_src_id': 'loaMajRmbsmtSrcID',  # noqa: E501
        'loa_dtl_rmbsmt_src_id': 'loaDtlRmbsmtSrcID',  # noqa: E501
        'loa_cust_nm': 'loaCustNm',  # noqa: E501
        'loa_obj_cls_id': 'loaObjClsID',  # noqa: E501
        'loa_srv_src_id': 'loaSrvSrcID',  # noqa: E501
        'loa_spcl_intr_id': 'loaSpclIntrID',  # noqa: E501
        'loa_bdgt_acnt_cls_nm': 'loaBdgtAcntClsNm',  # noqa: E501
        'loa_doc_id': 'loaDocID',  # noqa: E501
        'loa_cls_ref_id': 'loaClsRefID',  # noqa: E501
        'loa_instl_acntg_act_id': 'loaInstlAcntgActID',  # noqa: E501
        'loa_lcl_instl_id': 'loaLclInstlID',  # noqa: E501
        'loa_fms_trnsactn_id': 'loaFmsTrnsactnID',  # noqa: E501
        'loa_dsc_tx': 'loaDscTx',  # noqa: E501
        'loa_bgn_dt': 'loaBgnDt',  # noqa: E501
        'loa_end_dt': 'loaEndDt',  # noqa: E501
        'loa_fnct_prs_nm': 'loaFnctPrsNm',  # noqa: E501
        'loa_stat_cd': 'loaStatCd',  # noqa: E501
        'loa_hist_stat_cd': 'loaHistStatCd',  # noqa: E501
        'loa_hs_gds_cd': 'loaHsGdsCd',  # noqa: E501
        'org_grp_dfas_cd': 'orgGrpDfasCd',  # noqa: E501
        'loa_uic': 'loaUic',  # noqa: E501
        'loa_trnsn_id': 'loaTrnsnID',  # noqa: E501
        'loa_sub_acnt_id': 'loaSubAcntID',  # noqa: E501
        'loa_bet_cd': 'loaBetCd',  # noqa: E501
        'loa_fnd_ty_fg_cd': 'loaFndTyFgCd',  # noqa: E501
        'loa_bgt_ln_itm_id': 'loaBgtLnItmID',  # noqa: E501
        'loa_scrty_coop_impl_agnc_cd': 'loaScrtyCoopImplAgncCd',  # noqa: E501
        'loa_scrty_coop_dsgntr_cd': 'loaScrtyCoopDsgntrCd',  # noqa: E501
        'loa_scrty_coop_ln_itm_id': 'loaScrtyCoopLnItmID',  # noqa: E501
        'loa_agnc_dsbr_cd': 'loaAgncDsbrCd',  # noqa: E501
        'loa_agnc_acntng_cd': 'loaAgncAcntngCd',  # noqa: E501
        'loa_fnd_cntr_id': 'loaFndCntrID',  # noqa: E501
        'loa_cst_cntr_id': 'loaCstCntrID',  # noqa: E501
        'loa_prj_id': 'loaPrjID',  # noqa: E501
        'loa_actvty_id': 'loaActvtyID',  # noqa: E501
        'loa_cst_cd': 'loaCstCd',  # noqa: E501
        'loa_wrk_ord_id': 'loaWrkOrdID',  # noqa: E501
        'loa_fncl_ar_id': 'loaFnclArID',  # noqa: E501
        'loa_scrty_coop_cust_cd': 'loaScrtyCoopCustCd',  # noqa: E501
        'loa_end_fy_tx': 'loaEndFyTx',  # noqa: E501
        'loa_bg_fy_tx': 'loaBgFyTx',  # noqa: E501
        'loa_bgt_rstr_cd': 'loaBgtRstrCd',  # noqa: E501
        'loa_bgt_sub_act_cd': 'loaBgtSubActCd',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'valid_loa_for_tac': 'validLoaForTac',  # noqa: E501
        'valid_hhg_program_code_for_loa': 'validHhgProgramCodeForLoa',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """LineOfAccounting - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            loa_sys_id (str, none_type): [optional]  # noqa: E501
            loa_dpt_id (str, none_type): [optional]  # noqa: E501
            loa_tnsfr_dpt_nm (str, none_type): [optional]  # noqa: E501
            loa_baf_id (str, none_type): [optional]  # noqa: E501
            loa_trsy_sfx_tx (str, none_type): [optional]  # noqa: E501
            loa_maj_clm_nm (str, none_type): [optional]  # noqa: E501
            loa_op_agncy_id (str, none_type): [optional]  # noqa: E501
            loa_allt_sn_id (str, none_type): [optional]  # noqa: E501
            loa_pgm_elmnt_id (str, none_type): [optional]  # noqa: E501
            loa_tsk_bdgt_sbln_tx (str, none_type): [optional]  # noqa: E501
            loa_df_agncy_alctn_rcpnt_id (str, none_type): [optional]  # noqa: E501
            loa_jb_ord_nm (str, none_type): [optional]  # noqa: E501
            loa_sbaltmt_rcpnt_id (str, none_type): [optional]  # noqa: E501
            loa_wk_cntr_rcpnt_nm (str, none_type): [optional]  # noqa: E501
            loa_maj_rmbsmt_src_id (str, none_type): [optional]  # noqa: E501
            loa_dtl_rmbsmt_src_id (str, none_type): [optional]  # noqa: E501
            loa_cust_nm (str, none_type): [optional]  # noqa: E501
            loa_obj_cls_id (str, none_type): [optional]  # noqa: E501
            loa_srv_src_id (str, none_type): [optional]  # noqa: E501
            loa_spcl_intr_id (str, none_type): [optional]  # noqa: E501
            loa_bdgt_acnt_cls_nm (str, none_type): [optional]  # noqa: E501
            loa_doc_id (str, none_type): [optional]  # noqa: E501
            loa_cls_ref_id (str, none_type): [optional]  # noqa: E501
            loa_instl_acntg_act_id (str, none_type): [optional]  # noqa: E501
            loa_lcl_instl_id (str, none_type): [optional]  # noqa: E501
            loa_fms_trnsactn_id (str, none_type): [optional]  # noqa: E501
            loa_dsc_tx (str, none_type): [optional]  # noqa: E501
            loa_bgn_dt (date, none_type): [optional]  # noqa: E501
            loa_end_dt (date, none_type): [optional]  # noqa: E501
            loa_fnct_prs_nm (str, none_type): [optional]  # noqa: E501
            loa_stat_cd (str, none_type): [optional]  # noqa: E501
            loa_hist_stat_cd (str, none_type): [optional]  # noqa: E501
            loa_hs_gds_cd (str, none_type): [optional]  # noqa: E501
            org_grp_dfas_cd (str, none_type): [optional]  # noqa: E501
            loa_uic (str, none_type): [optional]  # noqa: E501
            loa_trnsn_id (str, none_type): [optional]  # noqa: E501
            loa_sub_acnt_id (str, none_type): [optional]  # noqa: E501
            loa_bet_cd (str, none_type): [optional]  # noqa: E501
            loa_fnd_ty_fg_cd (str, none_type): [optional]  # noqa: E501
            loa_bgt_ln_itm_id (str, none_type): [optional]  # noqa: E501
            loa_scrty_coop_impl_agnc_cd (str, none_type): [optional]  # noqa: E501
            loa_scrty_coop_dsgntr_cd (str, none_type): [optional]  # noqa: E501
            loa_scrty_coop_ln_itm_id (str, none_type): [optional]  # noqa: E501
            loa_agnc_dsbr_cd (str, none_type): [optional]  # noqa: E501
            loa_agnc_acntng_cd (str, none_type): [optional]  # noqa: E501
            loa_fnd_cntr_id (str, none_type): [optional]  # noqa: E501
            loa_cst_cntr_id (str, none_type): [optional]  # noqa: E501
            loa_prj_id (str, none_type): [optional]  # noqa: E501
            loa_actvty_id (str, none_type): [optional]  # noqa: E501
            loa_cst_cd (str, none_type): [optional]  # noqa: E501
            loa_wrk_ord_id (str, none_type): [optional]  # noqa: E501
            loa_fncl_ar_id (str, none_type): [optional]  # noqa: E501
            loa_scrty_coop_cust_cd (str, none_type): [optional]  # noqa: E501
            loa_end_fy_tx (int, none_type): [optional]  # noqa: E501
            loa_bg_fy_tx (int, none_type): [optional]  # noqa: E501
            loa_bgt_rstr_cd (str, none_type): [optional]  # noqa: E501
            loa_bgt_sub_act_cd (str, none_type): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
            valid_loa_for_tac (bool, none_type): [optional]  # noqa: E501
            valid_hhg_program_code_for_loa (bool, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """LineOfAccounting - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            loa_sys_id (str, none_type): [optional]  # noqa: E501
            loa_dpt_id (str, none_type): [optional]  # noqa: E501
            loa_tnsfr_dpt_nm (str, none_type): [optional]  # noqa: E501
            loa_baf_id (str, none_type): [optional]  # noqa: E501
            loa_trsy_sfx_tx (str, none_type): [optional]  # noqa: E501
            loa_maj_clm_nm (str, none_type): [optional]  # noqa: E501
            loa_op_agncy_id (str, none_type): [optional]  # noqa: E501
            loa_allt_sn_id (str, none_type): [optional]  # noqa: E501
            loa_pgm_elmnt_id (str, none_type): [optional]  # noqa: E501
            loa_tsk_bdgt_sbln_tx (str, none_type): [optional]  # noqa: E501
            loa_df_agncy_alctn_rcpnt_id (str, none_type): [optional]  # noqa: E501
            loa_jb_ord_nm (str, none_type): [optional]  # noqa: E501
            loa_sbaltmt_rcpnt_id (str, none_type): [optional]  # noqa: E501
            loa_wk_cntr_rcpnt_nm (str, none_type): [optional]  # noqa: E501
            loa_maj_rmbsmt_src_id (str, none_type): [optional]  # noqa: E501
            loa_dtl_rmbsmt_src_id (str, none_type): [optional]  # noqa: E501
            loa_cust_nm (str, none_type): [optional]  # noqa: E501
            loa_obj_cls_id (str, none_type): [optional]  # noqa: E501
            loa_srv_src_id (str, none_type): [optional]  # noqa: E501
            loa_spcl_intr_id (str, none_type): [optional]  # noqa: E501
            loa_bdgt_acnt_cls_nm (str, none_type): [optional]  # noqa: E501
            loa_doc_id (str, none_type): [optional]  # noqa: E501
            loa_cls_ref_id (str, none_type): [optional]  # noqa: E501
            loa_instl_acntg_act_id (str, none_type): [optional]  # noqa: E501
            loa_lcl_instl_id (str, none_type): [optional]  # noqa: E501
            loa_fms_trnsactn_id (str, none_type): [optional]  # noqa: E501
            loa_dsc_tx (str, none_type): [optional]  # noqa: E501
            loa_bgn_dt (date, none_type): [optional]  # noqa: E501
            loa_end_dt (date, none_type): [optional]  # noqa: E501
            loa_fnct_prs_nm (str, none_type): [optional]  # noqa: E501
            loa_stat_cd (str, none_type): [optional]  # noqa: E501
            loa_hist_stat_cd (str, none_type): [optional]  # noqa: E501
            loa_hs_gds_cd (str, none_type): [optional]  # noqa: E501
            org_grp_dfas_cd (str, none_type): [optional]  # noqa: E501
            loa_uic (str, none_type): [optional]  # noqa: E501
            loa_trnsn_id (str, none_type): [optional]  # noqa: E501
            loa_sub_acnt_id (str, none_type): [optional]  # noqa: E501
            loa_bet_cd (str, none_type): [optional]  # noqa: E501
            loa_fnd_ty_fg_cd (str, none_type): [optional]  # noqa: E501
            loa_bgt_ln_itm_id (str, none_type): [optional]  # noqa: E501
            loa_scrty_coop_impl_agnc_cd (str, none_type): [optional]  # noqa: E501
            loa_scrty_coop_dsgntr_cd (str, none_type): [optional]  # noqa: E501
            loa_scrty_coop_ln_itm_id (str, none_type): [optional]  # noqa: E501
            loa_agnc_dsbr_cd (str, none_type): [optional]  # noqa: E501
            loa_agnc_acntng_cd (str, none_type): [optional]  # noqa: E501
            loa_fnd_cntr_id (str, none_type): [optional]  # noqa: E501
            loa_cst_cntr_id (str, none_type): [optional]  # noqa: E501
            loa_prj_id (str, none_type): [optional]  # noqa: E501
            loa_actvty_id (str, none_type): [optional]  # noqa: E501
            loa_cst_cd (str, none_type): [optional]  # noqa: E501
            loa_wrk_ord_id (str, none_type): [optional]  # noqa: E501
            loa_fncl_ar_id (str, none_type): [optional]  # noqa: E501
            loa_scrty_coop_cust_cd (str, none_type): [optional]  # noqa: E501
            loa_end_fy_tx (int, none_type): [optional]  # noqa: E501
            loa_bg_fy_tx (int, none_type): [optional]  # noqa: E501
            loa_bgt_rstr_cd (str, none_type): [optional]  # noqa: E501
            loa_bgt_sub_act_cd (str, none_type): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
            valid_loa_for_tac (bool, none_type): [optional]  # noqa: E501
            valid_hhg_program_code_for_loa (bool, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")