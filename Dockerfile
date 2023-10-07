FROM python:3.10

# My working directory
WORKDIR /app

COPY requirements.txt /app/ 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Run Django website
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
