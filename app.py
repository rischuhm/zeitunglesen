import json
from requests_html import HTMLSession
s = HTMLSession()

r = s.get(input("Please enter Url: "))

scripts = r.html.find('script')
textfilter = list(filter(lambda script: "type" in script.attrs and script.attrs["type"] == "application/ld+json" and "articleBody" in script.text , scripts))
text = textfilter[0].text

text = json.loads(text)

print(f'\n\033[1m{text["headline"]}\033[0m', end="\n\n")
print(text["articleBody"])