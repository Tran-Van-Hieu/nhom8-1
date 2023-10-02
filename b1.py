import tkinter as tk

def calculate():
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
        sum_result.set(a + b)
        difference_result.set(a - b)
        product_result.set(a * b)
        if b != 0:
            division_result.set(a / b)
        else:
            division_result.set("Không thể chia cho 0")
    except ValueError:
        sum_result.set("Dữ liệu không hợp lệ")
        difference_result.set("Dữ liệu không hợp lệ")
        product_result.set("Dữ liệu không hợp lệ")
        division_result.set("Dữ liệu không hợp lệ")

app = tk.Tk()
app.title("Tính toán hai số")

a_label = tk.Label(app, text="Nhập số a:")
a_label.pack()

a_entry = tk.Entry(app)
a_entry.pack()

b_label = tk.Label(app, text="Nhập số b:")
b_label.pack()

b_entry = tk.Entry(app)
b_entry.pack()

calculate_button = tk.Button(app, text="Tính toán", command=calculate)
calculate_button.pack()

sum_result = tk.StringVar()
difference_result = tk.StringVar()
product_result = tk.StringVar()
division_result = tk.StringVar()

sum_label = tk.Label(app, text="Tổng:")
sum_label.pack()
sum_output = tk.Label(app, textvariable=sum_result)
sum_output.pack()

difference_label = tk.Label(app, text="Hiệu:")
difference_label.pack()
difference_output = tk.Label(app, textvariable=difference_result)
difference_output.pack()

product_label = tk.Label(app, text="Tích:")
product_label.pack()
product_output = tk.Label(app, textvariable=product_result)
product_output.pack()

division_label = tk.Label(app, text="Thương:")
division_label.pack()
division_output = tk.Label(app, textvariable=division_result)
division_output.pack()

app.mainloop()

