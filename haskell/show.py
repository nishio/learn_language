import re
ESCAPE_SEQUENCE = '\x1B\[...|\x1b[^[]'
data = open('typescript').read()
data = re.sub(ESCAPE_SEQUENCE, '', data)
data = re.search(r'Prelude>.*(?=[*]\w+> [\s]+Leaving GHCi.)', data, re.DOTALL)
print data.group()
