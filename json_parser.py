# Handles reading and writing of JSON configuration files.
import json
from typing import Dict, Any
from parser_base import ConfigParserBase

class JSONConfigParser(ConfigParserBase):
    def load(self, path: str) -> Dict[str, Any]:
        with open(path, 'r') as f:
            return json.load(f)

    def save(self, path: str, config: Dict[str, Any]):
        with open(path, 'w') as f:
            json.dump(config, f, indent=4)
