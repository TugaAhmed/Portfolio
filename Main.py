import requests
import streamlit as st
from streamlit_lottie import st_lottie  # for inserting GIF image from lottie using json
from PIL import Image   # used to import images from folder to webstie 

from pathlib import Path


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()  # Get the path for current directory 
css_file = current_dir / "style" / "style.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "images" / "tuga.png"


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Portfolio", page_icon=":wave:", layout="wide" )



# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Load CSS file
local_css(css_file)

# --- Load CV pdf file
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


def load_lottieurl(url):
    '''
        Request GIF json file from lotti 
        return GIF json file
    '''
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



with st.container() :
	# ----  Add something (text , image .. ) to the sidebar 
	# st.sidebar()
	pass

with st.container() :
	# ---- General Info About Me 
	NAME = "Tuga Yousif"
	DESCRIPTION = """
	Machine Learning/Deep Learning / Computational Neuroscience Practitioner.
	"""
	EMAIL = "tugakariem@gmail.com"
	LinkedIn = "https://www.linkedin.com/in/tuga-yousif-495a27b7/",
	GitHub = "https://github.com/TugaAhmed",
	



with st.container() :
	# --- Name , Mail , CV and profile picture ---
	col1, col2 = st.columns((1,2), gap="small")
	with col1:
		st.image(str(profile_pic), width=230)

	with col2:
		st.title(NAME)
		st.write(DESCRIPTION)
		st.download_button(
			label=" 📄 Download Resume",
			data=PDFbyte,
			file_name=resume_file.name,
			mime="application/octet-stream",
		)

		with st.container() :
				# --- Social Media --------
			mail_image = Image.open(str(current_dir / "images" / "gmail.png"))
			github_image = Image.open(str(current_dir / "images" / "github.png"))
			linkedin_image = Image.open(str(current_dir / "images" / "linkedin.png"))
			with st.container():
				col1, col2 , col3 , col4 , col5 , col6= st.columns([1, 15 , 1 , 10 , 1 , 10])
				#   --------- Mail -------
				with col1:
					st.image(mail_image, width=20)
				with col2:
					st.write(EMAIL)
				with col3:
					st.image(linkedin_image, width=20)
				with col4:
					st.markdown("[LinkedIn](%s)" % LinkedIn)
				with col5:
					st.image(github_image, width=20)
				with col6:
					st.markdown("[GitHub](%s)" % GitHub)



# with st.container() :  # Used for organising the code
# 	# ---- HEADER SECTION ----
# 	st.title("Hi , I am Tuga :wave: ")
# 	st.subheader("Machine Learning/Deep Learning / Computational Neuroscience Practitioner")

# 	my_intersts = "Interested in applying Machine Learning in Mental Health and in understanding how the brain works "
# 	my_intersts_capitalize_first_letter = ' '.join(elem.capitalize() for elem in my_intersts.split())
# 	st.write(my_intersts_capitalize_first_letter)




with st.container() :
	# ----  EDUCATION SECTION -------
	st.write("---")  # This will add horizantal line as a divider 
	left_col , right_col = st.columns([1,2] ,  gap="small")  # Use this to divide your screen into columns for design purpose 

	with left_col :
		st.subheader("Education")
		st.write("- Al-Neelain University")
		st.write("- Ankara Yıldırım Beyazıt Üniversitesi")

	# with right_col : # add GIF image in the right col 
	# 	lottie_ai_gif = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_rI827y2g0K.json")
	# 	st_lottie(lottie_ai_gif, height=400, width=600, key="coding")



with st.container() :
	# ----  EXPERIENCE ------
	pass

with st.container() :
	# ----  SKILLS ------
	pass






# # ---- CONTACT ----
# with st.container():
#     st.write("---")
#     st.header("Get In Touch With Me!")
#     st.write("##")

#     # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
#     contact_form = """
#     <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
#         <input type="hidden" name="_captcha" value="false">
#         <input type="text" name="name" placeholder="Your name" required>
#         <input type="email" name="email" placeholder="Your email" required>
#         <textarea name="message" placeholder="Your message here" required></textarea>
#         <button type="submit">Send</button>
#     </form>
#     """
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.markdown(contact_form, unsafe_allow_html=True)
#     with right_column:
#         st.empty()























