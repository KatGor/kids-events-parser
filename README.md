# 🎉 Hamburg Kids Events Parser 🧒👧

Welcome to the Hamburg Kids Events Parser! This project is all about making life easier for parents—because let’s be real, you already have enough on your plate. Our parser scrapes websites for kids’ events in Hamburg, so you can chat with our bot and instantly find activities near you, tailored to your child’s age and interests. No more endless Googling or FOMO at the playground!

---

## 🛠️ Tech Stack

- **Python 3.10+** (with lots of love for type hints via the `typing` library)
- **BeautifulSoup** for HTML parsing
- **Requests** for fetching web pages
- **OpenAI** for chat and embeddings (because who doesn’t want a little AI magic?)
- **dotenv** for environment variable management
- **Custom tokenization** for handling those pesky token limits
- **Markdown** for beautiful output
- **Git** for version control (because chaos is only fun in theory)

---

## 🚀 How to Run

1. **Set up your virtual environment**  
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Add your environment variables
Create a .env file and add your OpenAI API key

```bash
OPENAI_API_KEY=your-openai-key-here
```

4. **Run the parser workflow**  
```bash
python workflow.py
```

## 🚀 Feature plans
- Store events in a vector db
- Create a chat interface to interact with the db of events