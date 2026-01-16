#!/usr/bin/env python3
"""
Скрипт для импорта заданий в CTFd с автоматической заменой HOST
Использование: python3 import_challenges.py <CTFd_URL> <API_TOKEN> <CHALLENGES_HOST>

Пример:
  python3 import_challenges.py http://localhost:8000 abc123token 192.168.1.100
"""

import requests
import json
import sys

def import_challenges(ctfd_url, token, challenges_host):
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    
    with open("challenges.json") as f:
        data = json.load(f)
    
    success = 0
    failed = 0
    
    print(f"\n{'='*50}")
    print(f"CTFd URL: {ctfd_url}")
    print(f"Challenges Host: {challenges_host}")
    print(f"{'='*50}\n")
    
    for challenge in data["challenges"]:
        # Заменяем HOST на реальный IP
        description = challenge["description"].replace("HOST", challenges_host)
        
        try:
            # Создаём задание
            resp = requests.post(
                f"{ctfd_url}/api/v1/challenges",
                headers=headers,
                json={
                    "name": challenge["name"],
                    "category": challenge["category"],
                    "description": description,
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
                
                print(f"✓ [{challenge['category']}] {challenge['name']} ({challenge['value']} pts)")
                success += 1
            else:
                print(f"✗ [{challenge['category']}] {challenge['name']} - Error {resp.status_code}")
                if resp.text:
                    print(f"  Response: {resp.text[:100]}")
                failed += 1
                
        except requests.exceptions.ConnectionError:
            print(f"✗ Connection error - is CTFd running at {ctfd_url}?")
            failed += 1
        except Exception as e:
            print(f"✗ [{challenge['category']}] {challenge['name']} - {str(e)}")
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"Results: {success} created, {failed} failed")
    print(f"{'='*50}")

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        print("\nUsage: python3 import_challenges.py <CTFd_URL> <API_TOKEN> [CHALLENGES_HOST]")
        print("\nExamples:")
        print("  python3 import_challenges.py http://ctfd.local:8000 mytoken123 192.168.1.50")
        print("  python3 import_challenges.py http://localhost:8000 mytoken123 localhost")
        sys.exit(1)
    
    ctfd_url = sys.argv[1].rstrip('/')
    token = sys.argv[2]
    challenges_host = sys.argv[3] if len(sys.argv) > 3 else "localhost"
    
    import_challenges(ctfd_url, token, challenges_host)

if __name__ == "__main__":
    main()
