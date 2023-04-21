import os
from flask import Flask, request
from flask_cors import CORS
from blockchain.broker import getNft2000Discount, nft2000DiscountSum

from log import logger

app = Flask(__name__)
CORS(app, supports_credentials=True)

currPath = os.path.dirname(os.path.abspath(__file__))
logFile = "{}/log/logs.log".format(currPath)
logger.config_log(logFile)


@app.route('/', methods=['GET'])
def root():
    return "Web3 API"


@app.route('/getNft2000Discount', methods=['GET'])
def getDiscount():
    sender = str(request.args.get("sender"))
    discount = getNft2000Discount(sender)
    if discount is None:
        return {
            "status": "failed",
            "msg": "server is busy",
        }
    return discount


@app.route('/nft2000DiscountSum', methods=['GET'])
def getDiscountSum():
    discountSum = nft2000DiscountSum()
    if discountSum is None:
        return {
            "status": "failed",
            "msg": "server is busy",
        }
    return discountSum


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9100)
