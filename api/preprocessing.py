# ------------------------------------- #
# чистка умений:                        #
#   1. разделяем на токены              #
#   2. пунктуация                       #
#   3. стоп-слова                       #
#   4. приводим все в нижний регистр    #
#   5. стеминг                          #
# ------------------------------------- #

from nltk.tokenize import sent_tokenize #(1)
from nltk.corpus import stopwords #(3)
from nltk.stem.snowball import SnowballStemmer #(5)

