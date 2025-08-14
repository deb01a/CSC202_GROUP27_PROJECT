# Configuration File Manager – Group 27

A modular configuration file manager that can parse, validate, and manage configuration files in **INI**, **JSON**, and **XML** formats.  
This tool is designed to be **extensible**, **easy to use**, and **developer-friendly**.

---

## ✨ Features
- **Multi-format parsing**: INI, JSON, XML support.
- **Validation**: Validate configs against JSON schema files.
- **Modular design**: Easy to add new file formats or validation rules.
- **CLI interface**: Run operations directly from the command line.
- **Example files included** for quick testing.

---

## 📂 Project Structure
config_manager_Group27/
│
├── pycache/ # Python cache files
├── example_files/ # Sample config and schema files
│ ├── config.ini
│ ├── config.json
│ ├── config.xml
│ ├── config_schema.json
│ └── schema.json
├── cli.py # Command-line interface
├── ini_parser.py # INI file parser
├── json_parser.py # JSON file parser
├── xml_parser.py # XML file parser
├── manager.py # Main manager logic
├── parser_base.py # Base parser class
├── utils.py # Helper functions
├── validator.py # Validation logic
├── main.py # Entry point
└── README.md # This file


---

## 🚀 How to Use
1. Modify or create your own config files in **INI**, **JSON**, or **XML**.
2. Use the CLI to parse, validate, or display configurations:
   ```bash
   python cli.py parse example_files/config.json
   python cli.py validate example_files/config.json example_files/config_schema.json

Authors

Group 27 – CSC202 Project

Adebola Ajagbe Benjamin – 2023005749 (@deb01a)

Abdulsemiu Zainab Odunayo – 2023007472 (Leader)

Okelola Malik Oyewale – 2023003935

Salahudeen Abdulbasit Alade – 2023008958

Oladipo Isreal Omotola – 2023007292
