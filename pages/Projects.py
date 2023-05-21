import streamlit as st
from PIL import Image   # used to import images from folder to webstie 


from pathlib import Path


# --- PATH SETTINGS ---
# css_file = "/home/tuga/Desktop/ml_projects/Portfolio/style/style.css"
st.set_page_config(page_title="My Portfolio", page_icon=":tada:", layout="wide")



st.title("Projects")


st.markdown("<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}</style>", 
	unsafe_allow_html=True)



# ----  PROJECTS ------
with st.container() :
	# ---- PROJECT 1 ------
	st.write("---")
	st.header("My projects")
	st.write("##")
	image_column, text_column = st.columns((1,2))  # this will create 2 cols. the second col is twice size
	with image_column:
		img_ecog_proj = Image.open('images/ecog.jpeg')
		st.image(img_ecog_proj , width=250)
		
	with text_column:
		st.subheader("Classifying Motor Imagery ECoG Signal With Optimal Selection Of Minimum Electrodes ")
		st.write(
            """
            This work aims to create a classifier for ECoG signals that can achieve high accuracy with a small number of electrodes. 
            We utilized the ECoG datasets from Miller 2019, which were captured in a clinical environment while seven patients performed motor and imaging tasks with their hands and tongues.
            """
            )
		st.markdown("[Watch Video...](https://www.world-wide.org/neuromatch-5.0/classifying-motor-imagery-ecog-signal-bb5dedd9/)")


