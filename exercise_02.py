# Find the most frequent character in the paragraph

from collections import Counter

rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'
without_space = rhyme.replace(' ', '')
print(without_space)
res = Counter(without_space)
max_frequent_ch = max(res, key = res.get)
print(f"most frequent character : {max_frequent_ch}")
