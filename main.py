# main.py — Entry point for Brightness Controller

from utils.logger import setup_logger
from ui import BrightnessApp

logger = setup_logger("main")


def main():
    logger.info("Starting Brightness Controller")
    app = BrightnessApp()
    app.run()
    logger.info("Brightness Controller closed")


if __name__ == "__main__":
    main()
