# LawFactsQA-TW

LawFactsQA-TW 是一個跨語言的法條檢索資料集，專門為解決多語言環境下的法律資訊檢索問題而設計。這個資料集的特點在於，它包含口語化的法律查詢，每個查詢都包括英文問題、對應的中文翻譯、相關的法律條文，以及查詢的正確答案。資料集涵蓋台灣的民法、刑法以及行政法規，提供了台灣法律體系的完整範圍。

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
        "reference_law": [
            [
                "外國專業人才延攬及僱用法",
                "第7條"
            ],
            [
                "外國專業人才延攬及僱用法",
                "第25條"
            ]
        ],
        "reference_law_id": [
            "1187#4",
            "1187#5",
            "1187#23"
        ],
        "ground_truth_answer": "一、依據外國專業人才延攬及僱用法第7條規定，外國專業人才、外國特定專業人才及外國高級專業人才，其本人、配偶、未成年子女及因身心障礙無法自理生活之成年子女，經許可永久居留者，在我國從事工作，不須向勞動部或教育部申請許可。因前開法令為特別法，故符合前開條件者，無須按就業服務法第51條規定申請個人工作許可。二、依據外國專業人才延攬及僱用法第25條規定，經歸化取得我國國籍且兼具外國國籍而未在我國設有戶籍，並持外國護照或我國護照入國從事專業工作或尋職者，得免申請工作許可。因前開法令為特別法，故符合前開條件者，無須按就業服務法第79條規定辦理。"
    }
```

## Source
[Laws and Regulations Database of The Republic of China(Taiwan)](https://law.moj.gov.tw/ENG/Index.aspx)

If you find this dataset works for you, please cite the paper "Wang et al. A Cross-Lingual Statutory Article Retrieval Dataset for Taiwan Legal Studies, ROCLING 2024"
