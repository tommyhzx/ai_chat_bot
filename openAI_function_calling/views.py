from django.shortcuts import render
import openai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
from .service import get_chip_production, get_scrapped_chip, call_gpt_api  # 导入服务层函数


@csrf_exempt
def gpt_chat(request):
    if request.method == 'POST':
        # 从请求中获取数据
        print("request:", request)
        data = json.loads(request.body)

        user_message = data.get('message', '')
        # 定义角色，并把用户的消息和系统的消息组合起来
        messages = [
            {"role": "system", "content": "你是一个管理工厂数据的助手，能够提供非常多有用的工厂数据。"},
            {"role": "user", "content": user_message}
        ]
        # 定义函数调用接口
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_chip_production",
                    "description": "获取当天生产的芯片数量",
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "required": [],
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_scrapped_chip",
                    "description": "获取当天报废的芯片数量",
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "required": [],
                    }
                }
            }
        ]

        # 反复调用GPT API，直到finish_reason为stop
        stop = False
        while not stop:
            print("你的问题是，messages:", messages)
            response = call_gpt_api(messages, tools)
            finish_reason = response.choices[0].finish_reason
            # 根据finish_reason的不同，做出不同的处理
            if finish_reason == "stop":
                assistant_message = response.choices[0].message.content
                print("finish_reason gpt的回答:", assistant_message)
                return JsonResponse({'message': assistant_message})

            elif finish_reason == "tool_calls":
                tool_calls = response.choices[0].message.tool_calls
                for tool_call in tool_calls:
                    function_name = tool_call.function.name
                    if function_name == "get_chip_production":
                        chip_production = get_chip_production()
                        messages.append(
                            {"role": "function", "name": "get_chip_production", "content": str(chip_production)})
                        print(f"今天生产了 {chip_production} 块芯片。")

                    elif function_name == "get_scrapped_chip":
                        scrapped_chip = get_scrapped_chip()
                        messages.append(
                            {"role": "function", "name": "get_scrapped_chip", "content": str(scrapped_chip)})
                        print(f"今天报废了 {scrapped_chip} 块芯片。")

                # 再次调用GPT API以获取最终回复
                # response = call_gpt_api(messages, tools)
                # assistant_message = response.choices[0].message.content
                # return JsonResponse({'message': assistant_message})

    return JsonResponse({'error': 'Invalid request method'}, status=400)
