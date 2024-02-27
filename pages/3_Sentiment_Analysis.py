# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import pipeline
from nltk.corpus import brown


def sent_analysis(text):
    @st.cache_data
    def read_model():
        MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
        tokenizer1 = AutoTokenizer.from_pretrained(MODEL)
        model1 = AutoModelForSequenceClassification.from_pretrained(MODEL)
        try:          
            sent_pipeline1 = pipeline("sentiment-analysis")
        except:
            sent_pipeline1 = ""
            pass
        return tokenizer1,model1,sent_pipeline1

    try:
        sia = SentimentIntensityAnalyzer()
        out_SA = sia.polarity_scores(text)
        st.title("SentimentIntensityAnalyzer NLTK")
        st.write(out_SA)
    except Exception as ex:
        st.write(ex)
        pass
    
    try:
        tokenizer,model,sent_pipeline = read_model()
        
        encoded_text = tokenizer(text, return_tensors='pt')
        output = model(**encoded_text)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        scores_dict = {
            'roberta_neg' : scores[0],
            'roberta_neu' : scores[1],
            'roberta_pos' : scores[2]
        }
        st.title("twitter-roberta-base-sentiment")
        st.write(scores_dict)
    except Exception as ex:
        st.write(ex)
        pass
    try:
        st.title("Pre-trained sentiment-analysis Pipeline")
        st.write(sent_pipeline("Everyone try to loves you which is bad"))
    except Exception as ex:
        st.write(ex)
        pass
    
nltk.download()
nltk.download('maxent_ne_chunker')
nltk.download('vader_lexicon')   
    
st.set_page_config(page_title="Sentiment Analysis", page_icon="📊")
st.markdown("# Enter the sentence to identify the sentiments")
st.write(
    """Kindly Input your Sentence Text in Textbox. """
)

textinp = st.text_input('Please enter the Sentence Text & Click Analysis', 'I am a good Developer')


if st.button("Sentiment Analysis"):
    sent_analysis(textinp)
