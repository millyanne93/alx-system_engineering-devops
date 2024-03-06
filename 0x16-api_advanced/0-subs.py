#!/usr/bin/python3

''' This module contains the function number_of_subscribers '''
import json
import requests


def number_of_subscribers(subreddit):
    ''' Gets the number of subscribers of a subreddit '''
    try:
        response = requests.get("https://www.reddit.com/r/{}/about.json"
                                .format(subreddit),
                                headers={"User-Agent": "GetSubscriberCount"},
                                allow_redirects=False)
        data = response.json().get('data')
        if data:
            return data['subscribers']
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
