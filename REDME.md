Medical Pre-Consultation Assistant
1. Problem Description
In Ethiopian public hospitals, doctors handle a very high number of patients every day. Because of this heavy patient flow, each patient is given only a very short consultation time (often less than 5 minutes). During this limited time, doctors must still collect important information such as symptoms, medical history, and the duration of illness.
Another major challenge is the language barrier. Patients usually speak local languages such as Amharic or Afaan Oromo, while medical documentation is written in English. This creates delays because doctors must translate and reorganize patient information during consultation.
As a result, most of the consultation time is spent collecting basic information instead of focusing on diagnosis and treatment decisions. This reduces efficiency and increases pressure on healthcare professionals.

2. Project Idea
To address this problem, I developed a Goal-Based AI Medical Pre-Consultation Assistant.
The system is designed to interact with patients before they meet the doctor and collect structured medical information in an efficient way.
Main Idea of the System:
The AI asks patients a set of structured questions in Amharic
Patients respond using simple natural language
The system processes the input using a rule-based NLP matching system
It compares symptoms with a predefined medical knowledge base
It determines possible conditions based on urgency levels
It generates a structured medical summary for doctors
This system helps reduce the workload of doctors by preparing patient information in advance.

Why it is a Goal-Based AI Agent
This system is considered a Goal-Based AI Agent because it does not simply react to user input. Instead, it follows a specific objective:
The goal of the agent is to analyze patient symptoms, match them with known medical conditions, and generate a structured clinical summary.
The agent uses a step-by-step decision process:
Collect patient responses through guided questions
Combine and analyze the input
Match keywords with a medical knowledge base
Select the most relevant condition using urgency scoring
Produce a structured SBAR-style report (Situation, Background, Assessment, Recommendation)







3. How It Works
The system operates in the following steps:
Step 1: Patient Interaction (GUI Interface)
The user interacts with a graphical interface built using Tkinter. The system presents 5 structured medical questions in Amharic.



Step 2: Data Collection
The patient answers each question one by one using a simple input field. The system allows navigation using:
Next button
Back button
Step 3: AI Analysis
After completing all questions, the system combines all answers into a single text input and sends it to the AI agent.
The agent:
Scans for medical keywords in Amharic
Matches them with the knowledge base
Determines the most relevant condition using urgency scoring
Step 4: Confirmation Stage
The system displays the AI-generated suggestion to the user and asks for confirmation:
If the user confirms → the system proceeds to generate the report
If the user rejects → the system restarts the questionnaire

Step 5: Report Generation
Once confirmed, the system generates a structured medical report that includes:
Patient condition (Situation)
Background summary
Possible diagnosis (Assessment)
Suggested medication and warning signs (Recommendation)


4. Output (Result)
The system produces a structured medical summary that helps doctors quickly understand the patient before consultation.
The final output includes:
Main patient problem
Symptom-based analysis
Possible condition identification
Medication suggestions
Red flag warnings
Structured SBAR-style format
This reduces the time doctors spend on basic questioning and improves decision-making efficiency.



5. Conclusion
This project demonstrates how a Goal-Based AI system can improve healthcare efficiency in Ethiopian hospitals.
By collecting and analyzing patient information before consultation, the system:
Reduces waiting and consultation time
Minimizes language barriers
Improves communication between patients and doctors
Helps doctors focus more on diagnosis rather than data collection
Overall, the Medical Pre-Consultation Assistant shows how artificial intelligence can support healthcare systems in resource-constrained environments.

.

