# UDP-Socket-Banking-Application
Kinda like payall :) 


To use - Have 2 Ubuntu Terminals Open (or any terminal) <br /> <br />

You will need to create a Python Virtual Environment <br />
Run the following:  <br />

  1. Install the vritualenv package <br />
     'pip install virtualenv' <br />

  2. Create a virtual enviornment (venv) directory <br />
      'python3 -m venv venv' <br />

  3. Activate/Turn On the Virtual Environment <br />
     From the your current directory: <br />
     'source venv/bin/activate' <br />

After Activating Virtual Environment, Install the necessary Libraries
Make sure to install them while being active inside the virtual environment (venv)
or you may break your OS

  1. 'pip install cryptography'

To run the Server/Client, run 1. in the first terminal, run 2. in the second terminal  <br />    

  1. 'python3 ServerBank.py' <br />
  2. 'python3 ClientBank.py' <br />

The result should be the Client talks to the Server, they exchange a secret key via diffie-hellmen, <br />
and the client sends an ecrypted message using AES and HMAC and the server Decrypts the message and verifies the HMAC <br />
