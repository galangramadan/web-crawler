from urllib.parse import urlparse

def normalize_url(url: str) -> str:
    parsed_url = urlparse(url)
    return (parsed_url.netloc + parsed_url.path).rstrip("/").lower()
