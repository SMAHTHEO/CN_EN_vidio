
import requests
import json
import deepl


# 翻译提交的文本
def Trans(text):
    api_url = ''
    api_key = ''

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'auth_key': api_key,
        'text': text,
        'target_lang': 'ZH'
    }
    response = requests.post(api_url, headers=headers, data=data)
    response_dict = json.loads(response.text)
    CN = response_dict['translations'][0]['text']

    # 终端显示
    print("[XMeng] 成功翻译 : " + text[:-1])
    print("[XMeng] 翻译结果 : " + CN[:-1])

    return CN
def Trans_deepl(text):
    api_key = ''
    translator = deepl.Translator(api_key)

    CN = translator.translate_text(text, target_lang="ZN")

    # 终端显示
    print("[XMeng] 成功翻译 : " + text[:-1])
    print("[XMeng] 翻译结果 : " + CN[:-1])

    return CN
