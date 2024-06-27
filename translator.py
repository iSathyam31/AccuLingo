import streamlit as st 
import numpy as np

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

## Setting up the API Key configuaration
API_key = os.environ['IBM_API_KEY']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey=API_key)

langtranslator = LanguageTranslatorV3(
    version='2024-05-01',  
    authenticator=authenticator
)

langtranslator.set_service_url(url)

st.title("AccuLingo")

## Drop down list for the languages

option = st.selectbox(
    "Which language would you like to translate",
    ("English", "Hindi", "Japanese", "Korean", "Spanish", "French", "German"))

option1 = st.selectbox(
    "Which language would you like to translate to",
    ("English", "Hindi", "Japanese", "Korean", "Spanish", "French", "German"))

sent = "Enter the text in "+option+" language in the text area provided below"


## Setting up the dictionary of languages to their keywords


language_lib = {'English': 'en', 'Hindi': 'hi',
                'Japanese': 'ja', 'Korean': 'ko', 'Spanish': 'es', 'French': 'fr',
                'German': 'de'} 

sentence = st.text_area(sent, height=250)


if st.button("Translate"):

    try:

        if option == option1:
            st.write("Please Select different Language for Translation")

        else:

            translate_code = language_lib[option]+'-'+language_lib[option1]

            translation = langtranslator.translate(
                text=sentence, model_id=translate_code)

            ans = translation.get_result()['translations'][0]['translation']

            sent1 = 'Translated text in '+option1+' language is shown below'

            st.markdown(sent1)
            st.write(ans)

    except:
        st.write("Please do cross check if text area is filled with sentences or not")
