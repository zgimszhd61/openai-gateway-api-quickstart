#coding:utf-8
from openai import OpenAI
client = OpenAI(
            base_url="http://127.0.0.1:8000",
            api_key="abcaaa-",
)

completion = client.chat.completions.create(
            model="llama-3-sonar-large-32k-chat",
            messages=[
                {"role": "system", "content": "hihi"},
                {"role": "user", "content": "bbbbbb"}
            ]
)
result = completion.choices[0].message.content
print(result)
