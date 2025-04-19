import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# دالة لضبط النافذة في منتصف الشاشة
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# التحقق من العمر
def check_age():
    try:
        age = int(age_entry.get())
        if age < 18:
            messagebox.showerror("خطأ", "عذرًا، لا يسمح لك بالدخول لأن عمرك أقل من 18 عامًا.")
        else:
            messagebox.showinfo("مرحبًا", "مرحبًا بك! يمكنك الدخول.")
            show_main_window()
    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال عمر صحيح (رقم فقط).")

# إرسال الرسالة
def send_message():
    user_name = name_entry.get()
    user_email = email_entry.get()
    recipient_email = recipient_entry.get()
    message = message_entry.get("1.0", tk.END).strip()
    
    if user_name and user_email and recipient_email and message:
        try:
            # إعدادات البريد الإلكتروني
            sender_email = "your_email@gmail.com"  # ضع بريدك الإلكتروني هنا
            sender_password = "your_password"      # ضع كلمة مرور بريدك الإلكتروني هنا
            
            # إنشاء الرسالة
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = f"رسالة من {user_name}"
            msg.attach(MIMEText(message, 'plain'))
            
            # إرسال الرسالة باستخدام SMTP
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient_email, msg.as_string())
            
            messagebox.showinfo("نجاح", f"تم إرسال الرسالة بنجاح إلى {recipient_email}")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء إرسال الرسالة: {e}")
    else:
        messagebox.showerror("خطأ", "يرجى ملء جميع الحقول!")

# نافذة الترحيب
def show_main_window():
    # إخفاء نافذة إدخال العمر
    age_window.destroy()

    # إنشاء نافذة الترحيب
    root = tk.Tk()
    root.title("واجهة الترحيب")
    center_window(root, 600, 500)  # ضبط النافذة في المنتصف

    # رسالة الترحيب
    tk.Label(root, text="أهلاً بك عزيز المستخدم!", font=("Arial", 16, "bold")).pack(pady=20)

    # إدخال الاسم
    tk.Label(root, text="الاسم:", font=("Arial", 14)).pack(pady=5)
    global name_entry
    name_entry = tk.Entry(root, font=("Arial", 14), width=30)
    name_entry.pack(pady=5)

    # إدخال البريد الإلكتروني الشخصي
    tk.Label(root, text="البريد الإلكتروني الشخصي:", font=("Arial", 14)).pack(pady=5)
    global email_entry
    email_entry = tk.Entry(root, font=("Arial", 14), width=30)
    email_entry.pack(pady=5)

    # إدخال البريد الإلكتروني للمرسل إليه
    tk.Label(root, text="البريد الإلكتروني للمرسل إليه:", font=("Arial", 14)).pack(pady=5)
    global recipient_entry
    recipient_entry = tk.Entry(root, font=("Arial", 14), width=30)
    recipient_entry.pack(pady=5)

    # إدخال الرسالة
    tk.Label(root, text="الرسالة:", font=("Arial", 14)).pack(pady=5)
    global message_entry
    message_entry = tk.Text(root, height=8, width=50, font=("Arial", 14))
    message_entry.pack(pady=5)

    # زر الإرسال
    send_button = tk.Button(root, text="إرسال الرسالة", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=send_message)
    send_button.pack(pady=20)

    root.mainloop()

# نافذة إدخال العمر
age_window = tk.Tk()
age_window.title("التحقق من العمر")
center_window(age_window, 400, 200)  # ضبط النافذة في المنتصف

tk.Label(age_window, text="كم عمرك؟", font=("Arial", 14)).pack(pady=20)
age_entry = tk.Entry(age_window, font=("Arial", 14), width=15)
age_entry.pack(pady=10)

check_button = tk.Button(age_window, text="تحقق", font=("Arial", 14, "bold"), bg="#2196F3", fg="white", command=check_age)
check_button.pack(pady=20)

age_window.mainloop()