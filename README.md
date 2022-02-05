# searchable-encryption
symmetric searchable encryption

This repository is a python implementation of song et al’s "Practical Techniques for Searches on Encrypted Data". http://www.cs.berkeley.edu/~dawnsong/papers/se.pdf

This encryption technique can securely protect contents of a document yet allows keyword search to be carried without the secret key.  


**Pre-requisites :**  
To see which version of Python 3 you have installed, open a command prompt and run  
python3 --version  
If you are using Ubuntu 16.10 or newer, then you can easily install Python 3.6 with the following commands:  

    sudo apt-get update  
    sudo apt-get install python3.6  
The two most crucial third-party Python packages are setuptools and pip.  
Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default.  
To see if pip is installed, open a command prompt and run  

    command -v pip3

**External Packages :**  
PyCryptodome can be installed with 

    pip3 install pycryptodome  
  
All modules are installed under the Crypto package. You can test everything is right with:

    python3 -m Crypto.SelfTest
  
  
  
**Description :**  
Initially, we store a few keywords (one word per line) which we want to encrypt, in the file key.txt. Next, we run the searchable_encryption_client.py , which is the client side code for encrypting the keywords given in the input file, ‘key.txt’.

    python3 searchable_encryption_client.py

This will automatically produce an output file with the name ‘trapdoor.txt’ in the same folder, but which contains the same keywords in encrypted form.  
We can now upload this file on to the cloud server.  
In order to search on the encrypted content of the file trapdoor_key.txt (whether or not a particular keyword exists in encrypted form), we run the searchable_encryption_cloud.py , which is the server side code for searching the keywords.  


    python3 searchable_encryption_cloud.py
Input : 
i) name of the trapdoor file on which search is to be done  
ii) test keyword  
Output : 
true, if the keyword is present in the trapdoor file  
false, otherwise
