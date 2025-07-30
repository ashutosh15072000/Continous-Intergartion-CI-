import streamlit as st

## Streamlit UI
st.title("power calculator")
st.write("Enter the number to calculate its square,cubic,and the fifth power")

## Get user input
num1 = st.number_input("Enter the first number", value=1,step=1)


## Calculate results
square = num1 ** 2
cube=num1**3
fifth_power=num1**5

## Display
st.write(f"Square of {num1} is {square}")
st.write(f"Cube of {num1} is {cube}")
st.write(f"Fifth power of {num1} is {fifth_power}")