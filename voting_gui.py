import tkinter as tk
from tkinter import messagebox, scrolledtext
from blockchain import Blockchain

chain = Blockchain()

def vote():
    voter_id = entry_voter.get().strip()
    candidate = entry_candidate.get().strip()

    if not voter_id or not candidate:
        messagebox.showwarning("Input Error", "Voter ID and Candidate are required.")
        return

    chain.add_vote(voter_id, candidate)

    if len(chain.pending_votes) == 0:  # Block just got created
        messagebox.showinfo("Block Created", f"✅ New block added! Total blocks: {len(chain.chain)}")

    entry_voter.delete(0, tk.END)
    entry_candidate.delete(0, tk.END)

def show_blockchain():
    output.delete("1.0", tk.END)
    for block in chain.chain:
        output.insert(tk.END, f"\nBlock {block.index} - Hash: {block.hash[:10]}...\n")
        output.insert(tk.END, f"Timestamp: {block.timestamp}\n")
        output.insert(tk.END, f"Previous Hash: {block.previous_hash[:10]}...\n")
        output.insert(tk.END, f"Votes: {block.votes}\n")
        output.insert(tk.END, "-" * 50 + "\n")

# GUI setup
root = tk.Tk()
root.title("Blockchain Voting System")
root.geometry("500x600")
root.config(bg="#f0f0f0")

# Labels
tk.Label(root, text="Voter ID:", bg="#f0f0f0").pack(pady=5)
entry_voter = tk.Entry(root, width=40)
entry_voter.pack()

tk.Label(root, text="Candidate Name:", bg="#f0f0f0").pack(pady=5)
entry_candidate = tk.Entry(root, width=40)
entry_candidate.pack()

# Buttons
tk.Button(root, text="Cast Vote", command=vote, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(root, text="Show Blockchain", command=show_blockchain, bg="#2196F3", fg="white").pack(pady=5)

# Output window
output = scrolledtext.ScrolledText(root, height=20, width=60)
output.pack(pady=10)

root.mainloop()
