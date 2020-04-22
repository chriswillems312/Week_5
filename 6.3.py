import pandas as pd
df = pd.read_csv('C:/Users/cwill/Dropbox/Master/Python/Basic track/Week 5/book.txt')
words_count = df.count().sum()
print(words_count)

