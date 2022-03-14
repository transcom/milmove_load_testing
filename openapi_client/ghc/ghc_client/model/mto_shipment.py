"""
    move.mil API

    The API for move.mil  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dp3@truss.works
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
    from ghc_client.model.address import Address
    from ghc_client.model.destination_type import DestinationType
    from ghc_client.model.loa_type import LOAType
    from ghc_client.model.mto_agents import MTOAgents
    from ghc_client.model.mto_service_items import MTOServiceItems
    from ghc_client.model.mto_shipment_status import MTOShipmentStatus
    from ghc_client.model.mto_shipment_type import MTOShipmentType
    from ghc_client.model.reweigh import Reweigh
    from ghc_client.model.sit_extensions import SITExtensions
    from ghc_client.model.sit_status import SITStatus
    from ghc_client.model.storage_facility import StorageFacility
    globals()['Address'] = Address
    globals()['DestinationType'] = DestinationType
    globals()['LOAType'] = LOAType
    globals()['MTOAgents'] = MTOAgents
    globals()['MTOServiceItems'] = MTOServiceItems
    globals()['MTOShipmentStatus'] = MTOShipmentStatus
    globals()['MTOShipmentType'] = MTOShipmentType
    globals()['Reweigh'] = Reweigh
    globals()['SITExtensions'] = SITExtensions
    globals()['SITStatus'] = SITStatus
    globals()['StorageFacility'] = StorageFacility


class MTOShipment(ModelNormal):
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
            'move_task_order_id': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'deleted_at': (datetime, none_type,),  # noqa: E501
            'prime_estimated_weight': (int, none_type,),  # noqa: E501
            'prime_actual_weight': (int, none_type,),  # noqa: E501
            'calculated_billable_weight': (int, none_type,),  # noqa: E501
            'nts_recorded_weight': (int, none_type,),  # noqa: E501
            'scheduled_pickup_date': (date, none_type,),  # noqa: E501
            'requested_pickup_date': (date,),  # noqa: E501
            'actual_pickup_date': (date, none_type,),  # noqa: E501
            'requested_delivery_date': (date,),  # noqa: E501
            'approved_date': (datetime, none_type,),  # noqa: E501
            'diversion': (bool,),  # noqa: E501
            'pickup_address': (Address,),  # noqa: E501
            'destination_address': (Address,),  # noqa: E501
            'destination_type': (DestinationType,),  # noqa: E501
            'secondary_pickup_address': (Address,),  # noqa: E501
            'secondary_delivery_address': (Address,),  # noqa: E501
            'customer_remarks': (str, none_type,),  # noqa: E501
            'counselor_remarks': (str, none_type,),  # noqa: E501
            'shipment_type': (MTOShipmentType,),  # noqa: E501
            'status': (MTOShipmentStatus,),  # noqa: E501
            'rejection_reason': (str, none_type,),  # noqa: E501
            'reweigh': (Reweigh,),  # noqa: E501
            'mto_agents': (MTOAgents,),  # noqa: E501
            'mto_service_items': (MTOServiceItems,),  # noqa: E501
            'sit_days_allowance': (int, none_type,),  # noqa: E501
            'sit_extensions': (SITExtensions,),  # noqa: E501
            'sit_status': (SITStatus,),  # noqa: E501
            'e_tag': (str,),  # noqa: E501
            'billable_weight_cap': (int, none_type,),  # noqa: E501
            'billable_weight_justification': (str, none_type,),  # noqa: E501
            'tac_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'sac_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'uses_external_vendor': (bool,),  # noqa: E501
            'service_order_number': (str, none_type,),  # noqa: E501
            'storage_facility': (StorageFacility,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'move_task_order_id': 'moveTaskOrderID',  # noqa: E501
        'id': 'id',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'deleted_at': 'deletedAt',  # noqa: E501
        'prime_estimated_weight': 'primeEstimatedWeight',  # noqa: E501
        'prime_actual_weight': 'primeActualWeight',  # noqa: E501
        'calculated_billable_weight': 'calculatedBillableWeight',  # noqa: E501
        'nts_recorded_weight': 'ntsRecordedWeight',  # noqa: E501
        'scheduled_pickup_date': 'scheduledPickupDate',  # noqa: E501
        'requested_pickup_date': 'requestedPickupDate',  # noqa: E501
        'actual_pickup_date': 'actualPickupDate',  # noqa: E501
        'requested_delivery_date': 'requestedDeliveryDate',  # noqa: E501
        'approved_date': 'approvedDate',  # noqa: E501
        'diversion': 'diversion',  # noqa: E501
        'pickup_address': 'pickupAddress',  # noqa: E501
        'destination_address': 'destinationAddress',  # noqa: E501
        'destination_type': 'destinationType',  # noqa: E501
        'secondary_pickup_address': 'secondaryPickupAddress',  # noqa: E501
        'secondary_delivery_address': 'secondaryDeliveryAddress',  # noqa: E501
        'customer_remarks': 'customerRemarks',  # noqa: E501
        'counselor_remarks': 'counselorRemarks',  # noqa: E501
        'shipment_type': 'shipmentType',  # noqa: E501
        'status': 'status',  # noqa: E501
        'rejection_reason': 'rejectionReason',  # noqa: E501
        'reweigh': 'reweigh',  # noqa: E501
        'mto_agents': 'mtoAgents',  # noqa: E501
        'mto_service_items': 'mtoServiceItems',  # noqa: E501
        'sit_days_allowance': 'sitDaysAllowance',  # noqa: E501
        'sit_extensions': 'sitExtensions',  # noqa: E501
        'sit_status': 'sitStatus',  # noqa: E501
        'e_tag': 'eTag',  # noqa: E501
        'billable_weight_cap': 'billableWeightCap',  # noqa: E501
        'billable_weight_justification': 'billableWeightJustification',  # noqa: E501
        'tac_type': 'tacType',  # noqa: E501
        'sac_type': 'sacType',  # noqa: E501
        'uses_external_vendor': 'usesExternalVendor',  # noqa: E501
        'service_order_number': 'serviceOrderNumber',  # noqa: E501
        'storage_facility': 'storageFacility',  # noqa: E501
    }

    read_only_vars = {
        'calculated_billable_weight',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """MTOShipment - a model defined in OpenAPI

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
            move_task_order_id (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
            deleted_at (datetime, none_type): [optional]  # noqa: E501
            prime_estimated_weight (int, none_type): [optional]  # noqa: E501
            prime_actual_weight (int, none_type): [optional]  # noqa: E501
            calculated_billable_weight (int, none_type): [optional]  # noqa: E501
            nts_recorded_weight (int, none_type): The previously recorded weight for the NTS Shipment. Used for NTS Release to know what the previous primeActualWeight or billable weight was.. [optional]  # noqa: E501
            scheduled_pickup_date (date, none_type): [optional]  # noqa: E501
            requested_pickup_date (date): [optional]  # noqa: E501
            actual_pickup_date (date, none_type): [optional]  # noqa: E501
            requested_delivery_date (date): [optional]  # noqa: E501
            approved_date (datetime, none_type): [optional]  # noqa: E501
            diversion (bool): [optional]  # noqa: E501
            pickup_address (Address): [optional]  # noqa: E501
            destination_address (Address): [optional]  # noqa: E501
            destination_type (DestinationType): [optional]  # noqa: E501
            secondary_pickup_address (Address): [optional]  # noqa: E501
            secondary_delivery_address (Address): [optional]  # noqa: E501
            customer_remarks (str, none_type): [optional]  # noqa: E501
            counselor_remarks (str, none_type): The counselor can use the counselor remarks field to inform the movers about any special circumstances for this shipment. Typical examples:   * bulky or fragile items,   * weapons,   * access info for their address. Counselors enters this information when creating or editing an MTO Shipment. Optional field. . [optional]  # noqa: E501
            shipment_type (MTOShipmentType): [optional]  # noqa: E501
            status (MTOShipmentStatus): [optional]  # noqa: E501
            rejection_reason (str, none_type): [optional]  # noqa: E501
            reweigh (Reweigh): [optional]  # noqa: E501
            mto_agents (MTOAgents): [optional]  # noqa: E501
            mto_service_items (MTOServiceItems): [optional]  # noqa: E501
            sit_days_allowance (int, none_type): [optional]  # noqa: E501
            sit_extensions (SITExtensions): [optional]  # noqa: E501
            sit_status (SITStatus): [optional]  # noqa: E501
            e_tag (str): [optional]  # noqa: E501
            billable_weight_cap (int, none_type): TIO override billable weight to be used for calculations. [optional]  # noqa: E501
            billable_weight_justification (str, none_type): [optional]  # noqa: E501
            tac_type ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            sac_type ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            uses_external_vendor (bool): [optional]  # noqa: E501
            service_order_number (str, none_type): [optional]  # noqa: E501
            storage_facility (StorageFacility): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
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
        """MTOShipment - a model defined in OpenAPI

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
            move_task_order_id (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
            deleted_at (datetime, none_type): [optional]  # noqa: E501
            prime_estimated_weight (int, none_type): [optional]  # noqa: E501
            prime_actual_weight (int, none_type): [optional]  # noqa: E501
            calculated_billable_weight (int, none_type): [optional]  # noqa: E501
            nts_recorded_weight (int, none_type): The previously recorded weight for the NTS Shipment. Used for NTS Release to know what the previous primeActualWeight or billable weight was.. [optional]  # noqa: E501
            scheduled_pickup_date (date, none_type): [optional]  # noqa: E501
            requested_pickup_date (date): [optional]  # noqa: E501
            actual_pickup_date (date, none_type): [optional]  # noqa: E501
            requested_delivery_date (date): [optional]  # noqa: E501
            approved_date (datetime, none_type): [optional]  # noqa: E501
            diversion (bool): [optional]  # noqa: E501
            pickup_address (Address): [optional]  # noqa: E501
            destination_address (Address): [optional]  # noqa: E501
            destination_type (DestinationType): [optional]  # noqa: E501
            secondary_pickup_address (Address): [optional]  # noqa: E501
            secondary_delivery_address (Address): [optional]  # noqa: E501
            customer_remarks (str, none_type): [optional]  # noqa: E501
            counselor_remarks (str, none_type): The counselor can use the counselor remarks field to inform the movers about any special circumstances for this shipment. Typical examples:   * bulky or fragile items,   * weapons,   * access info for their address. Counselors enters this information when creating or editing an MTO Shipment. Optional field. . [optional]  # noqa: E501
            shipment_type (MTOShipmentType): [optional]  # noqa: E501
            status (MTOShipmentStatus): [optional]  # noqa: E501
            rejection_reason (str, none_type): [optional]  # noqa: E501
            reweigh (Reweigh): [optional]  # noqa: E501
            mto_agents (MTOAgents): [optional]  # noqa: E501
            mto_service_items (MTOServiceItems): [optional]  # noqa: E501
            sit_days_allowance (int, none_type): [optional]  # noqa: E501
            sit_extensions (SITExtensions): [optional]  # noqa: E501
            sit_status (SITStatus): [optional]  # noqa: E501
            e_tag (str): [optional]  # noqa: E501
            billable_weight_cap (int, none_type): TIO override billable weight to be used for calculations. [optional]  # noqa: E501
            billable_weight_justification (str, none_type): [optional]  # noqa: E501
            tac_type ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            sac_type ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            uses_external_vendor (bool): [optional]  # noqa: E501
            service_order_number (str, none_type): [optional]  # noqa: E501
            storage_facility (StorageFacility): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
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
