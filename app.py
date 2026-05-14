import streamlit as st
from analyzer import analyze_car_complaint

st.set_page_config(page_title="Car Complaint Analyzer", page_icon="🚗", layout="centered")

st.title("🚗 Car Complaint Analyzer")
st.subheader("Describe your car problem — AI will diagnose it instantly")
st.markdown("---")

# Sample complaints for quick testing
st.markdown("**Quick Examples — Click to try:**")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Grinding noise on brake"):
        st.session_state.complaint = "My car makes a grinding noise when I press the brake"

with col2:
    if st.button("White smoke from exhaust"):
        st.session_state.complaint = "White smoke is coming from my exhaust pipe"

with col3:
    if st.button("Engine light is on"):
        st.session_state.complaint = "My check engine light is on and car vibrates"

st.markdown("---")

complaint = st.text_area(
    "Enter your car complaint:",
    value=st.session_state.get("complaint", ""),
    placeholder="e.g. My engine light is on and car vibrates at high speed",
    height=120
)

if st.button("Analyze My Car Problem", type="primary"):
    if complaint.strip():
        with st.spinner("AI is analyzing your complaint..."):
            result = analyze_car_complaint(complaint)
        st.success("Analysis Complete!")
        st.markdown("### Diagnosis Report")
        st.markdown(result)
    else:
        st.warning("Please enter a complaint first")

st.markdown("---")
st.caption("Powered by Claude AI — For reference only. Always consult a certified mechanic.")
