================================================
Django-Jinja2-Bootstrap project skeleton
================================================

Reason
======

Every project needs to start with something. This project is meant to provide the the boilerplate needed to set up Django project using Jinja2 as template markup and Bootstrap as CSS framework, ready for development without necessity of going through integration of Jinja in Django.

Usage
=====

Just start project with this repo as template (available since Django 1.4.):

``django-admin.py startproject yourprojectname --template https://github.com/marekbrzoska/djb-skeleton/archive/master.zip``

Then install the project dependencies:

``make install``


Once you you you are comfortable with project setup you will want to delete example: just remove ``apps/pilot/`` directory and pilot urls from project/urls.py file.

Jinja2 Usage
============

In you ``views.py``::

  from project.utils.djangojinja2 import render_to_response

  def your_view(request):
    return render_to_response('pilot/template.html', {'template_variable': 1}, request)

And put your jinja template in ``templates/jinja/pilot/template.html``.


You still can use normal django templates the usual way. Just put them in ``apps/app_directory/templates/`` or in ``templates/django/``.
    
See pilot application for example.
