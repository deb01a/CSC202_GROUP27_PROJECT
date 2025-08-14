# Returns the appropriate parser based on file extension.
from json_parser import JSONConfigParser
from ini_parser import INIConfigParser
from xml_parser import XMLConfigParser
from parser_base import ConfigParserBase

def get_parser(path: str) -> ConfigParserBase:
    if path.endswith('.json'):
        return JSONConfigParser()
    elif path.endswith('.ini'):
        return INIConfigParser()
    elif path.endswith('.xml'):
        return XMLConfigParser()
    else:
        raise ValueError("Unsupported config format.")
