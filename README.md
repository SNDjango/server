<p align="center">
   <img width="180" height="190" src="https://raw.githubusercontent.com/SNDjango/server/devel/snd/image_board/static/img/logo.png" />
   <img width="200" height="190" src="https://raw.githubusercontent.com/SNDjango/server/devel/snd/image_board/static/img/index_design.png" />
</p>

## Synopsis

**SNDjango - TU GAG** is a simple but rich django application featuring a social media platform where users can post content, like posts and comment on posts, subscribe to boards etc. It's perfect for:

* Social Intranets
* Enterprise Social Networks
* Private Social Networks

#### Main Features

- User registration and login
- Upload posts with title, description, hashtags
- Boards: add new boards, subscribe/unsubscribe to boards
- Search funcitonality (for posts, hashtags)
- Like functionality (posts, comments)
- Comment functionality: Comment on posts
- User profile: profile picture, personal & contact information
- Sort functionality for content according to "Hot" & "Top"
- Sort functionality for comments with most likes

## Motivation

The motivation of this project is to provide the option for individuals, groups and companies to incorporate a social intranet where they can have fun and share posts about things related to their workplace/environment. This project is created by a group of students from the module "Programmierpraktikum: Soziale Netzwerke" at the University of Technology in Berlin as a part of their coursework.

## Documentation

The documentation for SNDjango can be found on  https://github.com/SNDjango/server/wiki.


## Installation

### Docker

See all information regarding Installing the SNDjango Docker container  [here](https://github.com/SNDjango/server/wiki/Docker).


### Local Testing


##### 1. Requirements

- Python 3
- Django 1.11

##### 2. Virtualenv

Start with setting up a virtual environment. Follow our [wiki](https://github.com/SNDjango/server/wiki/venv) for more information.


##### 3. Download

Clone the *SNDjango* app to your workspace:

    $ cd /path/to/your/workspace
    $ git clone https://github.com/SNDjango/server.git


##### 4. Install Requirements
In the project root, you will find the *requirements.txt* file. To install type:

    $ pip install -r requirements.txt

##### 5. Migrate


    $ cd snd
    $ python manage.py migrate

##### 6. Run the server

    $ python manage.py runserver

In order to test the application, open a browser at: http://127.0.0.1:8000/

##### 6. Create Admin-user

To get access to the admin pages, create a "superuser" for your application in the database.

    $ python manage.py createsuperuser

You will be prompted to enter username, email and password. You can use these credentials to login when testing the TU GAG application locally. You find the admin pages on  http://127.0.0.1:8000/admin.


## API Reference

See the [Rest API WIKI User Guide](https://github.com/SNDjango/server/wiki/REST-API-User-Guide) for more information.


## License

This project is open-source and is licensed under the MIT License - see [License](https://github.com/SNDjango/server/blob/devel/LICENSE) file for details