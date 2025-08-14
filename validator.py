# Implements the ConfigValidator class for schema-based validation of config files.
from typing import Dict, Any, Tuple, List

class ConfigValidator:
    def __init__(self, schema: Dict[str, Dict[str, Any]]):
        self.schema = schema

    def validate(self, config: Dict[str, Any]) -> Tuple[bool, List[str]]:
        errors = []
        for key, rules in self.schema.items():
            value = config.get(key)
            if rules.get('required') and value is None:
                errors.append(f"{key} is required.")
                continue

            if value is not None:
                typ = rules.get('type')
                if typ:
                    try:
                        if typ == 'int':
                            value = int(value)
                        elif typ == 'float':
                            value = float(value)
                    except ValueError:
                        errors.append(f"{key} must be a {typ}.")
                        continue

                if 'min' in rules and float(value) < rules['min']:
                    errors.append(f"{key} must be >= {rules['min']}")
                if 'max' in rules and float(value) > rules['max']:
                    errors.append(f"{key} must be <= {rules['max']}")
        return len(errors) == 0, errors
