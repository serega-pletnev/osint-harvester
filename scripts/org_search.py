#!/usr/bin/env python3
"""
OSINT Org Search — базовый пример
Сбор информации о домене через crt.sh
"""

import requests

def search_crtsh(domain: str):
    url = f"https://crt.sh/?q={domain}&output=json"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return {"error": "not found"}

if __name__ == "__main__":
    print("=== Org Search Demo ===")
    print(search_crtsh("example.com"))

