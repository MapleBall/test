# import json

# def get_pinecone_config():
#     with open('pinecone_config.json', 'r') as f:
#         pinecone_config = json.load(f)
#         return pinecone_config

import os

def get_pinecone_config():
    return {
        "api_key": os.getenv("PINECONE_API_KEY"),
        "env": os.getenv("PINECONE_ENV")
    }

# # 獲取配置
#config = get_pinecone_config()

# # 打印 API Key 和環境名稱
# print("API Key:", config["api_key"])
# print("Environment:", config["env"])
