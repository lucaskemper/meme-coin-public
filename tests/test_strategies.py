import pytest
from src.strategies.entry_strategy import EntryStrategy
from src.strategies.launch_sniper import LaunchSniper
from src.strategies.scalping import Scalping
from src.strategies.trend_trader import TrendTrader

@pytest.mark.asyncio
async def test_entry_strategy():
    strategy = EntryStrategy()
    result = await strategy.execute_entry(amount=1.0, tranche_index=0, max_slippage=0.02)
    assert result["success"], "Entry strategy should execute successfully"
    assert result["tx_hash"], "Transaction hash should be present"

@pytest.mark.asyncio
async def test_launch_sniper():
    strategy = LaunchSniper()
    result = await strategy.snipe_launch(token_address="TOKEN_ADDRESS", amount=1.0, max_slippage=0.02)
    assert result["success"], "Launch sniping should execute successfully"
    assert result["tx_hash"], "Transaction hash should be present"

@pytest.mark.asyncio
async def test_scalping():
    strategy = Scalping()
    result = await strategy.execute_scalping(token_address="TOKEN_ADDRESS", amount=1.0, max_slippage=0.02)
    assert result["success"], "Scalping strategy should execute successfully"
    assert result["tx_hash"], "Transaction hash should be present"

@pytest.mark.asyncio
async def test_trend_trader():
    strategy = TrendTrader()
    result = await strategy.execute_trend_trade(token_address="TOKEN_ADDRESS", amount=1.0, max_slippage=0.02)
    assert result["success"], "Trend trading should execute successfully"
    assert result["tx_hash"], "Transaction hash should be present"
