# 獲取配置
config = get_pinecone_config()

# 打印 API Key 和環境名稱
print("API Key:", config["api_key"])
print("Environment:", config["env"])