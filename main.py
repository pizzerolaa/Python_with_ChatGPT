import openai
import config

openai.api_key = config.api_key

resp = openai.ChatCompletion.create(model="gpt-3.5-turbo", #pasamos el modelo que queramos usar de chatgpt
                             messages=[{"role": "user", "content": "What is the OpenAI mission?"}])

print(resp)

