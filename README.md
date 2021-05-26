# Scramblr
A password scramblr algorithm that will take unsanitized user passwords then sanitize them with various alphanumeric and special characters.

# Idea
A developer would take a user's password, scramble it, then save the scrambled phrase in one database, while saving the decoder file to another database. The reason for this is to have a defense against database breaches. Even if the hacker got access to the passwords in your database, and they were able to unhash it, they would receive a phrase that is still not the user's password. Though, if the decoder file is compromised, you are back to the original issue.

# Reason To Use
Security is a feature and like all features, they can enhance or hinder an application's performance for users. While still maintaining your application server's security, you could apply ehanced methodologies to a dedicated decoder database, instead of the application server. Then you could whitelist certain IPs to access the decoder database and numerous other ideas.  

# Notes
You should NEVER store passwords in plain text, and this library should not replace such practice. This is a security feature, not replacement.

If this library is to be used with your application, do NOT store this decoder file in the same database or server. That defeats the purpose.



