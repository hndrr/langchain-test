import gradio as gr  # type: ignore
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser


# 翻訳する関数を定義
def translate_text(text: str, target_language: str):  # type: ignore
    model = ChatOllama(model="llama3.1")
    parser = StrOutputParser()
    chain = model | parser
    messages = [
        {
            "role": "system",
            "content": f"Translate the following text to {target_language}:",
        },
        {"role": "user", "content": text},
    ]

    # Ollamaチャットモデルで翻訳を実行
    response = chain.invoke(messages)
    return response


# Gradioインターフェースの設定
demo = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(label="翻訳したいテキスト"),
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
    description="Ollamaを使ってテキストを指定した言語に翻訳します。",
)

# アプリを起動
demo.launch()
