import json
from model_utils import get_api_model_answer
from tqdm import tqdm


if __name__ == "__main__":
    cor_path="synthetic_legal_QAdataset_retrieval_task.json"
    with open(cor_path, "r", encoding="utf-8") as json_file:
        dataset = json.load(json_file)
    for idx,content in tqdm(enumerate(dataset)):
        all_rel_docs=""
        question=content["query_tw"]
        law_name=content["Related_law"]
        for doc in content["ref_law_content"]:
            all_rel_docs+=doc['content']
            all_rel_docs+="\n"
        input_prompt=f"問題:{question}\n參考下列{law_name}條文回答問題\n{all_rel_docs}\n"
        input_prompt+="生成答案應精確(如：根據XX法律第幾條)並簡短，不需條列出文章內容。"
        result=get_api_model_answer(input_prompt,"gpt-4-turbo")
        print("input:",input_prompt)
        print("長度:",len(input_prompt))

        print("模型回答:", result)
        dataset[idx]["Answer"]=result
    with open("synthetic_legal_QAdataset_odqa.json", "w", encoding="utf-8") as json_file:
        json.dump(dataset, json_file, ensure_ascii=False,indent=4)
    
        
