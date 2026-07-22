from dotenv import load_dotenv
import os
from mem0 import MemoryClient
import json
from collections import defaultdict

load_dotenv()

api_key = os.getenv("MEM0_API_KEY")

if not api_key:
    raise ValueError("❌ MEM0_API_KEY not found in .env")

mem0 = MemoryClient(api_key=api_key)

user_name = "Vikas"


def get_schema():
    # ✅ FIXED QUERY
    results = mem0.search("user information preferences details", user_id=user_name)

    print("\n📦 Raw Results:\n")
    print(json.dumps(results, indent=4))  # debug

    schema = defaultdict(set)

    for item in results:
        for key, value in item.items():
            schema[key].add(type(value).__name__)

    schema_clean = {k: list(v) for k, v in schema.items()}

    print("\n🔍 Inferred Schema:\n")
    print(json.dumps(schema_clean, indent=4))

    return schema_clean


if __name__ == "__main__":
    get_schema()