import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]

# genai.configure(api_key="AIzaSyBvNGzZOziNPBLqoMRLHjdyYb7IZLlgPp0")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hello :wave: ")
    st.title("I am Tony Lee")
with col2:
    st.image("Images/My_Portrait.png")

st.title(" ")

persona = """
        You are Tony AI bot. You help people answer questions about your self (i.e Tony)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Tony: 
         
        Tony Lee is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Tony obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
        Bristol University (UK). He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Tony worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.
 
        Tony's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        Tony's Email: contact@murtazahassan.com 
        Tony's Facebook: https://www.facebook.com/murtazasworkshop
        Tony's Instagram: https://www.instagram.com/murtazasworkshop/
        Tony's Linkdin: https://www.linkedin.com/in/murtaza-hassan-8045b38a/
        Tony's Github :https://github.com/murtazahassan
        """

st.title("Tony's AI BOT")

user_question = st.text_input("Ask anything about me")

if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Largest Computer Vision Channel")
    st.write("- 400k Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 15 Million + Views")
    st.write("- 1.5 Million Hours + Watch time")
with col2:
    st.video("https://www.youtube.com/watch?v=uhxDJGZz594")

st.title(" ")
st.title("My Setup")
st.image("Images/gallery5.jpg")

st.markdown(
    """
    <style>
    .stSlider > div > div > div > div {
        background-color: #00FFFF !important;  /* Change slider thumb color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 79)
st.slider("Teaching", 0, 100, 85)
st.slider("Robotics", 0, 100, 75)

st.file_uploader("Upload a file")

st.write(" ")
st.title("Gallery")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("Images/g1.png")
    st.image("Images/g2.png")
    st.image("Images/g3.png")
with col2:
    st.image("Images/g4.png")
    st.image("Images/g5.png")
    st.image("Images/g6.png")
with col3:
    st.image("Images/g7.png")
    st.image("Images/g8.png")
    st.image("Images/g9.png")

st.write(" ")
st.write("CONTACT")
st.title("For any inquiries, email at: ")
st.subheader("lythanhdat21@gmail.com")

# streamlit run portfolio_website.py



