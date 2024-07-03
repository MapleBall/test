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


INDEX_NAME = "podrecom-test"
embeddings = HuggingFaceEmbeddings()

transcriber = Transcriber(WhisperModel.base)
episodes = [
        {
            "rss": "/Users/stanl/Downloads/ep1.mp3",
            "channel": "科技浪 Techwav",
            "episode": 1
        }
    ]

for episode in episodes:
    fname = episode['rss']
    result = transcriber.get_text(fname)
    document = Document(page_content=result, metadata=episode)
    print(document)
    index = Pinecone.from_documents([document], embeddings, index_name=INDEX_NAME)
    
    similar_docs = index.similarity_search("墮胎", k=3)
    print(similar_docs)

