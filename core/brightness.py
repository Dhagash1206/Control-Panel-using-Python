# core/brightness.py — Brightness control logic (isolated from UI)

import subprocess
import logging
from config import NIRCMD_PATH, MIN_BRIGHTNESS, MAX_BRIGHTNESS

logger = logging.getLogger(__name__)


class BrightnessController:
    """Handles all brightness-related operations via NirCmd."""

    def __init__(self, nircmd_path: str = NIRCMD_PATH):
        self.nircmd_path = nircmd_path
        self._current_brightness: int = 0

    # ── Public API ─────────────────────────────────────────────────────────────

    def set_brightness(self, value: int) -> bool:
        """
        Set monitor brightness.
        Returns True on success, False on failure.
        """
        value = self._clamp(value)
        try:
            result = subprocess.run(
                [self.nircmd_path, "setbrightness", str(value)],
                check=False,
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                self._current_brightness = value
                logger.info("Brightness set to %d%%", value)
                return True
            else:
                logger.warning(
                    "NirCmd returned non-zero exit code: %d | stderr: %s",
                    result.returncode,
                    result.stderr.strip(),
                )
                return False
        except FileNotFoundError:
            logger.error("NirCmd executable not found at: %s", self.nircmd_path)
            return False
        except subprocess.TimeoutExpired:
            logger.error("NirCmd timed out while setting brightness.")
            return False
        except Exception as exc:  # pylint: disable=broad-except
            logger.exception("Unexpected error setting brightness: %s", exc)
            return False

    @property
    def current_brightness(self) -> int:
        return self._current_brightness

    # ── Helpers ────────────────────────────────────────────────────────────────

    @staticmethod
    def _clamp(value: int) -> int:
        return max(MIN_BRIGHTNESS, min(MAX_BRIGHTNESS, int(value)))
