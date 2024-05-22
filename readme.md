This is a project for django-react-docker.

1. Clone the project from github 
git clone git@github.com:bibek977/django-api.git

2. Workdir
cd django_api

3. Python virtual environments
python3 -m venv venv_django_api
source venv_django_api/bin/activate

4. Install requirements.txt
pip install -r requirements.txt

5. Copy .env file
cp .env.example .env

6. Fill the credentials data in env file

7. Migrate the project
python manage.py migrate

8. Run the project
python manage.py runserver

=============== For docker ===================

1. Clone the project from github 
git clone git@github.com:bibek977/django-api.git

2. Workdir
cd django_api

3. Docker build 
docker compose build

4. Docker run
docker compose up