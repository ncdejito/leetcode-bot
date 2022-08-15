#!/usr/bin/env python3

import zulip
import os

# Pass the path to your zuliprc file here.
client = zulip.Client(
    api_key = os.environ.get("ZULIP_API_KEY"),
    email = os.environ.get("ZULIP_EMAIL"),
    site = os.environ.get("ZULIP_SITE"),
    # config_file="zuliprc"
)

# Send a stream message
request = {
    "type": "stream",
    "to": "397 Bridge",
    "topic": "Daily LeetCode!",
    # "content": "Hello world!",
    "content": """
**Beginner**: Blind75 at neetcode. io
[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

**Intermediate**: Enjeck's list
08/09 Problems for Tuesday, theme is Factors:
1. [Medium](https://leetcode.com/problems/binary-trees-with-factors/)
1. [Medium](https://leetcode.com/problems/the-kth-factor-of-n)
1. [Hard](https://leetcode.com/problems/largest-component-size-by-common-factor)
    
    """,
}
result = client.send_message(request)
