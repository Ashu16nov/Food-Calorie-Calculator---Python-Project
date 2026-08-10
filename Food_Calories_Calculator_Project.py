# ---------------------------------------------------
# Project: Food Calorie Calculator (Attractive GUI)
# All Rights Reserved To:
# Name: [Aashutosh]
# UID: [25MCA20107]
# Section: [25MCA-1A]
# ---------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox

# Food Database
food_data = {
    "Apple": 905, "Banana": 105, "Orange": 62, "Mango": 150, "Grapes": 64,
    "Watermelon": 805, "Papaya": 59, "Strawberry": 33, "Pineapple": 82,
    "Rice": 206, "Roti": 80, "Bread": 80, "Pasta": 221, "Noodles": 138,
    "Poha": 180, "Idli": 58, "Dosa": 168, "Upma": 240, "Paratha": 260,
    "Egg": 78, "Milk": 122, "Paneer": 265, "Chicken": 335, "Fish": 206,
    "Dal": 198, "Chole": 280, "Rajma": 215, "Samosa": 262, "Burger": 354,
    "Pizza": 285, "Sandwich": 250, "Fries": 365, "Chips": 152,
    "Cake": 240, "Coffee": 2, "Tea": 30, "Juice": 112, "Cold Drink": 150,
    "Lassi": 250, "Milkshake": 300, "Ice Cream": 207, "Salad": 50, "Water":00
}

# Functions 
def add_food():
    """Add selected food to list"""
    food = food_combo.get()
    if not food:
        messagebox.showwarning("Select Food", "Please choose a food item first!")
        return
    food_listbox.insert(tk.END, food)
    update_total()


def remove_food():
    """Remove selected food from list"""
    selected = food_listbox.curselection()
    if selected:
        food_listbox.delete(selected)
        update_total()
    else:
        messagebox.showwarning("Select Item", "Please select a food item to remove!")

def clear_all():
    """Clear all selected items"""
    food_listbox.delete(0, tk.END)
    update_total()

def update_total():
    """Recalculate total calories"""
    foods = food_listbox.get(0, tk.END)
    total = sum(food_data.get(food, 0) for food in foods)
    total_label.config(text=f"🔥 Total: {total} kcal")

def show_summary():
    """Show detailed calorie summary"""
    foods = food_listbox.get(0, tk.END)
    if not foods:
        messagebox.showinfo("No Items", "Please add some foods first!")
        return

    summary = "\n".join(f"{f} → {food_data[f]} kcal" for f in foods)
    total = sum(food_data.get(f, 0) for f in foods)
    summary += f"\n\nTotal Calories: {total} kcal"
    messagebox.showinfo("Calorie Summary", summary)

# GUI Window Setup
root = tk.Tk()
root.title("🍔 Food Calorie Calculator 🍎")
root.geometry("650x550")
root.resizable(False, False)
root.configure(bg="#FFF7E9")

# Title Section
title_frame = tk.Frame(root, bg="#FF6B6B")
title_frame.pack(fill="x")

title_label = tk.Label(
    title_frame,
    text="🍎 FOOD CALORIE CALCULATOR 🍔",
    font=("Poppins", 18, "bold"),
    fg="white",
    bg="#FF6B6B",
    pady=10
)
title_label.pack()

# Food Selection Frames
select_frame = tk.Frame(root, bg="#FFF7E9")
select_frame.pack(pady=20)

food_label = tk.Label(select_frame, text="Select Food Item:", font=("Poppins", 12), bg="#FFF7E9")
food_label.grid(row=0, column=0, padx=5, pady=5)

food_combo = ttk.Combobox(select_frame, values=sorted(food_data.keys()), width=30, font=("Poppins", 11))
food_combo.grid(row=0, column=1, padx=5, pady=5)

add_button = tk.Button(select_frame, text="➕ Add", command=add_food, font=("Poppins", 10, "bold"),
                       bg="#4CAF50", fg="white", width=10, relief="flat")
add_button.grid(row=0, column=2, padx=10)

remove_button = tk.Button(select_frame, text="🗑 Remove", command=remove_food, font=("Poppins", 10, "bold"),
                          bg="#E74C3C", fg="white", width=10, relief="flat")
remove_button.grid(row=0, column=3, padx=10)

# Food List Frame
list_frame = tk.LabelFrame(root, text="🍽️ Your Selected Foods", font=("Poppins", 12, "bold"),
                           bg="#FFF7E9", fg="#444", padx=10, pady=10)
list_frame.pack(pady=10)

food_listbox = tk.Listbox(list_frame, width=50, height=10, font=("Consolas", 11),
                          bg="#FFF", fg="#333", relief="groove", selectbackground="#FF6B6B")
food_listbox.pack(padx=10, pady=5)

# Action Buttons
action_frame = tk.Frame(root, bg="#FFF7E9")
action_frame.pack(pady=15)

calc_button = tk.Button(action_frame, text="💪 Calculate", command=show_summary, font=("Poppins", 11, "bold"),
                        bg="#3498DB", fg="white", width=12, relief="flat")
calc_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(action_frame, text="🧹 Clear All", command=clear_all, font=("Poppins", 11, "bold"),
                         bg="#9B59B6", fg="white", width=12, relief="flat")
clear_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(action_frame, text="🚪 Exit", command=root.quit, font=("Poppins", 11, "bold"),
                        bg="#7F8C8D", fg="white", width=12, relief="flat")
exit_button.grid(row=0, column=2, padx=10)

# Live Calorie Display
total_label = tk.Label(root, text="🔥 Total: 0 kcal", font=("Poppins", 16, "bold"), bg="#FFF7E9", fg="#FF6B6B")
total_label.pack(pady=10)

# Footer 
footer_label = tk.Label(root, text="💡 Tip: Eat healthy & stay hydrated daily!",
                        font=("Poppins", 10, "italic"), bg="#FFF7E9", fg="#555")
footer_label.pack(side="bottom", pady=10)

# Run GUI
root.mainloop()
