# Lengow

## Requierements

```bash
sudo apt-get install python3-pip
pip3 install django
pip3 install djangorestframework
pip3 install markdown
pip3 install django-filter 
```

## Deploy

```bash
git clone https://github.com/Valentincrasnier/lengow.git
cd lengow
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
