import tkinter as tk

def decimal_to_binary():
    decimal_num = decimal_field.get()
    if not decimal_num: # إذا كان الإدخال فارغًا
        result_field.config(text="Error: Input cannot be empty!")
        return
    elif not decimal_num.isdigit(): # إذا كان الإدخال يحتوي على حروف أو رموز غير أرقام
        result_field.config(text="Error: Input must contain digits only!")
        return
    decimal_num = int(decimal_num)
    operation = "" # لتخزين العملية المنفذة
    while decimal_num != 0:
        if decimal_num % 2 == 0: # عدد صحيح
            operation += "0"
        else: # عدد عشري
            operation += "1"
        decimal_num = int(decimal_num / 2) # تحويل إلى عدد صحيح وقسمة على 2
    operations.append(operation[::-1]) # إضافة العملية المنفذة إلى القائمة بعد عكسها
    result_field.config(text=operation[::-1])

def show_operations():
    operations_text = ""
    for i, operation in enumerate(operations):
        binary_num = int(operation, 2)
        decimal_num = str(int(operation, 2))
        operations_text += f"{i+1}. {operation} -> {decimal_num} in decimal\n"
    operations_field.config(text=operations_text)

operations = [] # قائمة لتخزين جميع العمليات المنفذة

window = tk.Tk()
window.title("Decimal to Binary Converter")

decimal_label = tk.Label(window, text="Enter a decimal number:")
decimal_label.pack()

decimal_field = tk.Entry(window)
decimal_field.pack()

convert_button = tk.Button(window, text="Convert", command=decimal_to_binary)
convert_button.pack()

result_field = tk.Label(window, text="")
result_field.pack()

show_button = tk.Button(window, text="Show all operations", command=show_operations)
show_button.pack()

operations_label = tk.Label(window, text="All operations:")
operations_label.pack()

operations_field = tk.Label(window, text="")
operations_field.pack()

window.mainloop()
