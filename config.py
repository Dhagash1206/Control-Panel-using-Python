# config.py — Central configuration for Brightness Controller

import os

# ─── Executable ────────────────────────────────────────────────────────────────
NIRCMD_PATH = os.environ.get(
    "NIRCMD_PATH",
    r"C:\Users\dhagash\Desktop\nircmd-x64\nircmd.exe"
)

# ─── Window ────────────────────────────────────────────────────────────────────
APP_TITLE       = "Brightness Controller"
WINDOW_SIZE     = "460x320"
WINDOW_RESIZABLE = False

# ─── Defaults ──────────────────────────────────────────────────────────────────
DEFAULT_BRIGHTNESS = 60
MIN_BRIGHTNESS     = 0
MAX_BRIGHTNESS     = 100
PRESET_VALUES      = [25, 50, 75, 100]

# ─── Theme ─────────────────────────────────────────────────────────────────────
THEME = {
    "bg_root":        "#0b1412",
    "bg_topbar":      "#08100e",
    "bg_card":        "#0f1f1b",
    "bg_btn":         "#132925",
    "bg_btn_active":  "#1f4d42",
    "bg_apply":       "#f4b942",
    "bg_apply_hover": "#ffd36a",
    "fg_title":       "#6fe3c1",
    "fg_text":        "#cfeee6",
    "fg_apply":       "#0b1412",
    "trough":         "#1e3a32",
    "font_family":    "Segoe UI",
}
