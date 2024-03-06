#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Gets the number of subscribers of a subreddit.
    Returns 0 if the subreddit is invalid or inaccessible.
    """
    try:
        # Make the request to Reddit API
        response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers={"User-Agent": "GetSubscriberCount"},
            allow_redirects=False
        )
        response.raise_for_status()  # Raise an error for non-200 status codes

        # Parse the response JSON
        data = response.json().get('data')

        # Check if the subreddit exists and has subscriber count
        if data and 'subscribers' in data:
            return data['subscribers']
        else:
            return 0

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
