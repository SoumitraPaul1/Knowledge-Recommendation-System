import tkinter as tk
from tkinter import messagebox
from K_R_S import KnowledgeGraph

kg = KnowledgeGraph()

GRAPH_FILE = "Python\DSA\graph_data.txt"
LEARNED_FILE = "Python\DSA\learned_data.txt"

# Load saved graph data
import os

if os.path.exists(GRAPH_FILE):
    with open(GRAPH_FILE, "r") as f:
        for line in f:
            if "->" in line:
                prereq, topic = line.strip().split("->")
                prereq = prereq.strip()
                topic = topic.strip()
                kg.add_prerequisite(topic, prereq)

if os.path.exists(LEARNED_FILE):
    with open(LEARNED_FILE, "r") as f:
        for line in f:
            kg.mark_learned(line.strip())


def add_topic():
    topic = entry_topic.get()
    prereq = entry_prereq.get()
    if topic and prereq:
        kg.add_prerequisite(topic, prereq)
        with open(GRAPH_FILE, "a") as f:
            f.write(f"{prereq} -> {topic}\n")
        messagebox.showinfo("Added", f"{prereq} -> {topic}")
    else:
        messagebox.showwarning("Input", "Enter both Topic and Prerequisite")

def mark_learned():
    topic = entry_learned.get()
    if topic:
        kg.mark_learned(topic)
        with open(LEARNED_FILE, "a") as f:
            f.write(f"{topic}\n")
        messagebox.showinfo("Learned", f"Marked {topic} as learned")
    else:
        messagebox.showwarning("Input", "Enter a topic to mark as learned")

def show_path():
    topic = entry_check.get()
    if topic:
        path = kg.get_prerequisites(topic)
        output.set(" <- ".join(path) if path else "No prerequisites found")
    else:
        messagebox.showwarning("Input", "Enter a topic to check path")

def show_next():
    next_topics = kg.get_next_learnable()
    output.set("Next learnable topics: " + ", ".join(next_topics))

# GUI setup
root = tk.Tk()
root.title("Knowledge Recommendation System")
root.geometry("400x300")  # Set the window size to 400px wide and 300px high

entry_topic = tk.Entry(root)
entry_topic.grid(row=0, column=1, padx=10, pady=5)
entry_prereq = tk.Entry(root)
entry_prereq.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Topic").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Prerequisite").grid(row=1, column=0, padx=10, pady=5)
tk.Button(root, text="Add Prerequisite", command=add_topic).grid(row=2, columnspan=2, pady=5)

entry_learned = tk.Entry(root)
entry_learned.grid(row=3, column=1, padx=10, pady=5)
tk.Label(root, text="Learned Topic").grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Mark Learned", command=mark_learned).grid(row=4, columnspan=2, pady=5)

entry_check = tk.Entry(root)
entry_check.grid(row=5, column=1, padx=10, pady=5)
tk.Label(root, text="Check Path For").grid(row=5, column=0, padx=10, pady=5)
tk.Button(root, text="Show Path", command=show_path).grid(row=6, columnspan=2, pady=5)

tk.Button(root, text="Show Next Learnable", command=show_next).grid(row=7, columnspan=2, pady=5)

output = tk.StringVar()
tk.Label(root, textvariable=output, wraplength=350).grid(row=8, columnspan=2, padx=10, pady=10)
root.mainloop()
