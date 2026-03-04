#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CVES_FILE = ROOT / "data" / "cves.txt"
BADGE_FILE = ROOT / "data" / "cve_badge.json"
META_FILE = ROOT / "data" / "cve.json"

def main():
    if not CVES_FILE.exists():
        raise SystemExit(f"Missing {CVES_FILE}")

    cves = []
    for line in CVES_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        cves.append(line)

    count = len(cves)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Shields "endpoint" schema
    badge = {
        "schemaVersion": 1,
        "label": "CVEs",
        "message": str(count),
        "color": "informational"
    }

    meta = {
        "cves": cves,
        "count": count,
        "last_updated_utc": now
    }

    BADGE_FILE.parent.mkdir(parents=True, exist_ok=True)
    BADGE_FILE.write_text(json.dumps(badge, indent=2) + "\n", encoding="utf-8")
    META_FILE.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

    print(f"Generated: {BADGE_FILE} (count={count})")
    print(f"Generated: {META_FILE}")

if __name__ == "__main__":
    main()
