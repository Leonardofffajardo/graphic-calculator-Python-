import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphicCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Graphic Calculator")

        self.label_function = tk.Label(self.master, text="Enter a function (e.g., x**2 + 3*x - 2):")
        self.label_function.grid(row=0, column=0, padx=10, pady=10)

        self.entry_function = tk.Entry(self.master)
        self.entry_function.grid(row=0, column=1, padx=10, pady=10)

        self.plot_button = tk.Button(self.master, text="Plot", command=self.plot_function)
        self.plot_button.grid(row=0, column=2, padx=10, pady=10)

        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.grid(row=1, columnspan=3, padx=10, pady=10)

    def plot_function(self):
        function_str = self.entry_function.get()

        if not function_str:
            messagebox.showerror("Error", "Please enter a function")
            return

        try:
            x = np.linspace(-10, 10, 400)
            y = eval(function_str)

            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.axhline(0, color='black', lw=0.5)
            ax.axvline(0, color='black', lw=0.5)
            ax.grid(True)

            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title(f'Graph of {function_str}')

            canvas = FigureCanvasTkAgg(fig, master=self.canvas)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = GraphicCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
