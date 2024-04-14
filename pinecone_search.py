from pinecone import Pinecone
from pinecone_text.sparse import BM25Encoder
from pinecone import ServerlessSpec
import time
import sys,os
from corpus_processor import CorpusProcessor
from typing import List
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.retrievers import PineconeHybridSearchRetriever

class pineconeSearch:
    INDEX_NAME= 'hybrid-search-demo-apr13'
    MODEL_NAME='sentence-transformers/all-MiniLM-L12-v2'
    CORPUS_FILE_PATH = "data/bm25_values.json"
    def __init__(self) -> None:
        # 1 load index, encoder, model
        self.index = self.load_index(self.INDEX_NAME)
        
        if os.path.exists(self.CORPUS_FILE_PATH): 
            self.bm25encoder = self.load_bm25encoder(self.CORPUS_FILE_PATH)
            self.retriever = self.load_retriever(self.bm25encoder, self.MODEL_NAME)
        else:
            print(f"corpus doesn't exits, need to create it {self.CORPUS_FILE_PATH}")

        print("*********************initialized*********************")
        

    def load_index(self, index_name:str):
        pc = Pinecone(api_key='a0dc6c02-46e1-4e75-9859-1fe7fb211c7c')
        if index_name not in pc.list_indexes().names():
            print("the index does not exists")
            sys.exit()
        # wait for index to be initialized
        while not pc.describe_index(index_name).status['ready']:
            time.sleep(1)

        index_info = pc.describe_index(index_name)
        print("*********************INDEX-INFO******************************************")
        print(index_info)
        index = pc.Index(index_name)
        # view index stats
        status_info = index.describe_index_stats()
        print(status_info)
        print("*********************INFO-END******************************************")
        return index

    # it is unnecessary, leave it temporary
    def encode(self, query:str):
        return self.bm25encoder.encode_queries(query)

    def load_bm25encoder(self, corpus_file_path:str):
        processor = CorpusProcessor()
        # Initialize BM25 from a corpus file
        bm25_encoder = BM25Encoder()
        bm25_encoder.load(corpus_file_path)
        return bm25_encoder
    
    def create_bm25encoder(self, docs:List[str]):
        processor = CorpusProcessor()
        corpus = processor.create_single_corpus(docs)
        print(f"create corpus:{corpus}")
        # Initialize BM25 and fit to our corpus
        bm25_encoder = BM25Encoder()
        bm25_encoder.fit(corpus)
        bm25_encoder.dump(self.CORPUS_FILE_PATH)
        return bm25_encoder

    def load_retriever(self, encoder, model_name:str):
        retriever = PineconeHybridSearchRetriever(
            embeddings=HuggingFaceEmbeddings(model_name=model_name), 
            sparse_encoder=encoder,
            index=self.index, 
            alpha=0.5,
            top_k=2
        )
        return retriever
    def search(self, query:str):
        return self.retriever.get_relevant_documents(query)
