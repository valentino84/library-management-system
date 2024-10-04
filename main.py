import tkinter as tk
from tkinter import ttk, messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x500")
        self.root.configure(bg="#f7f7f7")

        # Initialize data storage
        self.books = {}
        self.members = {}
        self.loans = {}

        # Create tabs
        self.tab_control = ttk.Notebook(root)
        self.home_tab = ttk.Frame(self.tab_control)
        self.books_tab = ttk.Frame(self.tab_control)
        self.members_tab = ttk.Frame(self.tab_control)
        self.loans_tab = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.home_tab, text='Home')
        self.tab_control.add(self.books_tab, text='Add Books')
        self.tab_control.add(self.members_tab, text='Add Members')
        self.tab_control.add(self.loans_tab, text='Book Issue')

        self.tab_control.pack(expand=1, fill='both', padx=10, pady=10)

        self.create_home_tab()
        self.create_books_tab()
        self.create_members_tab()
        self.create_loans_tab()

    def create_home_tab(self):
        label = tk.Label(self.home_tab, text="Welcome to the Library Management System!", font=("Arial", 18, "bold"), bg="#f7f7f7")
        label.pack(pady=20)

    def create_books_tab(self):
        frame = ttk.Frame(self.books_tab)
        frame.pack(pady=10)

        self.book_title_entry = ttk.Entry(frame, width=40)
        self.book_title_entry.grid(row=0, column=0, padx=5)
        self.book_title_entry.insert(0, "Book Title")

        self.add_book_button = ttk.Button(frame, text="Add Book", command=self.add_book)
        self.add_book_button.grid(row=0, column=1, padx=5)

        self.books_list = tk.Listbox(self.books_tab, height=10, width=60, bg="#fff", selectmode=tk.SINGLE)
        self.books_list.pack(pady=10)

    def create_members_tab(self):
        frame = ttk.Frame(self.members_tab)
        frame.pack(pady=10)

        self.member_name_entry = ttk.Entry(frame, width=40)
        self.member_name_entry.grid(row=0, column=0, padx=5)
        self.member_name_entry.insert(0, "Member Name")

        self.add_member_button = ttk.Button(frame, text="Add Member", command=self.add_member)
        self.add_member_button.grid(row=0, column=1, padx=5)

        self.members_list = tk.Listbox(self.members_tab, height=10, width=60, bg="#fff", selectmode=tk.SINGLE)
        self.members_list.pack(pady=10)

    def create_loans_tab(self):
        frame = ttk.Frame(self.loans_tab)
        frame.pack(pady=10)

        self.loan_member_entry = ttk.Entry(frame, width=40)
        self.loan_member_entry.grid(row=0, column=0, padx=5)
        self.loan_member_entry.insert(0, "Member Name")

        self.loan_book_entry = ttk.Entry(frame, width=40)
        self.loan_book_entry.grid(row=1, column=0, padx=5)
        self.loan_book_entry.insert(0, "Book Title")

        self.issue_book_button = ttk.Button(frame, text="Issue Book", command=self.issue_book)
        self.issue_book_button.grid(row=2, column=0, pady=5)

        self.return_book_button = ttk.Button(frame, text="Return Book", command=self.return_book)
        self.return_book_button.grid(row=2, column=1, pady=5)

        self.loans_list = tk.Listbox(self.loans_tab, height=10, width=60, bg="#fff", selectmode=tk.SINGLE)
        self.loans_list.pack(pady=10)

    def add_book(self):
        title = self.book_title_entry.get().strip()
        if title and title not in self.books:
            self.books[title] = True  # True indicates the book is available
            self.books_list.insert(tk.END, title)
            self.book_title_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Book title is empty or already exists.")

    def add_member(self):
        name = self.member_name_entry.get().strip()
        if name and name not in self.members:
            self.members[name] = []
            self.members_list.insert(tk.END, name)
            self.member_name_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Member name is empty or already exists.")

    def issue_book(self):
        member_name = self.loan_member_entry.get().strip()
        book_title = self.loan_book_entry.get().strip()

        if member_name in self.members and book_title in self.books and self.books[book_title]:
            self.loans[member_name] = book_title
            self.members[member_name].append(book_title)
            self.books[book_title] = False  # Book is now loaned out
            self.loans_list.insert(tk.END, f"{member_name} borrowed '{book_title}'")
            self.loan_member_entry.delete(0, tk.END)
            self.loan_book_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid member name or book title, or book is not available.")

    def return_book(self):
        member_name = self.loan_member_entry.get().strip()
        book_title = self.loan_book_entry.get().strip()

        if member_name in self.members and book_title in self.members[member_name]:
            self.members[member_name].remove(book_title)
            del self.loans[member_name]  # Remove loan record
            self.books[book_title] = True  # Book is now available
            self.loans_list.delete(0, tk.END)
            for member, book in self.loans.items():
                self.loans_list.insert(tk.END, f"{member} borrowed '{book}'")
            self.loan_member_entry.delete(0, tk.END)
            self.loan_book_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid return request.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
