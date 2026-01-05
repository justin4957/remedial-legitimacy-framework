#!/usr/bin/env python3
"""
Query Perplexity API for research on constitutional amendment language,
Federalist Papers style, and founding principles relevant to extending
the remedial legitimacy framework as natural constitutional amendments
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
                'content': f'As a constitutional law and American history research assistant, please provide thorough analysis with citations to founding documents, constitutional amendments, Federalist Papers, and legal scholarship. Question: {question}'
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
        'title': 'Constitutional Amendment Language and Structure',
        'question': '''What are the structural conventions, language patterns, and drafting principles used in U.S. Constitutional Amendments? Include:
1. Text and structure of key amendments (1st, 4th, 9th, 10th, 13th, 14th)
2. Common linguistic patterns ("Congress shall," "No person shall," etc.)
3. Relationship between negative rights (prohibitions on government) and positive rights (affirmative obligations)
4. Use of Section 1 (substantive right) vs Section 2 (enforcement mechanism) structure
5. Evolution of amendment language from Bill of Rights through modern amendments
Provide specific amendment text examples and scholarly analysis.'''
    },
    {
        'title': 'Federalist Papers Style and Argumentation',
        'question': '''What are the characteristic elements of Federalist Papers argumentation and prose style? Include:
1. Structure of Federalist arguments (classical rhetoric, appeals to reason and experience)
2. Key linguistic patterns and vocabulary ("experience hath shewn," "candid," "prudence," etc.)
3. Use of Roman/Greek historical examples and republican theory
4. Appeals to popular sovereignty and consent of the governed
5. Treatment of checks and balances, separation of powers, and accountability
6. Madison, Hamilton, and Jay's distinctive styles
Provide specific Federalist Paper citations and characteristic passages.'''
    },
    {
        'title': 'Popular Sovereignty and Consent in Founding Documents',
        'question': '''How do founding-era documents articulate principles of popular sovereignty, consent of the governed, and right of the people to alter or abolish government? Include:
1. Declaration of Independence language on consent and revolution
2. Preamble to Constitution ("We the People")
3. 9th Amendment (retained rights) and 10th Amendment (reserved powers)
4. State constitutions and their popular sovereignty clauses
5. Anti-Federalist concerns about consolidated power
6. Founding-era understanding of "the people" as ultimate authority
Provide specific document text and scholarly analysis.'''
    },
    {
        'title': 'Rights Enforcement Mechanisms in Constitutional Law',
        'question': '''What constitutional frameworks exist for enforcing rights when institutional mechanisms fail? Include:
1. 14th Amendment Section 5 enforcement powers
2. Ex parte Young doctrine (suing state officers in federal court)
3. Section 1983 civil rights actions
4. Habeas corpus and its constitutional foundation
5. Structural constitutional rights (access to courts, due process)
6. Remedies for constitutional violations (damages, injunctions, declaratory relief)
7. Congressional enforcement of constitutional rights
Provide case citations and statutory framework analysis.'''
    },
    {
        'title': 'Accountability and Checks on Government Power',
        'question': '''What founding-era and constitutional principles establish accountability mechanisms and checks on governmental power? Include:
1. Separation of powers doctrine and its constitutional foundation
2. Checks and balances in original Constitution
3. Impeachment and removal mechanisms
4. Electoral accountability and representative government
5. Freedom of press as "Fourth Estate" check on power
6. Right to petition for redress of grievances
7. Jury trial as popular check on government
8. Founding-era understanding of popular resistance to tyranny
Provide constitutional text, Federalist Paper citations, and historical examples.'''
    },
    {
        'title': 'Distributed Documentation and Evidence in Law',
        'question': '''What legal frameworks recognize distributed documentation, witness networks, and collective evidence preservation? Include:
1. Historical use of affidavits and sworn testimony
2. Authentication of documents in legal proceedings
3. Business records exception and reliable documentation
4. Chain of custody requirements and distributed evidence
5. Pattern and practice evidence in civil rights law
6. Class action mechanisms and aggregated claims
7. Archival preservation and historical documentation
8. Freedom of Information Act and transparency requirements
Provide case law, evidentiary rules, and statutory frameworks.'''
    }
]

print("=" * 80)
print("PERPLEXITY API RESEARCH: CONSTITUTIONAL AMENDMENTS & FEDERALIST LANGUAGE")
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
with open('perplexity_constitutional_amendments_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("\n" + "=" * 80)
print("Research complete. Results saved to perplexity_constitutional_amendments_results.json")
print("=" * 80)
