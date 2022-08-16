#!/usr/bin/env python3

import zulip
from typing import Dict, Any

# Pass the path to your zuliprc file here.
client = zulip.Client(config_file="zuliprc")

# Get the 100 last messages sent by "iago@zulip.com" to the stream "Verona"
request: Dict[str, Any] = {
    "anchor": "newest",
    "num_before": 100,
    "num_after": 0,
    "narrow": [
        
        {"operator": "stream", "operand": "397 Bridge"},
        {"operator": "topic", "operand": "Daily LeetCode!"},
        {"operator": "sender", "operand": "patrathewhiz@gmail.com"},
    ],
}
result = client.get_messages(request)
print(result)