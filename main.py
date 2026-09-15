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

customer_review = f'''
바지 밑위가 길고 제 허벅지는 터져나가서 상의를 넣어 입고 가만있을 때 정면모습이 쪼금 애매한 주름이 지네요
그래도 착용감은 편안하고 밝은 바지인데도 부한 느낌도 없어서 마음에 들어요
크림진이 하나도 없어서 고민고민하다 구매했는데 이정도면 만족입니다
다만 허리에 있는 가죽패치가 검정이라 세탁시 이염될까봐 무서운거랑 바지밑단 주름이 좀 자글자글하게 지는 단점은 있어요!
'''

example = '''{
'Sentiment': 'Positive',

'supporting_keywords': {
'positive':['keyword1','keyword2'],
'negative':['keyword1','keyword2']},

'reason': 'reason for the sentiment classification'
}'''

user_prompt = f'''
다음 <고객리뷰>의 내용을 분석하여 긍정 또는 부정으로 감성 분류하고, 해당 분류의
판단 근거가 되는 핵심 키워드들을 추출한 후 <출력형식>을 철저히 준수하여 결과를 제시하고,
긍정과 부정의 요소가 다 포함이 되어 있는 경우에는 긍정 또는 부정이라고 판단한 이유를 제시하시오.

<고객리뷰>
{customer_review}

<출력형식>
아래 JSON 형식을 엄격하게 준수하여 결과를 생성해야 합니다.
{example}
긍정 혹은 부정이라고 판단한 이유제시
'''

output = get_completions(user_prompt)
print(f'bot: \n{output}')