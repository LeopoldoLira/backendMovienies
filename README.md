# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/LeopoldoLira/backendMovienies.git
    $ cd backendMovinies
    
Download and Activate the virtualenv for your project from the python modules:

    $ python -m venv /path/to/new/virtual/environment
    $ envname\scripts\activate

Install project dependencies:

    $ pip install -r requirements.txt
    
    
Apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

Remember to set Environment Variables!
