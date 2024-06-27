import streamlit as st
from Customer import Customer
from CustomerDAO import CustomerDAO

# streamlit run main_streamlit.py
def main():

    st.set_page_config(layout='wide')
    st.write('# Bonjour')
    st.write('Hello, *World!* :sunglasses:')
    
    title = st.text_input("Movie title", "Life of Brian")
    show_button = st.button("Show", type="primary")
    if show_button:
        st.write("The current movie title is", title)


    with CustomerDAO(r"customers_db.db") as customerDAO:
        customers = list(customerDAO.findAll())

    st.table(customers)

if __name__=='__main__':
    main()
