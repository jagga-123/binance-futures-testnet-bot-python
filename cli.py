import argparse
from bot.client import BinanceFuturesClient
from bot.orders import create_order_payload
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    # 🔑 DIRECT TESTNET API KEYS (learning purpose)
    API_KEY = "QBP3bFgwxZhxuYuFUqOStcHUSm1FG0xt15F9HETafa4SOjLmuocsoQcinO3cysUC"
    API_SECRET = "KT2JK5FgnAVasznJpmVRfBC7iu3Ktwey2vIBeTMJlXqvq2Pq2UYZIO8UeUCjavJc"

    client = BinanceFuturesClient(API_KEY, API_SECRET)

    order_payload = create_order_payload(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price,
    )

    print("\nOrder Request Summary:")
    for k, v in order_payload.items():
        print(f"{k}: {v}")

    response = client.place_order(**order_payload)

    print("\nOrder Response:")
    print(f"Order ID: {response.get('orderId')}")
    print(f"Status: {response.get('status')}")
    print(f"Executed Qty: {response.get('executedQty')}")
    print(f"Average Price: {response.get('avgPrice', 'N/A')}")
    print("\n✅ Order placed successfully")


if __name__ == "__main__":
    main()
