# Scramblr
A password scrambling algorithm that will take unsanitized user passwords then sanitize them with various alphanumeric and special characters.

# Idea
A developer would take a user's password, scramble it, then save the scrambled phrase in one database, while saving the decoder file to another database. The reason for this is to have a defense against database breaches. Even if the hacker got access to the passwords in your database, and they were able to unhash it, they would receive a phrase that is still not the user's password. Though, if the decoder file is compromised, you are back to the original issue.

# Reason To Use
Security is a feature and like all features, they can enhance or hinder an application's performance for users. While maintaining your application server's security, you could apply enhanced security methodologies to your dedicated decoder database. For example, you could whitelist certain IPs to access the decoder database, limiting traffic. Be sure not to create API endpoints on your application server to return the decoder file, from your decoder database, to your client-side application. That would defeat the purpose of seperating the databases. Be careful to hide or manipulate the HTTP trace header, this could give the user the direct IP address associated with your decoder database.

# Decoder File
The decode file is saved as a hidden .pwd file in the root of the project folder. As of now it is hardcoded that way, but future updates will allow you to rename this file via environment variables.

# Notes
You should NEVER store passwords in plain text, and this library should not replace such practice. This is a security feature, not a secure password storage replacement.

If this library is to be used with your application, do NOT store this decoder file in the same database or server (as mentioned in the Reason to Use section).

# How To Use/How To Install

## CLI
```bash
usage: cli.py [-h] [--scramble SCRAMBLE] [--unscramble UNSCRAMBLE]
              [reverse [reverse ...]] [specialchars [specialchars ...]]

Encryption tool

positional arguments:
  reverse               Use the scramblr in reverse. Unscramble with original
                        phrase, against the scrambled phrase
  specialchars          Whether or not to use special characters

optional arguments:
  -h, --help            show this help message and exit
  --scramble SCRAMBLE   The phrase to be scrambled
  --unscramble UNSCRAMBLE
                        The phrase to be unscrambled
```
Run the CLI locally:
```bash
git clone https://github.com/ableinc/Scramblr.git
cd scramblr
python3 scramblr/cli.py --help
```

## Example
Please run the example.py file.
```bash
git clone https://github.com/ableinc/Scramblr.git
cd scramblr
python3 example.py
```
Output:
```bash
Enter phrase: hello
Original Phrase:  hello
Scrambled:  SQJSB
-------------
Unscrambled:  hello # using SQJSB  (new scrambled phrase)
Unscrambled Reverse:  SQJSB # using hello (original phrase)
```


