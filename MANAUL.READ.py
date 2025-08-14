First, open CMD and navigate to your project root:

cd path\to\config_manager_Group27
Now you can use the following commands:

1. Validate a config file

python cli.py validate --config1 example_files/config.json --schema example_files/config_schema.json

2. Merge two config files


python cli.py merge --config1 example_files/config.json --config2 example_files/config2.json --output merged_config.json

3. Detect conflicts between two files

python cli.py conflicts --config1 example_files/config.json --config2 example_files/config2.json

4. Generate a config template from schema

python cli.py template --config1 example_files/config.json --schema example_files/config_schema.json --output template_config.json

5. Analyze the config file for issues or suggestions

python cli.py analyze --config1 example_files/config.json

Notes:
These commands assume all input files are in example_files/

All Python modules are in the root (same folder as cli.py)

Replace filenames if you renamed them (schema.json → config_schema.json)

