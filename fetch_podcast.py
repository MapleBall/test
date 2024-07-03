import json
import pinecone
from langchain.docstore.document import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone

from util import get_pinecone_config
from podcast_crawler.audio2text import WhisperModel, Transcriber


pinecone_config = get_pinecone_config()
pinecone.init(
    api_key=pinecone_config["api_key"], environment=pinecone_config['env']
)













# # 獲取 Pinecone 配置
# pinecone_config = get_pinecone_config()

# # 初始化 Pinecone 客戶端
# LangChainPinecone.create(
#     index_name="podrecom-test",
#     api_key=pinecone_config["api_key"],
#     environment=pinecone_config["env"],
#     dimension=1536,
#     metric='cosine'  # 根據需要選擇合適的相似度度量
# )

# # 使用 HuggingFaceEmbeddings 和 Pinecone 對象
# embeddings = HuggingFaceEmbeddings()
# vector_store = LangChainPinecone(
#     index_name="podrecom-test",
#     embedding=embeddings
# )

# # 初始化 Transcriber 和其他參數
# transcriber = Transcriber(WhisperModel.base)
# episodes = [
#     {
#         "rss": "/Users/stanl/Downloads/EP1.mp3",
#         "channel": "科技浪",
#         "episode": 1
#     }
# ]

# # 執行轉錄和存儲邏輯
# def transcribe_and_store(episode):
#     audio_path = episode["rss"]
#     text = transcriber.transcribe(audio_path)
#     vector_store.add_texts([text], ids=[f"episode_{episode['episode']}"])

# for ep in episodes:
#     transcribe_and_store(ep)
