import markovify
import streamlit as st
from PIL import Image
image = Image.open('App.jpg')
st.image(image, caption='What would Hafez say?')
# Get raw text as string.
st.title("What would Hafez say?")


@st.cache  # cache the result of the hafez.txt file
def get_data():
    with open("hafez.txt", "r", encoding="utf-8") as f:
        text = f.read()
    return text


data = get_data()


# Build the model.
@st.cache
def build_model():
    get_data()
    model = markovify.Text(data)
    return model


m = build_model()
# ask user how many sentences to generate
st.sidebar.markdown("How many sentences would you like to generate?")
num_sentences = st.sidebar.slider("Sentences", min_value=2, max_value=4)
st.sidebar.markdown("How many characters would you like to generate for each sentence?")
num_words = st.sidebar.slider("Sentences", min_value=200, max_value=500)


# Generate a sentence.
@st.cache
def generate_sentence():
    for i in range(num_sentences):
        sentence = m.make_short_sentence(num_words)
        return sentence


s = generate_sentence()

# show the generated sentence
st.write("##Hafez wants to tell you: ", s)
