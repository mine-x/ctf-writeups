# Introduction

As a member of Personalyz.io's Cybersecurity team, I've received an extortion email at the top of your inbox, claiming that sensitive data has been stolen from the company. 
The email demands a ransom and threatens to release the data if the demand is not met within 48 hours.  

The first task is to determine the sender's original IP address using the attached email file.

# Email sender header
[placeholder for image]  
To check the email sender header of this email message, I downloaded and opened the email in Outlook desktop and went to File > Properties to view the Internet headers.  
[placeholder for image]  
There are several "Received" lines, each of which indicates a server that the email passed through. They are listed in reverse chronological order, seeing that the first "Received" line is Personalyz's own mail server.<br /><br />
I identified the sender IP address as: 
```
252.44.98.29
```  
