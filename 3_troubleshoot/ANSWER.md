# Answers for Problem 3

We need to troubleshoot our website at https://www.mastercard.ca/. In any Linux based system, use CLI tools to do the following (send us commands + outputs):

a. Test if port 443 is answering at the IP address of our website.

> `nc -vz -w 5 mastercard.com 443`
> Connection to mastercard.com 443 port [tcp/https] succeeded

b. Check when the SSL certificate expires.

> `echo -n | openssl s_client -servername mastercard.com -connect mastercard.com:443 2>/dev/null | openssl x509 -noout -dates`
> notBefore=Aug 23 13:13:40 2018 GMT
> notAfter=Nov 22 13:43:39 2020 GMT

c. Connect to http://www.mastercard.com/ using telnet and “GET /” (note: not https).

> `telnet mastercard.com 80`
```
Trying 216.119.216.188...
Connected to mastercard.com.
Escape character is '^]'.
GET /
HTTP/1.1 400 Bad Request
Cache-Control: no-cache
Connection: close
Content-Type: text/html
Pragma: no-cache
Content-Length: 188

<html><head><title>Request Rejected</title></head><body>The requested URL was rejected. Please consult with your administrator.<br><br>Your support ID is: 6474552098475199010</body></html>Connection closed by foreign host.
```