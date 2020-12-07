from . import test
from app import *
from flask import jsonify,request
import bitly_api
from bitly_api import Connection, BitlyError, Error
from bitly_api import bitly_api



@test.route('/tes', methods=['GET'])
def tes():
    return jsonify({"msg": "welcome to new module"})


@test.route('/url_shorterner', methods=['GET'])
def url_shorterner():
    query_url = request.args["long_url"]
    try:
        BITLY_ACCESS_TOKEN = "897d61ccfa3d581689952326eb8059a0e3d8b67e"

        bitly = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)

        response = bitly.shorten(query_url)
        return jsonify({"shorten_url": response})
    
    except Exception as e:
        print(str(e))
        return jsonify({"message": "error", "error_info": str(e)})


