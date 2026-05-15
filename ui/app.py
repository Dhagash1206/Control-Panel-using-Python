# ui/app.py — Main application window

import tkinter as tk
from tkinter import messagebox

from config import (
    APP_TITLE, WINDOW_SIZE, WINDOW_RESIZABLE,
    DEFAULT_BRIGHTNESS, MIN_BRIGHTNESS, MAX_BRIGHTNESS,
    PRESET_VALUES, THEME,
)
from core import BrightnessController
from ui.widgets import make_label, make_button, make_slider
from utils.logger import setup_logger

logger = setup_logger(__name__)


class BrightnessApp:
    """Top-level application controller and view."""

    def __init__(self):
        self.controller = BrightnessController()
        self.root = tk.Tk()
        self._build_window()
        self._build_topbar()
        self._build_content()
        self._build_statusbar()

    # ── Window construction ────────────────────────────────────────────────────

    def _build_window(self):
        self.root.title(APP_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.resizable(WINDOW_RESIZABLE, WINDOW_RESIZABLE)
        self.root.configure(bg=THEME["bg_root"])
        # Centre on screen
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        x = (self.root.winfo_screenwidth()  // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f"+{x}+{y}")

    def _build_topbar(self):
        bar = tk.Frame(self.root, bg=THEME["bg_topbar"], height=48)
        bar.pack(fill="x", side="top")
        bar.pack_propagate(False)

        make_label(
            bar, APP_TITLE,
            size=12, bold=True,
            bg=THEME["bg_topbar"], fg=THEME["fg_title"],
        ).pack(side="left", padx=18, pady=10)

        # Version badge
        make_label(
            bar, "v1.0",
            size=8,
            bg=THEME["bg_topbar"], fg=THEME["trough"],
        ).pack(side="right", padx=14)

    def _build_content(self):
        card = tk.Frame(
            self.root, bg=THEME["bg_card"],
            padx=20, pady=14,
        )
        card.pack(fill="both", expand=True, padx=16, pady=(10, 0))

        # ── Slider row ──────────────────────────────────────────────────────
        make_label(card, "Brightness Level", size=9).pack(anchor="w")

        self.slider = make_slider(card, MIN_BRIGHTNESS, MAX_BRIGHTNESS, length=380)
        self.slider.set(DEFAULT_BRIGHTNESS)
        self.slider.pack(pady=(4, 0))

        # Live readout
        self.readout_var = tk.StringVar(value=f"{DEFAULT_BRIGHTNESS}%")
        make_label(
            card, "",
            size=20, bold=True,
            fg=THEME["fg_title"],
            textvariable=self.readout_var,
        ).pack(pady=(0, 6))

        self.slider.config(command=self._on_slider_move)

        # ── Divider ─────────────────────────────────────────────────────────
        tk.Frame(card, bg=THEME["trough"], height=1).pack(fill="x", pady=6)

        # ── Presets row ──────────────────────────────────────────────────────
        make_label(card, "Quick Presets", size=9).pack(anchor="w")
        preset_row = tk.Frame(card, bg=THEME["bg_card"])
        preset_row.pack(pady=(6, 0))

        for val in PRESET_VALUES:
            make_button(
                preset_row,
                text=f"{val}%",
                command=lambda v=val: self._apply_preset(v),
                style="preset",
                width=7,
                padx=4,
            ).pack(side="left", padx=5)

        # ── Apply button ─────────────────────────────────────────────────────
        make_button(
            card,
            text="Apply Brightness",
            command=self._apply,
            style="apply",
            width=28,
            pady=6,
        ).pack(pady=(14, 4))

    def _build_statusbar(self):
        self.status_var = tk.StringVar(value="Ready")
        bar = tk.Frame(self.root, bg=THEME["bg_topbar"], height=26)
        bar.pack(fill="x", side="bottom")
        bar.pack_propagate(False)
        make_label(
            bar, "",
            size=8,
            bg=THEME["bg_topbar"], fg=THEME["fg_title"],
            textvariable=self.status_var,
        ).pack(side="left", padx=10, pady=4)

    # ── Event handlers ─────────────────────────────────────────────────────────

    def _on_slider_move(self, value):
        self.readout_var.set(f"{int(float(value))}%")

    def _apply_preset(self, value: int):
        self.slider.set(value)
        self.readout_var.set(f"{value}%")
        self._apply()

    def _apply(self):
        value = self.slider.get()
        success = self.controller.set_brightness(value)
        if success:
            self.status_var.set(f"Brightness set to {value}%")
            logger.info("Applied brightness: %d%%", value)
        else:
            self.status_var.set("Error: could not apply brightness")
            messagebox.showerror(
                "NirCmd Error",
                f"Failed to set brightness.\n"
                f"Ensure NirCmd is installed at:\n{self.controller.nircmd_path}",
            )

    # ── Entry point ────────────────────────────────────────────────────────────

    def run(self):
        self.root.mainloop()
