# Not-so-simple mail protocol

Points: 100

## Objective

Search through SMTP logs in an OpenSearch dashboard to find the first extortion email from this incident.

## Log analysis

I started by searching for the originating IP address `252.44.98.29` and only found 1 result, the same ransom email message that was provided in the previous challenge.

```log
From: "Samantha Green" <sgreen123@gwagm.co>
Rcptto: security@personalyz.io
User_Agent: XyzMailer
Path: 252.44.98.29, 250.24.46.164, 251.14.1.16, 245.31.211.54
Helo: gwagm.co 
Msg_id: <1742692263.849341@gwagm.co>
```

I tried looking for logs containing a similar email subject, but this turned up too many false positives. I also searched based on the email domain `gwagm.co` and user agent `XyzMailer` and did not find anything useful.  

I went back to the known ransom email and took a closer look at the other attributes and noticed that "Path" shows an intermediary mail server with an IP address of `250.24.46.164`.
Searching for this IP did turn up results - both the provided ransom email and another email that was sent out one day prior.

![opensearch_result](<opensearch.png>)

The "Subject" indicates this email is indeed part of this incident.

**Flag:** ```tharris456@tgwnaagm.co```
