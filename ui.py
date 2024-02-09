import streamlit as st

# Sidebar
st.sidebar.title("Sidebar Title")

# Icons
st.sidebar.markdown('<i class="fas fa-home"></i> Home', unsafe_allow_html=True)
st.sidebar.markdown('<i class="fas fa-chart-bar"></i> Charts', unsafe_allow_html=True)
st.sidebar.markdown('<i class="fas fa-cog"></i> Settings', unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        transition: margin-left 0s;
    }
    </style>
    """,
    unsafe_allow_html=True
)
