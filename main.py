import argparse
import json
from pipeline import plan_pipeline

def main():
    parser = argparse.ArgumentParser(description="Generate a function call plan from a user query.")
    parser.add_argument("query", type=str, help="User natural language query")
    args = parser.parse_args()
    plan = plan_pipeline(args.query)
    print(json.dumps(plan, indent=2))

if __name__ == "__main__":
    main() 