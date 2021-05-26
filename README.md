# Scramblr
A password scrambling algorithm that will take unsanitized user passwords then sanitize them with various alphanumeric and special characters.

# Idea
A developer would take a user's password, scramble it, then save the scrambled phrase in one database, while saving the decoder file to another database. The reason for this is to have a defense against database breaches. Even if the hacker got access to the passwords in your database, and they were able to unhash it, they would receive a phrase that is still not the user's password. Though, if the decoder file is compromised, you are back to the original issue.

# Reason To Use
Security is a feature and like all features, they can enhance or hinder an application's performance for users. While still maintaining your application server's security, you could apply ehanced methodologies to a dedicated decoder database, instead of the application server. Then you could whitelist certain IPs to access the decoder database and numerous other ideas.  

# Decoder File
The decode file is saved as a hidden .pwd file in the root of the project folder. As of now it is hardcoded that way, but future updates will allow you to rename this file via environment variables.

# Notes
You should NEVER store passwords in plain text, and this library should not replace such practice. This is a security feature, not replacement.

If this library is to be used with your application, do NOT store this decoder file in the same database or server. That defeats the purpose.

# CLI
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
python scramblr/cli.py --help
```

# Example
Please run the example.py file.
```bash
git clone https://github.com/ableinc/Scramblr.git
cd scramblr
python3 example.py
```



