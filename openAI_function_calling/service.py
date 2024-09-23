import openai
from django.conf import settings

from .models.work_order import WorkOrder

openai.api_key = settings.OPENAI_API_KEY


def get_chip_production():
    # 查询WorkOrder的数量
    work_order_count = WorkOrder.objects.count()
    print(f"今天生产了 {work_order_count} 块芯片。")
    return work_order_count


def get_scrapped_chip():
    return 200


# 调用GPT API
def call_gpt_api(messages, tools):
    client = openai.OpenAI(
        base_url="https://api.xiaoai.plus/v1",
        api_key=settings.OPENAI_API_KEY
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        tools=tools,
    )
    return completion


# 调用openai embedded api
def call_openai_embedded_api(messages, tools):

    model = 'text-embedding-3-small'
    response = openai.embeddings.create(input=[messages], model=model)
    print(response.data[0].embedding)

    return response
