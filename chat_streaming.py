import config  # type: ignore
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

messages = [
    SystemMessage("You are a helpful assistant."),
    HumanMessage("こんにちは！私はJohn Smithです。"),
    AIMessage(
        content="こんにちは！John Smithさん。私はAIです。なにかお手伝いできることはありますか？"
    ),
    HumanMessage(content="はい、私の名前がわかりますか？"),
]

for chunk in model.stream(messages):
    print(chunk.content, end="", flush=True)
