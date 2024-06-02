import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))


def AI(prompt):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{
                    "role": "user",
                    "content": f"Напиши пост на тему книга {prompt} українською "
                }])
    return response.choices[0].message.content

#print(response.choices[0].message.content)

if __name__ == "__main__":
    print(AI(input("Введи тему: ")))