import tkinter as tk
from tkinter import messagebox


import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    try:
        sender_email = gmail_entry.get()
        app_password = app_pass_entry.get()
        recipient_email = to_entry.get()
        subject = subject_entry.get()
        message_body = message_text.get("1.0", tk.END).strip()

        if not (sender_email and app_password and recipient_email and subject and message_body):
            messagebox.showwarning("Input Error", "⚠️ Please fill in all fields before sending.")
            return

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message_body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        messagebox.showinfo("Success", f"✅ Email sent successfully to {recipient_email}!")

    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to send email.\n\nError: {str(e)}")

# UI Setup
root = tk.Tk()
root.title("Email Automation App")
root.geometry("900x650")
root.configure(bg="#f8f9fa")

# Card Frame 
card = tk.Frame(root, bg="white", bd=3, relief="solid", padx=30, pady=30)
card.place(relx=0.5, rely=0.5, anchor="center")

# Title
title = tk.Label(card, text="📧 Email Automation Tool", font=("Segoe UI", 18, "bold"),
                 bg="white", fg="#34495e")
title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Label Style
label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "white"}

# Gmail ID
tk.Label(card, text="Gmail ID:", **label_style, fg="#2980b9").grid(row=1, column=0, sticky="w", pady=5)
gmail_entry = tk.Entry(card, font=("Segoe UI", 11), width=42,
                       relief="solid", bd=2, highlightbackground="#2980b9", highlightthickness=2)
gmail_entry.grid(row=1, column=1, pady=5)

# App Password 
tk.Label(card, text="App Password:", **label_style, fg="#e67e22").grid(row=2, column=0, sticky="w", pady=5)
app_pass_entry = tk.Entry(card, font=("Segoe UI", 11), show="*", width=42,
                          relief="solid", bd=2, highlightbackground="#e67e22", highlightthickness=2)
app_pass_entry.grid(row=2, column=1, pady=5)

# Recipient Email 
tk.Label(card, text="Recipient Email:", **label_style, fg="#16a085").grid(row=3, column=0, sticky="w", pady=5)
to_entry = tk.Entry(card, font=("Segoe UI", 11), width=42,
                    relief="solid", bd=2, highlightbackground="#16a085", highlightthickness=2)
to_entry.grid(row=3, column=1, pady=5)

# Subject 
tk.Label(card, text="Subject:", **label_style, fg="#8e44ad").grid(row=4, column=0, sticky="w", pady=5)
subject_entry = tk.Entry(card, font=("Segoe UI", 11), width=42,
                         relief="solid", bd=2, highlightbackground="#8e44ad", highlightthickness=2)
subject_entry.grid(row=4, column=1, pady=5)

# Message 
tk.Label(card, text="Message:", **label_style, fg="#c0392b").grid(row=5, column=0, sticky="nw", pady=5)
message_text = tk.Text(card, wrap="word", font=("Segoe UI", 11), height=8, width=42,
                       relief="solid", bd=2, highlightbackground="#c0392b", highlightthickness=2)
message_text.grid(row=5, column=1, pady=5)

# Send Button 
send_btn = tk.Button(card, text="🚀 Send Email", font=("Segoe UI", 13, "bold"),
                     bg="#27ae60", fg="white", activebackground="#219150",
                     relief="flat", padx=20, pady=10, command=send_email)
send_btn.grid(row=6, column=0, columnspan=2, pady=20)

root.mainloop()