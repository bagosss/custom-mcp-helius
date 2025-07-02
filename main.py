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
