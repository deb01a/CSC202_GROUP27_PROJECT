print("CLI started")
# Handles command-line argument parsing and delegates functionality to the appropriate modules.

import argparse
import json
import sys

from utils import get_parser
from validator import ConfigValidator
from manager import merge_configs, detect_conflicts, generate_template, analyze_config

def main():
    parser = argparse.ArgumentParser(description="Configuration Management CLI Tool")
    parser.add_argument("action", choices=["validate", "merge", "conflicts", "template", "analyze"])
    parser.add_argument("--config1", required=True)
    parser.add_argument("--config2")
    parser.add_argument("--schema")
    parser.add_argument("--output")

    args = parser.parse_args()

    try:
        parser1 = get_parser(args.config1)
        config1 = parser1.load(args.config1)

        config2 = {}
        if args.config2:
            parser2 = get_parser(args.config2)
            config2 = parser2.load(args.config2)

        if args.action == "validate":
            if not args.schema:
                print("Schema required for validation.")
                sys.exit(1)
            with open(args.schema) as f:
                schema = json.load(f)
            validator = ConfigValidator(schema)
            valid, errors = validator.validate(config1)
            print("Configuration is valid." if valid else "Validation errors:\n" + "\n".join("- " + e for e in errors))

        elif args.action == "merge":
            merged = merge_configs(config1, config2)
            if args.output:
                parser1.save(args.output, merged)
            print("Merged configuration:")
            print(json.dumps(merged, indent=4))

        elif args.action == "conflicts":
            conflicts = detect_conflicts(config1, config2)
            print("Conflicts found:" if conflicts else "No conflicts detected.")
            for c in conflicts:
                print("-", c)

        elif args.action == "template":
            if not args.schema:
                print("Schema required to generate template.")
                sys.exit(1)
            with open(args.schema) as f:
                schema = json.load(f)
            template = generate_template(schema)
            if args.output:
                parser1.save(args.output, template)
            print("Template generated.")

        elif args.action == "analyze":
            suggestions = analyze_config(config1)
            print("Analysis suggestions:" if suggestions else "No suggestions.")
            for s in suggestions:
                print("-", s)

    except Exception as e:
        print("Error:", str(e))
        sys.exit(1)
if __name__ == "__main__":
    main()

