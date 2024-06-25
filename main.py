import streamlit as st
#from navigation import navigate

#from teacher import teacher_page
# Set custom theme using CSS
st.markdown("""
<style>
:root {
    --backgroundColor: #f5f5f5;
    --textColor: #333;
    --primaryColor: #007acc;
    --secondaryBackgroundColor: #eee;
    --secondaryTextColor: #666;
    --errorColor: #dd2c00;
    --font: 'sans-serif';
}

.stSidebar .stSidebarNav div[role="navigation"] {
    padding: 1rem;
    font-size: 1.2rem;
    color: #007acc;
}
</style>
""", unsafe_allow_html=True)

# Main page
st.title('Automated Grading System')
st.write('Welcome to the Automated Grading System!')

# Options for teachers and students
option = st.selectbox('Select an option', ['Teacher', 'Student'])

if option == 'Teacher':
    st.write('You selected the Teacher option.')
    st.markdown('<a href="/teacher" target="_self"><button>Proceed as Teacher</button></a>', unsafe_allow_html=True)
elif option == 'Student':
    st.write('You selected the Student option.')
    st.markdown('<a href="/student" target="_self"><button>Proceed as Student</button></a>', unsafe_allow_html=True)

# Add navigation menu
#navigate("main")

