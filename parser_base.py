# Defines the base class for all config parsers (JSON, INI, XML).
from typing import Any, Dict

class ConfigParserBase:
    def load(self, path: str) -> Dict[str, Any]:
        raise NotImplementedError

    def save(self, path: str, config: Dict[str, Any]):
        raise NotImplementedError
