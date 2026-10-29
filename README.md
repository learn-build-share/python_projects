# 🚀 Python Projects

A collection of beginner-friendly Python projects and practice programs to help you learn Python through hands-on examples. This repository covers core Python concepts with simple projects and interactive apps built using Python.

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
* 🚀 AI Interview Feedback (Streamlit + Groq)
* 🎟️ VIP Entry System
* 🥊 WWE Players Info API (FastAPI mini project)
* 🧠 Data structures and algorithm examples (DSA/LL)


## 🐍 Python Version

> Python 3.13

---

## 📂 Project Structure

```text
python_projects/
├── calculator/
├── certificate_generator/
├── Classes/
├── DSA/
├── FileHandling/
├── fastapi-series/
│   └── wwe_project/
├── FrozenSet/
├── Lists/
├── Patterns/
├── Set/
├── Strings/
├── Tuple/
├── Decorator/
├── functions/
├── quizapp/
├── mini_chatgpt/
├── allany.py
├── filemodes.py
├── generator.py
├── zip_func.py
├── requirements.txt
├── README.md
└── .venv/ (local environment)
```

> The repository is intentionally kept in its existing folder layout. The DSA examples are preserved under their current folder names without renaming or reinterpreting them.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd python_projects
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

3. Run the Streamlit apps from their respective folders.

---

## ▶️ Run Projects

| Project | Command |
| --- | --- |
| 📜 Certificate Generator | `streamlit run certificate_generator/app.py` |
| 🎬 Netflix Watch List | `streamlit run Lists/netflix_watch_list.py` |
| 🔐 OTP Verification | `streamlit run Tuple/otp_verification.py` |
| 📱 Instagram Follower Cleaner | `streamlit run Set/instagram_cleaner/app.py` |
| 🎫 Event ID Pass Generator | `streamlit run FrozenSet/event_verification_id.py` |
| 🍔 Food Delivery App | `streamlit run functions/food_delivery_app/food_app.py` |
| 🔒 Password Strength Checker | `streamlit run functions/password_strength_build.py` |
| 🔑 Password Checker (Console) | `python functions/password_checker.py` |
| 🚀 AI Interview Feedback | `streamlit run functions/AI_Interview_Feedback/app.py` |
| 📄 AI Resume Analyzer | `streamlit run functions/Ai_Resume_Analyser/app.py` |
| 🧠 AI Prompt Generator | `streamlit run functions/Ai_Prompt_Generator/app.py` |
| 📝 AI Notes Builder | `streamlit run functions/Ai_Notes_Builder/app.py` |
| 🏆 AI Student Certificate Builder | `streamlit run functions/AI_Student_Certificate/app.py` |
| 🎟️ VIP Entry System | `streamlit run Decorator/app.py` |
| 🥊 WWE Players Info API | `cd fastapi-series/wwe_project && python run.py` |
| 🧩 WWE Player Hub UI | `cd fastapi-series/wwe_project && streamlit run app.py` |

---

## 🧠 Learning Focus

This repo covers the following beginner learning tracks:

* Python fundamentals and syntax
* Object-oriented programming
* File handling and file modes
* Exception handling and input validation
* Data structures and algorithm practice
* Small real-world mini projects

> The repository does not define a separate DSS acronym in a formal way, so the existing DSA examples are preserved as-is rather than being renamed or reinterpreted.

---

## 🧪 Notes

* The top-level examples such as `allany.py`, `filemodes.py`, and `zip_func.py` are intended as learning demos, not production modules.
* Some examples rely on `.env` values or external APIs, so keep your environment variables configured before running them.
* The dependency list was trimmed to direct packages actually used by the project.

---

## 🤝 Contributing

Contributions are welcome. If you want to improve existing projects or add beginner-friendly examples, keep the current structure and explain the learning goal clearly in your code and documentation.

---

## 📄 License

This repository is intended for learning and educational purposes.
