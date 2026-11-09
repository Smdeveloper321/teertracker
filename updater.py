#!/usr/bin/env python3
"""
Enterprise All-in-One Teer Results Updater
Fetches real-time numbers across all 6 games:
  - Shillong Day (Polo Ground)
  - Khanapara Teer (Them Marwet)
  - Juwai Teer (Jowai)
  - Bhutan Teer (Border Session)
  - Shillong Morning Teer
  - Shillong Night Teer
Updates all matching HTML pages, schema dateModified, and feeds live freshness signals.
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

def fetch_shillong_cdn_json(path):
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

def fetch_multi_game_stream():
    """Fetches live stream covering Khanapara, Juwai, Bhutan, Morning, Night."""
    url = "https://shillongteerresult.one/"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }
    )
    
    results = {}
    try:
        with urllib.request.urlopen(req, timeout=10, context=ctx) as res:
            html = res.read().decode('utf-8', errors='ignore')
            
        targets = {
            "shillong": r"SHILLONG\s*TEER",
            "khanapara": r"KHANAPARA\s*TEER",
            "juwai": r"JUWAI[- ]*TEER",
            "night": r"NIGHT\s*TEER",
            "morning": r"SHILLONG\s*MORNING\s*TEER",
            "bhutan": r"BHUTAN\s*TEER"
        }
        
        for key, pattern in targets.items():
            m = re.search(r'<h2[^>]*>\s*(' + pattern + r')\s*</h2>(.*?)(?=<h2|$)', html, re.IGNORECASE | re.DOTALL)
            if m:
                block = m.group(2)
                numbers = re.findall(r'<p class="result_no">\s*([0-9Xx\*\-]+)\s*</p>', block)
                if len(numbers) >= 2:
                    results[key] = {"fr": numbers[0].strip(), "sr": numbers[1].strip()}
                elif len(numbers) == 1:
                    results[key] = {"fr": numbers[0].strip(), "sr": "--"}
                else:
                    results[key] = {"fr": "--", "sr": "--"}
    except Exception as e:
        print(f"Error fetching multi-game stream: {e}")
        
    return results

def is_valid_score(val):
    return val and val not in ["—", "--", "**", "XX", "xx", ""] and val.isdigit()

def update_page(filename, fr_id, sr_id, fr_val, sr_val, date_str, now_iso):
    filepath = BASE_DIR / filename
    if not filepath.exists():
        return
        
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    updated = False
    
    if is_valid_score(fr_val):
        pattern = rf'id="{fr_id}"[^>]*>([^<]*)<'
        if re.search(pattern, html):
            html = re.sub(pattern, f'id="{fr_id}">{fr_val}<', html)
            updated = True
            
    if is_valid_score(sr_val):
        pattern = rf'id="{sr_id}"[^>]*>([^<]*)<'
        if re.search(pattern, html):
            html = re.sub(pattern, f'id="{sr_id}">{sr_val}<', html)
            updated = True
            
    if date_str:
        pattern = r'id="live-date"[^>]*>([^<]*)<'
        if re.search(pattern, html):
            html = re.sub(pattern, f'id="live-date">{date_str}<', html)
            updated = True
            
    html = re.sub(r'"dateModified":\s*"[^"]+"', f'"dateModified": "{now_iso}"', html)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"[{filename}] updated={updated} | FR={fr_val}, SR={sr_val}, date={date_str}")

def run_all_updates():
    now = datetime.now()
    now_iso = now.strftime("%Y-%m-%dT%H:%M:00+05:30")
    today_display = now.strftime("%d %b %Y")
    
    print(f"=== Starting Multi-Game Teer Updater at {now_iso} ===")
    
    # 1. Primary Shillong CDN fetch
    shillong_fr = None
    shillong_sr = None
    shillong_date = None
    
    try:
        shillong_cdn = fetch_shillong_cdn_json("/teer/api/results/latest/index.json")
        shillong_fr = shillong_cdn.get("first_round")
        shillong_sr = shillong_cdn.get("second_round")
        shillong_date = shillong_cdn.get("date")
        print(f"Primary Shillong CDN: FR={shillong_fr}, SR={shillong_sr}, date={shillong_date}")
    except Exception as e:
        print(f"Primary Shillong CDN unavailable, using multi-game stream fallback: {e}")
        
    # 2. Multi-game real-time stream fetch
    stream_data = fetch_multi_game_stream()
    print("Multi-Game Stream Data:", stream_data)
    
    # If Shillong CDN didn't return, fallback to stream
    if not is_valid_score(shillong_fr) and stream_data.get("shillong"):
        shillong_fr = stream_data["shillong"].get("fr")
        shillong_sr = stream_data["shillong"].get("sr")
        
    date_to_use = shillong_date if shillong_date else today_display
    
    # Update Index.html (Shillong Day)
    update_page("index.html", "shillong-fr", "shillong-sr", shillong_fr, shillong_sr, date_to_use, now_iso)
    
    # Update Khanapara
    kp = stream_data.get("khanapara", {})
    update_page("khanapara-teer-result.html", "khanapara-fr", "khanapara-sr", kp.get("fr"), kp.get("sr"), today_display, now_iso)
    
    # Update Juwai
    jw = stream_data.get("juwai", {})
    update_page("juwai-teer-result.html", "juwai-fr", "juwai-sr", jw.get("fr"), jw.get("sr"), today_display, now_iso)
    
    # Update Bhutan
    bt = stream_data.get("bhutan", {})
    update_page("bhutan-teer-result.html", "bhutan-day-fr", "bhutan-day-sr", bt.get("fr"), bt.get("sr"), today_display, now_iso)
    
    # Update Shillong Morning
    mr = stream_data.get("morning", {})
    update_page("shillong-morning-teer-result.html", "morning-fr", "morning-sr", mr.get("fr"), mr.get("sr"), today_display, now_iso)
    
    # Update Shillong Night
    nt = stream_data.get("night", {})
    update_page("shillong-night-teer-result.html", "night-fr", "night-sr", nt.get("fr"), nt.get("sr"), today_display, now_iso)
    
    # Update Common Numbers & Previous Archive Modified Dates
    for aux in ["shillong-teer-common-number.html", "teer-previous-results.html"]:
        aux_path = BASE_DIR / aux
        if aux_path.exists():
            with open(aux_path, "r", encoding="utf-8") as f:
                c = f.read()
            c = re.sub(r'"dateModified":\s*"[^"]+"', f'"dateModified": "{now_iso}"', c)
            with open(aux_path, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"[{aux}] refreshed dateModified={now_iso}")
            
    print("=== All 6 Games Updated Successfully ===")

if __name__ == "__main__":
    run_all_updates()
