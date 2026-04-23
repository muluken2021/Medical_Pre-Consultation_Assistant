# Medical Pre-Consultation Assistant

---

## 1. Problem Description

In Ethiopian public hospitals, doctors handle a very high number of patients every day. Because of this heavy patient flow, each patient is given only a very short consultation time (often less than 5 minutes). During this limited time, doctors must still collect important information such as symptoms, medical history, and the duration of illness.

Another major challenge is the language barrier. Patients usually speak local languages such as Amharic or Afaan Oromo, while medical documentation is written in English. This creates delays because doctors must translate and reorganize patient information during consultation.

As a result, most of the consultation time is spent collecting basic information instead of focusing on diagnosis and treatment decisions. This reduces efficiency and increases pressure on healthcare professionals.

---

## 2. Project Idea

To address this problem, I developed a **Goal-Based AI Medical Pre-Consultation Assistant**.

The system is designed to interact with patients before they meet the doctor and collect structured medical information in an efficient way.

### Main Idea of the System:
- The AI asks patients 5 structured questions in Amharic  
- Patients respond using simple natural language  
- The system processes input using a rule-based NLP matching system  
- It compares symptoms with a medical knowledge base  
- It determines possible conditions using urgency scoring  
- It generates a structured medical summary for doctors  

This system helps reduce the workload of doctors by preparing patient information in advance.

---

## 3. Why it is a Goal-Based AI Agent

This system is considered a **Goal-Based AI Agent** because it does not simply react to user input. Instead, it follows a specific objective:

> The goal of the agent is to analyze patient symptoms, match them with known medical conditions, and generate a structured clinical summary.

### Decision Process:
- Collect patient responses through guided questions  
- Combine and analyze the input  
- Match keywords with medical knowledge base  
- Select most relevant condition using urgency scoring  
- Produce SBAR-style report (Situation, Background, Assessment, Recommendation)

---

## 4. How It Works

### Step 1: Patient Interaction (GUI Interface)
The user interacts with a Tkinter-based graphical interface. The system presents 5 structured medical questions in Amharic.

---

### Step 2: Data Collection
The patient answers each question one by one using an input field.

Navigation options:
- Next button  
- Back button  

---

### Step 3: AI Analysis
After completing all questions, the system combines all answers and sends them to the AI agent.

The agent:
- Scans Amharic keywords  
- Matches them with knowledge base  
- Selects best condition using urgency scoring  

---

### Step 4: Confirmation Stage
The system shows AI prediction:

- If user confirms → proceed to report generation  
- If user rejects → restart questionnaire  

---

### Step 5: Report Generation
The system generates a structured medical report including:
- Situation (patient condition)  
- Background  
- Assessment (possible diagnosis)  
- Recommendation (medication + warnings)  

---

## 5. Output (Result)

The system produces a structured SBAR-style medical summary.

### Final Output Includes:
- Main patient problem  
- Symptom analysis  
- Possible condition  
- Medication suggestion  
- Red flag warnings  
- Structured medical report  

This helps doctors quickly understand patients before consultation.

---

## 6. Conclusion

This project demonstrates how a Goal-Based AI system can improve healthcare efficiency in Ethiopian hospitals.

It helps to:
- Reduce waiting time  
- Minimize language barriers  
- Improve communication  
- Assist doctors in faster diagnosis  
- Automate patient pre-consultation  

Overall, it shows how AI can support healthcare systems in resource-limited environments.