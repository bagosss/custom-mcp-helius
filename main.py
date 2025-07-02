import httpx
from uuid import uuid4
from enum import Enum
from typing import Union, List
from decouple import config
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("custom-helius")

# class SolanaCommitment(Enum):
#     PROCESSED = "processed"
#     CONFIRMED = "confirmed" 
#     FINALIZED = "finalized"

# class SolanaCommitmentDesc(Enum):
#     PROCESSED = "New data entered mempool, not yet confirmed to enter blockchain"
#     CONFIRMED = "Data has entered block and has been confirmed by 1 validator, but is not yet considered final"
#     FINALIZED = "Data is final & cannot be canceled, guaranteed to enter chain"

# def generate_commitment_schema():
#     return {
#         "oneOf": [
#             {
#                 "const": commitment.value,
#                 "description": SolanaCommitmentDesc[commitment.name].value
#             }
#             for commitment in SolanaCommitment
#         ],
#         "default": SolanaCommitment.FINALIZED.value
#     }

# commitment_types = generate_commitment_schema()

def main():
    print("Hello from custom-mcp-helius!")

if __name__ == "__main__":
    main()

helius_api_key = config('HELIUS_API_KEY', default="", cast=str)

@mcp.tool
async def getAccountInfo(wallet_address: str, commitment_type: str):
    """
    Get Account Info
    """

    # if commitment_type not in [c.value for c in SolanaCommitment]:
    #     raise ValueError(f"Invalid commitment: {commitment_type}. Valid options: {[c.value for c in SolanaCommitment]}")

    async with httpx.AsyncClient() as client:
        try:
            url = "https://mainnet.helius-rpc.com/"
            headers = {
                "Content-Type": "application/json"
            }
            query_params = {
                "api-key": helius_api_key
            }
            payload = {
                "jsonrpc": "2.0",
                "id": str(uuid4),
                "method": "getAccountInfo",
                "params": [
                    wallet_address,
                    {
                        "encoding": "jsonParsed",
                        "commitment": commitment_type # processed, confirmed, finalized
                    }
                ]
            }
            
            response = await client.post(
                url,
                headers=headers,
                params=query_params,
                json=payload,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


@mcp.tool
async def getAccountBalance(wallet_address: str, commitment_type: str):
    """
    Get Account Balance
    """
    
    # if commitment_type not in [c.value for c in SolanaCommitment]:
    #     raise ValueError(f"Invalid commitment: {commitment_type}. Valid options: {[c.value for c in SolanaCommitment]}")
    
    async with httpx.AsyncClient() as client:
        try:
            url = "https://mainnet.helius-rpc.com/"
            headers = {
                "Content-Type": "application/json"
            }
            query_params = {
                "api-key": helius_api_key
            }
            payload = {
                "jsonrpc": "2.0",
                "id": str(uuid4),
                "method": "getBalance",
                "params": [
                    wallet_address,
                    {
                        "encoding": "jsonParsed",
                        "commitment": commitment_type # processed, confirmed, finalized
                    }
                ]
            }
            
            response = await client.post(
                url,
                headers=headers,
                params=query_params,
                json=payload,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


@mcp.tool
async def getBlock(block: int, commitment_type: str):
    """
    Get Account Balance
    """
    
    # if commitment_type not in [c.value for c in SolanaCommitment]:
    #     raise ValueError(f"Invalid commitment: {commitment_type}. Valid options: {[c.value for c in SolanaCommitment]}")
    
    async with httpx.AsyncClient() as client:
        try:
            url = "https://mainnet.helius-rpc.com/"
            headers = {
                "Content-Type": "application/json"
            }
            query_params = {
                "api-key": helius_api_key
            }
            payload = {
                "jsonrpc": "2.0",
                "id": str(uuid4),
                "method": "getBlock",
                "params": [
                    block,
                    {
                        "rewards": True,
                        "transactionDetails": "full", # full, account, signatures, none
                        "commitment": commitment_type # finalized
                    }
                ]
            }
            
            response = await client.post(
                url,
                headers=headers,
                params=query_params,
                json=payload,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
