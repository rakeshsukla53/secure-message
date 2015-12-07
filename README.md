# Secure message transfer 

In this project we have designed a `data pipeline` through which message can be securely transferred to the other party using encryption, decryption and hashing techniques. The pipeline is designed in such a way so as to prevent any kind of attack on confidentiality, authenticity, integrity of data. The end user will get to know if the `message` is changed.

Techniques utilized to prevent attacks:

* Digital Signature
* Encryption (AES CFB)
* Decryption (AES CFB)
* Hashing SHA-3
* Encode 64 

# AES CFB Encryption and Decryption
 
The Cipher Feedback (CFB) mode, a close relative of CBC, makes a block cipher into a self-synchronizing stream cipher. Operation is very similar; in particular, CFB decryption is almost identical to CBC encryption performed in reverse:

    *C_i = E_K (C_{i-1}) \oplus P_i*
    
    *P_i = E_K (C_{i-1}) \oplus C_i*
    
    *C_{0} = \ \mbox{IV}*

![Block Cipher](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Block_cipher.png)

# Project Description

User will enter into the application using `username` and `password`.

![Page 1](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Page%201.png)

![Page 2](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Page%202.png)

If you have any incoming message, then you can see on your left side. But since there no transfer of any message, the below page is completely blank.

![Page 3](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Page%203.png)

By clicking on the `send message` button, you will redirected to the below page. Select to whom the message will be transferred from the drop down list.
 
![Page 4](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Page%204.png)

Type any `message` you want to send. The recipient will only receive the `cipher text` and `hashed of plaintext`. Once you type any `message` hit the `send message` button.

![Page 5](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Page%205.png)

Type two more `messsages` and send!

![Page 6](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Page%206.png)

The `recipent` will know `decrypt` the `ciphertext` and find the plaintext. if the hashed version of the plaintext is mapped to sender's hashed value, then the message will be displayed. Otherwise you will get an error `Message is corrupted`.

Each `user` is associated with a public key and digital signature is assigned to it using `token ID`. The database is completely public so message will also be verified with the `public key` and the `real identity of user`.
 
The `cipher text` is completely encoded using base64. Even though decoding is possible, but still it provides an extra layer of protection.

The `recipent` will know now open his account.

![Page 7](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Page%207.png)

You can see messages displayed on this inbox. Since the messages are securely transferred, and the recipent will able to successfully decrypt the ciphertext, the message will be displayed properly.

![Page 8](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Page%208.png)

# Eve changes the message

Suppose somehow eve changes the content of the message.

![Page 9](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Page%209.png)

The pipeline will be able to know the message is changed, and let the user know about it! See the below image!

![Page 10](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Page%2010.png)

Each user is connected with a `digital signature` so there is no way for any kind of `impersonation attack`. The `digital signature` and `public key` is verified before displaying the message.

Nobody can change the digital signature, and it is unique.

![Page 11](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Page%2011.png)

![Page 12](https://github.com/rakeshsukla53/secure-message/blob/master/static_cdn/staticfiles/img/Page%2012.png)


# Additional Information for TA

This is a web application and technologies used to build this is `Python`, `Django`, `Crypto Modules`, `Django Modules`, `PostgreSQL Database`, `HTML, CSS`. Before running this application, you need to install `postgreSQL` database, and perform the following steps:

* Follow the link to install [PostgreSQL](https://github.com/codingforentrepreneurs/Guides/blob/master/all/install_postgresql_mac_&_linux.md)

* Once the installation is successful then you need to follow the guide [here](https://github.com/codingforentrepreneurs/Guides/blob/master/all/postgresql_and_django.md) to setup settings for `Django` application. The `postgreSQL` database setting should exactly match with `Django` settings.


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'nextdoor',
            'USER': 'rakesh',
            'PASSWORD': 'ranjan',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

* My Dev Environment is Linux Ubuntu 14.04

* Programming Languages - Python 2.7, HTML, CSS, Javascript, Jquery

* Web Framework - Django 1.8.6
 
* For generating digital signature for each user we have used a `UUID` package in Django. Its an inbuild library, so you don't have to worry about it. 

* Packages you need to install is listed down below.

    Django==1.8.6
    django-registration-redux==1.2
    Pillow==3.0.0
    psycopg2==2.6.1
    pycrypto==2.6.1
    wheel==0.24.0

* I have used virtual environment `virtualenv`, and all packages and files are contained in one folder. Unfortunately `postgreSQL` database is not portable, and you need to setup exactly as in my Django setting. Otherwise you won't be able build `tables` and send `messages`. 

# How to run

Step 1:`Git clone https://github.com/rakeshsukla53/secure-message`

Step 2: Go to the `secure-message` folder. 

Step 3: Activate the virtual environment `source bin/activate`. 

Step 4: Navigate to `source` folder.

Step 5: `pip install -r requirements.txt` If you need pip to install all requirements. If you don't have `pip`, then follow this [guide](http://www.liquidweb.com/kb/how-to-install-pip-on-ubuntu-14-04-lts/)

Step 6: If you have installed `postgreSQL` then navigate skip this step.

Step 7: `python manage.py runserver`

Step 8: Go to `localhost:8000/login` to start the app.
 
If you see the below page, then everything is fine! Otherwise shoot a mail [rrs402@nyu.edu]
 

![Front Page](https://github.com/rakeshsukla53/secure-message/blob/master/source/static/img/Front%20Page.png)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 



