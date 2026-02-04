import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

# ---------------- LOGGING CONFIG ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ---------------- BINANCE FUTURES CLIENT ----------------
class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        # Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        logger.info("Binance Futures client initialized")

    def place_order(self, **kwargs):
        try:
            logger.info(f"Placing order: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"Order response: {response}")
            return response
        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e}")
            raise
        except BinanceRequestException as e:
            logger.error(f"Network error: {e}")
            raise


# ---------------- MAIN EXECUTION ----------------
if __name__ == "__main__":
    # ⚠️ Testnet API keys use karo (real money nahi)
    API_KEY = "QBP3bFgwxZhxuYuFUqOStcHUSm1FG0xt15F9HETafa4SOjLmuocsoQcinO3cysUC"
    API_SECRET = "KT2JK5FgnAVasznJpmVRfBC7iu3Ktwey2vIBeTMJlXqvq2Pq2UYZIO8UeUCjavJc"

    client = BinanceFuturesClient(API_KEY, API_SECRET)

    # ----- TEST ORDER -----
    order = client.place_order(
        symbol="BTCUSDT",
        side="BUY",
        type="MARKET",
        quantity=0.002
    )

    print("Order placed successfully")
    print(order)

