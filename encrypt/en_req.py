import requests
from . import dh, enstr
import const
import os
import json
import base64_tool
import hashlib

dhc = dh.DH()

with open(os.path.join(const.data_dir, "config.json"), "r") as f:
    config = json.load(f)

if config.get("base_url",""):
    key = base64_tool.base64_to_bytes(requests.get(config["base_url"]+"/api/v1/encrypt/get/dh/public_key").json()["public_key"])
    dhs = dhc.generate_shared_key(key)
    
# 发送加密请求
def send_encrypted_request(url, data):
    str_data = json.dumps(data)
    encrypted_data = enstr.encrypt_text(str_data, dhs)
    
    request = {
        "enq": base64_tool.bytes_to_base64(dhc.get_public_key()),
        "end": encrypted_data
    }
    response = requests.post(config["base_url"]+ url, json=request)
    response_data = enstr.decrypt_text(response.json()["body"], dhs)
    return json.loads(response_data)
    
