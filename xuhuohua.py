import os
import requests

def run_fire():
    # 从 GitHub 的“保险箱”读取你的 Cookie
    cookie = os.getenv('DOUYIN_COOKIE')
    
    if not cookie:
        print("❌ 错误：在 GitHub Secrets 中未找到 DOUYIN_COOKIE，请检查设置！")
        return

    # 这是一个标准的抖音网页版请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": cookie,
        "Referer": "https://www.douyin.com/",
        "Accept": "application/json"
    }

    # 模拟点火/签到的接口 (这里仅为示例，如果是特定功能的点火需要替换对应 URL)
    # 注意：纯 API 模式不需要屏幕和鼠标，运行速度极快
    test_url = "https://www.douyin.com/aweme/v1/web/general/search/" 

    print("🚀 正在启动云端点火程序...")
    
    try:
        response = requests.get(test_url, headers=headers, timeout=10)
        if response.status_code == 200:
            print("✅ 成功连接抖音服务器！")
            print(f"📡 服务器返回状态: {response.status_code}")
            # 这里可以根据具体的点火接口返回逻辑来判断是否成功
        else:
            print(f"⚠️ 访问受限，状态码: {response.status_code} (可能是 Cookie 过期)")
    except Exception as e:
        print(f"❌ 运行异常: {str(e)}")

if __name__ == "__main__":
    run_fire()
