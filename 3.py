import streamlit as st

st.title("คำนวณแรงในเสาเข็ม (เยื้องศูนย์)")

# Input
Q = st.number_input("Q (แรงรวม)", value=0.0)
Mx = st.number_input("Mx", value=0.0)
My = st.number_input("My", value=0.0)
n = st.number_input("จำนวนเสาเข็ม", min_value=1, value=2)

x = []
y = []

st.subheader("พิกัดเสาเข็ม (จาก Centroid)")

for i in range(n):
    col1, col2 = st.columns(2)
    with col1:
        xi = st.number_input(f"x{i+1}", key=f"x{i}")
    with col2:
        yi = st.number_input(f"y{i+1}", key=f"y{i}")
    x.append(xi)
    y.append(yi)

if st.button("คำนวณ"):
    sumx2 = sum([xi**2 for xi in x])
    sumy2 = sum([yi**2 for yi in y])

    st.subheader("ผลลัพธ์")

    sumP = 0
    for i in range(n):
        Pi = Q/n

        if sumx2 != 0:
            Pi += My * x[i] / sumx2

        if sumy2 != 0:
            Pi += Mx * y[i] / sumy2

        sumP += Pi
        st.write(f"Pile {i+1} = {Pi:.2f}")

    st.write("---")
    st.write(f"ΣPi = {sumP:.2f}")
    st.write(f"Q = {Q:.2f}")
