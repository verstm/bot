import requests
import openai
import json
def find_by_name(name, l="ru"):
    result = requests.get(f"https://codeforces.com/api/problemset.problems?locale={l}")
    problems = result.json()['result']['problems']
    ans =[]
    for i in problems:
        if name in i["name"]:
            ans.append(i)
    return ans
def problem_to_link(problem):
    link = f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']}"
    return link
def gptask(q, s='sample.txt'):
    print("Generation started")
    openai.api_key = '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'
    prompt = q
    with open(s, 'r', encoding='utf-8') as f:
        sample = f.read()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": sample.replace('{x}', prompt)},
        ]
    )
    answer = response['choices'][0]['message']['content']
    with open("lastanswer.txt", 'w', encoding='utf-8') as f:
        f.write(answer)
    return answer
