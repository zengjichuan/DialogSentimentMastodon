
# remove non-french dialogs
# remove HTML stuff

# we can detect language for every post in a dialog, and infer the most probable language for the whole dialog: we should thus be very confident about language detection (at least for most common language)

from bs4 import BeautifulSoup

soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)

