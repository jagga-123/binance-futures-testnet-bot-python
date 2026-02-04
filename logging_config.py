import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def setup_logging():
    logging.basicConfig(
        filename=LOG_DIR / "trading_bot.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

# 👇 TESTING PURPOSE ONLY
if __name__ == "__main__":
    setup_logging()
    logging.info("Logging setup working successfully!")
    print("Logging initialized. Check logs/trading_bot.log")
