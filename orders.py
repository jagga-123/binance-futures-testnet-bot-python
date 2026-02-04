try:
    
    from .validators import validate_inputs
except ImportError:
   
    from validators import validate_inputs


def create_order_payload(symbol, side, order_type, quantity, price=None):
    validate_inputs(symbol, side, order_type, quantity, price)

    payload = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        payload["price"] = price
        payload["timeInForce"] = "GTC"

    return payload

if __name__ == "__main__":
    test_payload = create_order_payload(
        symbol="BTCUSDT",
        side="BUY",
        order_type="MARKET",
        quantity=0.002
    )

    print("Order payload created successfully:")
    print(test_payload)
