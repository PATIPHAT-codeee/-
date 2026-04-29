import tkinter as tk
from tkinter import ttk

def create_inputs():
    global entries_x, entries_y

    for widget in frame_piles.winfo_children():
        widget.destroy()

    n = int(entry_n.get())
    entries_x = []
    entries_y = []

    tk.Label(frame_piles, text="Pile").grid(row=0, column=0)
    tk.Label(frame_piles, text="x").grid(row=0, column=1)
    tk.Label(frame_piles, text="y").grid(row=0, column=2)

    for i in range(n):
        tk.Label(frame_piles, text=f"{i+1}").grid(row=i+1, column=0)

        ex = tk.Entry(frame_piles, width=10)
        ey = tk.Entry(frame_piles, width=10)

        ex.grid(row=i+1, column=1)
        ey.grid(row=i+1, column=2)

        entries_x.append(ex)
        entries_y.append(ey)


def calculate():
    try:
        n = int(entry_n.get())
        Q = float(entry_Q.get())
        Mx = float(entry_Mx.get())
        My = float(entry_My.get())

        x = [float(e.get()) for e in entries_x]
        y = [float(e.get()) for e in entries_y]

        sumx2 = sum([xi**2 for xi in x])
        sumy2 = sum([yi**2 for yi in y])

        result_text.delete("1.0", tk.END)

        result_text.insert(tk.END, "Pile\tPi\n")

        sumP = 0

        for i in range(n):
            Pi = Q/n

            if sumx2 != 0:
                Pi += My * x[i] / sumx2

            if sumy2 != 0:
                Pi += Mx * y[i] / sumy2

            sumP += Pi

            result_text.insert(tk.END, f"{i+1}\t{Pi:.2f}\n")

        result_text.insert(tk.END, "\n")
        result_text.insert(tk.END, f"ΣPi = {sumP:.2f}\n")
        result_text.insert(tk.END, f"Q = {Q:.2f}\n")

    except Exception as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Error: {e}")


# ===== UI =====
root = tk.Tk()
root.title("คำนวณฐานรากเยื้องศูนย์")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

tk.Label(frame_top, text="Q").grid(row=0, column=0)
entry_Q = tk.Entry(frame_top)
entry_Q.grid(row=0, column=1)

tk.Label(frame_top, text="Mx").grid(row=1, column=0)
entry_Mx = tk.Entry(frame_top)
entry_Mx.grid(row=1, column=1)

tk.Label(frame_top, text="My").grid(row=2, column=0)
entry_My = tk.Entry(frame_top)
entry_My.grid(row=2, column=1)

tk.Label(frame_top, text="จำนวนเสาเข็ม (n)").grid(row=3, column=0)
entry_n = tk.Entry(frame_top)
entry_n.insert(0, "2")
entry_n.grid(row=3, column=1)

tk.Button(frame_top, text="สร้างตาราง", command=create_inputs).grid(row=4, columnspan=2, pady=5)

frame_piles = tk.Frame(root)
frame_piles.pack()

tk.Button(root, text="คำนวณ", command=calculate).pack(pady=10)

result_text = tk.Text(root, height=10, width=40)
result_text.pack()

root.mainloop()
