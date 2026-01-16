#!/usr/bin/env python3
"""
Скрипт для импорта заданий в CTFd
"""

import requests
import json
import sys

def import_challenges(ctfd_url, token, challenges_file):
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    
    with open(challenges_file) as f:
        data = json.load(f)
    
    success = 0
    failed = 0
    
    for challenge in data["challenges"]:
        # Создаём задание
        try:
            resp = requests.post(
                f"{ctfd_url}/api/v1/challenges",
                headers=headers,
                json={
                    "name": challenge["name"],
                    "category": challenge["category"],
                    "description": challenge["description"],
                    "value": challenge["value"],
                    "type": "standard",
                    "state": "visible"
                }
            )
            
            if resp.status_code == 200:
                challenge_id = resp.json()["data"]["id"]
                
                # Добавляем флаги
                for flag in challenge.get("flags", []):
                    requests.post(
                        f"{ctfd_url}/api/v1/flags",
                        headers=headers,
                        json={
                            "challenge_id": challenge_id,
                            "type": flag.get("type", "static"),
                            "content": flag["content"]
                        }
                    )
                
                # Добавляем подсказки
                for hint in challenge.get("hints", []):
                    requests.post(
                        f"{ctfd_url}/api/v1/hints",
                        headers=headers,
                        json={
                            "challenge_id": challenge_id,
                            "content": hint["content"],
                            "cost": hint.get("cost", 0)
                        }
                    )
                
                print(f"✓ Created: {challenge['name']}")
                success += 1
            else:
                print(f"✗ Failed: {challenge['name']} - {resp.status_code}")
                failed += 1
                
        except Exception as e:
            print(f"✗ Error: {challenge['name']} - {str(e)}")
            failed += 1
    
    print(f"\nResults: {success} created, {failed} failed")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python import_to_ctfd.py <CTFd_URL> <API_TOKEN>")
        print("Example: python import_to_ctfd.py http://localhost:8000 your_token_here")
        sys.exit(1)
    
    ctfd_url = sys.argv[1].rstrip('/')
    token = sys.argv[2]
    
    import_challenges(ctfd_url, token, "challenges.json")
