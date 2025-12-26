import streamlit as st

st.title("📋 Student Attendance Tracker")

# Initialize session state
if "attendance" not in st.session_state:
    st.session_state.attendance = []

student_name = st.text_input("Enter Student Name")

status = st.radio("Attendance Status", ["Present", "Absent"])

if st.button("Add Attendance"):
    if student_name != "":
        st.session_state.attendance.append(
            {"name": student_name, "status": status}
        )
        st.success("Attendance Added")

st.subheader("Attendance List")

for record in st.session_state.attendance:
    st.write(f"👤 {record['name']} — {record['status']}")