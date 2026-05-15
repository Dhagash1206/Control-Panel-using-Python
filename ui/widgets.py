# ui/widgets.py — Reusable custom Tkinter widgets

import tkinter as tk
from config import THEME


def make_label(parent, text: str, size: int = 10, bold: bool = False, **kw) -> tk.Label:
    """Convenience factory for themed labels."""
    weight = "bold" if bold else "normal"
    return tk.Label(
        parent,
        text=text,
        bg=kw.pop("bg", THEME["bg_card"]),
        fg=kw.pop("fg", THEME["fg_text"]),
        font=(THEME["font_family"], size, weight),
        **kw,
    )


def make_button(parent, text: str, command, style: str = "default", **kw) -> tk.Button:
    """
    Factory for themed buttons.
    style: 'default' | 'apply' | 'preset'
    """
    styles = {
        "default": {
            "bg": THEME["bg_btn"],
            "fg": THEME["fg_text"],
            "activebackground": THEME["bg_btn_active"],
            "activeforeground": THEME["fg_text"],
        },
        "apply": {
            "bg": THEME["bg_apply"],
            "fg": THEME["fg_apply"],
            "activebackground": THEME["bg_apply_hover"],
            "activeforeground": THEME["fg_apply"],
        },
        "preset": {
            "bg": THEME["bg_btn"],
            "fg": THEME["fg_text"],
            "activebackground": THEME["bg_btn_active"],
            "activeforeground": THEME["fg_text"],
        },
    }
    s = styles.get(style, styles["default"])
    return tk.Button(
        parent,
        text=text,
        command=command,
        relief="flat",
        cursor="hand2",
        font=(THEME["font_family"], 10),
        **{**s, **kw},
    )


def make_slider(parent, from_: int, to: int, length: int = 320) -> tk.Scale:
    """Factory for a themed horizontal Scale widget."""
    return tk.Scale(
        parent,
        from_=from_,
        to=to,
        orient="horizontal",
        bg=THEME["bg_card"],
        fg=THEME["fg_text"],
        troughcolor=THEME["trough"],
        highlightthickness=0,
        length=length,
        font=(THEME["font_family"], 9),
        relief="flat",
        sliderlength=18,
    )
