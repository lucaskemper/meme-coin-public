import pytest
from src.core.dex import dex_manager

@pytest.mark.asyncio
async def test_dex_integration():
    # Initialize DEX manager
    dex = dex_manager.DEXManager()

    # Test fetching token price
    token_price = await dex.get_token_price("TOKEN_ADDRESS")
    assert token_price > 0, "Token price should be greater than 0"

    # Test executing a trade
    trade_result = await dex.execute_trade("TOKEN_ADDRESS", amount=1.0, max_slippage=0.02)
    assert trade_result["success"], "Trade should be successful"
    assert trade_result["tx_hash"], "Transaction hash should be present"
