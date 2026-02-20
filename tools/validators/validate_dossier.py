#!/usr/bin/env python3
import json, sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("usage: validate_dossier.py <dossier.json>")
        return 2
    p = Path(sys.argv[1])
    data = json.loads(p.read_text(encoding="utf-8"))
    required = ["version","system","tier","data","model","evaluation","monitoring","escalation","redress"]
    missing = [k for k in required if k not in data]
    if missing:
        print("Missing fields:", ", ".join(missing))
        return 1
    print("OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
