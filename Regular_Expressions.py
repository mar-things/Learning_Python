import numpy
import re                       # This is the regular expression library (Is used to iterate over files to extract specific characters):

pattern = r"Cookie"
text = r"Cookie"

if re.match(pattern, text):
    print("ok")
else:
    print('not')

if pattern == text:
    print("ok")
else:
    print('not')


#. - Matches any single character
print(re.search(r"Co.kie","Cookie").group())
print(re.search(r".o.kie","Kookie").group())

# ^ - Matches in the bigining of text line
print(re.search(r"Eat","^Eat eastern egg"))

# $ - Matches at the end of the text line
print(re.search(r"cake$","It was nice cake").group())

# [abc] - Matches a or b or c 
#[a-z A-Z 0-9] - Matches characters from a to z, from A to Z, and digits from 0 to 9

print(re.search(r"[0-6]","The user gave an input of : 5 ").group())
print(re.search(r"[^5]","Number:0").group())

# \w - matches any single letter, digit or underscore
# \W - matches any other letter that \w dont match 
print("Lowercase w: ", re.search(r'Co\wkie','Cookie').group())
print("Uppercase W: ", re.search(r'C\Wke','C@ke').group())

# \s - matches single whitespace character: space, newline, tab, return
# \S - matches any other characters
print("Lowercase s: ", re.search(r"Eat\scake", 'Eat cake').group())
print('Uppercase s: ', re.search(r"cook\Se","Let's eat cookie").group())

# \d - matches a digit 0-9
# \D - matches any other
print("How many sousainiu do you want to eat?",re.search(r'\d+','55 sousainiu').group())

# \t - matches tab 
# \n - newline
# \r - matches return
# \A - works like ^ it matches somthin in the beginning of string
# \Z - works like$ it matches in the end of string

# + - cheks if the preceding character appears one or more times starting from that position
print(re.search(r'Co+kie','Coooooooooooookie').group())

# * - cheks if the preceding character appears zero or more times 
print(re.search(r'Ca*o*kie','Coooooooookie').group())

#? - charactre appear zero or one time starting from that position
print(re.search(r'Colou?r', 'Color').group())

# {x} - repeat exactly x iterations
# {x,} - at least x times and more
# {x,y} - at least x times but not more than y 
print(re.search(r'\d{9}','numbers 123456789').group())
print(re.search(r'\d{4,8}.\d{1,3}','DataA: 123456.90').group())

#()  - groups regular expression symbols to work as one script

text = 'Please contact us at support.support@datacamp.com'
result = re.search(r'([\w\.-]+)@([\w\.-]+)',text)

print(result)q

print('Email address: ',result.group())
print('User name: ',result.group(1))
print('Hostname: ',result.group(2))

result2 = re.search(r'(?P<email>(?P<username>[\w\.-]+)@(?P<host>[\w\.-]+))',text)
print('Email: ',result2.group('email'))
print('User name:'result2.group('username'))

#findall( searches in all text

text2 = "Please contact us at: info@gmail.com, something@ktu.lt, sun@sun.edu"
addresses = re.findall(r'([\w\.-]+@[\w\.-]+)',text2)