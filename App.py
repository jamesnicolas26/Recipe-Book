import tkinter as tk
from tkinter import messagebox

recipes = {}

def add_recipe():
    """Add a recipe to the book."""
    title = entry_title.get()
    ingredients = text_ingredients.get("1.0", tk.END).strip()
    if title and ingredients:
        recipes[title] = ingredients
        entry_title.delete(0, tk.END)
        text_ingredients.delete("1.0", tk.END)
        listbox_recipes.insert(tk.END, title)
    else:
        messagebox.showwarning("Warning", "Title and ingredients are required!")

def view_recipe(event):
    """View the selected recipe's ingredients."""
    try:
        selected_index = listbox_recipes.curselection()[0]
        title = listbox_recipes.get(selected_index)
        ingredients = recipes.get(title, "No ingredients found.")
        text_ingredients_display.config(state=tk.NORMAL)
        text_ingredients_display.delete("1.0", tk.END)
        text_ingredients_display.insert(tk.END, ingredients)
        text_ingredients_display.config(state=tk.DISABLED)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("Recipe Book")

# Create and place widgets
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_title = tk.Label(frame_input, text="Recipe Title:")
label_title.pack()

entry_title = tk.Entry(frame_input, width=40)
entry_title.pack()

label_ingredients = tk.Label(frame_input, text="Ingredients:")
label_ingredients.pack()

text_ingredients = tk.Text(frame_input, width=40, height=10)
text_ingredients.pack()

button_add = tk.Button(frame_input, text="Add Recipe", command=add_recipe)
button_add.pack(pady=5)

listbox_recipes = tk.Listbox(root, width=50, height=10)
listbox_recipes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
listbox_recipes.bind("<<ListboxSelect>>", view_recipe)

text_ingredients_display = tk.Text(root, width=50, height=10, state=tk.DISABLED)
text_ingredients_display.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Start the main loop
root.mainloop()
