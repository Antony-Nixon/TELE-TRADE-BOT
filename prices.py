import websocket
import json
import ssl
from threading import Thread
import time
from typing import Dict, List, Optional

class PriceManager:
    def __init__(self):
        self.latest_prices: Dict[str, str] = {}
        self.symbols: List[str] = []
        self.websocket_thread: Optional[Thread] = None
        self.is_running = False

    def on_message(self, ws, message):
        try:
            data = json.loads(message)
            if 's' in data and 'c' in data:
                symbol = data['s']
                price = data['c']
                self.latest_prices[symbol] = price
            else:
                print(f"Unexpected message format: {message}")
        except json.JSONDecodeError:
            print(f"Failed to decode JSON: {message}")
        except Exception as e:
            print(f"Error in on_message: {e}")

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print(f"WebSocket connection closed: {close_status_code} - {close_msg}")

    def on_open(self, ws):
        print("WebSocket connection opened")
        for symbol in self.symbols:
            subscribe_msg = json.dumps({
                "method": "SUBSCRIBE",
                "params": [f"{symbol.lower()}@ticker"],
                "id": 1
            })
            ws.send(subscribe_msg)

    def connect_to_websocket(self):
        socket = "wss://stream.binance.com:9443/ws"
        ws = websocket.WebSocketApp(
            socket,
            on_message=lambda ws, msg: self.on_message(ws, msg),
            on_error=lambda ws, err: self.on_error(ws, err),
            on_close=lambda ws, code, msg: self.on_close(ws, code, msg),
            on_open=lambda ws: self.on_open(ws)
        )
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def start_websocket(self):
        while self.is_running:
            try:
                self.connect_to_websocket()
            except Exception as e:
                print(f"WebSocket connection failed: {e}")
            print("Attempting to reconnect in 5 seconds...")
            time.sleep(5)

    def start(self, symbol_list: List[str]):
        """Start the price manager with the given symbol list"""
        self.symbols = [s.upper() for s in symbol_list]
        self.is_running = True
        self.websocket_thread = Thread(target=self.start_websocket)
        self.websocket_thread.daemon = True
        self.websocket_thread.start()

    def stop(self):
        """Stop the price manager"""
        self.is_running = False
        if self.websocket_thread:
            self.websocket_thread.join(timeout=1)

    def get_price(self, symbol: str) -> Optional[str]:
        """Get the latest price for a symbol"""
        symbol = symbol.upper() + "USDT"  # Append USDT to the symbol
        return self.latest_prices.get(symbol)
