# X Crypto

The project is a set of APIs for crypto exchange and related functionalities.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the App Manually](#running-the-app-manually)
- [Running the App via Docker](#running-the-app-via-docker) (incomplete!)
- [Configuration](#configuration)
- [Load Data](#load-data)
- [Testing](#testing)

---

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.12+ 
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hamidrasti/xcrypto.git
   cd xcrypto
   ```
   
2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the Python dependencies:

   ```bash
   pip install -r requirements/development.txt
   ```
   
## Running the App Manually

Once the dependencies are installed, you can run the Django project manually.

1. Run the Application:
    - Use the django server to run the app:

   ```bash
   python manage.py runserver
   ```
   
   - By default, the app will be available at: http://127.0.0.1:8000

2. Access the Interactive API Docs:
   - This project provides interactive API documentation using Swagger UI:
   - Go to http://127.0.0.1:8000/api/schema/swagger/ for the Swagger UI documentation.
   - Alternatively, visit http://127.0.0.1:8000/api/schema/redoc for ReDoc documentation.
   - You can also import the `X Crypto.postman_collection.json` to Postman.

## Running the App via Docker

If you'd like to run the app using Docker, follow these steps:

1. Build the Docker Image:

   ```bash
   docker compose build
   ```

2. Run the Docker Container:
    - Use the following command to start the application with Docker:
   ```bash
   docker compose up -d
   ```
    - This will start the Django project along with any other services defined in your docker-compose.yml file (e.g., databases, caching services, etc.).

3. Stopping the Container:
   ```bash
   docker compose down
   ```
   
4. Accessing the Application:
   - The app will be available at http://localhost:8000 (or the port defined in your Docker setup).
   - Access the API docs at:
        - http://127.0.0.1:8000/api/schema/swagger/
        - http://127.0.0.1:8000/api/schema/redoc/
   - You can also import the `X Crypto.postman_collection.json` to Postman.

## Configuration
- You can define environment variables in a .env file or in the docker-compose.yml file for configuration purposes (e.g., database credentials, API keys).
- Make sure to adapt the Docker and Python settings as needed for production use (e.g., setting up proper logging, configuring uwsgi, etc.).


## Load Data

You can load fixtures provided for users, cryptos and orders using:

```shell
python manage.py loaddata
```

Now we have two users with this info:

- admin
    ```json
    {
      "username": "admin",
      "password": "pass123456"
    }
    ```

- hamid
    ```json
    {
      "username": "hamid",
      "password": "pass"
    }
    ```
  

## Testing

### Run tests

Execute this command:

```shell
pytest
```

or this:

```shell
python manage.py test
```

### Tests coverage

Run this commands to get coverage report:

```shell
coverage run --source='.' manage.py test
coverage report
```

