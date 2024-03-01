import streamlit as st
import pickle 

st.title('Iris Prediction')

a = st.number_input('Enter Sepal length ')
b = st.number_input('Enter Sepal width ')
c = st.number_input('Enter Petal length ')
d = st.number_input('Enter Petal width ')

process = st.selectbox('Choose the OPERATIONS: ', ('Addition', 'Subtraction', 'Multiplication', 'Division'))

if st.button('Good to execute??'):
    if process=='Addition':
        st.write(a+b+c+d)
    elif process=='Multiplication':
        st.write(a*b*c*d)
    else:
        st.write('Development in process')