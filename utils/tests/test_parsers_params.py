# -*- coding: utf-8 -*-
# flake8: noqa
""" Assertions and parameters for the test_parsers.py test cases """

# test_api definitions:
APPLE_DEF = {
    "type": "string",
    "enum": ["Granny Smith", "Red Delicious", "Pink Lady", "Braeburn", "Fuji", "Honeycrisp",],
}
TREE_DEF = {
    "type": "object",
    "discriminator": "treeType",
    "properties": {
        "id": {"type": "string", "format": "uuid", "readOnly": True,},
        "datePlanted": {"type": "string", "format": "date",},
        "timeMilitaryPlanted": {"type": "string", "pattern": "\\d{4}Z",},
        "treeType": {"type": "string", "enum": ["AppleTree", "CherryTree", "LemonTree", "PeachTree",]},
    },
}
CHERRY_TREE_DEF = {
    "allOf": [
        TREE_DEF,
        {
            "type": "object",
            "properties": {
                "cherryBunchSize": {"type": "integer", "minimum": 1, "maximum": 3, "default": 2},
                "cherryTaste": {"type": "string", "enum": ["sweet", "sour"]},
            },
        },
    ]
}
APPLE_TREE_DEF = {
    "allOf": [
        TREE_DEF,
        {"type": "object", "properties": {"apples": {"type": "array", "items": APPLE_DEF,},}, "required": ["apples"]},
    ]
}
APPLE_TREES_DEF = {
    "type": "array",
    "items": APPLE_TREE_DEF,
}
ADDRESS_DEF = {
    "type": "object",
    "properties": {
        "streetAddress1": {"type": "string"},
        "streetAddress2": {"type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "postalCode": {"type": "string", "format": "zip", "pattern": "^(\\d{5}([\\-]\\d{4})?)$"},
        "country": {"type": "string", "default": "USA"},
    },
    "required": ["streetAddress1", "city", "state", "postalCode"],
}
FARMER_DEF = {
    "type": "object",
    "properties": {
        "id": {"type": "string", "format": "uuid", "readOnly": True},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "phone": {"type": "string", "format": "telephone", "pattern": "^[2-9]\\d{2}-\\d{3}-\\d{4}$"},
        "favoriteDateTime": {"type": "string", "format": "date-time"},
        "likesApples": {"type": "boolean"},
    },
    "required": ["firstName"],
}
ORCHARD_DEF = {
    "type": "object",
    "properties": {
        "id": {"type": "string", "format": "uuid", "readOnly": True,},
        "address": ADDRESS_DEF,
        "farmer": FARMER_DEF,
        "trees": {"type": "array", "items": TREE_DEF, "minItems": 1, "maxItems": 30,},
    },
}

# test_api responses:
APPLE_TREE_GET_200 = {
    "description": "OK",
    "schema": APPLE_TREE_DEF,
}
APPLE_TREE_GET_404 = {"description": "Couldn't find the apple tree."}
APPLE_TREE_DELETE_200 = {"description": "OK"}
FARMERS_POST_201 = {
    "description": "OK",
    "schema": FARMER_DEF,
}
FARMER_PUT_422 = {
    "description": "The input was invalid.",
    "schema": {
        "allOf": [
            {"type": "object", "properties": {"message": {"type": "string"}}},
            {
                "type": "object",
                "properties": {
                    "invalidFields": {
                        "type": "object",
                        "additionalProperties": {
                            "description": "List of errors for the field",
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    }
                },
                "required": ["invalidFields"],
            },
        ]
    },
}

# test_api endpoints:
APPLE_TREE_GET = {
    "summary": "Get a specific apple tree.",
    "responses": {"200": APPLE_TREE_GET_200, "404": APPLE_TREE_GET_404,},
}
APPLE_TREE_DELETE = {"summary": "Delete a specific apple tree.", "responses": {"200": APPLE_TREE_DELETE_200}}
ORCHARDS_POST = {
    "summary": "Create an orchard of fruit trees.",
    "parameters": [{"in": "body", "name": "body", "required": True, "schema": ORCHARD_DEF,}],
    "responses": {"201": {"description": "OK", "schema": ORCHARD_DEF,}},
}
