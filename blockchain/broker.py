import logging
from web3 import Web3

from abi.abi import getABI
from config.config import BlockChain


def getNft2000Discount(sender):
    try:
        if sender == "":
            return {
                "status": "failed",
                "msg": "sender is required",
            }
        if Web3.is_address(sender) is False:
            return {
                "status": "failed",
                "msg": "sender format error",
            }
        sender = Web3.to_checksum_address(sender)
        abi = getABI("broker")
        w3 = Web3(Web3.HTTPProvider(BlockChain['broker']['RPC']))
        broker = w3.eth.contract(address=Web3.to_checksum_address(BlockChain['broker']['contractAddress']), abi=abi)
        return {
            "status": "ok",
            "data": broker.functions.getNft2000Discount(sender).call(),
        }
    except Exception as e:
        logging.error("getNft2000Discount error:", e)
        return None


def nft2000DiscountSum():
    try:
        abi = getABI("broker")
        w3 = Web3(Web3.HTTPProvider(BlockChain['broker']['RPC']))
        broker = w3.eth.contract(address=Web3.to_checksum_address(BlockChain['broker']['contractAddress']), abi=abi)
        return {
            "status": "ok",
            "data": broker.functions.nft2000DiscountSum().call(),
        }
    except Exception as e:
        logging.error("nft2000DiscountSum error:", e)
        return None
