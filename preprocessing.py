from nltk.tokenize import word_tokenize
import re


import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('words')

from nltk.corpus import stopwords
stopwords = stopwords.words('arabic')

arabic_diacritics = re.compile("""
                             ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                            ـ    | # Tatwil/Kashida
                         """, re.VERBOSE)

def drop_stop_words(text):
  words = word_tokenize(text)
  wordsFiltered = []
  for w in words:
      if w.lower() not in stopwords:
          wordsFiltered.append(w)

  wordsFiltered = " ".join(wordsFiltered)
  return wordsFiltered


def processing(text, flag = 1):
    text = re.sub(r'@+\w+\s', '', text).strip()                                           # mention
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)                                      # remove URLs
    text = re.sub(r'[^\w\s]', ' ', text)                                                  # remove non word or spaces (punctuation & emojis)
    if flag:
        text = drop_stop_words(text)                                                      # remove arabic stopwords
    text = re.sub(arabic_diacritics, '', text)                                            # remove tanwen
    text = re.sub('user\s', '', text)                                                     # remove user name
    text = re.compile(r"(.)\1{2,}").sub(r"\1", text)                                      # remove elongation
    text = re.sub(r'\w*[0-9]+\w*', '', text)                                              # remove digits

    return text