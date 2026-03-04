#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CVES_FILE = ROOT / "data" / "cves.txt"
BADGE_FILE = ROOT / "data" / "cve_badge.json"
META_FILE = ROOT / "data" / "cve.json"

def main():
    cves = []
    for line in CVES_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        cves.append(line)

    count = len(cves)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    badge = {
        "schemaVersion": 1,
        "label": "CVEs",
        "message": str(count),
        "color": "informational"
    }

    meta = {
        "count": count,
        "last_updated_utc": now,
        "cves": cves
    }

    BADGE_FILE.parent.mkdir(parents=True, exist_ok=True)
    BADGE_FILE.write_text(json.dumps(badge, indent=2) + "\n", encoding="utf-8")
    META_FILE.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
