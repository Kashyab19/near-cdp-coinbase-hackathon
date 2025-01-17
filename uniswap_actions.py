
from cdp import Wallet
from typing import Optional

def get_uniswap_quote(
    wallet: Wallet,
    token_in: str,
    token_out: str,
    amount_in: str,
    amount_in_wei: Optional[bool] = True
) -> str:
    """Get a Uniswap quote for swapping tokens.
    
    Args:
        wallet: CDP wallet instance
        token_in: Address of input token
        token_out: Address of output token  
        amount_in: Amount of input token
        amount_in_wei: Whether amount is in wei/smallest unit
        
    Returns:
        str: Quote details
    """
    try:
        quote = wallet.get_uniswap_quote(
            token_in=token_in,
            token_out=token_out, 
            amount_in=str(int(amount_in)),  # Ensure amount is handled as uint256
            amount_in_wei=amount_in_wei
        )
        
        return f"Quote for swapping {amount_in} {token_in}:\nExpected output: {quote.amount_out} {token_out}\nPrice impact: {quote.price_impact}%"
    except Exception as e:
        return f"Error fetching quote: {str(e)}"
