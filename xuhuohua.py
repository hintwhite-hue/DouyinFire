import os
import requests

def start_fire():
    # 从 GitHub Secrets 读取 Cookie
    cookie = os.getenv('DOUYIN_COOKIE')
    
    if not cookie:
        print("❌ 错误：未发现 DOUYIN_COOKIE，请检查设置")
        return

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": cookie.strip(),
        "Referer": "https://www.douyin.com/",
        "Accept": "application/json"
    }

    # 验证账号信息的接口
    test_url = "https://www.douyin.com/aweme/v1/web/user/profile/self/"

    print("🚀 正在启动云端点火测试...")
    
    try:
        response = requests.get(test_url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            nickname = data.get('user', {}).get('nickname', '未知用户')
            print(f"✅ 成功！已连接到账号: {nickname}")
        else:
            print(f"⚠️ 状态异常: {response.status_code}，请检查 Cookie 是否完整")
    except Exception as e:
        print(f"❌ 运行异常: {e}")

if __name__ == "__main__":
    start_fire()
