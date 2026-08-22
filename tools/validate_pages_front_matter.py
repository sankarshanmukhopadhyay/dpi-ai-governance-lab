from __future__ import annotations

from pathlib import Path
import yaml


def parse_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening front matter delimiter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing closing front matter delimiter")
    data = yaml.safe_load(text[4:end]) or {}
    if not isinstance(data, dict):
        raise ValueError("front matter must be a mapping")
    return data


def main() -> int:
    manifest = yaml.safe_load(Path("docs/pages-manifest.yaml").read_text(encoding="utf-8"))
    failures: list[str] = []
    for item in manifest.get("pages", []):
        path = Path(item)
        if not path.exists():
            failures.append(f"{item}: missing")
            continue
        try:
            front = parse_front_matter(path)
        except ValueError as exc:
            failures.append(f"{item}: {exc}")
            continue
        if front.get("layout") != "default":
            failures.append(f"{item}: layout must be default")
        if not str(front.get("title", "")).strip():
            failures.append(f"{item}: title is required")
    if failures:
        print("Pages front matter validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 2
    print(f"Pages front matter OK: {len(manifest.get('pages', []))} rendered pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
