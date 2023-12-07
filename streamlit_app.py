"""import streamlit as st
import pandas as pd

data = {'Név': ['John', 'Jane', 'Bob', 'Alice'],
        'Életkor': [25, 30, 22, 28],
        'Város': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Streamlit alkalmazás kódja

st.dataframe(df)"""


import streamlit as st

def main():
    st.title("E-mail Bekérés")

    # Felhasználó nevének bekérése
    name = st.text_input("Kérlek, add meg a neved:")

    # E-mail cím bekérése
    email = st.text_input("Kérlek, add meg az e-mail címed:")

    age = st.number_input("Kérlek, add meg az életkorod:", min_value=0, max_value=150)    

    # Elküld gomb
    if st.button("Elküld"):
        if name and email:
            save_to_file(name, email)
            st.success(f"Köszönjük, {name}! Az e-mail címed: {email}. Az adatokat elmentettük.")
        else:
            st.error("Kérlek, töltsd ki mindkét mezőt!")
                

def save_to_file(name, email,age):
    with open("adatok.txt", "a") as file:
        file.write(f"Név: {name}, E-mail: {email}\n")

if __name__ == "__main__":
    main()
