import csv
from pprint import pprint
from Customer import Customer
from CustomerDAO import CustomerDAO


def filter_male(gen):
    for customer in gen:
        if  customer.gender == "Male":
            yield customer


def main():
    with CustomerDAO(r".\tp09\customers_db.db") as customerDAO:
        # customerDAO = CustomerDAO(r".\tp09\customers_db.db")
        customers = customerDAO.findAll()
        raise Exception()
        # customer_male = filter_male(customers)

        # for c in customer_male:
        #     print(c)
            

def main_insert():

    customerDAO = CustomerDAO(r".\tp09\customers_db.db")
    with open(r'tp09\MOCK_DATA.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c = Customer(*row.values())
            customerDAO.save(c)
            # print(c)


if __name__=='__main__':
    main()
