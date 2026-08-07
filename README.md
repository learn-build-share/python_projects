# 🚀 Python Projects

A collection of **beginner-friendly Python projects** and practice programs to help you learn Python through hands-on examples. This repository covers core Python concepts with mini projects and interactive applications built using **Python**.
---

## 📖 About

This repository contains small Python projects and practice files covering topics such as:

* 🧮 Calculator programs
* 📜 Certificate Generator
* ❓ Quiz Applications
* 📋 Lists
* 🔤 Strings
* 📦 Tuples
* 🧩 Sets
* ❄️ Frozen Sets
* ⚙️ Functions
* 🎨 Pattern Programs
* 🧠 AI Notes Builder (Streamlit)
* 🏆 AI Student Certificate (Streamlit + Groq)

The goal is to provide simple, practical examples that help beginners understand Python fundamentals and AI-enhanced workflows.

---

## 🐍 Python Version

> **Python 3.13**

---

## 📂 Project Structure

```text
Python_Projects/
│
├── calculator/
├── certificate_generator/
├── quizapp/
├── Lists/
├── Strings/
├── Tuple/
├── Set/
├── FrozenSet/
├── functions/
│   ├── AI_Interview_Feedback/
│   ├── AI_Resume_Analyser/
│   ├── Ai_Prompt_Generator/
│   ├── Ai_Student_Certificate/
│   ├── Ai_Notes_Builder/
│   └── food_delivery_app/
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Python_Projects
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Groq / LLM access for AI apps

1. Create a `.env` file in the repo root.
2. Add your API key:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

3. Run the Streamlit apps from the `functions` folder.

---

## ▶️ Run Projects

| Project                            | Command                                               |
| ---------------------------------- | ----------------------------------------------------- |
| 📜 Certificate Generator           | `streamlit run certificate_generator/app.py`          |
| 🎬 Netflix Watch List              | `streamlit run Lists/netflix_watch_list.py`           |
| 🔐 OTP Verification                | `streamlit run Tuple/otp_verification.py`             |
| 📱 Instagram Follower Cleaner      | `streamlit run Set/instagram_cleaner/app.py`          |
| 🎫 Event ID Pass Generator         | `streamlit run FrozenSet/event_verification_id.py`    |
| 🍔 Food Delivery App               | `streamlit run functions/food_delivery_app/food_app.py` |
| 🚀 AI Interview Feedback           | `streamlit run functions/AI_Interview_Feedback/app.py` |
| 📄 AI Resume Analyzer              | `streamlit run functions/AI_Resume_Analyser/app.py`   |
| 🧠 AI Prompt Generator             | `streamlit run functions/Ai_Prompt_Generator/app.py`  |
| 📝 AI Notes Builder                | `streamlit run functions/Ai_Notes_Builder/app.py`     |
| 🏆 AI Student Certificate Builder  | `streamlit run functions/AI_Student_Certificate/app.py` |

---

## 🧠 AI and Groq Notes

* `functions/AI_Interview_Feedback/app.py` generates interview feedback for resumes using `langchain_groq` and `ChatGroq`.
* `functions/Ai_Notes_Builder/app.py` helps generate study notes and prompts using AI.
* `functions/AI_Student_Certificate/app.py` uses `langchain_groq` and `ChatGroq` to generate certificate JSON and render a preview.
* The AI apps depend on `streamlit`, `python-dotenv`, and Groq API access.
* Keep the example JSON and prompt variables clearly separated from template variables when using `ChatPromptTemplate`.

---

## 💡 Real World Examples

* Generate polished course completion certificates for training programs.
* Build note summaries for interviews, study guides, or learning materials.
* Use the AI Prompt Generator to prototype chatbot and automation prompts.
* Deploy Streamlit apps for small team demos or learning tools.

---

## ❓ Interview Questions

* What are the benefits of using Streamlit for data apps?
* How do you manage secrets like API keys with `.env` files?
* Why is parsing LLM output important for production-ready apps?
* How can you use HTML preview + download buttons in Streamlit?
* What are common prompt engineering best practices for AI assistants?

---

## ✨ Features

* Beginner-friendly examples
* Streamlit interactive apps
* AI-enabled workflows with Groq
* Clear code organization
* Practice files for Python fundamentals

---

## 📦 Requirements

```bash
pip install -r requirements.txt
```

> Notes:
> * Make sure `streamlit` and `python-dotenv` are installed.
> * Add `GROQ_API_KEY` for AI certificate generation.

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve existing projects or add new beginner-friendly Python projects:

1. Fork this repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## ⭐ Support

If you found this repository helpful, consider giving it a **⭐ Star** on GitHub.

---

## 📄 License

This repository is intended for **learning and educational purposes**.
