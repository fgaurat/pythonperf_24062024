import sqlite3
from Customer import Customer

class CustomerDAO:

    def __init__(self,db_file) -> None:
        self.__con = sqlite3.connect(db_file)
    
    def __enter__(self):
        print("def __enter__(self)")
        return self
    
    def __exit__(self, *exc):
        print("def __exit__(self, *exc)")
        self.__con.close()


    def save(self,customer):
        sql = """INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) 
        VALUES (?,?,?,?,?)"""
        cur = self.__con.cursor()
        d = customer.__dict__
        del d["id"]
        cur.execute(sql,list(d.values()))
        self.__con.commit()

    def findAll(self):
        sql = "SELECT * FROM customers_tbl"
        cur = self.__con.cursor()
        res = cur.execute(sql)

        for row in res.fetchall():
            c = Customer(*row)
            yield c


    def __del__(self):
        self.__con.close()



