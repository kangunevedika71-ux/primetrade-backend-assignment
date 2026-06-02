# setup_env.py
import os

env_content = '''# Django Security
DJANGO_SECRET_KEY=primetrade-super-secret-key-change-this-in-production-2026

# Database Configuration (PostgreSQL)
DB_NAME=primetrade_db
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432

# Development Settings
DEBUG=True
'''

with open('.env', 'w') as f:
    f.write(env_content)

print(".env file created successfully!")