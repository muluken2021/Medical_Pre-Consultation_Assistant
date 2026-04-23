import tkinter as tk
import json
from main import TriageAgent
from knowledge_base import medical_knowledge_base

# AI
agent = TriageAgent(medical_knowledge_base)

# STATE
answers = [""] * 5
current_q = 0
detected = None

questions = [
    "ዋና ህመምዎ ምንድን ነው?",
    "ትኩሳት አለዎት?",
    "መቼ ጀመረ?",
    "ምን ያህል ከባድ ነው?",
    "ሌሎች ምልክቶች አሉ?"
]

# RESET
def start_new_patient():
    global answers, current_q, detected

    answers = [""] * 5
    current_q = 0
    detected = None

    question_label.config(text=questions[0], fg="#f8fafc")
    progress_label.config(text="ደረጃ 1 ከ 5", fg="#38bdf8")

    entry.delete(0, tk.END)
    entry.pack(pady=20, ipady=8) # Added internal padding for modern look

    btn_frame.pack(pady=15)

    yes_btn.pack_forget()
    no_btn.pack_forget()

    output.delete("1.0", tk.END)

# UPDATE
def update_ui():
    question_label.config(text=questions[current_q])
    progress_label.config(text=f"ደረጃ {current_q+1} ከ 5")

    entry.delete(0, tk.END)
    entry.insert(0, answers[current_q])

# NEXT
def next_step():
    global current_q

    val = entry.get().strip()
    if not val:
        return

    answers[current_q] = val

    if current_q < 4:
        current_q += 1
        update_ui()
    else:
        show_result()

# BACK
def back_step():
    global current_q

    answers[current_q] = entry.get().strip()

    if current_q > 0:
        current_q -= 1
        update_ui()

# RESULT (FIXED AI MATCHING)
def show_result():
    global detected

    full_text = "".join(answers).replace(" ", "")

    detected = agent.analyze(full_text)

    entry.pack_forget()
    btn_frame.pack_forget()

    if detected:
        question_label.config(
            text=f"የተገኘ ውጤት: {detected.english_name}\n\nይህ መረጃ ትክክል ነው?",
            fg="#38bdf8"
        )

        yes_btn.pack(pady=8)
        no_btn.pack(pady=8)

    else:
        question_label.config(
            text="❗ ይቅርታ፣ ግልጽ የሆነ ምርመራ ማግኘት አልተቻለም።\nእባክዎ በአቅራቢያዎ ወደሚገኝ ሐኪም ይሂዱ።",
            fg="#f87171"
        )

        root.after(4000, start_new_patient)

# YES
def confirm_yes():
    yes_btn.pack_forget()
    no_btn.pack_forget()

    result = {
        "የጤና ሁኔታ": detected.english_name,
        "የሚወሰድ መድኃኒት": detected.medication,
        "ማስጠንቀቂያ": detected.red_flags,
        "አስቸኳይነት": detected.urgency
    }

    question_label.config(
        text="🙏 እናመሰግናለን!\nመረጃው ተመዝግቧል። በመጠበቂያ ክፍል ይጠብቁ።",
        fg="#4ade80"
    )

    output.insert(tk.END, "--- የሕክምና ሪፖርት ---\n")
    output.insert(tk.END, json.dumps(result, indent=4, ensure_ascii=False))

    root.after(7000, start_new_patient)

# NO
def confirm_no():
    start_new_patient()

# GUI
root = tk.Tk()
root.title("የቅድመ ሕክምና ረዳት")
root.geometry("750x680")
root.configure(bg="#0f172a")

# Header Section
title = tk.Label(
    root,
    text="🏥 የቅድመ ሕክምና AI ረዳት",
    font=("Helvetica", 20, "bold"),
    fg="#38bdf8",
    bg="#0f172a"
)
title.pack(pady=(30, 5))

progress_label = tk.Label(
    root,
    text="ደረጃ 1 ከ 5",
    font=("Helvetica", 11),
    fg="#64748b",
    bg="#0f172a"
)
progress_label.pack()

# Content Card
question_label = tk.Label(
    root,
    text=questions[0],
    font=("Helvetica", 16, "bold"),
    fg="#f8fafc",
    bg="#0f172a",
    wraplength=600,
    justify="center"
)
question_label.pack(pady=50)

entry = tk.Entry(
    root, 
    width=40, 
    font=("Helvetica", 14), 
    bg="#1e293b", 
    fg="white", 
    insertbackground="white", 
    relief="flat",
    borderwidth=10
)
entry.pack(pady=10)

# Navigation
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack()

back_btn = tk.Button(
    btn_frame, 
    text="⬅ ተመለስ", 
    command=back_step, 
    bg="#475569", 
    fg="white", 
    font=("Helvetica", 11, "bold"),
    width=12,
    relief="flat",
    cursor="hand2"
)
back_btn.grid(row=0, column=0, padx=10)

next_btn = tk.Button(
    btn_frame, 
    text="ቀጣይ ➜", 
    command=next_step, 
    bg="#2563eb", 
    fg="white", 
    font=("Helvetica", 11, "bold"),
    width=12,
    relief="flat",
    cursor="hand2"
)
next_btn.grid(row=0, column=1, padx=10)

# Final Confirmation
yes_btn = tk.Button(
    root, 
    text="አዎ፣ ትክክል ነው ✔", 
    command=confirm_yes, 
    bg="#059669", 
    fg="white", 
    font=("Helvetica", 12, "bold"),
    width=25,
    relief="flat"
)

no_btn = tk.Button(
    root, 
    text="አይ፣ እንደገና ልጀምር ✖", 
    command=confirm_no, 
    bg="#b91c1c", 
    fg="white", 
    font=("Helvetica", 12, "bold"),
    width=25,
    relief="flat"
)

# Output Terminal
output = tk.Text(
    root, 
    height=10, 
    width=70,
    bg="#020617", 
    fg="#94a3b8", 
    font=("Consolas", 11),
    padx=15,
    pady=15,
    relief="flat"
)
output.pack(pady=30)

start_new_patient()
root.mainloop()