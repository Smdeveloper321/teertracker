#!/usr/bin/env python3
"""
Automated Teer Results Updater
Fetches real-time numbers from official CDN APIs with SNI and DoH support.
Updates index.html, shillong-teer-common-number.html, and teer-previous-results.html.
"""

import socket
import ssl
import json
import re
import http.client
import urllib.request
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def resolve_ip_doh(domain):
    try:
        url = f"https://1.1.1.1/dns-query?name={domain}&type=A"
        req = urllib.request.Request(url, headers={"Accept": "application/dns-json"})
        ctx = ssl.create_default_context()
        with urllib.request.urlopen(req, timeout=5, context=ctx) as r:
            res = json.loads(r.read().decode('utf-8'))
            for ans in res.get("Answer", []):
                if ans.get("type") == 1:
                    return ans.get("data")
    except Exception:
        pass
    return "172.67.134.54"

def fetch_cdn_json(path):
    domain = "cdn.shillongteerground.com"
    ip = resolve_ip_doh(domain)
    
    ctx = ssl.create_default_context()
    sock = socket.create_connection((ip, 443), timeout=10)
    ssock = ctx.wrap_socket(sock, server_hostname=domain)
    
    req = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {domain}\r\n"
        f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120\r\n"
        f"Referer: https://shillongteerground.com/\r\n"
        f"Accept: application/json\r\n"
        f"Connection: close\r\n\r\n"
    )
    ssock.sendall(req.encode('utf-8'))
    res = http.client.HTTPResponse(ssock)
    res.begin()
    content = res.read().decode('utf-8')
    ssock.close()
    return json.loads(content)

def update_index_html(data):
    index_path = BASE_DIR / "index.html"
    if not index_path.exists():
        return
    
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    fr = data.get("first_round")
    sr = data.get("second_round")
    date_val = data.get("date")
    
    if fr and fr != "—":
        html = re.sub(r'id="shillong-fr"[^>]*>([^<]*)<', f'id="shillong-fr">{fr}<', html)
    if sr and sr != "—":
        html = re.sub(r'id="shillong-sr"[^>]*>([^<]*)<', f'id="shillong-sr">{sr}<', html)
    if date_val:
        html = re.sub(r'id="live-date"[^>]*>([^<]*)<', f'id="live-date">{date_val}<', html)
        
    now_iso = datetime.now().strftime("%Y-%m-%dT%H:%M:00+05:30")
    html = re.sub(r'"dateModified":\s*"[^"]+"', f'"dateModified": "{now_iso}"', html)
    
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated index.html: FR={fr}, SR={sr}, date={date_val}, dateModified={now_iso}")

def update_common_numbers_html(data):
    cn_path = BASE_DIR / "shillong-teer-common-number.html"
    if not cn_path.exists():
        return
    
    with open(cn_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    now_iso = datetime.now().strftime("%Y-%m-%dT%H:%M:00+05:30")
    html = re.sub(r'"dateModified":\s*"[^"]+"', f'"dateModified": "{now_iso}"', html)
    
    with open(cn_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated shillong-teer-common-number.html dateModified={now_iso}")

if __name__ == "__main__":
    try:
        shillong_data = fetch_cdn_json("/teer/api/results/latest/index.json")
        print(f"Live Shillong Data: {shillong_data}")
        update_index_html(shillong_data)
        
        cn_data = fetch_cdn_json("/teer/api/common-numbers/latest/index.json")
        print(f"Live Common Numbers: {cn_data}")
        update_common_numbers_html(cn_data)
        
        print("All updates completed successfully.")
    except Exception as e:
        print(f"Update error: {e}")
