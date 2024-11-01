import config
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate(
    [
        ("system","You are a helpful assistant."),
        ("human","こんにちは！私は{name}です。"),
        ("ai","こんにちは！{name}さん。私はAIです。なにかお手伝いできることはありますか？"),
        ("human","はい、私の名前がわかりますか？"),
    ]
)

ai_messages = prompt.invoke({
    "name": "John Smith"
})    
print(ai_messages)
# parser = StrOutputParser()
# parsed_result = parser.invoke(ai_messages)

# print(parsed_result)
