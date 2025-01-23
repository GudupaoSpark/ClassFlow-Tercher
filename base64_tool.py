import base64

def bytes_to_base64(data: bytes) -> str:
    """将字节数据编码为Base64字符串"""
    return base64.b64encode(data).decode('utf-8')

def base64_to_bytes(b64_str: str) -> bytes:
    """将Base64字符串解码为字节数据"""
    return base64.b64decode(b64_str.encode('utf-8'))