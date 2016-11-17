Django-GIGYA
============

Integrate GIGYA Customer identity and access management into Django projects using Django auth.

* http://www.gigya.com/
* https://docs.djangoproject.com/en/dev/topics/auth/


Installation
------------

Update your settings to add GIGYA_API_KEY variable and
add 'gigya' app to your installed apps.

    ./manage.py migrate

    ./manage.py runserver

Development
-----------

CSS used in test views is compiled using Compass with config.rb in the root folder of the project.