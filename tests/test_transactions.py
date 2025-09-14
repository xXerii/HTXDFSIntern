import os
import pytest
from src.HTXDFS_Challenge_2 import get_transactions

API_KEY = os.getenv("ETHERSCAN_API_KEY", "demo")  # use env var for safety
TEST_WALLET = "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae"  # Ethereum Foundation

def test_fetch_transactions():
    txs = get_transactions(TEST_WALLET, API_KEY, limit=5)
    assert isinstance(txs, list)
    if txs:  # If API works
        assert "from" in txs[0]
        assert "to" in txs[0]