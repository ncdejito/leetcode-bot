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
    "to": "test-bot",
    "topic": "testing botji",
    "content": "env file works ok",
    # "content": "Hello world! - Heroku",
#     "content": """
# **Beginner**: Blind75 at neetcode. io
# [Best time to Buy and Sell Stocks](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

# **Intermediate**: Enjeck's list
# 07/29 Problems for Friday, theme is Pattern recognition:
# 1. [Easy](https://leetcode.com/problems/word-pattern)
# 1. [Medium](https://leetcode.com/problems/find-and-replace-pattern/)
# 1. [Medium](https://leetcode.com/problems/132-pattern)
    
#     """,
}
result = client.send_message(request)
