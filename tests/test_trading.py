import pytest
from src.trading.trading_logic import TradingLogic

@pytest.mark.asyncio
async def test_trading_logic():
    trading_logic = TradingLogic()

    # Test trade execution
    trade_result = await trading_logic.execute_trade("TOKEN_ADDRESS", amount=1.0, max_slippage=0.02)
    assert trade_result["success"], "Trade should be successful"
    assert trade_result["tx_hash"], "Transaction hash should be present"

    # Test trade cancellation
    cancel_result = await trading_logic.cancel_trade("TX_HASH")
    assert cancel_result["success"], "Trade cancellation should be successful"
    assert cancel_result["message"] == "Trade cancelled", "Cancellation message should be 'Trade cancelled'"
