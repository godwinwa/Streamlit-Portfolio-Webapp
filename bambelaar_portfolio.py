import streamlit as st
from PIL import Image
import smtplib as s




#Page settings
st.set_page_config(  # Alternate names: setup_page, page, layout
	layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
	page_title=None,  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
)

# Sidebar
add_selectbox = st.sidebar.selectbox(
    'What are you interested in?',
    ('Art', 'Books', 'Products', 'Flyers')
)
def sidebar():
    
    st.sidebar.title('Want to know more?'
    )

    st.sidebar.text('Get in touch with the Bambelaar.'
    )
    password = 'emaildoor1'
    email_sender = st.sidebar.text_input('Your email:')
    email_receiver = 'bambelaarmail@gmail.com'
    subject = st.sidebar.text_input('Topic:')
    body = st.sidebar.text_area('Type your message')
    message = "Subject:{}\n\n{} \n\n From:{}".format(subject, body, email_sender)
    if st.sidebar.button('Send email'):
        try:
            connection = s.SMTP('smtp.gmail.com', 587)
            connection.starttls()
            connection.login(email_receiver, password)
            connection.sendmail(email_receiver, 'chakaobi@gmail.com', message)
            connection.quit()
            st.sidebar.success('Email send succesfully')
        except Exception as e:
            if email_sender == '':
                st.sidebar.error('Please fill user email field')
                
            elif message == '':
                st.sidebar.error('Please type a message')
            
    #Expander
    with st.sidebar.expander("About"):
         st.write("""
            This is the story of a young Nigerian Bambelaar from Lagos city. Follow him on his journey to becoming the ultimate Bambelaar.
            ©G6 
         """)
    return None

sidebar()

#Header
st.markdown("<h1 style='text-align: center; color: white;'>A Bambelaars Creations</h1>", unsafe_allow_html=True)

#Page layout
col1, col2, col3 = st.columns(3)

#Get image
@st.cache
def get_image(image_number):
    image = Image.open('./images/IMG_{}.JPG'.format(image_number))
    return image


#Checkbox to show images
if st.checkbox('Click to experience'):
    if add_selectbox == 'Art':
        with col1:
            st.image(get_image(4769), caption='©Chass creation',width=300)
            st.image(get_image(4772), caption='©Chass creation',width=300)
            st.image(get_image(4776), caption='©Chass creation',width=300)
        with col2:
            st.image(get_image(4773), caption='©Chass creation',width=300)
            st.image(get_image(4777), caption='©Chass creation',width=300)
            
        with col3:
            st.image(get_image(4774), caption='©Chass creation',width=300)
            st.image(get_image(4775), caption='©Chass creation',width=300)
            st.image(get_image(4779), caption='©Chass creation',width=300)
    elif add_selectbox == 'Books':
        with col1:
            
            st.image(get_image(4750), caption='©Chass creation',width=300)
        with col2:
            st.image(get_image(4751), caption='©Chass creation',width=300)
            
        with col3:
            st.image(get_image(4747), caption='©Chass creation',width=300)
            
    elif add_selectbox == 'Products':
        with col1:
            st.image(get_image(4759), caption='©Chass creation',width=300)
            st.image(get_image(4761), caption='©Chass creation',width=300)
            st.image(get_image(4778), caption='©Chass creation',width=300)
        with col2:
            st.image(get_image(4763), caption='©Chass creation',width=300)
            st.image(get_image(4766), caption='©Chass creation',width=300)
            st.image(get_image(4780), caption='©Chass creation',width=300)
        with col3:
            st.image(get_image(4767), caption='©Chass creation',width=300)
            st.image(get_image(4768), caption='©Chass creation',width=300)
    elif add_selectbox == 'Flyers':
        with col1:
            st.image(get_image(4752), caption='©Chass creation',width=300)
            st.image(get_image(4753), caption='©Chass creation',width=300)
        with col2:
            st.image(get_image(4754), caption='©Chass creation',width=300)
            
        with col3:
            st.image(get_image(4756), caption='©Chass creation',width=300)
            st.image(get_image(4756), caption='©Chass creation',width=300)


#Hide streamlit logo and settings menu
hide_st_style = """
            <style>
            
            footer {visibility: hidden;}
            
            </style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)


