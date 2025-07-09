# Introduction
As a member of Personalyz.io's Cybersecurity team, I've received an extortion email at the top of my inbox, claiming that sensitive data has been stolen from the company. The email demands a ransom and threatens to release the data if the demand is not met within 48 hours.  

The first task is to determine the sender's original IP address using the attached email file.

# Email sender header
![ransom email](https://github.com/user-attachments/assets/4ac56601-4cea-4b3a-ab42-e592063ac4e2)
To check the email sender header of this email message, I downloaded and opened the email in Outlook desktop (classic) and went to File > Properties to view the Internet headers.  
```
Received:
 from 251.14.1.16 by mx3.personalyz.io; Sun, 23 Mar 2025 10:10:30 +0900
Received: from 250.24.46.164 by klaviyo.com; Sun, 23 Mar 2025 10:10:15 +0900
Received: from 252.44.98.29 by gwagm.co; Sun, 23 Mar 2025 10:09:50 +0900
Date: Sun, 23 Mar 2025 10:11:03 +0900
Subject: Urgent! Are you paying attention? We have your data and can prove it!
From: "Samantha Green" <sgreen123@gwagm.co>
To: security@personalyz.io
Reply-To: "Samantha Green" <sgreen123@gwagm.co>
Message-ID: <1742692263.849341@gwagm.co>
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: quoted-printable
MIME-Version: 1.0
```

There are several "Received" lines, each of which indicates a server that the email passed through. They are listed in reverse chronological order, seeing that the first "Received" line is Personalyz's own mail server.

The last "Received" line shows the sender IP address as: 
```
252.44.98.29
```  
