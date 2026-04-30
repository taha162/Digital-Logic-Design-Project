import tkinter as tk
from tkinter import messagebox

# دالة لتحويل الرقم من أي نظام إلى العشري أولاً
def to_decimal(number_str, base):
    try:
        return int(number_str, base)
    except:
        return None

# دالة التحويل الرئيسية
def convert():
    number = entry_input.get().strip().upper()
    from_base = base_var.get()

    if not number:
        messagebox.showwarning("تنبيه", "الرجاء إدخال رقم")
        return

    # التحقق من صحة الإدخال
    valid_chars = {
        2:  "01",
        8:  "01234567",
        10: "0123456789",
        16: "0123456789ABCDEF"
    }

    for ch in number:
        if ch not in valid_chars[from_base]:
            messagebox.showerror("خطأ", f"الرقم يحتوي على رمز غير صالح للنظام المختار: '{ch}'")
            return

    # تحويل إلى عشري أولاً
    decimal = to_decimal(number, from_base)
    if decimal is None:
        messagebox.showerror("خطأ", "تعذّر تحويل الرقم")
        return

    # حساب النتائج
    result_bin  = bin(decimal)[2:]   # إزالة 0b
    result_oct  = oct(decimal)[2:]   # إزالة 0o
    result_dec  = str(decimal)
    result_hex  = hex(decimal)[2:].upper()  # إزالة 0x

    # عرض النتائج
    lbl_bin.config(text=result_bin)
    lbl_oct.config(text=result_oct)
    lbl_dec.config(text=result_dec)
    lbl_hex.config(text=result_hex)

# دالة المسح
def clear_all():
    entry_input.delete(0, tk.END)
    lbl_bin.config(text="-")
    lbl_oct.config(text="-")
    lbl_dec.config(text="-")
    lbl_hex.config(text="-")

# ── إعداد النافذة ──────────────────────────────────
window = tk.Tk()
window.title("محول الأنظمة العددية")
window.geometry("480x420")
window.resizable(False, False)
window.configure(bg="#f0f4f8")

# ── العنوان ────────────────────────────────────────
tk.Label(window,
         text="محول الأنظمة العددية",
         font=("Arial", 16, "bold"),
         bg="#f0f4f8", fg="#1a1a2e").pack(pady=(20, 4))

tk.Label(window,
         text="Binary  |  Octal  |  Decimal  |  Hexadecimal",
         font=("Arial", 9),
         bg="#f0f4f8", fg="#888").pack(pady=(0, 4))

tk.Label(window,
         text="اعداد الطالبين: طه جاسم محمد | " \
         "ثوبان عمر شاكر",
         font=("Arial", 12),
         bg="#f0f4f8", fg="#888").pack(pady=(0, 15))

# ── إطار الإدخال ───────────────────────────────────
frame_input = tk.Frame(window, bg="#f0f4f8")
frame_input.pack(pady=4)

tk.Label(frame_input, text="أدخل الرقم:", font=("Arial", 11),
         bg="#f0f4f8").grid(row=0, column=0, padx=8, sticky="e")

entry_input = tk.Entry(frame_input, font=("Courier", 13),
                       width=18, bd=2, relief="groove",
                       justify="center")
entry_input.grid(row=0, column=1, padx=8)

# ── اختيار النظام ──────────────────────────────────
frame_base = tk.Frame(window, bg="#f0f4f8")
frame_base.pack(pady=10)

tk.Label(frame_base, text="النظام المدخل:", font=("Arial", 11),
         bg="#f0f4f8").grid(row=0, column=0, padx=8, sticky="e")

base_var = tk.IntVar(value=10)

bases = [("ثنائي (2)",    2),
         ("ثُماني (8)",   8),
         ("عشري (10)",   10),
         ("سداسي  عشر (16)", 16)]

for i, (label, val) in enumerate(bases):
    tk.Radiobutton(frame_base, text=label, variable=base_var, value=val,
                   font=("Arial", 10), bg="#f0f4f8",
                   activebackground="#f0f4f8").grid(row=0, column=i+1, padx=6)

# ── الأزرار ────────────────────────────────────────
frame_btns = tk.Frame(window, bg="#f0f4f8")
frame_btns.pack(pady=10)

tk.Button(frame_btns, text="تحويل", font=("Arial", 11, "bold"),
          bg="#3a86ff", fg="white", width=10, bd=0, pady=6,
          cursor="hand2", command=convert).grid(row=0, column=0, padx=10)

tk.Button(frame_btns, text="مسح", font=("Arial", 11),
          bg="#e0e0e0", fg="#333", width=10, bd=0, pady=6,
          cursor="hand2", command=clear_all).grid(row=0, column=1, padx=10)

# ── إطار النتائج ───────────────────────────────────
frame_results = tk.Frame(window, bg="white",
                         bd=2, relief="groove",
                         padx=20, pady=0)
frame_results.pack(padx=20, pady=0, fill="x")

tk.Label(frame_results, text="النتائج",
         font=("Arial", 12, "bold"),
         bg="white", fg="#1a1a2e").grid(row=0, column=0,
                                         columnspan=2, pady=(0, 0))

labels_info = [
    ("ثنائي  (Base 2):",   "#e63946"),
    ("ثُماني  (Base 8):",   "#f4a261"),
    ("عشري  (Base 10):",   "#2a9d8f"),
    ("سداسي عشر (Base 16):", "#6a4c93"),
]

result_labels = []
for i, (text, color) in enumerate(labels_info):
    tk.Label(frame_results, text=text,
             font=("Arial", 10, "bold"),
             bg="white", fg=color,
             anchor="e", width=20).grid(row=i+1, column=0,
                                         pady=5, padx=(0, 10))

    lbl = tk.Label(frame_results, text="-",
                   font=("Courier", 12, "bold"),
                   bg="white", fg="#222",
                   anchor="w", width=22)
    lbl.grid(row=i+1, column=1, pady=5)
    result_labels.append(lbl)

lbl_bin, lbl_oct, lbl_dec, lbl_hex = result_labels

# ── تشغيل التطبيق ──────────────────────────────────
entry_input.bind("<Return>", lambda e: convert())
window.mainloop()
