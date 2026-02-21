#!/usr/bin/env python3
"""Shared validation helpers.

This repo intentionally keeps validators lightweight (no heavy framework),
so contributors can run them with a stock Python install.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional


@dataclass
class ValidationResult:
    ok: bool
    errors: List[str]
    warnings: List[str]

    def exit_code(self) -> int:
        return 0 if self.ok else 1


def as_list(x) -> list:
    if x is None:
        return []
    return x if isinstance(x, list) else [x]


def add_error(errors: List[str], msg: str, path: Optional[str] = None) -> None:
    errors.append(f"{path}: {msg}" if path else msg)


def add_warning(warnings: List[str], msg: str, path: Optional[str] = None) -> None:
    warnings.append(f"{path}: {msg}" if path else msg)


def print_result(result: ValidationResult) -> None:
    """Human-friendly output for CLI."""
    if result.ok:
        print("OK")
        if result.warnings:
            print("Warnings:")
            for w in result.warnings:
                print(f"- {w}")
        return

    print("FAILED")
    if result.errors:
        print("Errors:")
        for e in result.errors:
            print(f"- {e}")
    if result.warnings:
        print("Warnings:")
        for w in result.warnings:
            print(f"- {w}")
