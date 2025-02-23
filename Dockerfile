FROM python:3.11

# Set the working directory
WORKDIR /app

# Install pipenv(it is a package manager for Python that provides an easy way to set up a virtual environment and install packages from the Python Package Index)
RUN pip install pipenv

RUN pip install psycopg2-binary

# Copy pipfile and pipfile.lock
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pipenv install --deploy --system

# Copy the current directory contents into the container at /app
COPY inventory_project /app/inventory_project


# Copy Pipfile and Pipfile.lock first (to leverage Docker cache)
COPY Pipfile Pipfile.lock ./



WORKDIR /app/inventory_project

# Expose port 8000
EXPOSE 8000


# Run the application:(migrate the database and run the server)
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

# N.B:  sh
# sh is the shell (Bourne shell) used inside the container.
# It allows you to execute shell commands.
# 🔹 -c
# -c tells sh to execute the following string as a command.
