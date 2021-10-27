## 0. Create new virtual environment and install dependencies:
```shell
pip install -r requirements.txt
```
## 1. Fill ".env" file with custom configuration

## 2. Run PostgreSQL in docker:
```shell
docker run --name postgres_db -p 5432:5432 -d -e POSTGRES_DB="db" -e POSTGRES_USER="admin" -e POSTGRES_PASSWORD="admin" postgres:latest 
```
## 3. Make migrations:
```shell
python manage.py makemigrations
```
## 4. Migrate:
```shell
python manage.py migrate
```
## 5. Run server:
```shell
python manage.py runerver
```
## 6. Go to swagger:
> http://localhost:8000/api/v1/docs

## 7. Create the user:
> You need to click on /user/ with POST method and type your credentials

## 8. Activate your account:
> Go to your email account and push the button in activation letter

## 9. Create JWT token:
> You need to click on /jwt/create/ with POST method and type your credentials

## 10. Authorize with JWT access token:
> Push authorize button on swagger and insert your token: JWT <token>