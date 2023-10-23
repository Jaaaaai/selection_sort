import pandas as pd
import tkinter as tk
from tkinter import ttk

def display_data_in_table(df):
    root = tk.Tk()
    root.title("Sorted Data by Family Members")

    tree = ttk.Treeview(root, columns=list(df.columns), show="headings")
    tree.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    # Setting up the columns
    for col in df.columns:
        tree.heading(col, text=col)
        # Dynamically adjust the column width based on column name length
        tree.column(col, width=100 + len(col) * 10)

    # Inserting the rows
    for index, row in df.iterrows():
        tree.insert("", "end", values=tuple(row))

    # Adding a vertical scrollbar
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=scrollbar.set)

    root.mainloop()

def selection_sort(df, column_name):
    n = len(df)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if df.iloc[j][column_name] > df.iloc[max_idx][column_name]:
                max_idx = j

        df.iloc[i], df.iloc[max_idx] = df.iloc[max_idx].copy(), df.iloc[i].copy()
    return df        

# Read the data from the Excel file
file_path = "sample_data.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')
df['age'] = pd.to_numeric(df['age'])
df = df.dropna(subset=['age'])
df['age'] = df['age'].astype(int)
df_sorted = selection_sort(df, 'age')
# Check if the 'age' column exists in the DataFrame
# if 'family_members' not in df.columns:
    # raise ValueError("'family_members' column not found in the Excel file")

# Sort the data by the 'age' column in descending order
# df_sorted = df.sort_values(by="family_members", ascending=False)

# Display the sorted data in a table
display_data_in_table(df_sorted)