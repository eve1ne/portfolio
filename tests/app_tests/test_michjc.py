"""
Test log in and log out michjc.

EECS 485 Project 2

Andrew DeOrio <awdeorio@umich.edu>
"""
import re
from urllib.parse import urlparse
from urllib.parse import urlencode
import bs4


def test_login(client):
    """Login michjc.

    Note: 'client' is a fixture fuction that provides a Flask test server
    interface with a clean database.  It is implemented in conftest.py and
    reused by many tests.  Docs: https://docs.pytest.org/en/latest/fixture.html
    """
    response = client.post(
        "/accounts/",
        data={
            "username": "michjc",
            "password": "password",
            "operation": "login"
        },
    )
    assert response.status_code == 302
    urlpath = urlparse(response.location).path
    assert urlpath == "/"


def test_index(client):
    """Verify all images are present in / URL for michjc user.

    Note: 'client' is a fixture fuction that provides a Flask test server
    interface with a clean database.  It is implemented in conftest.py and
    reused by many tests.  Docs: https://docs.pytest.org/en/latest/fixture.html
    """
    # Log in
    response = client.post(
        "/accounts/",
        data={
            "username": "michjc",
            "password": "password",
            "operation": "login"
        },
    )
    assert response.status_code == 302

    # Load and parse index page
    response = client.get("/")
    assert response.status_code == 200
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    srcs = [x.get("src") for x in soup.find_all('img')]

    # Verify images present of Jag, DeOrio, postid 4, postid 3, postid 1
    assert "/uploads/73ab33bd357c3fd42292487b825880958c595655.jpg" in srcs
    assert "/uploads/2ec7cf8ae158b3b1f40065abfb33e81143707842.jpg" in srcs
    assert "/uploads/e1a7c5c32973862ee15173b0259e3efdb6a391af.jpg" in srcs
    assert "/uploads/9887e06812ef434d291e4936417d125cd594b38a.jpg" in srcs
    assert "/uploads/e1a7c5c32973862ee15173b0259e3efdb6a391af.jpg" in srcs
    assert "/uploads/122a7d27ca1d7420a1072f695d9290fad4501a41.jpg" in srcs


def test_postid_4(client):
    """Check default content at /posts/4/ URL."""
    # Log in
    response = client.post(
        "/accounts/",
        data={
            "username": "michjc",
            "password": "password",
            "operation": "login"
        },
    )
    assert response.status_code == 302

    # Load and parse /posts/4/ page
    response = client.get("/posts/4/")
    assert response.status_code == 200
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    links = [x.get("href") for x in soup.find_all("a")]
    srcs = [x.get("src") for x in soup.find_all('img')]
    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    buttons = [submit.get("name") for button in soup.find_all('form')
               for submit in button.find_all("input") if submit]

    # Verify links in header are present
    assert "/" in links
    assert "/explore/" in links
    assert "/users/michjc/" in links

    # Verify post owner links are present
    assert "/users/jag/" in links

    # Verify no unexpected links to users are present
    assert "/users/jflinn/" not in links
    assert "/users/awdeorio/" not in links

    # Verify images present of jag, postid 4
    assert "/uploads/73ab33bd357c3fd42292487b825880958c595655.jpg" in srcs
    assert "/uploads/2ec7cf8ae158b3b1f40065abfb33e81143707842.jpg" in srcs

    # Verify that none of the other user images are present
    assert "/uploads/e1a7c5c32973862ee15173b0259e3efdb6a391af.jpg" not in srcs
    assert "/uploads/5ecde7677b83304132cb2871516ea50032ff7a4f.jpg" not in srcs
    assert "/uploads/505083b8b56c97429a728b68f31b0b2a089e5113.jpg" not in srcs

    # Verify that none of the other post's images are present
    assert "/uploads/9887e06812ef434d291e4936417d125cd594b38a.jpg" not in srcs
    assert "/uploads/ad7790405c539894d25ab8dcf0b79eed3341e109.jpg" not in srcs
    assert "/uploads/122a7d27ca1d7420a1072f695d9290fad4501a41.jpg" not in srcs

    # Verify expected content is in text on generated HTML page
    assert text.count("jag") == 2
    assert "0 likes" in text
    assert "Saw this on the diag yesterday!" in text

    # Verify unexpected buttons are not present in the page
    assert "unlike" not in buttons  # No current likes
    assert "follow" not in buttons
    assert "unfollow" not in buttons
    assert "uncomment" not in buttons  # No comments from current user
    assert "delete" not in buttons  # Post not owner by current user


def test_user(client):
    """Check default content at /users/michjc/ URL."""
    response = client.post(
        "/accounts/",
        data={
            "username": "michjc",
            "password": "password",
            "operation": "login"
        },
    )
    assert response.status_code == 302

    # Load and parse user page
    response = client.get("/users/michjc/")
    assert response.status_code == 200
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    links = [x.get("href") for x in soup.find_all("a")]
    buttons = [submit.get("name") for button in soup.find_all('form')
               for submit in button.find_all("input") if submit]

    # Verify links in header
    assert "/" in links
    assert "/explore/" in links
    assert "/users/michjc/" in links

    # Links specific to /users/michjc/followers/
    assert "/users/michjc/followers/" in links
    assert "/users/michjc/following/" in links
    assert "/users/jflinn/followers/" not in links
    assert "/users/jflinn/following/" not in links
    assert "/users/awdeorio/followers/" not in links
    assert "/users/awdeorio/following/" not in links
    assert "/users/jag/followers/" not in links
    assert "/users/jag/following/" not in links
    assert "/posts/1/" not in links
    assert "/posts/2/" not in links
    assert "/posts/3/" not in links
    assert "/posts/4/" not in links

    # Verify text
    assert "0 posts" in text
    assert "3 followers" in text.lower()
    assert "2 following" in text.lower()
    assert "Michael Cafarella" in text
    assert "Edit profile" in text
    assert "not following" not in text.lower()
    assert "login" not in text
    assert "No posts yet." in text
    assert text.count("michjc") == 2
    assert text.lower().count("following") == 1

    # Verify buttons
    assert "file" in buttons
    assert "create_post" in buttons
    assert "delete_post" not in buttons
    assert "delete" not in buttons
    assert "logout" in buttons


def test_explore(client):
    """Verify default content at /explore/ with michjc logged in."""
    # Login
    response = client.post(
        "/accounts/",
        data={
            "username": "michjc",
            "password": "password",
            "operation": "login"
        },
    )
    assert response.status_code == 302

    # Load and parse explore page
    response = client.get("/explore/")
    assert response.status_code == 200
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    srcs = [x.get("src") for x in soup.find_all('img')]
    links = [x.get("href") for x in soup.find_all("a")]
    buttons = [submit.get("name") for button in soup.find_all('form')
               for submit in button.find_all("input") if submit]

    # Verify links in header
    assert "/" in links
    assert "/explore/" in links
    assert "/users/michjc/" in links

    # Verify links specific to /explore/
    assert "/users/jflinn/" in links
    assert "/users/jag/" not in links
    assert "/users/awdeorio/" not in links

    # Verify images
    assert "/uploads/505083b8b56c97429a728b68f31b0b2a089e5113.jpg" in srcs
    assert "/uploads/73ab33bd357c3fd42292487b825880958c595655.jpg" not in srcs
    assert "/uploads/e1a7c5c32973862ee15173b0259e3efdb6a391af.jpg" not in srcs
    assert "/uploads/5ecde7677b83304132cb2871516ea50032ff7a4f.jpg" not in srcs

    # Verify buttons
    assert "follow" in buttons
    assert "username" in buttons
    assert "unfollow" not in buttons
    assert "commentid" not in buttons
    assert "postid" not in buttons
    assert "delete" not in buttons


def test_followers(client):
    """Verify correct followers."""
    # Log in
    response = client.post(
        "/accounts/",
        data={
            "username": "michjc",
            "password": "password",
            "operation": "login"
        },
    )
    assert response.status_code == 302

    # Load and parse followers page
    response = client.get("/users/michjc/followers/")
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
    assert "/users/michjc/" in links

    # Links specific to /users/awdeorio/followers/
    assert "/users/jflinn/" in links
    assert "/users/michjc/" in links
    assert "/users/jag/" in links

    # Check for images: Drew, Jason, Jag
    assert "/uploads/e1a7c5c32973862ee15173b0259e3efdb6a391af.jpg" in srcs
    assert "/uploads/73ab33bd357c3fd42292487b825880958c595655.jpg" in srcs
    assert "/uploads/505083b8b56c97429a728b68f31b0b2a089e5113.jpg" in srcs

    # Check for text
    assert text.lower().count("following") == 3
    assert text.lower().count("not following") == 1
    assert "jflinn" in text
    assert "jag" in text
    assert "awdeorio" in text
    assert "followers" in text.lower()

    # Check for buttons
    assert "unfollow" in buttons
    assert "username" in buttons
    assert "follow" in buttons
    assert "following" not in buttons


def test_unfollow(client):
    """Click unfollow.  Verify user is removed."""
    # Log in
    response = client.post(
        "/accounts/",
        data={
            "username": "michjc",
            "password": "password",
            "operation": "login"
        },
    )
    assert response.status_code == 302

    # Unfollow awdeorio and parse the followers page
    query_string = urlencode({
            "target": "/users/michjc/followers/"
        })
    response = client.post(
        f"/following/?{query_string}",
        data={"operation": "unfollow", "username": "awdeorio"}
    )
    assert response.status_code == 302
    urlpath = urlparse(response.location).path
    assert urlpath == "/users/michjc/followers/"

    response = client.get("/users/michjc/followers/")
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    links = [x.get("href") for x in soup.find_all("a")]
    buttons = [submit.get("name") for button in soup.find_all('form')
               for submit in button.find_all("input") if submit]

    assert text.lower().count("not following") == 2
    assert "unfollow" in buttons
    assert "follow" in buttons
    assert "/users/awdeorio/" in links
    assert "/users/jflinn/" in links
    assert "/users/jag/" in links


def test_follow(client):
    """Click follow.  Verify user is added."""
    # Log in
    response = client.post(
        "/accounts/",
        data={
            "username": "michjc",
            "password": "password",
            "operation": "login"
        },
    )
    assert response.status_code == 302

    # Follow jflinn and parse the followers page
    query_string = urlencode({
            "target": "/users/michjc/followers/"
        })
    response = client.post(
        f"/following/?{query_string}",
        data={"operation": "follow", "username": "jflinn"}
    )
    assert response.status_code == 302
    urlpath = urlparse(response.location).path
    assert urlpath == "/users/michjc/followers/"

    response = client.get("/users/michjc/followers/")
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    links = [x.get("href") for x in soup.find_all("a")]
    buttons = [submit.get("name") for button in soup.find_all('form')
               for submit in button.find_all("input") if submit]

    # michjc now follows every user.
    assert "not following" not in text.lower()
    assert text.lower().count("following") == 3
    assert "unfollow" in buttons
    assert "follow" not in buttons
    assert "/users/awdeorio/" in links
    assert "/users/jflinn/" in links
    assert "/users/jag/" in links


def test_following(client):
    """Check default content at /users/michjc/following/ URL."""
    # Login
    response = client.post(
        "/accounts/",
        data={
            "username": "michjc",
            "password": "password",
            "operation": "login"
        },
    )
    assert response.status_code == 302

    # Load and parse following page
    response = client.get("/users/michjc/following/")
    assert response.status_code == 200
    soup = bs4.BeautifulSoup(response.data, "html.parser")
    text = soup.get_text()
    text = re.sub(r"\s+", " ", text)
    links = [x.get("href") for x in soup.find_all("a")]
    srcs = [x.get("src") for x in soup.find_all('img')]

    # Verify text
    assert text.lower().count("following") == 3
    assert "not following" not in text.lower()

    # Verify images: Andrew and Jag, not Jason
    assert "/uploads/e1a7c5c32973862ee15173b0259e3efdb6a391af.jpg" in srcs
    assert "/uploads/73ab33bd357c3fd42292487b825880958c595655.jpg" in srcs
    assert "/uploads/505083b8b56c97429a728b68f31b0b2a089e5113.jpg" not in srcs

    # Verify links
    assert "/users/jflinn/" not in links
    assert "/users/michjc/" in links
    assert "/users/awdeorio/" in links
    assert "/users/jag/" in links
