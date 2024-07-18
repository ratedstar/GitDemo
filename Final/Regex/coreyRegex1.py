import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

cat
mat
pat
bat
emails = 
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

Ha HaHa

MetaCharacters (Need to be escaped):. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

urls =
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

'''
#Raw string: python handles \ in a special way when we use raw string it handles in a better way
print('\ttab')
print(r"\ttab")

# pattern = re.compile(r'abc')
# matches = pattern.finditer(text_to_search)
# pattern = re.compile(r'.')
# matches = pattern.finditer(text_to_search)

# pattern= re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
# only .- numbers
# pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
# # with open('data.txt','r') as f:
# #     contents = f.read()
# matches = pattern.finditer(contents)
# for match in matches:
#     print(match)
#only 800 or 900 series numbers
#pattern = re.compile((r'[89]00[.-]\d\d\d[.-]\d\d\d\d'))
#pattern = re.compile(r'[1-5]')
#pattern = re.compile(r'[a-zA-Z]')
#pattern = re.compile(r'[^a-zA-Z]')
#pattern = re.compile(r'[^b]at')
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#pattern = re.compile(r'Mr\.?\s[a-zA-Z]\w*')
#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*')
#pattern = re.compile(r'[a-zA-Z]+@[a-zA-z]+\.com')
#pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
#pattern = re.compile(r'https?://(www\.)?(\w+)\.(\w+)')

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

patternURL = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = patternURL.sub(r'\2\3',text_to_search)
print(subbed_urls)
#matchU = patternURL.finditer(text_to_search)

# for matchr in matchU:
#     print(matchr.group(3))
