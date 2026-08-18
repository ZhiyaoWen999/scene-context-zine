#!/usr/bin/env python3
"""Validate a serialized Scene Context Zine v2 plan.

The linter checks structural completeness and catches common context-loss
regressions before image generation. It uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROUTE_RANGES = {
    "documentary-editorial": (0.65, 1.00),
    "multi-frame-joiner": (0.55, 1.00),
    "graphic-scene-poster": (0.40, 0.80),
    "gathered-collage": (0.25, 0.60),
}

FIELD_MODES = {
    "source-tone",
    "material-continuation",
    "neutral-paper",
    "dark-stock",
    "chromatic-stock",
    "raw-photo",
}

PALETTE_MODES = {
    "native",
    "source-amplification",
    "tonal-translation",
    "graphic-counterpoint",
}

ABSTRACTION_LEVELS = {"light", "medium", "high"}
TYPOGRAPHY_MODES = {"none", "provided", "visible-source", "authored-phrase"}

PALETTE_KEYS = {
    "background_base",
    "midtone",
    "dark_anchor",
    "light_temperature",
    "meaningful_accent",
}

DETAIL_KEYS = {"preserve", "compress", "omit", "do_not_invent"}

PROMPT_STYLE_SHORTCUTS = {
    "herbert matter",
    "david hockney",
    "hockney",
    "apartamento",
    "tokyo style",
    "armin hofmann",
    "rodchenko",
}


class Report:
    def __init__(self, source: Path) -> None:
        self.source = source
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def print(self) -> None:
        status = "FAIL" if self.errors else "PASS"
        print(f"[{status}] {self.source}")
        for message in self.errors:
            print(f"  ERROR: {message}")
        for message in self.warnings:
            print(f"  WARN:  {message}")
        if not self.errors and not self.warnings:
            print("  Scene Plan is structurally complete.")


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def require_string_list(
    report: Report,
    value: Any,
    path: str,
    *,
    minimum: int = 1,
) -> list[str]:
    if not isinstance(value, list):
        report.error(f"{path} must be a list.")
        return []
    cleaned = [item.strip() for item in value if nonempty_string(item)]
    if len(cleaned) != len(value):
        report.error(f"{path} must contain only non-empty strings.")
    if len(cleaned) < minimum:
        report.error(f"{path} requires at least {minimum} item(s).")
    return cleaned


def validate_plan(data: Any, source: Path) -> Report:
    report = Report(source)
    if not isinstance(data, dict):
        report.error("Top-level JSON value must be an object.")
        return report

    route = data.get("route")
    if route not in ROUTE_RANGES:
        report.error(
            "route must be one of: " + ", ".join(sorted(ROUTE_RANGES)) + "."
        )

    if data.get("reference_mode") != "edit-source":
        report.error(
            "reference_mode must be 'edit-source'; prompt-only reconstruction is not allowed."
        )

    core = data.get("scene_core")
    if not isinstance(core, dict):
        report.error("scene_core must be an object.")
        return report

    anchors = require_string_list(
        report, core.get("identity_anchors"), "scene_core.identity_anchors", minimum=3
    )
    if len(anchors) > 5:
        report.warn("Use three to five identity anchors; too many can dilute the lock.")

    require_string_list(
        report, core.get("spatial_invariants"), "scene_core.spatial_invariants"
    )
    require_string_list(
        report,
        core.get("context_bearing_regions"),
        "scene_core.context_bearing_regions",
    )

    palette = core.get("environmental_palette")
    if not isinstance(palette, dict):
        report.error("scene_core.environmental_palette must be an object.")
    else:
        missing = sorted(PALETTE_KEYS - set(palette))
        if missing:
            report.error(
                "scene_core.environmental_palette is missing: " + ", ".join(missing) + "."
            )
        for key in PALETTE_KEYS & set(palette):
            if not nonempty_string(palette[key]):
                report.error(f"scene_core.environmental_palette.{key} must be non-empty.")

    require_string_list(report, core.get("light_time"), "scene_core.light_time")
    require_string_list(
        report,
        core.get("material_signatures"),
        "scene_core.material_signatures",
        minimum=2,
    )

    if not nonempty_string(core.get("density_character")):
        report.error("scene_core.density_character must be a non-empty string.")

    require_string_list(report, core.get("memory_cues"), "scene_core.memory_cues")

    detail_map = core.get("detail_map")
    if not isinstance(detail_map, dict):
        report.error("scene_core.detail_map must be an object.")
    else:
        missing = sorted(DETAIL_KEYS - set(detail_map))
        if missing:
            report.error("scene_core.detail_map is missing: " + ", ".join(missing) + ".")
        for key in DETAIL_KEYS & set(detail_map):
            require_string_list(
                report,
                detail_map[key],
                f"scene_core.detail_map.{key}",
            )

    require_string_list(
        report, core.get("flexible_zones"), "scene_core.flexible_zones"
    )

    field_mode = data.get("field_tone_mode")
    if field_mode not in FIELD_MODES:
        report.error("field_tone_mode is missing or unsupported.")

    palette_mode = data.get("palette_mode")
    if palette_mode not in PALETTE_MODES:
        report.error("palette_mode is missing or unsupported.")

    abstraction = data.get("abstraction_level")
    if abstraction not in ABSTRACTION_LEVELS:
        report.error("abstraction_level must be light, medium, or high.")

    photo_share = data.get("photo_share")
    if not isinstance(photo_share, (int, float)) or isinstance(photo_share, bool):
        report.error("photo_share must be a number between 0 and 1.")
    elif not 0 <= float(photo_share) <= 1:
        report.error("photo_share must be between 0 and 1.")
    elif route in ROUTE_RANGES:
        low, high = ROUTE_RANGES[route]
        if not low <= float(photo_share) <= high:
            report.warn(
                f"photo_share {photo_share:.2f} is outside the {route} guardrail "
                f"({low:.2f}-{high:.2f}); document the source-specific reason."
            )

    introduced_hues = data.get("introduced_hues")
    if not isinstance(introduced_hues, int) or isinstance(introduced_hues, bool):
        report.error("introduced_hues must be an integer.")
    elif introduced_hues < 0 or introduced_hues > 1:
        report.error("introduced_hues must be 0 or 1.")
    elif palette_mode in {"native", "source-amplification", "tonal-translation"}:
        if introduced_hues != 0:
            report.error(f"palette_mode '{palette_mode}' cannot introduce a new hue.")
    elif palette_mode == "graphic-counterpoint" and introduced_hues != 1:
        report.warn("graphic-counterpoint normally requires exactly one introduced hue.")

    typography = data.get("typography")
    if not isinstance(typography, dict):
        report.error("typography must be an object.")
    else:
        mode = typography.get("mode")
        text = typography.get("text", "")
        if mode not in TYPOGRAPHY_MODES:
            report.error("typography.mode is missing or unsupported.")
        elif mode == "none" and nonempty_string(text):
            report.warn("typography.text is ignored when typography.mode is 'none'.")
        elif mode != "none" and not nonempty_string(text):
            report.error(f"typography.text is required for mode '{mode}'.")

    prompt = data.get("final_generation_prompt", "")
    if prompt and not nonempty_string(prompt):
        report.error("final_generation_prompt must be a string when present.")
    elif nonempty_string(prompt):
        lowered = prompt.lower()
        shortcuts = sorted(name for name in PROMPT_STYLE_SHORTCUTS if name in lowered)
        if shortcuts:
            report.error(
                "final_generation_prompt uses historical/style name shortcuts: "
                + ", ".join(shortcuts)
                + ". Encode formal properties instead."
            )

    if abstraction == "high" and route == "documentary-editorial":
        report.warn(
            "High abstraction conflicts with the usual documentary route; verify every critical lock."
        )
    if field_mode == "neutral-paper" and route == "documentary-editorial":
        report.warn(
            "Neutral paper can replace fragile context; confirm that it matches the source field."
        )

    return report


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plans", nargs="+", type=Path, help="Scene Plan JSON file(s)")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as failures.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    failed = False

    for path in args.plans:
        try:
            data = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            report = Report(path)
            report.error(f"Could not load JSON: {exc}")
        else:
            report = validate_plan(data, path)

        report.print()
        if report.errors or (args.strict and report.warnings):
            failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
