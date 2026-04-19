#!/usr/bin/env bash
# exit on error
set -o errexit

# Frontend build
echo "Building frontend..."
npm install
npm run build

# Backend build
echo "Building backend..."
cd Nexora_backend
python -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
