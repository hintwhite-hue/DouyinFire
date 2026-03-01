import os
import requests

def start_fire():
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

    test_url = "https://www.douyin.com/aweme/v1/web/user/profile/self/"
    print("🚀 正在启动云端点火测试...")
    
    try:
        response = requests.get(test_url, headers=headers, timeout=10)
        print(f"📡 接口返回状态码: {response.status_code}")
        
        # 【关键改动】：直接打印抖音返回的原始信息，看看它到底说了什么！
        print(f"📦 抖音返回原文: {response.text[:300]}...") 
        
        if response.status_code == 200:
            data = response.json()
            # 安全地尝试获取信息，防止抓空报错
            if isinstance(data, dict) and data.get('user'):
                nickname = data['user'].get('nickname', '未知用户')
                print(f"✅ 成功！已连接到账号: {nickname}")
            else:
                print("⚠️ 警告：虽然连上了，但抖音没有返回账号信息，可能是 Cookie 失效了。")
        else:
            print("⚠️ 状态码非 200，连接存在问题。")
    except Exception as e:
        print(f"❌ 运行异常: {e}")

if __name__ == "__main__":
    start_fire()
