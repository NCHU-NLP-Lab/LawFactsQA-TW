import json
import time
from openai import OpenAI

# Set OpenAI API key
client = OpenAI(api_key="your_openai_api_key")



def get_api_model_response(input_q, model_name):
    sys_prompt = """
    You are a machine that only returns and replies with valid, iterable RFC8259 compliant JSON in your responses with codeblock json.
    """
    
    retries = 3
    while retries > 0:
        try:
            prompt_message = input_q
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": prompt_message},
                ]
            )
            response_text = response.choices[0].message.content
            time.sleep(1)
            return response_text
        except Exception as e:
            print("Model API Error:\n", e)
            retries -= 1
            time.sleep(100)
    
    return "API Error"

def get_local_model_response(query):
  # load your model
  pass

def get_api_model_answer(input_q,model_name):
    sys_prompt="""
    請作為助手生成答案。
    """
    retries=3
    while retries!=0:
        try:
            prompt_message=input_q
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": prompt_message},
                    ])
            print(response)
            response_text=response.choices[0].message.content
            time.sleep(1)
            return response_text

        except Exception as e:
            print("Model API Error:\n",e)
            retries-=1
            time.sleep(100)
            response_text="API Error"

    return response_text
