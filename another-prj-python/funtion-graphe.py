import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_function():
    # Clear the previous plot
    for widget in frame.winfo_children():
        widget.destroy()
    
    try:
        # Get the function and range from user input
        function_str = function_entry.get()
        x_min = float(x_min_entry.get())
        x_max = float(x_max_entry.get())
        
        # Generate x values
        x = np.linspace(x_min, x_max, 500)
        
        # Safely evaluate the function
        y = eval(function_str, {"x": x, "np": np})
        
        # Create a matplotlib figure
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, y, label=f"y = {function_str}")
        ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
        ax.axvline(0, color='black', linewidth=0.5, linestyle='--')
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        ax.legend()
        ax.set_title("Graph of the Function")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        
        # Embed the plot in the Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
    except Exception as e:
        error_label.config(text=f"Error: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Function Graph Plotter")

# Create input fields and labels
ttk.Label(root, text="Enter a function (e.g., x**2 + 3*x - 5):").pack(pady=5)
function_entry = ttk.Entry(root, width=40)
function_entry.pack(pady=5)

ttk.Label(root, text="Enter the minimum value of x:").pack(pady=5)
x_min_entry = ttk.Entry(root, width=20)
x_min_entry.pack(pady=5)

ttk.Label(root, text="Enter the maximum value of x:").pack(pady=5)
x_max_entry = ttk.Entry(root, width=20)
x_max_entry.pack(pady=5)

# Create a button to plot the function
plot_button = ttk.Button(root, text="Plot Graph", command=plot_function)
plot_button.pack(pady=10)

# Create a frame for the plot
frame = ttk.Frame(root)
frame.pack(pady=10)

# Label for displaying errors
error_label = ttk.Label(root, text="", foreground="red")
error_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
