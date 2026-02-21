s="A man, a plan, a canal: Panama"
s_cleaned=''.join(ch for ch in s if ch.isalnum())
s_cleaned=s_cleaned.lower()
print(s_cleaned)