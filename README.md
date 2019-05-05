# NOTEXBLOCK [![Build Status](https://travis-ci.org/Golub-Sergey/notexblock.svg?branch=master.svg?branch=add_basic_setup)](https://travis-ci.org/Golub-Sergey/notexblock.svg?branch=master)

This is a xblock which allows a student to add notes in time of exam.

## Dependencies

This tool compartible with the main openedx platform dependenies.

##Installation


Only for devxtack version of OpenEdx. For installation xblock on ypur openedx platform
you need make up your platform. At second step, you need to log into the LMS or Studio shell, at
root directory you should make:

    pip install \path\to\you\xblock
    
or, if you install from git:

    pip install git+ssh://git@github.com:<your git account>/<your repository name>.git@branch=add_basic_setup#egg=notexblock

After restart LMS or CMS, depends on where you make installation.

When all steps are done:

* Log in to Studio.
* Open the course.
* From the Settings menu, select Advanced Settings.
* In the Advanced Module List field, place your cursor between the braces, and then type the exact name of the XBlock.
If you see other values in the Advanced Module List field, add a comma after the closing quotation 
mark for the last value, and then type the name of your XBlock.
* At the bottom of the page, select Save Changes.