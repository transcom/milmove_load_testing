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


def lazy_import():
    from ghc_client.model.affiliation import Affiliation
    from ghc_client.model.customer import Customer
    from ghc_client.model.dept_indicator import DeptIndicator
    from ghc_client.model.duty_location import DutyLocation
    from ghc_client.model.entitlements import Entitlements
    from ghc_client.model.grade import Grade
    from ghc_client.model.orders_type import OrdersType
    from ghc_client.model.orders_type_detail import OrdersTypeDetail
    globals()['Affiliation'] = Affiliation
    globals()['Customer'] = Customer
    globals()['DeptIndicator'] = DeptIndicator
    globals()['DutyLocation'] = DutyLocation
    globals()['Entitlements'] = Entitlements
    globals()['Grade'] = Grade
    globals()['OrdersType'] = OrdersType
    globals()['OrdersTypeDetail'] = OrdersTypeDetail


class Order(ModelNormal):
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
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
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
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'customer_id': (str,),  # noqa: E501
            'customer': (Customer,),  # noqa: E501
            'move_code': (str,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'grade': (Grade,),  # noqa: E501
            'agency': (Affiliation,),  # noqa: E501
            'entitlement': (Entitlements,),  # noqa: E501
            'destination_duty_location': (DutyLocation,),  # noqa: E501
            'origin_duty_location': (DutyLocation,),  # noqa: E501
            'move_task_order_id': (str,),  # noqa: E501
            'uploaded_order_id': (str,),  # noqa: E501
            'uploaded_amended_order_id': (str, none_type,),  # noqa: E501
            'amended_orders_acknowledged_at': (datetime, none_type,),  # noqa: E501
            'order_number': (str, none_type,),  # noqa: E501
            'order_type': (OrdersType,),  # noqa: E501
            'order_type_detail': (OrdersTypeDetail,),  # noqa: E501
            'date_issued': (date,),  # noqa: E501
            'report_by_date': (date,),  # noqa: E501
            'department_indicator': (DeptIndicator,),  # noqa: E501
            'tac': (str, none_type,),  # noqa: E501
            'sac': (str, none_type,),  # noqa: E501
            'nts_tac': (str, none_type,),  # noqa: E501
            'nts_sac': (str, none_type,),  # noqa: E501
            'has_dependents': (bool,),  # noqa: E501
            'spouse_has_pro_gear': (bool,),  # noqa: E501
            'supply_and_services_cost_estimate': (str,),  # noqa: E501
            'packing_and_shipping_instructions': (str,),  # noqa: E501
            'method_of_payment': (str,),  # noqa: E501
            'naics': (str,),  # noqa: E501
            'e_tag': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'customer_id': 'customerID',  # noqa: E501
        'customer': 'customer',  # noqa: E501
        'move_code': 'moveCode',  # noqa: E501
        'first_name': 'first_name',  # noqa: E501
        'last_name': 'last_name',  # noqa: E501
        'grade': 'grade',  # noqa: E501
        'agency': 'agency',  # noqa: E501
        'entitlement': 'entitlement',  # noqa: E501
        'destination_duty_location': 'destinationDutyLocation',  # noqa: E501
        'origin_duty_location': 'originDutyLocation',  # noqa: E501
        'move_task_order_id': 'moveTaskOrderID',  # noqa: E501
        'uploaded_order_id': 'uploaded_order_id',  # noqa: E501
        'uploaded_amended_order_id': 'uploadedAmendedOrderID',  # noqa: E501
        'amended_orders_acknowledged_at': 'amendedOrdersAcknowledgedAt',  # noqa: E501
        'order_number': 'order_number',  # noqa: E501
        'order_type': 'order_type',  # noqa: E501
        'order_type_detail': 'order_type_detail',  # noqa: E501
        'date_issued': 'date_issued',  # noqa: E501
        'report_by_date': 'report_by_date',  # noqa: E501
        'department_indicator': 'department_indicator',  # noqa: E501
        'tac': 'tac',  # noqa: E501
        'sac': 'sac',  # noqa: E501
        'nts_tac': 'ntsTac',  # noqa: E501
        'nts_sac': 'ntsSac',  # noqa: E501
        'has_dependents': 'has_dependents',  # noqa: E501
        'spouse_has_pro_gear': 'spouse_has_pro_gear',  # noqa: E501
        'supply_and_services_cost_estimate': 'supplyAndServicesCostEstimate',  # noqa: E501
        'packing_and_shipping_instructions': 'packingAndShippingInstructions',  # noqa: E501
        'method_of_payment': 'methodOfPayment',  # noqa: E501
        'naics': 'naics',  # noqa: E501
        'e_tag': 'eTag',  # noqa: E501
    }

    read_only_vars = {
        'first_name',  # noqa: E501
        'last_name',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Order - a model defined in OpenAPI

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
            customer_id (str): [optional]  # noqa: E501
            customer (Customer): [optional]  # noqa: E501
            move_code (str): [optional]  # noqa: E501
            first_name (str): [optional]  # noqa: E501
            last_name (str): [optional]  # noqa: E501
            grade (Grade): [optional]  # noqa: E501
            agency (Affiliation): [optional]  # noqa: E501
            entitlement (Entitlements): [optional]  # noqa: E501
            destination_duty_location (DutyLocation): [optional]  # noqa: E501
            origin_duty_location (DutyLocation): [optional]  # noqa: E501
            move_task_order_id (str): [optional]  # noqa: E501
            uploaded_order_id (str): [optional]  # noqa: E501
            uploaded_amended_order_id (str, none_type): [optional]  # noqa: E501
            amended_orders_acknowledged_at (datetime, none_type): [optional]  # noqa: E501
            order_number (str, none_type): [optional]  # noqa: E501
            order_type (OrdersType): [optional]  # noqa: E501
            order_type_detail (OrdersTypeDetail): [optional]  # noqa: E501
            date_issued (date): [optional]  # noqa: E501
            report_by_date (date): [optional]  # noqa: E501
            department_indicator (DeptIndicator): [optional]  # noqa: E501
            tac (str, none_type): [optional]  # noqa: E501
            sac (str, none_type): [optional]  # noqa: E501
            nts_tac (str, none_type): [optional]  # noqa: E501
            nts_sac (str, none_type): [optional]  # noqa: E501
            has_dependents (bool): [optional]  # noqa: E501
            spouse_has_pro_gear (bool): [optional]  # noqa: E501
            supply_and_services_cost_estimate (str): [optional]  # noqa: E501
            packing_and_shipping_instructions (str): [optional]  # noqa: E501
            method_of_payment (str): [optional]  # noqa: E501
            naics (str): [optional]  # noqa: E501
            e_tag (str): [optional]  # noqa: E501
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
        """Order - a model defined in OpenAPI

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
            customer_id (str): [optional]  # noqa: E501
            customer (Customer): [optional]  # noqa: E501
            move_code (str): [optional]  # noqa: E501
            first_name (str): [optional]  # noqa: E501
            last_name (str): [optional]  # noqa: E501
            grade (Grade): [optional]  # noqa: E501
            agency (Affiliation): [optional]  # noqa: E501
            entitlement (Entitlements): [optional]  # noqa: E501
            destination_duty_location (DutyLocation): [optional]  # noqa: E501
            origin_duty_location (DutyLocation): [optional]  # noqa: E501
            move_task_order_id (str): [optional]  # noqa: E501
            uploaded_order_id (str): [optional]  # noqa: E501
            uploaded_amended_order_id (str, none_type): [optional]  # noqa: E501
            amended_orders_acknowledged_at (datetime, none_type): [optional]  # noqa: E501
            order_number (str, none_type): [optional]  # noqa: E501
            order_type (OrdersType): [optional]  # noqa: E501
            order_type_detail (OrdersTypeDetail): [optional]  # noqa: E501
            date_issued (date): [optional]  # noqa: E501
            report_by_date (date): [optional]  # noqa: E501
            department_indicator (DeptIndicator): [optional]  # noqa: E501
            tac (str, none_type): [optional]  # noqa: E501
            sac (str, none_type): [optional]  # noqa: E501
            nts_tac (str, none_type): [optional]  # noqa: E501
            nts_sac (str, none_type): [optional]  # noqa: E501
            has_dependents (bool): [optional]  # noqa: E501
            spouse_has_pro_gear (bool): [optional]  # noqa: E501
            supply_and_services_cost_estimate (str): [optional]  # noqa: E501
            packing_and_shipping_instructions (str): [optional]  # noqa: E501
            method_of_payment (str): [optional]  # noqa: E501
            naics (str): [optional]  # noqa: E501
            e_tag (str): [optional]  # noqa: E501
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
