#! python3

import re, pyperclip, sys

# TODO: Create regex for phone numbers

phoneRegex = re.compile(r'''

# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(((\d{3})|(\(\d{3}\)))?        # area code (optional)
(-|\s)                        # first separator
\d{3}                       # first 3 digits
-                             # separator
\d{4}                       # last 4 digits
(((ext(\.)?\s)|x)             # extension (optional)
(\d{2,5}))?)
''',re.VERBOSE)


# TODO: Create regex for  email addresses
emailRegex = re.compile(r'''

# sample.+_email@something.com

[a-zA-Z0-9.+_]+        # name
@                        # @ symbol
[a-zA-Z0-9.+_]+        # domain name
''',re.VERBOSE)

# TODO: Get text off the clipboard
text = pyperclip.paste()

# TODO: Extract email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phone in extractedPhone:
    allPhoneNumbers.append(phone[0])

# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

print('Scraped Successfully! Paste results to notepad.')
print(sys.argv)
