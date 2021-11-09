# Social Links

Social links is designed to be an open source version of the [LinkTree](https://linktr.ee/) web application. The goal of the application is to give content creators and buisiness owners the ability to consolidate all of their links behind a single customizealbe WebSite. The main page of the website is used to contain links to Instagram, Facebook, Twitter, Pinterest, Other websites, or whatever the user wants all behind a single easy to remember domain that is unique for each user. Currently LinkTree only offers users to have a linktr.ee/ domain followed by the users username. For the same price a user can purchase a custom domain name and hosting service from websites like [NameCheap](https://www.namecheap.com/) for the same price as LinkTree. Social Links is an easy to deploy, use, and customize regardless of a users technical ability. It contains an admin interface that gives the user the ability to change the text, links, and colors on the main page. 

Note: The Installation and Getting Started steps assume the user has already secured a website domain and hosting provider. 

## Installation
```
git clone git@github.com:cms-WebDesign/LinkTree.git
docker-compose build
```

## Getting Started
```
docker-compose up
docker-compose run django bash
python manage.py createsuperuser --username admin --email admin
```
Once the container is up and the admin account is created head on over to the /admin/ tab and login.

Once logged in the user can customize the links, background, colors, or text on the page to their choosing. 

# License
The MIT License (MIT)

Copyright (c) Christopher H. Schmitt 2021

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
