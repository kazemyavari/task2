# Python & Django Challenge - Backend

This is an API that serves shipment data and provides users with current weather conditions at their location.

# Getting Started
-   [Installation](#installation)
-   [Usage](#usage)
-   [Test](#test)
-   [Discussion Points](https://github.com/kazemyavari/task2/blob/main/discussion_points.md)

## Installation
1. Clone repository:
	```bash
	git clone git@github.com:kazemyavari/task2.git
	cd task2
	```
2. Create a copy of this `env.example` file and name it `.env`. This file will store your actual environment variables. Open the `.env` file in a text editor of your choice and set the values for each variable as required by the project.
	```bash
	cp env.example .env
	```
	
	> Remember to keep your `.env` file secure and never commit it to
	> version control. You should include it in your project's `.gitignore`
	> file to prevent accidental exposure of sensitive information`enter
	> code here`.

	##### Environment Variables

	Here is a list of environment variables that you need to configure in your `.env` file:

	-  `SECRET_KEY`: Django secret key for security. You should generate a unique secret key and set it here.
	-  `POSTGRES_HOST`: The host address where your PostgreSQL database is running.
	-  `POSTGRES_PORT`: The port on which PostgreSQL is listening.
	-  `POSTGRES_USER`: The username to authenticate with the PostgreSQL database.
	-  `POSTGRES_PASSWORD`: The password to authenticate with the PostgreSQL database.
	-  `POSTGRES_DB`: The name of the PostgreSQL database.
	-  `WEATHER_API_KEY`: An API key for accessing a weather service (e.g., OpenWeatherMap). This is required for fetching weather data.


## Usage
**Method 1: Running the Project with Docker** (Recommended)
- Prerequisites:
	 1. [Docker](https://www.docker.com/get-started)
	 2. [Docker Compose](https://docs.docker.com/compose/install/)
- Run the Docker Container:
	```bash
	 docker compose up -d
	```
- Import shipment data into the database:
	
 	You can use the following Docker Compose command.

	```bash
	 docker-compose exec api python manage.py import_shipments shipment.csv
	```

**Method 2: Running the Project with `Django`**
 
1. **Set Up Virtual Environment**:
	 ```bash
	  python -m venv venv
	  source venv/bin/activate # On Windows, use: venv\Scripts\activate
	 ```
2. **Install Dependencies**:
	 ```bash
	  pip install -r requirements.txt
	 ```
3. **Set or change database configuration in Django**:

   	If you want to use a PostgreSQL database (default in settings), make sure to set the appropriate environment variables for PostgreSQL in your `.env` file.

    If you prefer to use SQLite, you can modify the `DATABASES` configuration in the `settings.py` file. By default, the project is configured to use a PostgreSQL database. To switch to SQLite:

    - Open `settings.py`.
    - Locate the `DATABASES` section.
    - Change the `ENGINE` setting under the `default` database to `'django.db.backends.sqlite3'`.
    - Optionally, set the `NAME` to the desired SQLite database file name.

    Example configuration for SQLite:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / "db.sqlite3",
        }
    }
    ```

4. **Run the Migrate**:
	```bash
	 python manage.py migrate
	```

5. **Import shipment data into the database**:

	You can use the following Django command.

	```bash
	 python manage.py import_shipments shipment.csv
	```

6. **Run the Django Server**:
	 ```bash
	  python manage.py runserver
	 ```

##
Your project should now be running, and you can access it at [http://localhost:8000](http://localhost:8000/) in your web browser.

##### API Documentation
Swagger/OpenAPI documentation is available for your APIs. You can access it at:

http://localhost:8000/api/docs/

Use the API documentation to explore and test your APIs interactively.

## Test
To run tests for this project, follow these steps:

**Method 1: Running the Test with Docker**  (Recommended) 	
```bash
 # On Windows:
 docker compose -f docker-compose-test.yml up -d
 python manage.py test
 docker compose -f docker-compose-test.yml down
 # On Linux & Mac:
 ./run_test.sh
```
**Method 2: Running the Test with `Django`**
1. Activate your virtual environment (if not already activated):
	 ```bash
      source venv/bin/activate # On Windows, use: venv\Scripts\activate
	 ```
2. Install test dependencies (if not already installed):
	 ```bash
      pip install -r requirements.txt
	 ```
3. If needed:
   
    3.1. Set or change database configuration in Django: (Like: [Usage](#usage) > Method 2 > Step 3)
    
    3.2. Run the migrate: (Like: [Usage](#usage) > Method 2 > Step 4)
    
    3.3. Import shipment data into the database: (Like: [Usage](#usage) > Method 2 > Step 5)
  
4. Run the tests:
	 ```bash
      python manage.py test