# 🚗 Car Complaint Analyzer

An AI-powered web app that diagnoses car problems instantly based on your description.

## Demo

> Describe your car issue → Get a full diagnosis with severity, cause, repair cost, and suggested action.

## Features

- AI diagnosis using Groq (Llama 3.3 70B)
- Instant analysis: issue, severity, cause, cost estimate, and action
- Quick example buttons for common car problems
- Clean and simple UI built with Streamlit

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/DilliBabu911/automobile-ai.git
   cd automobile-ai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file (get a free API key from [console.groq.com](https://console.groq.com)):
   ```
   GROQ_API_KEY=your-groq-api-key-here
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Tech Stack

- [Streamlit](https://streamlit.io) — UI
- [Groq](https://groq.com) — AI inference (free tier)
- [Llama 3.3 70B](https://groq.com) — Language model
