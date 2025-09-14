#!/usr/bin/env python3
"""
OSINT Person Search — базовый пример
Поиск по email / username через публичные сервисы
"""

import requests

def check_hibp(email: str):
    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    headers = {"User-Agent": "OSINT-Harvester"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json()
    return {"error": "not found or blocked"}

if __name__ == "__main__":
    print("=== Person Search Demo ===")
    print(check_hibp("test@example.com"))

