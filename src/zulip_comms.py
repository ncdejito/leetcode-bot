import zulip
import os

# Staging
address = {
    "staging": {
        "type": "stream",
        "to": "test-bot",
        "topic": "testing botji",
    },
    "prod": {
        "type": "stream",
        "to": "397 Bridge",
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


def send(content="test", client=None, destination="staging"):
    # Send a stream message
    request = address[destination]
    request["content"] = content
    result = client.send_message(request)


def get_posts(num_before=10, client=None, destination="staging"):
    # Get the latest messages sent by "iago@zulip.com" to the stream "Verona"
    request = address[destination]
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
    result = client.get_messages(request)
    return result
