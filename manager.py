# Contains business logic for merging, conflict detection, template generation, and analysis.
from typing import Dict, Any, List

def merge_configs(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    merged = base.copy()
    merged.update(override)
    return merged

def detect_conflicts(config1: Dict[str, Any], config2: Dict[str, Any]) -> List[str]:
    return [f"Conflict on '{k}': '{config1[k]}' != '{config2[k]}'"
            for k in config1 if k in config2 and config1[k] != config2[k]]

def generate_template(schema: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    return {key: "" for key in schema}

def analyze_config(config: Dict[str, Any]) -> List[str]:
    suggestions = []
    if 'timeout' in config and int(config['timeout']) > 60:
        suggestions.append("Consider lowering 'timeout' to improve responsiveness.")
    if config.get('log_level') == 'debug':
        suggestions.append("Avoid using 'debug' in production.")
    return suggestions
