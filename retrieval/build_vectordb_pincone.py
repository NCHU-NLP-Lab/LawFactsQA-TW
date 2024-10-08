import os,json
from tqdm.auto import tqdm
from pinecone import Pinecone, ServerlessSpec, PodSpec
from sentence_transformers import SentenceTransformer
import config


model=SentenceTransformer(config.EMBEDDING_MODEL_NAME)
use_serverless = True
index_name=config.PINECONE_INDEXNAME
pc = Pinecone(api_key=config.PINECONE_API_KEY,environment=config.PINECONE_ENVIRONMENT)
if use_serverless:
    cloud = os.environ.get('PINECONE_CLOUD') or 'PINECONE_CLOUD'
    spec = ServerlessSpec(cloud='aws', region='us-west-2')
else:
    spec = PodSpec(environment=config.PINECONE_ENVIRONMENT)

# check if index already exists (it shouldn't if this is first time)
if index_name not in pc.list_indexes().names():
    # if does not exist, create index
    pc.create_index(
        index_name,
        dimension=1024,  # dimensionality of text-embedding-ada-002
        metric='cosine',
        spec=spec
    )

def conect():
    # connect to index
    index = pc.Index(index_name)
    # view index stats
    # print(pineconeIndex.describe_index_stats())
    return index


def get_embedding(context):

    emb=model.encode(context, normalize_embeddings=True)
    return emb


def pinecone_search(index,query, k:int):
    query_emb=get_embedding(query)
    res=index.query(
    namespace=config.PINECONE_NAMESPACE,
    vector=query_emb.tolist(),
    top_k=k)
    match_arr=[]
    for index, match in enumerate(res["matches"]):
        match_arr.append(match["id"])

    return match_arr

def upsert_file(file_path,index):
    with open(file_path, "r", encoding="utf-8") as json_file:
        corpus = json.load(json_file)
    # embeddings=[]
    for article_law in tqdm(corpus):
        context=article_law["title"]+" "+article_law["article"]
        emb= get_embedding(context)
        # embeddings.append(emb)
        doc_id=article_law["id"]
        text_array_to_metadata = {"law_title": article_law['title']} 
        vector=[{
            "id": doc_id, 
            "values": emb, 
            "metadata": text_array_to_metadata
        }]
        index.upsert(vector,namespace=config.PINECONE_NAMESPACE)
        

def pinecone_search(index,query, k:int):
    query_emb=get_embedding(query)
    res=index.query(
    namespace=config.PINECONE_NAMESPACE,
    vector=query_emb.tolist(),
    top_k=k)
    match_arr=[]
    for index, match in enumerate(res["matches"]):
        match_arr.append(match["id"])
    print(match_arr)
    return match_arr


if __name__ == "__main__":
    pineconeIndex=conect()
    print(pineconeIndex.describe_index_stats())

    test_query="""
    Do foreigners who hold a permanent residence permit or have obtained Taiwanese citizenship by naturalization apply for a work permit?
    """
    search_res=pinecone_search(pineconeIndex,test_query,config.TOP_K)
