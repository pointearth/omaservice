# Choose our version of Python
From python:3.11.6

# Set up a working directory
WORKDIR /code

# Copy just the requirements into the working directory so it gets cached by itself
COPY ./requirements.txt /code/requirements.txt

# Intall the dependencies from the requirements file
RUN pip install -r /code/requirements.txt

# Copy the code into the working directory
COPY ./app /code/app
COPY ./data /code/data


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]