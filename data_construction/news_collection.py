import requests
import json,sys
from bs4 import BeautifulSoup
import time
import random
import csv
from tqdm import tqdm

SEARCH_QUANT = 200
DATA_PATH = sys.argv[1]
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
]

# Convert to actual URL
def get_real_url(url):
    headers = {"User-Agent": random.choice(user_agent_list)}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    real_url = soup.find(jsname="tljFtd")
    if real_url:
        li = real_url.get('href')
        return li
    return url  # If no redirection, return original link

# Scrape Google News, but URL needs to be converted
def get_google_news(query, num):
    print(query)
    url = f'https://news.google.com/search?q={query}&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant'
    headers = {"User-Agent": random.choice(user_agent_list)}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a', jsaction="click:kkIcoc;")
    count = 0
    link_list = []
    for link in links:
        if count == num:
            break
        li = link.get('href').replace('.', 'https://news.google.com')
        li = get_real_url(li)
        link_list.append(li)
        count += 1

    time.sleep(1)
    return link_list

# Scrape the content of each news URL
def get_news_content(url):
    headers = {"User-Agent": random.choice(user_agent_list)}
    requests.adapters.DEFAULT_RETRIES = 5
    timetout = 10
    session = requests.session()
    all_snippets = ""

    try:
        response = session.get(url, headers=headers, verify=False, timeout=timetout)
        soup = BeautifulSoup(response.text, 'html.parser')
        contents = soup.find_all('p')
        for content in contents:
            all_snippets += content.get_text()
        time.sleep(random.randint(3, 5))

    except requests.Timeout:
        print('Request timeout!')

    except requests.RequestException as e:
        print(f'Error: {e}')
    
    return all_snippets

# Read CSV file to get weights
def get_weight_from_csv(csv_path):
    weight_dict = {}
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            law_k = row[0]
            weight = float(row[1])
            weight_dict[law_k] = weight
    return weight_dict

if __name__ == "__main__":
    csv_file_path = "Popular Search Regulations - number of clicks.csv"
    weight_dict = get_weight_from_csv(csv_file_path)
   
    for law_k in tqdm(weight_dict.keys()):
        n = int(SEARCH_QUANT * weight_dict[law_k] / 100)
        query = law_k + " Related News"
        print(query, "Count:", n)
        news_list = get_google_news(query, n)

        search_res = []
        for url in tqdm(news_list):
            search_res.append(get_news_content(url))

        output = {
            law_k: search_res
        }

        with open(DATA_PATH+"/"+law_k+"_news_"+str(n)+".json", "w", encoding="utf-8") as json_file:
            json.dump(output, json_file, ensure_ascii=False, indent=4)
