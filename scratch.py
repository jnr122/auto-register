import re

words = 'hey my dd<name> is josh'

re.sub('<.*?>', '', words)
print(words)