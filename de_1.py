import tkinter as tk

class Tugiac:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def chuvi(self):
        return self.a + self.b + self.c + self.d

    def canhlon(self):
        return max(self.a, self.b, self.c, self.d)

def nhapdulieu():
    c1 = float(canh1_entry.get())
    c2 = float(canh2_entry.get())
    c3 = float(canh3_entry.get())
    c4 = float(canh4_entry.get())
    obj = Tugiac(c1, c2, c3, c4)
    ds.append(obj)
    thongbao_label.config(text="Dữ liệu đã được thêm!")

def tinhtoan():
    s = ""
    cv = []
    for i, tugiac in enumerate(ds, 1):
        s += f'Hình {i}: Chu vi = {tugiac.chuvi()}, Cạnh lớn nhất = {tugiac.canhlon()}\n'
        cv.append(tugiac.chuvi())
    s += f'Chu vi nhỏ nhất: {min(cv)}'
    ketqua_label.config(text=s)

ds = []

app = tk.Tk()
app.geometry('400x400')
app.title('Tính chu vi và cạnh lớn nhất của tứ giác')

tk.Label(app, text='Nhập 4 cạnh của tứ giác:').pack()

canh1_entry = tk.Entry(app)
canh1_entry.pack()

canh2_entry = tk.Entry(app)
canh2_entry.pack()

canh3_entry = tk.Entry(app)
canh3_entry.pack()

canh4_entry = tk.Entry(app)
canh4_entry.pack()

tk.Button(app, text='Thêm dữ liệu', command=nhapdulieu).pack()
tk.Button(app, text='Tính toán', command=tinhtoan).pack()

thongbao_label = tk.Label(app, text="")
thongbao_label.pack()

ketqua_label = tk.Label(app, text="")
ketqua_label.pack()

app.mainloop()
