from main import main, client
from bs4 import BeautifulSoup
from src.zulip_comms import get_posts
import time
import re


def test_main():

    # send post
    post = main(destination="staging")

    time.sleep(1)
    results = get_posts(num_before=1, client=client)
    recs = []
    for msg in results["messages"]:
        html = BeautifulSoup(msg["content"])
        text = html.get_text()
        recs.append(text)

    def clean(s, pattern):
        return (
            " ".join(re.compile(pattern).findall("\n".join(s)))
            .lower()
            .replace(" ", "")
        )

    clean_post = clean(post, "\[.*\]").replace("[", "").replace("]", "")

    clean_text = clean(text, "\).*").replace(")", "")

    assert clean_post == clean_text
