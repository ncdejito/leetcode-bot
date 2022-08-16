# -*- coding: utf-8 -*-
"""
Ran on Google Colab
"""

def dict_to_twocolumndf():
    import json
    import pandas as pd
    from bs4 import BeautifulSoup
    from datetime import datetime, timezone

    enjeck = json.load(open("enjeck.json","r"))

    recs = []
    for msg in enjeck["messages"]:
        html = BeautifulSoup(msg['content'])
        text = html.get_text()
        dt = datetime.fromtimestamp(msg['timestamp'])
        recs.append((dt, text))

    df = pd.DataFrame(recs)

    df.columns = ['date','text']

    df2 = df[df.text.str.contains('Problem')].reset_index(drop=True)

    print(df2.text[84])

    df2.to_csv("enjeck.csv",index=False)

def twocolumndf_to_processeddf():
    import pandas as pd
    from tqdm import tqdm

    raw = pd.read_csv("data/raw/enjeck.csv")

    def text_to_df(text):
        lines = text.split("\n")
        category = lines.pop(0).lower().split("theme is")[-1].replace(":","").strip().capitalize()
        recs = []
        for line in lines:
            parts = line.split(": ")
            difficulty = parts[0].strip().capitalize()
            link = parts[1].strip()
            problem = link.split("/")[-2].replace("-", " ").title()
            recs.append((category, difficulty, problem, link))
        df = pd.DataFrame(recs)
        df.columns = ["Category", "Difficulty", "Problem", "Link"]

        return df

    dfs = []
    for i, row in tqdm(raw.iterrows(), total = len(raw)):
        df = text_to_df(row["text"])
        df["date"] = row["date"]
        dfs.append(df)
    df2 = pd.concat(dfs, axis = 0)
    df2.to_csv("data/enjeck.csv",index=False)



