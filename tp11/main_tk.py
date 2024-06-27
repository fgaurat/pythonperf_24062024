from tkinter import *
from tkinter import ttk
from Customer import Customer
from CustomerDAO import CustomerDAO

def main_hello():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()

def main():
    with CustomerDAO(r"customers_db.db") as customerDAO:
        customers = list(customerDAO.findAll())

    ws = Tk()
    ws.title('Customers')
    ws.geometry('800x600')

    tv = ttk.Treeview(ws,show="headings")
    tv['columns']=('Id', 'Name', 'FirstName')

    tv.column('Id',  anchor=CENTER,stretch=NO)
    tv.column('Name', anchor=CENTER, width=80)
    tv.column('FirstName', anchor=CENTER, width=80)

    tv.heading('Id', text='Id', anchor=CENTER)
    tv.heading('Name', text='Name', anchor=CENTER)
    tv.heading('FirstName', text='FirstName', anchor=CENTER)
    for customer in customers:
        tv.insert(parent='', index=customer.id, iid=customer.id, text='', values=(customer.id,customer.lastName,customer.firstName))
    
    tv.pack(fill=BOTH,expand=True)



    ws.mainloop()

if __name__=='__main__':
    main()
