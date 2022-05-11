schema_NewEmployee = {
    "required": [
        "registration", "name", "surname", "role", "leader", "salary", "password", "status"
    ],
    "properties": {
        "registration": {
            "type" : "integer"
        },
        "name": {
            "type": "string"
        },
        "surname": {
            "type": "string"
        },
        "role": {
            "type": "string"
        },
        "leader":{
            "type": "string"
        },
        "salary": {
            "type": "number"
        },
        "password": {
            "type": "string"
        },
        "status": {
            "type": "boolean"
        }
    },
    "additionalProperties": False
}
