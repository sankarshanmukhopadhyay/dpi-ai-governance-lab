from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("dpi-ai-governance-lab")
except PackageNotFoundError:  # editable / source tree
    __version__ = "0.4.1"
