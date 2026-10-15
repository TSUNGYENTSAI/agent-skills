"""Teaching fixture: summarize non-negative integer amounts from JSON stdin."""

import json
import sys


def summarize(payload):
    if not isinstance(payload, list):
        raise ValueError("input must be a JSON array")
    if any(type(amount) is not int or amount < 0 for amount in payload):
        raise ValueError("amounts must be non-negative integers")
    return {"count": len(payload), "total": sum(payload)}


def main():
    try:
        result = summarize(json.load(sys.stdin))
    except (ValueError, RecursionError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 1
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
