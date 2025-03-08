# TechSphere Backend Setup Guide

## Prerequisites
Make sure the following are installed on your machine:
- Python 3.8+
- PostgreSQL (Supabase is used in this project, but you can configure a local setup if preferred)
- pip (Python package installer)

## Step 1: Clone the Repository
Clone the project to your local machine:
<!-- ```bash
git clone https://github.com/
cd 
``` -->

## Step 2: Create and Activate the Virtual Environment
Create a virtual environment to isolate dependencies:
```bash
python -m venv venv
```
Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```

## Step 3: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Step 4: Apply Database Migrations
Run the migrations to set up the database schema:
```bash
python manage.py migrate
```

## Step 5: Start the Development Server
Run the server locally to test the backend:
```bash
python manage.py runserver
```
Now, you can visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to check if everything is working.