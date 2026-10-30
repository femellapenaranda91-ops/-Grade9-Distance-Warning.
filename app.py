import streamlit as st
import pandas as pd

st.title("Emergency Signal Monitoring System")

pressed = st.checkbox("Emergency Button Pressed")

# TASK 3: Change the displayed interval to 250 ms
blink_interval = 500

if pressed:
    st.error("EMERGENCY ACTIVATED")
    st.write("LED Status: BLINKING")
    st.metric("Blink Interval", f"{blink_interval} ms")
else:
    st.success("SYSTEM STANDBY")
    st.write("LED Status: OFF")

data = pd.DataFrame({
    "Button State": ["Released", "Pressed"],
    "LED Status": ["OFF", "BLINKING"]
})

st.dataframe(data)
