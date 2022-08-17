from bs4 import BeautifulSoup
import pytest

from src.zulip_comms import get_client, get_posts, send

client = get_client()


# @pytest.mark.skip(reason="")
def test_get_posts():
    results = get_posts(num_before=1, client=client, _from="staging")
    assert len(results) > 0


# @pytest.mark.skip(reason="")
def test_send():
    send("test send", client, to="staging")

    results = get_posts(num_before=1, client=client, _from="staging")
    recs = []
    for msg in results["messages"]:
        html = BeautifulSoup(msg["content"], "html.parser")
        text = html.get_text()
        recs.append(text)

    assert text == "test send"
