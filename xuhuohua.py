import os
import requests

def start_fire():
    # 从 GitHub Secrets 读取 Cookie
    cookie = os.getenv('DOUYIN_COOKIE')
    
    if not cookie:
        print("❌ 错误：未发现 DOUYIN_COOKIE，请检查 GitHub Secrets 设置")
        return

    # 模拟浏览器请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": cookie.strip(),
        "Referer": "https://www.douyin.com/",
        "Accept": "application/json"
    }

    # 验证 Cookie 是否有效的官方接口
    test_url = "https://www.douyin.com/aweme/v1/web/user/profile/self/"

    print("🚀 正在启动云端点火测试...")
    
    try:
        response = requests.get(test_url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            nickname = data.get('user', {}).get('nickname', '未知用户')
            print(f"✅ 成功！已连接到账号: {nickname}")
            print("🔥 今日火花任务指令已发出！")
        elif response.status_code == 403:
            print("❌ 错误：403 访问被拒绝，你的 Cookie 复制不完整或被抖音防火墙拦截")
        else:
            print(f"⚠️ 状态异常: {response.status_code}，请尝试更新 Cookie")
    except Exception as e:
        print(f"❌ 运行异常: {e}")

if __name__ == "__main__":
    start_fire()
