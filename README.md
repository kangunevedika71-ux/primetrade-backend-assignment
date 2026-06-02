# Primetrade Backend Assignment

## Scalable REST API with Authentication & Role-Based Access

### Features
- JWT Authentication (Register/Login)
- Role-based Access (User vs Admin)
- Complete CRUD Operations for Tasks
- Swagger API Documentation
- Frontend UI Dashboard

### Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
