import config  # type: ignore
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from typing import Any

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant."),
        ("human", "こんにちは！私は{name}です。"),
        (
            "ai",
            "こんにちは！{name}さん。私はAIです。なにかお手伝いできることはありますか？",
        ),
        ("human", "はい、私の名前がわかりますか？"),
    ]
)

parser = StrOutputParser()

chain: Any = prompt | model | parser

result: Any = chain.invoke({"name": "John Smith"})
print(result)

# ai_messages = prompt.invoke({"name": "John Smith"})  # type: ignore
# print(ai_messages)
