#!/usr/bin/env python3
"""
Query Perplexity API for legal analysis of the Compact of Mutual Witness
"""
import os
import json
import requests

API_KEY = os.environ.get('PERPLEXITY_API_KEY')
API_URL = 'https://api.perplexity.ai/chat/completions'

def query_perplexity(question):
    """Query Perplexity API with a question"""
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    payload = {
        'model': 'sonar',
        'messages': [
            {
                'role': 'user',
                'content': f'As a legal research assistant, please provide thorough analysis with citations to case law, statutes, and legal scholarship. Question: {question}'
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()

    result = response.json()
    return result['choices'][0]['message']['content']

# Questions for analysis
questions = [
    {
        'title': 'Legal Precedents for Witness Compacts',
        'question': '''What legal precedents exist for reciprocal agreements among witnesses to preserve evidence and provide testimony? Include analysis of:
1. Mutual aid agreements in legal contexts
2. Witness protection compacts
3. Evidence preservation obligations
4. Joint defense agreements
Please provide case citations and statutory references.'''
    },
    {
        'title': 'Historical Examples of Distributed Documentation Networks',
        'question': '''What historical examples exist of distributed networks for preserving evidence of institutional misconduct or rights violations? Include:
1. Truth and reconciliation commission documentation systems
2. Whistleblower networks and protection mechanisms
3. Underground documentation during authoritarian regimes
4. Civil rights movement documentation efforts
Provide specific examples with citations.'''
    },
    {
        'title': 'Legal Vulnerabilities and Compelled Disclosure',
        'question': '''What are the legal vulnerabilities of a distributed evidence preservation network where participants hold documents on behalf of others? Address:
1. Compelled disclosure and subpoena power
2. Privilege claims (attorney-client, work product, etc.)
3. Spoliation of evidence obligations
4. Conspiracy or coordination concerns
5. Cross-jurisdictional issues
Include relevant case law.'''
    },
    {
        'title': 'Evidentiary Standards for Pattern Documentation',
        'question': '''What legal standards apply to using aggregated individual accounts to demonstrate institutional patterns? Include:
1. Pattern and practice evidence in civil rights litigation
2. Collective testimony in class actions
3. Statistical evidence of discrimination
4. Admissibility of multiple witness accounts
Provide case citations, particularly from civil rights and employment discrimination contexts.'''
    },
    {
        'title': 'Third-Party Document Custody',
        'question': '''What legal frameworks govern when one party holds documents or evidence on behalf of another? Address:
1. Custodial obligations and responsibilities
2. Legal standing to resist disclosure
3. Bailment principles
4. Fiduciary duties in document preservation
5. Electronic discovery and third-party custodians
Include relevant case law and rules of civil procedure.'''
    }
]

print("=" * 80)
print("PERPLEXITY API ANALYSIS: COMPACT OF MUTUAL WITNESS")
print("=" * 80)
print()

results = []

for i, q in enumerate(questions, 1):
    print(f"\n{'=' * 80}")
    print(f"QUERY {i}: {q['title']}")
    print(f"{'=' * 80}\n")

    try:
        answer = query_perplexity(q['question'])
        results.append({
            'title': q['title'],
            'question': q['question'],
            'answer': answer
        })
        print(answer)
        print()
    except Exception as e:
        print(f"Error querying Perplexity: {e}")
        results.append({
            'title': q['title'],
            'question': q['question'],
            'error': str(e)
        })

# Save results to JSON
with open('perplexity_analysis_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("\n" + "=" * 80)
print("Analysis complete. Results saved to perplexity_analysis_results.json")
print("=" * 80)
