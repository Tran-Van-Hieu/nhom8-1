import tkinter as tk
from tkinter import messagebox
from sympy import Point, Triangle, simplify, latex

class GeometryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Xác định loại hình học")

        self.label = tk.Label(root, text="Chọn loại hình học:")
        self.label.pack()

        self.geometry_type = tk.StringVar()
        self.geometry_type.set("Tam giác")

        self.radio_triangle = tk.Radiobutton(root, text="Tam giác", variable=self.geometry_type, value="Tam giác")
        self.radio_triangle.pack()

        self.radio_quadrilateral = tk.Radiobutton(root, text="Tứ giác", variable=self.geometry_type, value="Tứ giác")
        self.radio_quadrilateral.pack()

        self.input_label = tk.Label(root, text="Nhập dữ liệu:")
        self.input_label.pack()

        self.input_entry = tk.Entry(root, width=40)
        self.input_entry.pack()

        self.calculate_button = tk.Button(root, text="Xác định loại hình", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate(self):
        input_data = self.input_entry.get()
        geometry_type = self.geometry_type.get()

        try:
            if geometry_type == "Tam giác":
                points = [Point(*map(int, input_data.split()))]
                triangle = Triangle(*points)
                result = f"Đây là {simplify(triangle)}"
            elif geometry_type == "Tứ giác":
                result = self.determine_quadrilateral(input_data)
            else:
                result = "Lựa chọn không hợp lệ"
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi tính toán: {str(e)}")
            return

        self.display_result(result)

    def determine_quadrilateral(self, input_data):
        sides = list(map(int, input_data.split()))
        if len(sides) != 4:
            return "Hãy nhập đúng 4 độ dài cạnh cho tứ giác."

        a, b, c, d = sides
        if a == b == c == d:
            return "Đây là hình vuông"
        elif a == c and b == d:
            return "Đây là hình chữ nhật"
        elif a == b == c or b == c == d or a == c == d or a == b == d:
            return "Đây là hình bình hành"
        else:
            return "Đây là tứ giác thường"

    def display_result(self, result):
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = GeometryApp(root)
    root.mainloop()
