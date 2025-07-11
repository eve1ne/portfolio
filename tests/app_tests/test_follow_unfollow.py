"""
Test /following/?target=URL POST request.

EECS 485 Project 2

Andrew DeOrio <awdeorio@umich.edu>
"""
import re
from urllib.parse import urlencode, urlparse

import bs4


def test_unfollow(client, noauth):
    """Click unfollow.  Verify user is removed."""
    # Login
    response = client.post(
        "/accounts/",
        data={
            "username": "awdeorio",
            "password": "chickens",
            "operation": "login"
        },
    )
    # Skip login check when authentication has not been implemented
    if not noauth:
        assert response.status_code == 302

    # Load and parse followers page
    response = client.get("/users/awdeorio/followers/")
    assert response.status_code == 200
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    links = [x.get("href") for x in soup.find_all("a")]
    buttons = [submit.get("name") for button in soup.find_all('form')
               for submit in button.find_all("input") if submit]

    # awdeorio is following michjc and jflinn, but not jag
    assert "not following" not in text.lower()
    assert "unfollow" in buttons
    assert "follow" not in buttons
    assert "/users/michjc/" in links
    assert "/users/jflinn/" in links
    assert "/users/jag/" not in links

    # Unfollow michjc and parse the followers page
    query_string = urlencode({
            "target": "/users/awdeorio/followers/"
        })
    response = client.post(
        f"/following/?{query_string}",
        data={"operation": "unfollow", "username": "michjc"}
    )
    assert response.status_code == 302
    urlpath = urlparse(response.location).path
    assert urlpath == "/users/awdeorio/followers/"

    response = client.get("/users/awdeorio/followers/")
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    links = [x.get("href") for x in soup.find_all("a")]
    buttons = [submit.get("name") for button in soup.find_all('form')
               for submit in button.find_all("input") if submit]

    # awdeorio is no longer following michjc, but he's still following jflinn.
    # michjc still shows up on the page, with the text "not following" and a
    # "follow" button.
    assert "not following" in text.lower()
    assert "unfollow" in buttons
    assert "follow" in buttons
    assert "/users/michjc/" in links
    assert "/users/jflinn/" in links
    assert "/users/jag/" not in links

    response = client.get("/users/awdeorio/following/")
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    links = [x.get("href") for x in soup.find_all("a")]
    srcs = [x.get("src") for x in soup.find_all('img')]

    # Verify text
    assert "not following" not in text.lower()
    assert text.lower().count("following") == 2

    # Verify images: Jason, Jag, Mike
    assert "/uploads/505083b8b56c97429a728b68f31b0b2a089e5113.jpg" in srcs
    assert "/uploads/73ab33bd357c3fd42292487b825880958c595655.jpg" not in srcs
    assert "/uploads/5ecde7677b83304132cb2871516ea50032ff7a4f.jpg" not in srcs

    # Verify links
    assert "/users/jflinn/" in links
    assert "/users/michjc/" not in links
    assert "/users/jag/" not in links


def test_follow(client, noauth):
    """Click follow.  Verify user is added on followers page."""
    # Login
    response = client.post(
        "/accounts/",
        data={
            "username": "awdeorio",
            "password": "chickens",
            "operation": "login"
        },
    )
    # Skip login check when authentication has not been implemented
    if not noauth:
        assert response.status_code == 302

    # Load and parse followers page
    response = client.get("/users/awdeorio/followers/")
    assert response.status_code == 200
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    text = re.sub(r"\s+", " ", soup.get_text())
    links = [x.get("href") for x in soup.find_all("a")]
    buttons = [submit.get("name") for button in soup.find_all('form')
               for submit in button.find_all("input") if submit]

    # awdeorio is following michjc and jfllinn, but not jag
    assert "not following" not in text.lower()
    assert "unfollow" in buttons
    assert "follow" not in buttons
    assert "/users/michjc/" in links
    assert "/users/jflinn/" in links
    assert "/users/jag/" not in links

    # Unfollow michjc and parse the followers page
    query_string = urlencode({
            "target": "/users/awdeorio/followers/"
        })
    response = client.post(
        f"/following/?{query_string}",
        data={"operation": "unfollow", "username": "michjc"}
    )
    assert response.status_code == 302
    urlpath = urlparse(response.location).path
    assert urlpath == "/users/awdeorio/followers/"

    response = client.get("/users/awdeorio/followers/")
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    links = [x.get("href") for x in soup.find_all("a")]
    buttons = [submit.get("name") for button in soup.find_all('form')
               for submit in button.find_all("input") if submit]

    # awdeorio is no longer following michjc, but he's still following jflinn.
    # michjc still shows up on the page, with the text "not following" and a
    # "follow" button.
    assert "not following" in text.lower()
    assert "unfollow" in buttons
    assert "follow" in buttons
    assert "/users/michjc/" in links
    assert "/users/jflinn/" in links
    assert "/users/jag/" not in links

    # Unfollow michjc and parse the followers page
    query_string = urlencode({
            "target": "/users/awdeorio/followers/"
        })
    response = client.post(
        f"/following/?{query_string}",
        data={"operation": "follow", "username": "michjc"}
    )
    assert response.status_code == 302
    urlpath = urlparse(response.location).path
    assert urlpath == "/users/awdeorio/followers/"

    response = client.get("/users/awdeorio/followers/")
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    links = [x.get("href") for x in soup.find_all("a")]
    buttons = [submit.get("name") for button in soup.find_all('form')
               for submit in button.find_all("input") if submit]

    # awdeorio is again following michjc
    assert "not following" not in text.lower()
    assert "unfollow" in buttons
    assert "follow" not in buttons
    assert "/users/michjc/" in links
    assert "/users/jflinn/" in links
    assert "/users/jag/" not in links


def test_follow_jag(client, noauth):
    """Click follow, then check /users/<user_url_slug>/following/ ."""
    # Login
    response = client.post(
        "/accounts/",
        data={
            "username": "awdeorio",
            "password": "chickens",
            "operation": "login"
        },
    )
    # Skip login check when authentication has not been implemented
    if not noauth:
        assert response.status_code == 302

    query_string = urlencode({
            "target": "/users/awdeorio/followers/"
        })
    response = client.post(
        f"/following/?{query_string}",
        data={"operation": "follow", "username": "jag"}
    )
    assert response.status_code == 302

    # Load and parse following page
    response = client.get("/users/awdeorio/following/")
    assert response.status_code == 200
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    srcs = [x.get("src") for x in soup.find_all('img')]
    links = [x.get("href") for x in soup.find_all("a")]

    # Verify links in header are present
    assert "/" in links
    assert "/explore/" in links
    assert "/users/awdeorio/" in links

    # Verify text
    # Check for following 3 people + the header "following" at the top
    assert text.lower().count("following") == 4
    assert "not following" not in text.lower()

    # Verify images: Mike, Jason, Jag
    assert "/uploads/5ecde7677b83304132cb2871516ea50032ff7a4f.jpg" in srcs
    assert "/uploads/505083b8b56c97429a728b68f31b0b2a089e5113.jpg" in srcs
    assert "/uploads/73ab33bd357c3fd42292487b825880958c595655.jpg" in srcs

    # Verify links
    assert "/users/jflinn/" in links
    assert "/users/michjc/" in links
    assert "/users/jag/" in links
