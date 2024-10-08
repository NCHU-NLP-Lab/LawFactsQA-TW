import json,os
from tqdm import tqdm

topk_list=[10,20,50]
def precision(ref_docs:list,pred_docs:list):
    precision = len(set(pred_docs) & set(ref_docs)) / len(pred_docs)
    return precision
def avg_precision(ref_docs:list,pred_docs:list):
    relevant_count = 0
    total_precision = 0.0
    for i, doc in enumerate(pred_docs):
        if doc in ref_docs:
            relevant_count += 1
            total_precision += relevant_count / (i + 1)
    average_precision = total_precision / len(ref_docs)
    return average_precision

def recall(ref_docs:list,pred_docs:list):
    recall = len(set(pred_docs) & set(ref_docs)) / len(ref_docs)
    return recall
def f1_cal(ref_docs, pred_docs):
    precision_score = precision(ref_docs, pred_docs)
    recall_score = recall(ref_docs, pred_docs)
    if precision_score + recall_score == 0:
        return 0
    f1 = 2 * (precision_score * recall_score) / (precision_score + recall_score)
    return f1


def save_final_score(textlist,output_file_name,topk_v,save_dir):
    with open(save_dir+output_file_name+ "top-"+str(topk_v)+"_score.txt", "w") as f:
        f.write("\n".join(textlist))

def save_each_score(result,source,topk_v,save_dir):
    # source=source.replace(".json","")
    output_name="score_"+source

    with open(save_dir+output_name+"top-"+str(topk_v)+".json", "w") as json_file:
        json.dump(result, json_file, indent=4) 

def eval(test_dir,topks,save_dir):
    json_file_paths = []
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            if file.endswith(".json"):
                json_file_paths.append(os.path.join(root, file))
    print(json_file_paths)
    ### refid
    # with open("../../data/QA_0325.json", "r", encoding="utf-8") as json_file:
    #     gt_answer = json.load(json_file)

    for json_file_path in json_file_paths:
        # get file name
        file_name = os.path.basename(json_file_path)
        file_name_part = file_name.replace(".json","")
        file_name_part = file_name_part.replace("searchRes","eval")
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            retrieve_res = json.load(json_file)
        
        precision_all=0
        avg_precision_all=0
        recall_all=0
        f1_all=0
        score_bycase=[]

        for idx,testcase in enumerate(retrieve_res):

            # ref_list=testcase["ref_law_id"]
            ref_list=testcase["reference_law_id"]
            predict_list=testcase["predict_ids"][0:topks-1]
            # prerank_id predict_id
            precision_score=precision(ref_list,predict_list)
            avg_precision_score=avg_precision(ref_list,predict_list)
            recall_score=recall(ref_list,predict_list)
            f1_score=f1_cal(ref_list,predict_list)
            # qid
            case_res={
                "id":testcase["qid"],
                "precision":precision_score,
                "avg_precision":avg_precision_score,
                "recall":recall_score,
                "f1":f1_score
            }
            precision_all+=precision_score
            avg_precision_all+=avg_precision_score
            recall_all+=recall_score
            f1_all+=f1_score
            score_bycase.append(case_res)
        #輸出算分結果
        score_output=[]
        precision_all/=len(retrieve_res)
        avg_precision_all/=len(retrieve_res)
        recall_all/=len(retrieve_res)
        f1_all/=len(retrieve_res)
        score_output.append(file_name_part)
        score_output.append("precision:"+str(precision_all))
        score_output.append("Average precision:"+str(avg_precision_all))
        score_output.append("recall:"+str(recall_all))
        score_output.append("F1:"+str(f1_all))
        save_final_score(score_output,file_name_part,topks,save_dir)
        #每一筆分數
        save_each_score(score_bycase,file_name_part,topks,save_dir)


        
        print("已完成")




if __name__ == "__main__":
    search_res_dir="../embedding_search/result_final"
    # "../embedding_search/clir_hyde"
    save_dir="eval_result_all/"
    # Legal_RAG/Retrieval/hypothesis_doc_gen/hyp_doc_0410

    for topk_v in  topk_list:
        eval(search_res_dir,topk_v,save_dir)