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
    Get Block Information
    """

    
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


@mcp.tool
async def getBlockCommitment(blocks: List[int]):
    """
    Get Block Commitment
    """

    
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
                "method": "getBlockCommitment",
                "params": blocks
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
async def getBlockHeight(first_slot: int, last_slot: int, commitment_type: str):
    """
    Get Block Height
    """

    
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
                "method": "getBlockHeight",
                "params": [
                    {
                        "commitment": commitment_type, # processed, confirmed, finalized
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
async def getBlockProduction(identity_public_key: str, range_first_slot: int, range_last_slot: int, commitment_type: str):
    """
    Get Block Production
    """

    
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
                "method": "getBlockProduction",
                "params": [
                    {
                        "identity": identity_public_key,
                        "commitment": commitment_type, # processed, confirmed, finalized
                        "range": {
                            "firstSlot": range_first_slot,
                            "lastSlot": range_last_slot
                        }
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
async def getBlocks(first_slot: int, end_slot: int, commitment_type: str):
    """
    Get Blocks
    """

    
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
                "method": "getBlocks",
                "params": [
                    first_slot,
                    end_slot,
                    {
                        "commitment": commitment_type # confirmed, finalized
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
async def getBlocksWithLimit(start_slot: int, limit: int, commitment_type: str):
    """
    Get Blocks but with Limit
    """

    
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
                "method": "getBlocksWithLimit",
                "params": [
                    {
                        "start_slot": start_slot,
                        "limit": limit,
                        "commitment": commitment_type # confirmed, finalized
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
async def getBlockTime(blocks: List[int]):
    """
    Get Block Time
    """

    
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
                "method": "getBlockTime",
                "params": blocks
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
async def getClusterNodes():
    """
    Get Cluster Nodes
    """

    
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
                "method": "getClusterNodes"
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
async def getEpochInfo(commitment_type: str):
    """
    Get Epoch Information
    """

    
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
                "method": "getEpochInfo",
                "params": [
                    {
                        "commitment": commitment_type # confirmed, finalized
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
async def getEpochSchedule(commitment_type: str):
    """
    Get Epoch Schedule
    """

    
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
                "method": "getEpochSchedule",
                "params": [
                    {
                        "commitment": commitment_type # confirmed, finalized
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
async def getFeeForMessage(serialized_transaction_message: str, commitment_type: str):
    """
    Get Fee Message
    """

    
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
                "method": "getFeeForMessage",
                "params": [
                    serialized_transaction_message,
                    {
                        "commitment": commitment_type # confirmed, finalized
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
async def getFirstAvailableBlock():
    """
    Get First Available Block
    """

    
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
                "method": "getFirstAvailableBlock"
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
async def getGenesisHash():
    """
    Get Genesih Hash
    """

    
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
                "method": "getGenesisHash"
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
async def getHealth():
    """
    Get Health
    """

    
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
                "method": "getHealth"
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
async def getHighestSnapshotSlot():
    """
    Get Highest Snapshot Slot
    """

    
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
                "method": "getHighestSnapshotSlot"
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