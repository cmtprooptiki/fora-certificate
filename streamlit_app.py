import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
import streamlit_authenticator as stauth
from streamlit.components.v1 import iframe
import time
import pandas as pd
from pymongo import MongoClient
import os



def main():
    newhtml="""
            <!DOCTYPE html>
            <header></header>
            <style>
            
           

                .css-1v3fvcr{
                background: rgb(34,193,195);
                background: radial-gradient(circle, rgba(34,193,195,1) 46%, rgba(229,229,184,1) 100%);
                }

                .css-k1vhr4 {
                    <!--background-image: url('https://healthcare-management.gr/wp-content/uploads/2022/10/Untitled-design-10.gif');-->
                    display: flex;
                    flex-direction: column;
                    width: 100%;
                    overflow: auto;
                    -webkit-box-align: center;
                    align-items: center;
                }



                div.css-nlntq9.e16nr0p33 p{background-color:white;
                }

                .css-nlntq9.e16nr0p33{}
                
                .block-container.css-12oz5g7.egzxvld2{
                    background-color:white;   
                    
                    border:5px solid white;
                    border-radius:15px;
                    margin-top:67px;
                }

                .css-6awftf.e19lei0e1{ display:none;}

                .title{}
                
                .css-1cpxqw2.edgvbvh5{
                    background-color:orange;
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
    html_logo ="<img style='display:block; margin-left:auto; margin-right:auto; text-align:center;' src='https://gbvcyclades.epapsy.gr/wp-content/uploads/2022/05/logoandtext.png'  width=200 >"
    st.markdown(html_logo, unsafe_allow_html=True)


    title = st.text_input('Email', '')
    submit_button = st.button("Είσοδος")

    try:




        client = MongoClient(st.secrets["path"])
        client.server_info() # force connection on a request as the
                            # connect=True parameter of MongoClient seems
                            # to be useless here 
        mydb = client["iamdb"]

        mycol = mydb["usergbv"]   
        item_details= mycol.find()
        list_cur=[]
        for item in item_details:
        # This does not give a very readable output
            list_cur.append(item)
    except MongoClient.errors.ServerSelectionTimeoutError as err:
        # do whatever you need 
        st.write(err)   
    if submit_button is True:
        df=pd.DataFrame.from_dict(list_cur)

        if title in df['email'].values:
        
            number=df.loc[df.isin([title]).any(axis=1)].index
            index=number.tolist()[0]
            # st.write(index)
            # st.write("\n  name is exists in DataFrame")

            # st.markdown(newhtml,unsafe_allow_html=True)
            st.write('Καλησπέρα, *%s*' % (df['name'][index]))
            # perds=period_counter(names,periods,name)

            # st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")


            left, right = st.columns(2)

            # right.write("Here's the template we'll be using:")

            right.image("https://cmtprooptiki.gr/api/thumbnail.gif", width=300)

            env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
            template = env.get_template("template.html")


            # left.write("Fill in the data:")
            form = left.form("template_form")
            student = df['name'][index]
            course="Report Generation in Streamlit"
            grade = 100
            # period=perds
            # submit = form.form_submit_button("Δημιουργία πιστοποιητικού")

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
                "⬇️ Παραλαβή βεβαίωσης παρακολούθησης",
                data=pdf,
                file_name="diploma.pdf",
                mime="application/octet-stream",
            )
        else:
            if (title!=''):
                st.write("Το email που δώσατε δεν υπάρχει στην λίστα παρακολούθησης του συνέδριου.")
            if (title==''):
                st.write("Παρακαλώ πληκτρολογήστε το email που δωσάστε κατα την εγγραφή σας στο συνέδριο")
        







# df=pd.read_json('datalist2.json')
# st.write(df)


# html_logo ="<img style='background-color:black;display:block; margin-left:auto; margin-right:auto; text-align:center;' src='https://healthcare-management.gr/wp-content/uploads/2022/10/MicrosoftTeams-image-16.png'  width=400 height=143>"


# st.markdown(html_logo, unsafe_allow_html=True)


# title = st.text_input('Email', '')




    

# # name='ΛΑΜΠΡΙΑΝΑ ΤΣΙΑΚΠΙΝΗ'


#     # # Find 'Reema' in name column
#     # if title in df['email'].values:
#     #     number=df.loc[df.isin([title]).any(axis=1)].index
#     #     index=number.tolist()[0]
#     #     st.write(index)
#     #     st.write("\n  name is exists in DataFrame")

# if title in df['email'].values:
        
#         number=df.loc[df.isin([title]).any(axis=1)].index
#         index=number.tolist()[0]
#         st.write(index)
#         st.write("\n  name is exists in DataFrame")

#         # st.markdown(newhtml,unsafe_allow_html=True)
#         st.write('Καλησπέρα, *%s*' % (df['name'][index]))
#         # perds=period_counter(names,periods,name)

#         # st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")


#         left, right = st.columns(2)

#         # right.write("Here's the template we'll be using:")

#         right.image("http://healthcare-management.gr/wp-content/uploads/2022/10/certificate.jpg", width=300)

#         env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
#         template = env.get_template("template.html")


#         # left.write("Fill in the data:")
#         form = left.form("template_form")
#         student = df['name'][index]
#         course="Report Generation in Streamlit"
#         grade = 100
#         # period=perds
#         submit = form.form_submit_button("Δημιουργία πιστοποιητικού")

#         if submit:
#             html = template.render(
#                 student=student,
#                 course=course,
#                 grade=f"{grade}/100",
#                 date=date.today().strftime("%B %d, %Y"),
#             )

#             pdf = pdfkit.from_string(html, False)
#             st.balloons()

#             right.success("🎉 Το πιστοποιητικό σας δημιουργήθηκε!")
#             # st.write(html, unsafe_allow_html=True)
#             # st.write("")
#             right.download_button(
#                 "⬇️ Παραλαβή πιστοποιητικού",
#                 data=pdf,
#                 file_name="diploma.pdf",
#                 mime="application/octet-stream",
#             )
            


# else:
#     if (title!=''):
#         st.write("Not exist in db")
#     if (title==''):
#         st.write("Please type email on the field")


    
   


if __name__ == "__main__":
    main()