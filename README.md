# wordcount-project
### My tutorial - Djnago
This is my tutorial page for learning Django.<BR>
Important command line codes are:<ul><li>
Install Django-2: fro https://www.djangoproject.com/</li><li>
pip install django (I installed with: conda install -c anaconda django)</li><li>
pip install djangorestframework (if you want to install Django REST-Framework)</li><li>
django-admin</li><li>
django-admin startproject projectname</li><li>
cd project directory</li><li>
python manage.py runserver</li><li>
Make a directory: "templates" in root project (highest) directory.</li><li>
Go to settings.py in project-directory, and add 'templates' in line: 'DIRS': ['..'] in TEMPLATES section</li><li>
Go to urls.py in project-directory, and add or edit path as required</li><li>
Go to views.py in project-directory, and add or edit new methods (def)</li><li>

For REST-API: <UL><LI>django-admin startapp AppName</li><li>
  python manage.py makemigrations</li><li>
  python manage.py migrate</li><li>
  In settings.py, add 'rest_framework' and 'ApiName' in INSTALLED_APPS section</li>
  </UL>


</li></ul>
