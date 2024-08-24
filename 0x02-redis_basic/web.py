#!/usr/bin/env python3
"""Implements caching"""
import redis
import requests
from typing import Optional


r = redis.Redis()


def get_page(url: str) -> Optional[str]:
    """Fetch the HTML content of a URL and cache it in Redis.

    Args:
        url (str): The URL to fetch.

    Returns:
        Optional[str]: The HTML content of the URL, or None if the request fails.
    """
    count_key = f"count:{url}"
    r.incr(count_key)
    cached_content = r.get(url)
    if cached_content:
        return cached_content.decode('utf-8')
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        r.setex(url, 10, content)
        return content
    
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
