import zulip
import os
import re
from bs4 import BeautifulSoup

# Staging
address = {
    "staging": {
        "type": "stream",
        "to": "test-bot",
        "topic": "testing botji",
    },
    "prod": {
        "type": "stream",
        "to": "🧑‍💻 current batches",
        "topic": "Daily LeetCode!",
    },
}


def get_client():
    return zulip.Client(
        api_key=os.environ.get("ZULIP_API_KEY"),
        email=os.environ.get("ZULIP_EMAIL"),
        site=os.environ.get("ZULIP_SITE"),
        # config_file="zuliprc"
    )


def send(content="test", client=None, to="staging"):
    # Send a stream message
    request = address[to]
    request["content"] = content
    result = client.send_message(request)


def get_posts(num_before=10, client=None, _from="staging"):
    # Get the latest messages sent by "iago@zulip.com" to the stream "Verona"
    request = address[_from]
    request = {
        "anchor": "newest",
        "num_before": num_before,
        "num_after": 0,
        "narrow": [
            {"operator": "stream", "operand": request["to"]},
            {"operator": "topic", "operand": request["topic"]},
            {
                "operator": "sender",
                "operand": "leetcode-test-bot@recurse.zulipchat.com",
            },
        ],
    }
    results = client.get_messages(request)
    recs = []
    for msg in results["messages"]:
        html = BeautifulSoup(msg["content"], "html.parser")
        text = html.get_text()
        recs.append(text)

    return recs


def no_duplicate_posts(post, from_latest_x_posts=10, _in="staging"):
    client = get_client()

    recs = get_posts(
        num_before=from_latest_x_posts, client=client, _from="staging"
    )

    occurrences = 0
    for text in recs:
        sent = clean_sent(post)
        received = clean_received(text)
        if sent == received:
            occurrences += 1
            print(f"Sent: {sent}")
            print(f"Received: {received}")

    return occurrences == 0


def clean(s, pattern):
    return " ".join(re.compile(pattern).findall(s)).lower().replace(" ", "")


def clean_sent(post):
    # finds problem names inside square brackets e.g. problem 1 in [problem 1](neetcode.io)
    return clean(post, "\[.*\]").replace("[", "").replace("]", "")


def clean_received(text):
    # finds problem names right outside parentheses e.g. problem 1 in (easy) problem 1\n
    return clean(text, "\).*").replace(")", "")
