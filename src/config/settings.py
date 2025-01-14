class Settings:
    def __init__(self):
        self.rpc_endpoints = ["https://your-rpc-endpoint-1", "https://your-rpc-endpoint-2"]
        self.wallet_private_key = "your_private_key"
        self.telegram_bot_token = "your_telegram_bot_token"
        self.telegram_chat_id = "your_telegram_chat_id"

        # Trading parameters
        self.max_slippage = 0.02
        self.tranche_size = 1.0
        self.tranche_index = 0
