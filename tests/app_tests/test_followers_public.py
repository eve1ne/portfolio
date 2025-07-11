"""
Test /users/<user_url_slug/followers/ URLs.

EECS 485 Project 2

Andrew DeOrio <awdeorio@umich.edu>
"""
import re

import bs4


def test_awdeorio_followers(client, noauth):
    """Check default content at /users/awdeorio/followers/ URL."""
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

    # Load and parse followers pages
    response = client.get("/users/awdeorio/followers/")
    assert response.status_code == 200
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    links = [x.get("href") for x in soup.find_all("a")]
    srcs = [x.get("src") for x in soup.find_all('img')]
    buttons = [submit.get("name") for button in soup.find_all('form')
               for submit in button.find_all("input") if submit]

    # Every page should have a header
    assert "/" in links
    assert "/explore/" in links
    assert "/users/awdeorio/" in links

    # Links specific to /users/awdeorio/followers/
    assert "/users/jflinn/" in links
    assert "/users/michjc/" in links
    assert "/users/jag/" not in links

    # Check for images: Mike, Jason, Jag
    assert "/uploads/5ecde7677b83304132cb2871516ea50032ff7a4f.jpg" in srcs
    assert "/uploads/505083b8b56c97429a728b68f31b0b2a089e5113.jpg" in srcs
    assert "/uploads/73ab33bd357c3fd42292487b825880958c595655.jpg" not in srcs

    # Check for text
    assert text.lower().count("following") == 2
    assert "jflinn" in text
    assert "following" in text.lower()
    assert "michjc" in text
    assert "followers" in text.lower()
    assert "not following" not in text.lower()

    # Check for buttons
    assert "unfollow" in buttons
    assert "username" in buttons
    assert "follow" not in buttons
    assert "following" not in buttons


def test_files(client, noauth):
    """Verify all expected files exist."""
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

    # Load images
    response = client.get(
        "/uploads/122a7d27ca1d7420a1072f695d9290fad4501a41.jpg"
    )
    assert response.status_code == 200
    response = client.get(
        "/uploads/9887e06812ef434d291e4936417d125cd594b38a.jpg"
    )
    assert response.status_code == 200
