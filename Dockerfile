# Dockerfile
FROM python:3.10-slim

WORKDIR /xa

# Install system dependencies
RUN apt-get update && apt-get install -y git libpq-dev
RUN apt-get update && \
    apt-get install -y \
        gcc \
        python3-dev \
        libffi-dev \
        build-essential \
        zlib1g-dev \
        libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install them
COPY requirements.txt /xa/requirements.txt
RUN pip install --upgrade "pip<24.1" && \
    pip install -r requirements.txt
RUN pip install --no-cache-dir cffi==1.14.4
RUN pip install django-utils-six
# RUN pip install --upgrade pip && \
#     pip install --no-use-pep517 anyjson==0.3.3 && \
#     pip install -r requirements.txt


# Copy the entire project
COPY . /xa/

# Expose the port for Gunicorn/Django
EXPOSE 8000

# Start Gunicorn, binding to 0.0.0.0:8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
