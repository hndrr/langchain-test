from langsmith import Client

client = Client()
prompt = client.pull_prompt("oshima/recipe")

prompt_value = prompt.invoke({
    "dish": "カレーライス",
})

print(prompt_value)