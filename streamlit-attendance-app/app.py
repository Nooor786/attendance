import streamlit as st
import pandas as pd

st.set_page_config(page_title="Attendance Tracker", layout="centered")

st.title("📋 Student Attendance Tracker (Advanced)")

# -----------------------------
# Initialize session state
# -----------------------------
if "attendance" not in st.session_state:
    st.session_state.attendance = []

# -----------------------------
# Input Section
# -----------------------------
st.subheader("➕ Mark Attendance")

col1, col2 = st.columns(2)

with col1:
    student_name = st.text_input("Student Name")

with col2:
    status = st.selectbox("Status", ["Present", "Absent"])

if st.button("Add Attendance"):
    if student_name.strip() == "":
        st.error("Please enter student name")
    else:
        st.session_state.attendance.append(
            {"Name": student_name, "Status": status}
        )
        st.success("Attendance Added")

# -----------------------------
# Display Attendance Table
# -----------------------------
st.subheader("📄 Attendance Records")

if st.session_state.attendance:
    df = pd.DataFrame(st.session_state.attendance)
    st.dataframe(df, use_container_width=True)

    # -----------------------------
    # Statistics Section
    # -----------------------------
    present_count = df[df["Status"] == "Present"].shape[0]
    absent_count = df[df["Status"] == "Absent"].shape[0]
    total = len(df)

    st.subheader("📊 Attendance Summary")

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Students", total)
    c2.metric("Present", present_count)
    c3.metric("Absent", absent_count)

    # -----------------------------
    # Download Feature
    # -----------------------------
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇ Download Attendance CSV",
        data=csv,
        file_name="attendance.csv",
        mime="text/csv"
    )

else:
    st.info("No attendance records yet")

# -----------------------------
# Clear Data
# -----------------------------
st.subheader("🗑 Manage Records")

if st.button("Clear All Attendance"):
    st.session_state.attendance = []
    st.warning("All attendance records cleared")
