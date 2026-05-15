# Control-Panel-using-Python

A professional, modular Python/Tkinter desktop app to control monitor brightness via [NirCmd](https://www.nirsoft.net/utils/nircmd.html).

---

## Project Structure

```
brightness_controller/
├── main.py              # Entry point
├── config.py            # All constants and theme values
├── core/
│   ├── __init__.py
│   └── brightness.py    # BrightnessController — pure logic, no UI
├── ui/
│   ├── __init__.py
│   ├── app.py           # BrightnessApp — main window
│   └── widgets.py       # Reusable themed widget factories
├── utils/
│   ├── __init__.py
│   └── logger.py        # Console + file logging
└── logs/                # Auto-created; daily log files
```

---

## Requirements

- Python 3.9+
- `tkinter` (bundled with standard Python on Windows)
- [NirCmd x64](https://www.nirsoft.net/utils/nircmd.html)

---

## Configuration

Edit `config.py` or set the environment variable:

```bash
set NIRCMD_PATH=C:\path\to\nircmd.exe
```

---

## Running

```bash
python main.py
```

---

## Features

- Slider with live percentage readout
- Quick-preset buttons (25 / 50 / 75 / 100 %)
- Error dialog if NirCmd is missing or fails
- Status bar with last action feedback
- Daily rotating log file under `logs/`
