import requests
import json

PRE_PROMPT = "Напиши то, как можно достигнуть следующей цели (пиши только шаги к достижению цели, каждый шаг выделяй как [goal] <шаг> [/goal]. Например для цели 'Построить кирпичный завод' приемлемым будет считаться примерно такой ответ: [goal] Провести анализ рынка и определить целесообразность строительства кирпичного завода[/goal][goal] Выбрать местоложение для завода, учитывая логистику и доступность сырья[/goal][goal] Разработать проект завода, включая технологические процессы и инфраструктуры[/goal] и т.д.) Каждая цель должна иметь несколько подцелей (или хотя бы одну) - [goal][subgoal] <text 1> [/subgoal][subgoal] <text 2> [/subgoal][subgoal] <text 3> [/subgoal][/goal]. После каждой цели или подцели должно стоять \\n: "
CLIENT_ID = "b68ba196-3ebe-44f1-a1af-8430231d4ef2"
AUTH_TOKEN = "YjY4YmExOTYtM2ViZS00NGYxLWExYWYtODQzMDIzMWQ0ZWYyOmU5MTY5NmJiLWQ1N2ItNDllMy05MGU5LTJlMTQ5NTMwYmRlNw=="

def get_token():
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload='scope=GIGACHAT_API_PERS'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': f'{CLIENT_ID}',
    'Authorization': f'Basic {AUTH_TOKEN}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    return response.json()

def get_answer(text):
    access_token = get_token()["access_token"]
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
            "role": "user",
            "content": PRE_PROMPT + text
            }
        ],
        "temperature": 1,
        "top_p": 0.1,
        "n": 1,
        "stream": False,
        "max_tokens": 512,
        "repetition_penalty": 1
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    return response.json()
