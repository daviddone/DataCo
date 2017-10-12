###install soft
sudo apt-get install python3-pip -y
pip3 install Django==1.9.7
pip3 install PyMySQL
sudo apt-get install apache2 -y
sudo apt-get install libapache2-mod-wsgi-py3 -y
sudo a2enmod wsgi  #start wsgi
#create project 
python django-admin startproject david_demo  
python manage.py startapp david_app 
### test server
python manage.py runserver 0.0.0:80

### deploy server on apache
# settings.py update
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
# wsgi.py update
#cp wsgi.py_back david_demo/wsgi.py 
#python manage.py collectstatic   #static to dir
#sudo vi /etc/apache2/sites-available/sitename.conf   
#ll /etc/apache2/sites-available/
#cp sitename.conf /etc/apache2/sites-available/sitename.conf
#sudo a2ensite sitename.conf
#sudo service apache2 restart
#sudo service apache2 stop

