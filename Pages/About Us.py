import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit import container


import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="About Us", page_icon="📌", layout="wide")

# Custom styling
st.markdown(
    """
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #4A90E2;
        }
        .subtitle {
            font-size: 22px;
            text-align: center;
            color: #2E3B4E;
        }
        .content {
            font-size: 18px;
            text-align: justify;
            color: #444;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Title
st.markdown('<p class="title">About Us</p>', unsafe_allow_html=True)

# Subtitle
st.markdown('<p class="subtitle">Who We Are & What We Do</p>', unsafe_allow_html=True)

# About Us Content
st.markdown(
    '<p class="content">We are a passionate team of developers, designers, and innovators dedicated to creating high-quality software solutions. Our mission is to deliver user-friendly, efficient, and scalable applications that empower businesses and individuals alike.</p>',
    unsafe_allow_html=True,
)

st.divider()

# Team Members
st.subheader("Meet Our Team")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://media.istockphoto.com/id/1364917563/photo/businessman-smiling-with-arms-crossed-on-white-background.jpg?s=1024x1024&w=is&k=20&c=O_h1ic7M0SWTC40NVzYUTLWE2Yy8511S8QPUGEUT9tE=", use_container_width=True)
    st.markdown("**Alice Johnson**")
    st.caption("Lead Developer")

with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/06/Gary_Coleman.jpg", use_container_width=True)
    st.markdown("**Bob Smith**")
    st.caption("UI/UX Designer")

with col3:
    st.image("https://media.istockphoto.com/id/526313661/photo/short-male-nerd.jpg?s=1024x1024&w=is&k=20&c=zRqYiqGnx9wUKbKkM7dun04MjWr8TowHZBl6PWqDsJU=", use_container_width=True)
    st.markdown("**Charlie Brown**")
    st.caption("Project Manager")

st.divider()

# Data Visualization with Seaborn
st.subheader("Our Growth Over the Years")


# Footer
st.markdown("---")
st.markdown("<p class='subtitle'>Thank you for visiting our About Us page! 🚀</p>", unsafe_allow_html=True)

# Contact Information
st.markdown("**Contact Us**")
st.markdown("📍 Address: 1234 Innovation Drive, Me Crazy, 54321")
st.markdown("📞 Contact Number: +1 09203912039")
st.markdown("📧 Email: contact@ourcompany.com")

