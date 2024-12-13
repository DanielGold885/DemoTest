import json
from jsonschema import validate, exceptions


class JSONSchemaValidator:
    @staticmethod
    def validate_schema(response_json, schema_file_path):
        """
        Validates the response JSON against the schema.

        :param response_json: The JSON response to validate
        :param schema_file_path: Path to the schema file
        :return: None if valid, raises an exception if invalid
        """
        try:
            # Load the schema from the file
            with open(schema_file_path, 'r') as schema_file:
                schema = json.load(schema_file)

            # Validate the response JSON against the schema
            validate(instance=response_json, schema=schema)
            print("INFO: JSON response matches the schema.")
        except exceptions.ValidationError as e:
            print(f"ERROR: JSON response does not match the schema: {e.message}")
            raise
        except FileNotFoundError as e:
            print(f"ERROR: Schema file not found: {e}")
            raise
