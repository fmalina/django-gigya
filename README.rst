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


 - Registration
 - Login
 - Logout
 - Link Accounts
 - 3rd party auth login (Gigya's social login plugin)
 - Missing email


Development
-----------

CSS used in test views are compiled using compass with config.rb in the root folder of the project.