import json
import os
from encrypt import en_req
from const import data_dir

def send_login_request(username, password, ui):
    # 发送登录请求
    try:
        re = en_req.send_encrypted_request("/api/v1/user/get/user_info", {
            "username": username,
            "password": password
        })
        print(re)
        print(f"Username: {username}, Password: {password}")
        
        if not re or not re.get("success"):
            return False

        # 保存用户信息
        if data_dir:
            user_data = {
                "username": username,
                "password": password,
                "role": re.get("role"),
            }
            with open(os.path.join(data_dir, "user.json"), "w") as f:
                json.dump(user_data, f)
        
        return True
        
    except Exception as e:
        ui.base_url_error = f"请求出错: {str(e)}"
        ui.the_page.update()
        return False

def get_user_info():
    """读取保存的用户信息"""
    if not data_dir:
        return None
        
    user_file = os.path.join(data_dir, "user.json")
    if not os.path.exists(user_file):
        return None
        
    with open(user_file, "r") as f:
        try:
            return json.load(f)
        except:
            return None

def refresh_user_info_from_cloud(ui):
    """从云端获取最新用户信息"""
    user_info = get_user_info()
    if not user_info:
        return None
        
    try:
        re = en_req.send_encrypted_request("/api/v1/user/get/user_info", {
            "username": user_info["username"],
            "password": user_info["password"]
        })
        
        if not re or not re.get("success"):
            return None
            
        # 更新本地用户信息
        if data_dir:
            user_data = {
                "username": user_info["username"],
                "password": user_info["password"],
                "role": re.get("role"),
            }
            with open(os.path.join(data_dir, "user.json"), "w") as f:
                json.dump(user_data, f)
        
        return user_data
        
    except Exception as e:
        ui.base_url_error = f"请求出错: {str(e)}"
        ui.the_page.update()
        return None