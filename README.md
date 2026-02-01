# 🔮 FutureYou AI — Academic Twin

FutureYou AI is an **Agentic Academic Assistant** that predicts a student’s future SGPA, simulates optimized academic paths, and provides real-time guidance through an integrated AI chatbot.

The idea behind this project is simple:

> *What if you could get an idea about your academic future — and try change it today?*

This system combines Machine Learning, Agent-based optimization, and a conversational AI interface to help students make better academic decisions.

---

## 🚀 Key Features

### 📊 SGPA Prediction (ML)

Predicts **next semester SGPA** using a trained XG Boost model based on:

- Study time  
- Absences  
- Health level  
- Family & school support  
- Lifestyle habits  
- Previous semester SGPA  

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

Powered using **OpenRouter (DeepSeek R1T Chimera – free model)**.

Works like ChatGPT directly inside the app.

---

## 🧠 Tech Stack

- Python  
- Streamlit (Frontend)  
- XGBoost + Joblib (ML Model)  
- Pandas / NumPy  
- OpenRouter API (Chatbot)  

---

## 📂 Project Structure

FutureYou-AI/

│
├── app.py                         

├── agent.py                                      

├── llm.py        

├── model.pkl      

├── features.pkl   

├── processed_data.csv

├── requirements.txt

└── README.md



### 🛠 Local Setup (Optional)

If you want to run locally:

### 1. Clone repository
git clone https://github.com/ayushaary/academic-agent-NEW.git

cd academic-agent-NEW

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run app
streamlit run app.py

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
