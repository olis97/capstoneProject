# Django Website

Welcome to the repository for my Capstone Django website. Below are instructions to set up and run the website yourself.

## Before Beginning

Make sure you have the following prerequisites installed on your system:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Python 3.10: [Install Python](https://www.python.org/downloads/)

## Setting Up Your Environment

Follow these steps to set up your development environment:

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/olis97/capstoneProject.git
   cd capstoneProject
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m virtualenv venv
   ```

   ```bash
   cd venv/scripts
   activate
   ```
   
3. Install the required Python packages inside your virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

4. Run Django web server using localhost:

   ```bash
   python manage.py runserver
   ```

## Running Capstone Project Website

Use Docker to run the Django website. Follow these steps:

1. Build the Docker image from the provided Dockerfile:

   ```bash
   docker build -t capstone-project .
   ```

2. Start a Docker container with the website:

   ```bash
   docker run -d -p 8000:8000 capstone-project
   ```

The website should now be accessible at [http://localhost:8000](http://127.0.0.1:8000).