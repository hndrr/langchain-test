import config  # type: ignore
import gradio as gr  # type: ignore
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI


# 翻訳する関数を定義
def translate_text(text: str, llm: str, target_language: str):  # type: ignore
    if llm == "gpt-4o-mini":
        model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    elif llm == "gpt-4o":
        model = ChatOpenAI(model="gpt-4o", temperature=0)
    elif llm == "gemini-1.5-flash":
        model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    elif llm == "gemini-1.5-pro":
        model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)
    else:
        raise ValueError(f"Invalid LLM: {llm}")

    parser = StrOutputParser()
    chain = model | parser
    messages = [
        SystemMessage(content=f"Translate the following text to {target_language}:"),
        HumanMessage(content=text),
    ]
    return chain.invoke(messages)


demo = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(label="翻訳したいテキスト"),
        gr.Dropdown(
            label="LLM",
            choices=[
                "gpt-4o-mini",
                "gpt-4o",
                "gemini-1.5-flash",
                "gemini-1.5-pro",
            ],
            value="gpt-4o-mini",
        ),
        gr.Dropdown(
            label="ターゲット言語",
            choices=[
                "English",
                "なんJ風",
                "Spanish",
                "French",
                "German",
                "Chinese",
                "Korean",
            ],
            value="English",
        ),
    ],
    outputs="text",
    title="翻訳アプリ",
    description="LLMを使ってテキストを指定した言語に翻訳します。",
)

# アプリを起動
demo.launch()
