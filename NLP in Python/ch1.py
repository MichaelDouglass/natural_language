"""
Prior to running, ensure that each component
is downloaded using the nltk.download() UI
"""
from nltk.book import *

# Look for "monstrous" in Moby Dick
text1.concordance("monstrous")

# Locate the lexicon in the books location of the three words
text4.dispersion_plot(["citizens", "democracy", "freedom"])
