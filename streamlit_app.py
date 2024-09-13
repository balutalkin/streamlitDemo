import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("My First Streamlit App")
    
    # Add a slider
    value = st.slider("Select a number", 0, 100, 50)
    
    # Display the selected value
    st.write(f"You selected: {value}")

    x = st.text_input("Favourite Movie ?")
    st.write(f"Your input value is: {x}")

    data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])

    st.title("Bar Chart")
    st.bar_chart(data)

    st.title("Line Chart")
    st.line_chart(data)

    st.title("Area Chart")
    st.area_chart(data)

if __name__ == "__main__":
    main()