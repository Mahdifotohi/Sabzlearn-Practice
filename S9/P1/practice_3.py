import re
from collections import Counter

# خواندن محتوای فایل
with open(r"C:\Users\victus 15\Desktop\Sabzlearn\S9\sample.txt", "r", encoding="utf8") as file:
    content = file.read()

# پیدا کردن تمام کلمات با استفاده از regex
words = re.findall(r'\b\w+\b', content.lower())

# شمارش تعداد هر کلمه
word_count = Counter(words)

# چاپ کلمات و تعداد آنها
for word, count in word_count.items():
    print(f"{word}: {count}")
