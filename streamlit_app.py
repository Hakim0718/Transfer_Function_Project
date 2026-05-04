import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

st.title("Control System Analyzer")

# INPUTS
num = st.text_input("Enter Numerator (space-separated)", "1")
den = st.text_input("Enter Denominator (space-separated)", "1 5")

if st.button("Run Analysis"):

    num = list(map(float, num.split()))
    den = list(map(float, den.split()))

    system = ctrl.TransferFunction(num, den)

    st.subheader("Transfer Function")
    st.write(system)

    # STEP RESPONSE
    t, y = ctrl.step_response(system)

    st.subheader("Step Response c(t)")
    fig, ax = plt.subplots()
    ax.plot(t, y)
    ax.set_xlabel("Time")
    ax.set_ylabel("Response")
    ax.grid()
    st.pyplot(fig)

    # SYSTEM INFO
    info = ctrl.step_info(system)

    st.subheader("System Characteristics")
    st.write("Rise Time:", info["RiseTime"])
    st.write("Settling Time:", info["SettlingTime"])

    # POLES
    st.subheader("Poles")
    poles = system.poles()

    for p in poles:
        if np.iscomplex(p):
            st.write(f"{p.real:.4f} {'+' if p.imag >= 0 else '-'} {abs(p.imag):.4f}j")
        else:
            st.write(f"{p:.4f}")