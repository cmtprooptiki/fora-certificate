import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
import streamlit_authenticator as stauth
from streamlit.components.v1 import iframe
import time
import pandas as pd



df=pd.read_json('datalist2.json')
st.write(df)



def viewDashboard():

    
    # newhtml="""
    #     <!DOCTYPE html>
    #     <header></header>
    #     <style>
    #        .css-1v3fvcr{background: rgb(34,193,195);
    #         background: radial-gradient(circle, rgba(34,193,195,1) 46%, rgba(229,229,184,1) 100%);
    #         }
    #         div.css-nlntq9.e16nr0p33 p{background-color:white;
    #         }
    #         .css-nlntq9.e16nr0p33{}
    #         .block-container.css-12oz5g7.egzxvld2{background-color:white;
    #             border:5px solid black;
    #             border-radius:15px;
    #             margin-top:67px;
    #         }

    #         .title{}
    #         .css-1cpxqw2.edgvbvh5{background-color:orange;
    #             color: white;
    #         }
        
    #     </style>
    #     <body> 
    #     </body
    # """

    html2="""
        <!DOCTYPE html>
        <header></header>
        <style>
        
        
        </style>
        <body> 
            <ul>
                <li>Πατήστε στο κουμπί "δημιουργία πιστοποιητικού" για να δημιουργήσετε το πιστοποιητικό σας</li>
                <li>Αφού δημιουργήσετε το πιστοποιητικό σας, πατήστε στο κουμπί "παραλαβή πιστοποιητικού" για να κατεβάσετε το πιστοποιητικό σας</li>
            </ul>
        </body
    """
    html3="""
        <!DOCTYPE html>
        <header></header>

        <body> 
        <h3 style="text-align:center;">🎓 Εκτυπώστε το πιστοποιητικό σας</h3>
        </body
    """
    # st.markdown(newhtml,unsafe_allow_html=True)
    st.write('Καλησπέρα, *%s*' % (df['name'][index]))
    # perds=period_counter(names,periods,name)

    # st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
    st.markdown(html3,unsafe_allow_html=True)

    st.markdown(html2,unsafe_allow_html=True)

    left, right = st.columns(2)

    # right.write("Here's the template we'll be using:")

    right.image("http://inclusiveeducation.eu/wp-content/uploads/2022/04/template.png", width=300)

    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
    template = env.get_template("template.html")

    
    # left.write("Fill in the data:")
    form = left.form("template_form")
    student = name
    course="Report Generation in Streamlit"
    grade = 100
    # period=perds
    # submit = st.button("Δημιουργία πιστοποιητικού")
    
    if st.button("Δημιουργία πιστοποιητικού"):
        html = template.render(
            student=student,
            course=course,
            grade=f"{grade}/100",
            date=date.today().strftime("%B %d, %Y"),
        )

        pdf = pdfkit.from_string(html, False)
        st.balloons()

        right.success("🎉 Το πιστοποιητικό σας δημιουργήθηκε!")
        # st.write(html, unsafe_allow_html=True)
        # st.write("")
        right.download_button(
            "⬇️ Παραλαβή πιστοποιητικού",
            data=pdf,
            file_name="diploma.pdf",
            mime="application/octet-stream",
        )




def period_counter(list1,list4,n):
    index = list1.index(n)
    per=list4[index]
    return per

auth=False
newhtml="""
            <!DOCTYPE html>
            <header></header>
            <style>
               .css-1v3fvcr{background: rgb(34,193,195);
                background: radial-gradient(circle, rgba(34,193,195,1) 46%, rgba(229,229,184,1) 100%);
                }
                div.css-nlntq9.e16nr0p33 p{background-color:white;
                }
                .css-nlntq9.e16nr0p33{}
                .block-container.css-12oz5g7.egzxvld2{background-color:white;
                    border:5px solid orange;
                    border-radius:15px;
                    margin-top:67px;
                }
                .css-6awftf.e19lei0e1{ display:none;}

                .title{}
                .css-1cpxqw2.edgvbvh5{background-color:orange;
                    color: white;
                }
                .css-1cpxqw2.edgvbvh5:focus{background-color:white;
                    color: orange;
                    font-weight:bold;
                    border:3px solid orange;

                }
            
            </style>
            <body> 
            </body
        """
st.markdown(newhtml,unsafe_allow_html=True)


# names = ['MARIA	TERZI','Στεριανή Αβράμη','ΔΕΣΠΟΙΝΑ ΑΒΡΑΜΙΔΟΥ','Μαρία Αγάθου']
# usernames = ['Maria-terzi@hotmail.com','stella-a88@hotmail.com','depi1970@hotmail.com','magathou@hotmail.com']
# passwords = ['tSYcA8GPCJ','hj2cJpZLXG','u46UXerHf9','pJH9CA7L2g']

html_logo = "<img style='background-color:black;display:block; margin-left:auto; margin-right:auto; text-align:center;' src='https://healthcare-management.gr/wp-content/uploads/2022/10/MicrosoftTeams-image-16.png'  width=400 height=143>"



st.markdown(html_logo, unsafe_allow_html=True)


names=['ΛΑΜΠΡΙΑΝΑ ΤΣΙΑΚΠΙΝΗ']
usernames=['labrianatsiak@icloud.com']
passwords=['kKw63vspMq']
periods=['11-19 Μαρτίου']

title = st.text_input('Email', 'labrianatsiak@icloud.com')


# hashed_passwords = stauth.hasher(passwords).generate()
# hashed_passwords = stauth.Hasher(passwords).generate()

# authenticator = stauth.Authenticate(names,usernames,hashed_passwords,'some_cookie_name','some_signature_key',cookie_expiry_days=0)


# name, authentication_status = authenticator.login('Login','main')

# name, authentication_status, username = authenticator.login('Login', 'main')

name='ΛΑΜΠΡΙΑΝΑ ΤΣΙΑΚΠΙΝΗ'




if st.button('Login'):
    # Find 'Reema' in name column
    if title in df['email'].values:
        number=df.loc[df.isin([title]).any(axis=1)].index
        index=number.tolist()[0]
        st.write(index)
        st.write("\n  name is exists in DataFrame")
        viewDashboard()
    else:
        st.write('didnt found on database')
        st.write('Why hello there')
# else:
#     st.write('Goodbye')




# elif authentication_status == False:
#     st.error('Username/password is incorrect')
# elif authentication_status == None:
#     st.warning('Please enter your username and password')


# if st.session_state['authentication_status']:
#     st.write('Welcome *%s*' % (st.session_state['name']))
#     st.title('Some content')

# elif st.session_state['authentication_status'] == False:
#     st.error('Username/password is incorrect')
# elif st.session_state['authentication_status'] == None:
#     st.warning('Please enter your username and password')