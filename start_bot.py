import asyncio
from src.core.dex import dex_manager
from src.strategies.entry_strategy import EntryStrategy
from src.config.settings import Settings
from src.monitoring.telegram_handler import TelegramNotifier

async def main():
    # Load settings
    settings = Settings()

    # Initialize strategy
    strategy = EntryStrategy(settings)

    # Initialize Telegram notifier
    notifier = TelegramNotifier(settings)

    # Execute trades
    await strategy.execute_entry(amount=1.0, tranche_index=0, max_slippage=0.02)

    # Send notification
    await notifier.send_message("Trade executed successfully")

if __name__ == "__main__":
    asyncio.run(main())
