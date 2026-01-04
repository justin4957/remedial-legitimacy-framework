#!/usr/bin/env python3
"""
Query Perplexity API for research on mutual assistance frameworks,
NATO Article 5, and legitimacy theory for outside accountability failsafes
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
                'content': f'As a legal and political theory research assistant, please provide thorough analysis with citations to treaties, case law, statutes, and academic scholarship. Question: {question}'
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
        'title': 'NATO Article 5 and Mutual Defense Principles',
        'question': '''What are the key principles, mechanisms, and legal frameworks of NATO Article 5 collective defense? Include:
1. The text of Article 5 and its interpretation
2. Triggering conditions and activation mechanisms
3. Obligations of member states
4. Historical invocations and precedents
5. Limits and constraints on mutual defense obligations
6. Relationship to UN Charter and international law
Please provide treaty text, case studies, and scholarly analysis.'''
    },
    {
        'title': 'Mutual Assistance Frameworks Beyond NATO',
        'question': '''What other mutual assistance, collective security, or mutual defense frameworks exist internationally? Include:
1. Regional defense pacts (CSTO, ANZUS, Rio Treaty, etc.)
2. Mutual aid compacts (EMAC for disaster response)
3. Extradition treaties and mutual legal assistance treaties
4. Responsibility to Protect (R2P) doctrine
5. Historical collective security arrangements
Provide specific examples, treaty citations, and analysis of triggering mechanisms.'''
    },
    {
        'title': 'Legitimacy Theory and Sovereignty Degradation',
        'question': '''What theoretical frameworks exist for understanding legitimacy crises and sovereignty degradation in democratic systems? Include:
1. Political legitimacy theory (Weber, Habermas, Rawls)
2. Democratic erosion and backsliding scholarship
3. State failure and fragile states literature
4. Constitutional crisis theory
5. When outside intervention becomes justified
Provide scholarly citations and key concepts.'''
    },
    {
        'title': 'Citizen Sovereignty and Popular Authority',
        'question': '''What legal and theoretical frameworks address citizen sovereignty and popular authority when government institutions fail? Include:
1. Popular sovereignty doctrine
2. Right of revolution and resistance theory
3. Consent of the governed principles
4. Civil disobedience and conscientious objection
5. Constituent power vs. constituted power
Provide philosophical, constitutional, and legal citations.'''
    },
    {
        'title': 'Outside Accountability Mechanisms',
        'question': '''What mechanisms exist for outside accountability when domestic institutions fail to protect rights? Include:
1. International human rights monitoring (UN Human Rights Council, Inter-American Commission)
2. Universal jurisdiction and international criminal law
3. Targeted sanctions and diplomatic pressure
4. NGO monitoring and shadow reporting
5. Transnational advocacy networks
Provide examples, legal frameworks, and scholarly analysis.'''
    },
    {
        'title': 'Compact Theory and Mutual Obligation Instruments',
        'question': '''What historical and contemporary examples exist of compacts, covenants, or mutual obligation instruments among citizens or groups? Include:
1. Mayflower Compact and colonial covenants
2. Interstate compacts in US federalism
3. Treaty of Waitangi and indigenous sovereignty compacts
4. Mutual aid societies and fraternal organizations
5. Networked governance and polycentric systems
Provide historical examples and theoretical frameworks.'''
    }
]

print("=" * 80)
print("PERPLEXITY API RESEARCH: MUTUAL INTERVENTION & ACCOUNTABILITY FAILSAFES")
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
with open('perplexity_mutual_intervention_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("\n" + "=" * 80)
print("Research complete. Results saved to perplexity_mutual_intervention_results.json")
print("=" * 80)
