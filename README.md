# LawFactsQA-TW

LawFactsQA-TW 是一個跨語言的法條檢索資料集，專門為解決多語言環境下的法律資訊檢索問題而設計。這個資料集的特點在於，它包含口語化的法律查詢，每個查詢都包括英文問題、對應的中文翻譯、相關的法律條文，以及查詢的正確答案。資料集涵蓋台灣的民法、刑法以及行政法規，提供了台灣法律體系的完整範圍。

```範例查詢：取得「度假打工」簽證來臺的外國人，雇主仍需要向本部申請聘僱許可嗎？ If a foreigner comes to Taiwan on a working holiday visa, does the employer still need to apply for a work permit from the Ministry?```

這個資料集的一個潛在應用場景是針對在台外籍人士，他們可能希望用自己的語言查詢法律權益或義務。舉例來說，一個人可能會用英文詢問其配偶是否能在台灣工作。理想的檢索系統應該能根據這個英文問題，找到對應的中文法律條文。進而，再透過語言模型與檢索所得之法條，來回覆提問者。

LawFactsQA-Tw is a cross-lingual statutory article retrieval dataset designed specifically to address the challenges of legal information retrieval in multilingual contexts. Our dataset is unique in that it features spoken-language-style legal inquiries, each including an English query, its corresponding Chinese version, the correct relevant statute, and the ground-truth answer for an inquiry. This dataset encompasses all Taiwanese civil law, criminal law, and administrative regulations, providing comprehensive coverage of the legal landscape in Taiwan.

A potential use case for this dataset is for foreign nationals in Taiwan who may wish to inquire about legal rights or obligations in their own language. For instance, a person might ask in English whether their spouse is allowed to work in Taiwan. An ideal retrieval system would then use this English query to locate the corresponding legal provisions in Chinese. This kind of cross-lingual legal information retrieval is essential for improving accessibility to legal information for non-native speakers, ultimately supporting a more inclusive legal system.

<img width="593" alt="image" src="https://github.com/user-attachments/assets/da30435d-e7d2-4e8b-9240-8a6c2d44fcf0">

## Data Example
**Corpus:**
```json
{
        "id": "1187#5",
        "title": "外國專業人才延攬及僱用法",
        "article": "。外國專業人才、外國特定專業人才及外國高級專業人才，其本人、配偶、未成年子女及因身心障礙無法自理生活之成年子女，經許可永久居留者，在我國從事工作，不須向勞動部或教育部申請許可。第8條雇主聘僱從事專業工作之外國特定專業人才，其聘僱許可期間最長為五年，期滿有繼續聘僱之需要者，得申請延期，每次最長為五年。前項外國特定專業人才經內政部移民署許可居留者，其外僑居留證之有效期間，自許可之翌日起算，最長為五年；期滿有繼續居留之必要者，得於居留期限屆滿前，向內政部移民署申請延期，每次最長為五年"
    }
```
**QA:**
```json
    {
        "query_en": "Are foreign nationals who hold permanent residency or have naturalized to obtain Taiwanese citizenship exempt from applying for a work permit?",
        "query_tw": "取得永久居留外國人或歸化取得我國國籍之外國人，是否不須申請工作許可？",
        "case_id": 0,
        "reference_law_id": [
            "1187#4",
            "1187#5",
            "1187#23"
        ],
        "ground_truth_answer": "一、依據外國專業人才延攬及僱用法第7條規定，外國專業人才、外國特定專業人才及外國高級專業人才，其本人、配偶、未成年子女及因身心障礙無法自理生活之成年子女，經許可永久居留者，在我國從事工作，不須向勞動部或教育部申請許可。因前開法令為特別法，故符合前開條件者，無須按就業服務法第51條規定申請個人工作許可。二、依據外國專業人才延攬及僱用法第25條規定，經歸化取得我國國籍且兼具外國國籍而未在我國設有戶籍，並持外國護照或我國護照入國從事專業工作或尋職者，得免申請工作許可。因前開法令為特別法，故符合前開條件者，無須按就業服務法第79條規定辦理。",
        "reference_law_list": [
            {
                "id": "1187#4",
                "title": "外國專業人才延攬及僱用法",
                "content": "。第6條外國人取得國內外大學之碩士以上學位，或教育部公告世界頂尖大學之學士以上學位者，受聘僱在我國從事就業服務法第四十六條第一項第一款專門性或技術性工作，除應取得執業資格、符合一定執業方式及條件者，及應符合中央目的事業主管機關所定之法令規定外，無須具備一定期間工作經驗。第7條外國專業人才、外國特定專業人才及外國高級專業人才在我國從事專業工作，有下列情形之一者，不須申請許可：一、受各級政府及其所屬學術研究機關（構）聘請擔任顧問或研究工作。二、受聘僱於公立或已立案之私立大學進行講座、學術研究經教育部認可"
            },
            {
                "id": "1187#5",
                "title": "外國專業人才延攬及僱用法",
                "content": "。外國專業人才、外國特定專業人才及外國高級專業人才，其本人、配偶、未成年子女及因身心障礙無法自理生活之成年子女，經許可永久居留者，在我國從事工作，不須向勞動部或教育部申請許可。第8條雇主聘僱從事專業工作之外國特定專業人才，其聘僱許可期間最長為五年，期滿有繼續聘僱之需要者，得申請延期，每次最長為五年。前項外國特定專業人才經內政部移民署許可居留者，其外僑居留證之有效期間，自許可之翌日起算，最長為五年；期滿有繼續居留之必要者，得於居留期限屆滿前，向內政部移民署申請延期，每次最長為五年"
            },
            {
                "id": "1187#23",
                "title": "外國專業人才延攬及僱用法",
                "content": "。但因回復我國國籍、取得我國國籍或兼具我國國籍經撤銷或廢止永久居留許可者，不在此限。第24條香港或澳門居民在臺灣地區從事專業工作或尋職，準用第五條第一項至第四項、第六條、第七條第一項、第八條至第十一條、第十三條、第二十條及第二十一條規定；有關入境、停留及居留等事項，由內政部依香港澳門關係條例及其相關規定辦理。第25條我國國民兼具外國國籍而未在我國設有戶籍，並持外國護照至我國從事專業工作或尋職者，依本法有關外國專業人才之規定辦理。但其係因歸化取得我國國籍者，得免申請工作許可。經歸化取得我國國籍且兼具外國國籍而未在我國設有戶籍，並持我國護照入國從事專業工作或尋職者，得免申請工作許可"
            }
        ]
    }
```
## Data Statistics

| **Human Labeled Data** | **數量** | **Synthetic Data**  | **數量** |
|------------------------|----------|---------------------|----------|
| 刑事訴訟法              | 16       | 中華民國刑法         | 71       |
| 入出國及移民法          | 10       | 勞動基準法           | 38       |
| 就業服務法              | 9        | 道路交通管理處罰條例 | 16       |
| 民事訴訟法              | 9        | 公司法               | 14       |
| 勞動基準法              | 8        | 性別平等工作法       | 11       |
| 臺灣地區與大陸地區人民關係條例 | 5 | 政府採購法           | 7        |
| 外國人從事就業服務法第四十六條第一項第一款至第六款工作資格及審查標準 | 3 | 民事訴訟法           | 6        |
| 外國專門知識及技術人員來台工作許可及管理辦法 | 3 | 土地法               | 5        |
| 兒少性交易防制條例      | 2        | 個人資料保護法       | 4        |
| 入出國及移民法施行細則  | 2        |                     |          |
| 土地法                  | 2        |                     |          |
| 國籍法施行細則          | 2        |                     |          |
| 陸地區人民申請來臺定居案件知照(十二歲以下親生子女) | 2 |                     |          |
| 新住民發展基金補助作業要點 | 2    |                     |          |
| 商標法                  | 2        |                     |          |
| 少年事件處理法          | 2        |                     |          |
| 行政訴訟法              | 2        |                     |          |
| 中華民國憲法            | 1        |                     |          |
| 外國人從事就業服務法第四十六條第四項第五款工作資格及審查標準 | 1 |                     |          |
| 特殊境遇家庭扶助條例    | 1        |                     |          |
| 勞動基準法第904050226號 | 1        |                     |          |
| 醫療法                  | 1        |                     |          |
| 發展觀光條例            | 1        |                     |          |
| 海外高層次人才來台工作許可及管理辦法 | 1   |                     |          |
| 禁止偽造貨幣條例        | 1        |                     |          |
| 香港澳門居民進入臺灣地區及居留定居許可辦法 | 1 |                     |          |
| 國安法                  | 1        |                     |          |
| 保險法                  | 1        |                     |          |
| 外國國籍專業技術人員短期停留或居留規範及管理辦法 | 1 |                     |          |
| 僑居國外國民取得國民身份證使用權辦法 | 1 |                     |          |
| 外國國籍專業技術人員申請入境、簽證及居留定居許可辦法 | 1 |                     |          |
| 外國專門知識及技術人員來台工作許可及管理辦法 | 1 |                     |          |

## Baselines
- LLM-Augmented Retrieval
  1. Answer Expansion 我們透過 LLM 直接生成查詢的答案，這些答案雖然可能不完全正確，但我們將它們用來進行檢索，類似於查詢擴展 (query expansion) 的概念，藉此提升正確法條檢索的準確性。
  2. Statutory Article Expansion 我們引導 LLM 生成可以回答查詢的法條內容，雖然生成的內容可能不完全正確，但這些法條可用於檢索，進一步提升找到正確法條的精確度。
  3. LLM as Reranker 我們使用 LLM 重新排序檢索結果。LLM 會重新評估檢索到的法條，將不相關的結果替換為更符合查詢的法條，直到所有結果都與查詢相符。


## Source
[Laws and Regulations Database of The Republic of China(Taiwan)](https://law.moj.gov.tw/ENG/Index.aspx)

If you find this dataset works for you, please cite the paper "Wang et al. A Cross-Lingual Statutory Article Retrieval Dataset for Taiwan Legal Studies, ROCLING 2024"
