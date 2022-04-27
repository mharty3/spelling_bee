import streamlit as st
import word_finder

st.title('NYT Spelling Bee Cheater')

"""[Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee) is a fun word puzzle from the New York Times. Every day, they release a new puzzle with seven letters. The challenge is to come up with as many words as you can that are spelled using only those letters. There is also a “center letter” which must be included in each word.

You get more points for longer words, and pangrams, words that use all seven letters at least once, are worth a bonus.

Use this app to win.

"""

letters = st.text_input("What are today's letters?")

if letters:
    key_letter = st.selectbox('Which is the middle letter? This is the one that must be included in all words.', letters.upper())

    letters = key_letter.lower() + letters.lower() # key letter must be the first in the string

if letters:
    good_words = word_finder.word_finder(letters)
    pangrams = word_finder.find_pangrams(good_words)
    data = dict(pangrams=pangrams, all_words=good_words)

    pangram_expander = st.expander("Pangrams")
    with pangram_expander:

        for w in data['pangrams']:
            st.write(w.upper())

    other_word_expander = st.expander("All Words")
    with other_word_expander:

        for w in data['all_words']:
            st.write(w.upper())


"""This app was built using Streamlit and hosted using Streamlit Sharing. 

You can find the code on [GitHub](https://github.com/mharty3/spelling_bee). Read about how I made it here: [Part 1](https://mharty3.github.io/blog/spelling-bee/) and [Part 2](https://mharty3.github.io/blog/spelling-bee-part-2/)"""
