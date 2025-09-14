#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re, sys, json, argparse, datetime as dt
import requests, pandas as pd
from bs4 import BeautifulSoup
import tldextract, whois

HEADERS={"User-Agent":"Mozilla/5.0"}
REQ_TIMEOUT=15

def safe_get(url,params=None):
    try:
        r=requests.get(url,headers=HEADERS,params=params,timeout=REQ_TIMEOUT)
        if r.status_code==200: return r
    except: return None

def now_iso(): return dt.datetime.utcnow().replace(microsecond=0).isoformat()+"Z"

def ddg_search(q, n=20):
    out=[]; r=safe_get("https://duckduckgo.com/html/",{"q":q})
    if not r: return out
    soup=BeautifulSoup(r.text,"html.parser")
    for a in soup.select("a.result__a")[:n]:
        out.append({"title":a.text.strip(),"url":a.get("href","")})
    return out

def crtsh(domain):
    r=safe_get("https://crt.sh/",{"q":f"%.{domain}","output":"json"})
    if not r: return []
    try: data=r.json()
    except: return []
    subs=set()
    for row in data: subs.update([h.strip() for h in row.get("name_value","").split("\n")])
    return sorted(subs)

def whois_domain(domain):
    try: return dict(whois.whois(domain))
    except: return {}

def write(path,data):
    import datetime as _dt
    def _san(o):
        if isinstance(o, (_dt.date, _dt.datetime)): return o.isoformat()
        if isinstance(o, (set,)): return list(o)
        return str(o)
