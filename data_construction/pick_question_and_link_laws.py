import os,sys
import json
import time
from tqdm import tqdm
from model_utils import get_api_model_response
import tiktoken


DATA_PATH = sys.argv[1]
USE_MODEL=sys.argv[2]
def num_tokens_from_string(string, encoding_name):
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(string))


def link_qa_to_laws(qa_results, corpus, model_name):
    output_qa_ref = []
    total_q, call_api_times, all_token_used = 0, 0, 0

    for qa_entry in tqdm(qa_results):
        for question in qa_entry["question"]:
            rel_docs, unrel_docs = [], []
            for passage in corpus:
                content = passage["article"]
                prompt = f"""
                法律條文:{content}\n問題:{question}
                請問上述法律問題是否能在法律條文中找到答案？請回答是或否，並補上原因。
                """
                input_len = num_tokens_from_string(prompt, "cl100k_base")
                response = get_api_model_response(prompt, model_name)
                output_len = num_tokens_from_string(response, "cl100k_base")
                call_api_times += 1
                all_token_used += input_len + output_len

                doc_entry = {"doc_id": passage["id"], "content": content, "reason": response}
                if response.startswith("是"):
                    rel_docs.append(doc_entry)
                else:
                    unrel_docs.append(doc_entry)

            output_qa_ref.append({
                "Question": question,
                "Positive_Doc": rel_docs,
                "Negative_Doc": unrel_docs,
            })

    return output_qa_ref, total_q, call_api_times, all_token_used


def process_qa_with_laws(input_dir, corpus_file, output_dir, model_name):
    with open(corpus_file, "r", encoding="utf-8") as json_file:
        corpus = json.load(json_file)

    qa_file_paths = [os.path.join(input_dir, file) for file in os.listdir(input_dir) if file.endswith(".json")]
    for qa_path in tqdm(qa_file_paths):
        with open(qa_path, "r", encoding="utf-8") as json_file:
            qa_results = json.load(json_file)

        law_name = os.path.basename(qa_path).replace(".json", "").split("_")[0]
        output_qa_ref, total_q, call_api_times, all_token_used = link_qa_to_laws(qa_results, corpus[law_name], model_name)

        with open(os.path.join(output_dir, f"{law_name}_dataset.json"), "w", encoding="utf-8") as json_file:
            json.dump(output_qa_ref, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    input_dir = "legal_news_qa/"
    corpus_file = "/user_data/LawQA-Facts-TW/data/Law_TW_corpus.json"
    output_dir = f"final_legal_dataset_{USE_MODEL}/"

    os.makedirs(output_dir, exist_ok=True)
    process_qa_with_laws(input_dir, corpus_file, output_dir, USE_MODEL)
