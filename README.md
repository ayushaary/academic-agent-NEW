# 🔮 FutureYou AI — Academic Twin

FutureYou AI is an **Agentic Academic Assistant** that predicts a student’s future SGPA, simulates optimized academic paths, and provides real-time guidance through an integrated AI chatbot.

The idea behind this project is simple:

> *What if you could get an idea about your academic future, and try change it today?*

This system combines Machine Learning, Agent-based optimization, and a conversational AI interface to help students make better academic decisions.

---

### Problem Statement

Students often struggle to understand why their academic performance is low and what exactly they should change to improve it. Most academic tools only show past grades or static analytics, they don’t answer questions like:
 - What will my SGPA look like next semester?
 - Which habit matters the most for improvement?
 - Should I study more, reduce absences, or focus on health?
 - What happens if I change just one thing?

Additionally, students rarely get personalized, real-time guidance. Generic study advice doesn’t account for individual lifestyle, attendance, health, or academic history.

There is a clear gap between:

 - Raw academic data
 - Actionable, personalized insights
 - Continuous guidance

This project aims to bridge that gap.

---

### About the Dataset

We used a dataset from Kaggle, the Dataset is for a Porteguese Institution (named - Student Performance Data Set by uci).

As per the Indian Education system, this dataset will not be that effective for predictions.

If we have the dataset of Indian Students, the predictions will be more accurate.

---

### Solution Overview

FutureYou AI – Academic Twin , is an intelligent academic assistant that predicts a student’s next semester SGPA using machine learning and then simulates multiple lifestyle changes to recommend the most effective improvement strategy.

The system combines:
 - XGBoost Prediction to forecast SGPA.
 - Agentic Optimization to evaluate “what-if” scenarios (study time, health, absences, etc.)
 - AI Chatbot for real-time academic guidance.
 - Streamlit Dashboard for an interactive user experience.

Instead of just showing predictions, FutureYou AI provides clear recommendations and conversational support, helping students make better academic decisions.

---

## 🚀 Key Features

### 📊 SGPA Prediction (XG Boost)

Predicts **next semester SGPA** using a trained XG Boost model based on:

- Study time  
- Absences  
- Health level  
- Family & school support  
- Lifestyle habits  
- Previous semester SGPA  

<img width="163" height="62" alt="image" src="https://github.com/user-attachments/assets/24af5d7b-483c-47bd-abd8-84983bb243eb" />

---

### 🤖 Agentic Optimization

Prediction alone isn’t enough.

An **Academic Agent** simulates multiple futures:

- Study +1 / +2 / +3 hours  
- Reduce absences  
- Improve health  
- Lifestyle changes  

It evaluates each scenario and automatically selects the **best action** that maximizes SGPA improvement.

You get:

- Predicted SGPA  
- Optimised SGPA  
- Best recommended action  
- All alternative futures  

---

### 🔥 Personalized Recommendation

After simulation, the system highlights:

- The most impactful change  
- Why it matters  
- How much SGPA improvement it gives  

---

### 💬 Academic Chatbot

An embedded chatbot allows students to ask:

- “How can I improve my GPA?”  
- “Give me study tips”  
- “How do I manage time better?”  

Powered using **OpenRouter (DeepSeek R1T Chimera)**.

Works like ChatGPT directly inside the app.

---

## 🧠 Tech Stack

- Python  
- Streamlit (Frontend)  
- XGBoost + Joblib (ML Model)  
- Pandas / NumPy  
- OpenRouter API (Chatbot)  
- Matplotlib / Seaborn
---

## 📂 Project Structure

├── app.py                         

├── agent.py                                      

├── llm.py 

├── model training.ipynb

├── model.pkl      

├── features.pkl   

├── processed_data.csv

├── requirements.txt

└── README.md

---

### 🛠 Local Setup (Optional)

If you want to run locally:

### 1. Clone repository
git clone https://github.com/ayushaary/academic-agent-NEW.git

cd academic-agent-NEW

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run app
streamlit run app.py

---

### ☁️ Deploy on Streamlit Cloud 
**Step 1 — Open Streamlit Cloud**

Go to:

👉 https://share.streamlit.io/

Login using GitHub.

**Step 2 — Create New App**

Click New App.

Fill:

**Field	-** Value

**Repository -** ayushaary/academic-agent-NEW

**Branch -**	main

**Main file path -**	app.py

Click Deploy.

Streamlit will automatically:
 - Create Python environment
 - Install dependencies from requirements.txt
 - Launch your app

---

### How to Use the App

 - Open the deployed Streamlit link.
 - Fill in your academic details from the left sidebar:
      - Study time, travel time, free time, social time.
      - Previous SGPA (G1, G2).
      - Health, absences, support indicators, etc.
 - Click Simulate Future.

**You’ll see:**

 - Predicted SGPA (Next Semester) — XG Boost output
 - Optimised SGPA — Agent-simulated best future
 - Best Action — highest impact improvement
 - All Agent Futures — alternative scenarios
 - Use the Academic Chatbot at the bottom to ask questions about study habits, GPA improvement, or time management.

---

### How It Works

**ML Prediction**
 - XGBoost model predicts baseline SGPA using student features.

**Agent Simulation**
 - Multiple “what-if” actions are applied (study + hours, fewer absences, better health, etc.).
 - Each scenario is re-evaluated.
 - The agent selects the action with maximum SGPA gain.

**Chatbot (using API)**
 - Chatbot calls OpenRouter using a private API key (stored as Streamlit Secret).
 - Frontend never sees the API key.
 - User queries are sent to OpenRouter (DeepSeek Chimera).
 - Responses are shown directly in the Streamlit UI.

---

### Architecture Overview

<img width="2816" height="1021" alt="Gemini_Generated_Image_7qbowm7qbowm7qbo" src="https://github.com/user-attachments/assets/0ea2ee60-2b20-4b2e-9fe7-651ac8c88e49" />


---

### Known Limitations
 - Model trained on a limited dataset.
 - Chatbot responses depend on free API quota.
 - SGPA predictions are indicative, not guaranteed outcomes.

---

### Future Improvements
 - Burnout / fatigue modeling.
 - Mental health scoring.
 - Calendar integration.
 - User login + saved profiles.
 - Better mobile UI.
 - Better Chatbot

---

### 🌐 Live Deployed Link

Deployed on Streamlit.io

https://academic-agent-new-6rrwyyehermyi3g4enytjk.streamlit.app/

---

### Images:

![Screenshot_1-2-2026_6505_academic-agent-new-6rrwyyehermyi3g4enytjk streamlit app](https://github.com/user-attachments/assets/ad21d244-120f-47d9-90e6-947acad8fa4e)
![Screenshot_1-2-2026_65045_academic-agent-new-6rrwyyehermyi3g4enytjk streamlit app](https://github.com/user-attachments/assets/31139842-1de7-4936-9ef2-e34706ec5fab)
![Screenshot_1-2-2026_65121_academic-agent-new-6rrwyyehermyi3g4enytjk streamlit app](https://github.com/user-attachments/assets/60ae2831-5113-43b4-9f9d-467fa419b306)

---

### Team Name :

    HAD H YRR 2

### Author:

    Disha Agrawal
    Ayush Aary

### Institution : 

    IIT Roorkee
