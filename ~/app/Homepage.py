from PIL import Image
import streamlit as st

# setting image
image = Image.open('image.png')


col1, col2 = st.columns(2)

col1.header("DataFest 2024 Hackathon")
col1.write("Challenges Faced by Students in WAEC and JAMB Exams in Africa")
col1.write("WAEC (West African Examinations Council) and JAMB (Joint Admissions and Matriculation Board) are critical examinations for students in West Africa, particularly Nigeria, as they determine access to secondary and tertiary education. Despite their importance, students face several challenges when preparing for and taking these exams, ranging from socioeconomic barriers to educational gaps.")

title_1 =  '<p style="font-family:sans-serif; color:Grey;">This data hackathon aims to explore these challenges using data-driven insights, providing solutions and recommendations to improve the exam processes and outcomes for students.</p>'
col1.markdown(title_1, unsafe_allow_html=True)
#title_2 =  '<p style="font-family:sans-serif; color:Grey;">in a simple and elegant way.</p>'
#col1.markdown(title_2, unsafe_allow_html=True)
col2.image(image)
col2.write("Team Members")
col2.write("Balogun Anuoluwapo")
col2.write("Babatunde Abdullateef")
col2.write("Oluwafemi Abiona")
# Markdown to add a clickable link to your GitHub repository
col2.markdown('Check out the project on [GitHub](https://github.com/analyticsengineer/Datafest_Datathon)')

# Setting menu visibility
st.markdown(""" <style>
#Mainmenu {visibility: hidden;}
footer {visibility: hidden;}
</style>""", unsafe_allow_html=True)
