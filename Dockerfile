# Use official version from python
FROM python:3.10-slim

# define work dir
WORKDIR /app

# Copy files
COPY . /app

# install dependencys
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# port
EXPOSE 5000

# init app
CMD ["python", "run.py"]
