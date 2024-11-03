# langchain-test

## Install

リポジトリをクローン

```bash
git clone https://github.com/hndrr/langchain-test.git
cd langchain-test
```

仮想環境を作成(venvの場合)

```bash
python -m venv .venv
. venv/bin/activate
```

依存関係をインストール

```bash
pip install -r requirements.txt
```

---

### Config

 `.env` ファイルに以下を設定してください。langsmithのAPIキーは[こちら](https://smith.langchain.com/settings)から取得。

```python
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY=""
LANGCHAIN_PROJECT=""
OPENAI_API_KEY=""
```
