#!/usr/bin/env python3
import os
import json
import requests

API_KEY = os.environ.get('PERPLEXITY_API_KEY')
API_URL = 'https://api.perplexity.ai/chat/completions'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

payload = {
    'model': 'sonar',
    'messages': [
        {
            'role': 'user',
            'content': 'What are joint defense agreements in legal contexts?'
        }
    ]
}

print("Testing Perplexity API...")
print(f"API URL: {API_URL}")
print(f"API Key present: {bool(API_KEY)}")
print(f"Payload: {json.dumps(payload, indent=2)}")
print()

try:
    response = requests.post(API_URL, headers=headers, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    response.raise_for_status()
    result = response.json()
    print("\nSuccess!")
    print(result['choices'][0]['message']['content'])
except Exception as e:
    print(f"Error: {e}")
    print(f"Response text: {response.text if 'response' in locals() else 'No response'}")
