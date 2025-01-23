import uuid
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from typing import Union
import os


def encrypt_bytes(data: bytes, pw: Union[str, bytes]) -> str:
    """加密二进制数据（返回Hex字符串）
    :param data: 要加密的二进制数据
    :param pw: 密码，支持字符串或字节类型
    :return: 加密后的Hex字符串
    :raises ValueError: 如果输入数据为空或密码为空
    """
    if not data:
        raise ValueError("Data cannot be empty")
    if not pw:
        raise ValueError("Password cannot be empty")
    
    # 改进的key生成方式
    if isinstance(pw, str):
        pw = pw.encode('utf-8')
    key = hashlib.sha256(pw).digest()  # 使用完整的256位密钥
    
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = iv + cipher.encrypt(pad(data, AES.block_size))
    return encrypted.hex()

def decrypt_bytes(encrypted_hex: str, pw: Union[str, bytes]) -> bytes:
    """解密Hex字符串为二进制数据
    :param encrypted_hex: 加密后的Hex字符串
    :param pw: 密码，支持字符串或字节类型
    :return: 解密后的二进制数据
    :raises ValueError: 如果输入数据无效或密码错误
    """
    if not encrypted_hex:
        raise ValueError("Encrypted data cannot be empty")
    if not pw:
        raise ValueError("Password cannot be empty")
    
    try:
        # 改进的key生成方式
        if isinstance(pw, str):
            pw = pw.encode('utf-8')
        key = hashlib.sha256(pw).digest()  # 使用完整的256位密钥
        
        encrypted = bytes.fromhex(encrypted_hex)
        if len(encrypted) < 16:
            raise ValueError("Invalid encrypted data")
            
        iv = encrypted[:16]
        ciphertext = encrypted[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ciphertext), AES.block_size)
    except (ValueError, KeyError) as e:
        raise ValueError("Decryption failed: invalid data or wrong password") from e

def encrypt_text(text: str, pw: str) -> str:
    """加密文本（返回Hex字符串）"""
    encrypted = encrypt_bytes(text.encode('utf-8'), pw)
    return encrypted

def decrypt_text(encrypted_hex: str, pw: str) -> str:
    """解密Hex字符串为文本"""
    data = decrypt_bytes(encrypted_hex, pw)
    return data.decode('utf-8')

if __name__ == "__main__":
    pw = "123456"
    text = "Hello, world!"
    byte = b"Hello, world!"
    encrypted = encrypt_text(text, pw)
    print(encrypted)
    decrypted = decrypt_text(encrypted, pw)
    print(decrypted)
    encrypted = encrypt_bytes(byte, pw)
    print(encrypted)
    decrypted = decrypt_bytes(encrypted, pw)
    print(decrypted)