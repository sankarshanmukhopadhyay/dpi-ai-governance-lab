from pathlib import Path
from urllib.parse import urlparse
import sys
import yaml

PATH = Path("corpora/digital-statecraft-dpi/corpus.yaml")


def main() -> int:
    data = yaml.safe_load(PATH.read_text(encoding="utf-8"))
    errors = []
    if data.get("status") != "frozen":
        errors.append("corpus status must be frozen")
    items = data.get("items", [])
    if len(items) != 6:
        errors.append(f"expected 6 first-wave items, found {len(items)}")
    ids = [item.get("id") for item in items]
    if len(ids) != len(set(ids)):
        errors.append("duplicate corpus item IDs")
    urls = [item.get("canonical_url") for item in items]
    if len(urls) != len(set(urls)):
        errors.append("duplicate canonical URLs")
    for item in items:
        for key in ("id", "title", "canonical_url", "author", "published_on", "themes", "inclusion_rationale", "evaluation_status"):
            if not item.get(key):
                errors.append(f"{item.get('id', '<unknown>')}: missing {key}")
        parsed = urlparse(str(item.get("canonical_url", "")))
        if parsed.scheme != "https" or parsed.netloc != "digitalstatecraft.substack.com":
            errors.append(f"{item.get('id')}: canonical URL must use digitalstatecraft.substack.com over https")
        if item.get("evaluation_status") != "pending":
            errors.append(f"{item.get('id')}: evaluation_status must remain pending in corpus-freeze PR")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 2
    print(f"Digital Statecraft corpus OK: {len(items)} frozen items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
