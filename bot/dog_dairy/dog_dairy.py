import requests


def dog_dairy():
    url = "https://api.oick.cn/api/dog"

    try:
        # 发送 GET 请求
        response = requests.get(url)

        # 检查请求是否成功
        if response.status_code == 200:
            print(response.text)
            # 返回 API 返回的字符串数据
            return response.text[1:-1]
        else:
            # 如果请求失败，打印错误信息
            print("Error:", response.status_code)
            return None
    except Exception as e:
        # 发生异常时打印异常信息
        print("Exception:", e)
        return None