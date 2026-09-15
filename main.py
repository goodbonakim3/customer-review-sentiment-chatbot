from dotenv import load_dotenv
from openai import OpenAI

env_file_path='C:\Users\김형선\chatbot-study\customer-review-sentiment\.env'
load_dotenv(env_file_path)

client = OpenAI()
def get_completions(prompt, model='gpt-5-nano'):
    response = client.chat.completions.create(
        model=model,
        messages = [
            {'role':'system','content':'You are an expert in sentiment analysis with over 10 years of experience analyzing Korean customer reviews.'},
            {'role':'user','content':prompt}
        ],
        response_format={'type':'json_object'}
    )
    return response.choices[0].message.content