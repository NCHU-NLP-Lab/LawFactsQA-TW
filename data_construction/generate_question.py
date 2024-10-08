import os
import json
from tqdm.auto import tqdm
from model_utils import get_api_model_response
import sys

DATA_PATH = sys.argv[1]
USE_MODEL=sys.argv[2]
def generate_all(test_dir):
    json_file_paths = []
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            if file.endswith(".json"):
                json_file_paths.append(os.path.join(root, file))
    
    print(json_file_paths)
    
    for json_file_path in tqdm(json_file_paths):
        file_name = os.path.basename(json_file_path)
        file_name_part = file_name.replace(".json", "")
        
        print("Processing file:", json_file_path)
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            news = json.load(json_file)
        
        law_name = list(news.keys())[0]
        print("Law name:", law_name)
        if news[law_name] is None:
            continue
        
        qa_pair = []
        for news_content in tqdm(news[law_name]):
            prompt = f"""
            你是台灣政府的法律顧問，想要生成一些民眾可能會遇到的法律相關問題，且這些問題都必須對應到實際的法條，
            若在情境中沒有提到台灣法條，內容不相干，提及他國法律，如:中國大陸民法典, 日本民法等，在輸出問題的欄位中填入"None"。

            以下會有提供的情境及對應法律名稱，請產生3-5題。
            情境: {news_content}
            請參考新聞情境生成需要查詢台灣法律：{law_name}內容方能獲取答案的問題，問題中不可提到法律條文名稱。

            以下是輸出範例:
            {{
                "問題": ["第一題", "第二題"],
                "答案": ["第一題答案", "第二題答案"],
                "法律名稱":"題目相關法律",
                "問題情境":"擷取問題相關的段落，完整情境說明",
            }}
            若無相關內容:
            {{
                "問題": "None",
                "問題情境":"段落",
            }}
            """
            res = get_api_model_response(prompt, USE_MODEL)
            
            try:
                res = res.replace("\n", "").strip()[7:-3]
                json_list = json.loads(res)
                qa_pair.append(json_list)
            except json.decoder.JSONDecodeError as e:
                print("JSON decode error:", e)
                continue
        
        output_file_path = f"legal_news_qa/{file_name_part}.json"
        with open(output_file_path, "w", encoding="utf-8") as json_file:
            json.dump(qa_pair, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    test_dir = "{DATA_PATH}"
    generate_all(test_dir)
