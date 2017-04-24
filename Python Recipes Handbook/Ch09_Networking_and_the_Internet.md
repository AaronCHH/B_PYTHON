
# Chapter 9: Networking and the Internet
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 9: Networking and the Internet](#chapter-9-networking-and-the-internet)
  * [9-1. Opening a Socket Connection](#9-1-opening-a-socket-connection)
  * [9-2. Reading/Writing Over a Socket](#9-2-readingwriting-over-a-socket)
  * [9-3. Reading an E-Mail with POP](#9-3-reading-an-e-mail-with-pop)
  * [9-4. Reading an E-Mail with IMAP](#9-4-reading-an-e-mail-with-imap)
  * [9-5. Sending an E-Mail](#9-5-sending-an-e-mail)
  * [9-6. Reading a Web Page](#9-6-reading-a-web-page)
  * [9-7. Posting to a Web Page](#9-7-posting-to-a-web-page)
  * [9-8. Acting as a Server](#9-8-acting-as-a-server)

<!-- tocstop -->


## 9-1. Opening a Socket Connection
* Problem
* Solution
* How It Works


```python
import socket
host = '192.168.0.1'
port = 5050
```


```python
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((host, port))
```


```python
import socket
host = '192.168.0.1'
port = 5050
my_sock = socket.create_connection((host, port))
```


```python
my_sock.close()
```

## 9-2. Reading/Writing Over a Socket
* Problem
* Solution
* How It Works


```python
msg = b'Hello World'
mesglen = len(msg)
totalsent = 0
```


```python
while totalsent < msglen:
    sent = my_sock.send(msg[totalsent:])
    totalsent = totalsent + sent
```


```python
my_sock.sendall(b'Hello World')
```


```python
data_in = my_sock.recv(1024)
```


```python
buffer = bytearray(b' ' * 1024)
my_sock.recv_into(buffer)
```

## 9-3. Reading an E-Mail with POP
* Problem
* Solution
* How It Works


```python
import getpass, poplib
pop_serv = poplib.POP3('192.168.0.1')
pop_serv.user(getpass.getuser())
pop_serv.pass_(getpass.getpass())
```


```python
msg_count, box_size = pop_serv.stat()
```


```python
msg_list = pop_serv.list()
```


```python
message = pop_serv.retr(1)
```


```python
pop_serv.quit()
```

## 9-4. Reading an E-Mail with IMAP
* Problem
* Solution
* How It Works


```python
import imaplib, getpass
my_imap = imaplib.IMAP4('myimap.com')
my_imap.login(getpass.getuser(), getpass.getpass())
```


```python
my_imap.select()
typ, data = my_imap.search(None, 'ALL')
```


```python
email_msg = my_imap.fetch(email_id, '(RFC822)')
```


```python
my_imap.store(email_id, '+FLAGS', '\\Deleted')
my_imap.expunge()
```


```python
my_imap.close()
my_imap.logout()
```

## 9-5. Sending an E-Mail
* Problem
* Solution
* How It Works


```python
import smtplib, getpass
my_smtp = smtplib.SMTP('my.smtp.com')
my_smtp.login(getpass.getuser(), getpass.getpass())
```


```python
from_addr = 'me@email.com'
to_addr = 'you@email.com'
msg = 'From: me@email.com\r\nTo: you@email.com\r\n\r\nHello World'
my_smtp.sendmail(from_addr, to_addr, msg)
```

## 9-6. Reading a Web Page
* Problem
* Solution
* How It Works


```python
import urllib.request
my_web = urllib.request.urlopen('http://www.python.org')
```


```python
print(my_web.read(100))
```

## 9-7. Posting to a Web Page
* Problem
* Solution
* How It Works


```python
import urllib.request
mydata = b'some form data'
my_req = urllib.request.Request('http://form.host.com', data=mydata, method='POST')
```


```python
my_form = urllib.request.urlopen(my_req)
print(my_form.status)
print(my_form.reason)
```

## 9-8. Acting as a Server
* Problem
* Solution
* How It Works


```python
import socket
host = ''
port = 4242
my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_server.bind((host, port))
my_server.listen(1)
```


```python
conn, addr = my_server.accept()
print('Connected from host ', addr)
data = conn.recv(1024)
```
