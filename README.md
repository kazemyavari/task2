# Python & Django Challenge - Backend

This is an API that serves shipment data and provides users with current weather conditions at their location.

# Getting Started
-   [Installation](#installation)
-   [Usage](#usage)
-   [Discussion Points](#discussion_points)

## Installation
- Prerequisites:
  - [Docker](https://www.docker.com/get-started)
  - [Docker Compose](https://docs.docker.com/compose/install/)

1. Clone repository:
	```bash
	git clone git@github.com:kazemyavari/task2.git
	cd task2
	```
2. Create a copy of this `env.example` file and name it `.env`. This file will store your actual environment variables. Open the `.env` file in a text editor of your choice and set the values for each variable as required by the project or You can use `.env.development`.
	```bash
	cp env.example .env
	# or
	cp env.development .env
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
	-  `REDIS_CACHES_LOCATION`: Location or connection string for Redis cache.
	-  `CELERY_BROKER_URL`: URL for Celery message broker.
	-  `CELERY_RESULT_BACKEND`: URL for Celery result backend.
	-  `WEATHER_API_KEY`: An API key for accessing a weather service (e.g., OpenWeatherMap). This is required for fetching weather data.


## Usage
**Running the Project with Docker**
- Run the Docker Container:
	```bash
	 docker compose up -d
	```
- Import shipment data into the database:
	
 	You can use the following Docker Compose command.

	```bash
	 docker compose exec web python manage.py import_shipments shipment.csv
	```

 - If you want to run the tests first, You can running the tests with Docker:
	```bash
	 docker compose exec web python manage.py test
	```

##
Your project should now be running, and you can access it at [http://127.0.0.1:8000](http://127.0.0.1:8000/) in your web browser.

##### API Documentation
Swagger/OpenAPI documentation is available for your APIs. You can access it at:

http://127.0.0.1:8000/api/docs/

Use the API documentation to explore and test your APIs interactively.
 

## Discussion Points

### Important Design Choices and Trade-offs:

1. Retrieving Weather Data Every 2 Hours:

	To efficiently retrieve weather data while minimizing API calls, I have implemented the following design choices and trade-offs:

    - **Celery and Celery Beat:**

  	   I have integrated Celery, a distributed task queue, along with Celery Beat, a scheduler for periodic tasks, to manage the periodic execution of the task to fetch weather data. This ensures that the `get_weather` task runs every 2 hours.
  
      - Advantages:
        - Scalability: Celery allows us to distribute the workload and scale the application horizontally.
        - Task Scheduling: Celery Beat simplifies the scheduling of periodic tasks, making it easy to manage and configure.
  
      - Trade-offs:
        - Infrastructure Overhead: Introducing Celery requires additional infrastructure components, such as a message broker (e.g., Redis). This adds complexity to the deployment.

   - **Caching:**

     To further optimize and reduce unnecessary API calls, I leverage caching. Weather data for a specific location (zip code) is cached, and subsequent requests within the 2-hour window retrieve the data from the cache.

      - Advantages:
        - Reduced API Calls: Caching minimizes the need to make redundant API calls for the same location within the 2-hour interval.
        - Improved Performance: Cached data retrieval is faster compared to making API calls.

      - Trade-offs:
        - Data Freshness: While caching improves performance, it introduces a trade-off with data freshness. Weather data may not always reflect real-time conditions if fetched from the cache.

2. Dockerization:
   
    The project is containerized using Docker to ensure consistency across development and production environments.

    - Trade-offs:
      - Resource Overhead: Docker adds a slight resource overhead, and the team must consider the trade-offs between resource usage and containerization benefits.


### Deployment to Production:

1. #### Database Setup:

    Set up a production-ready database like PostgreSQL.
    Configure database connection settings in the production environment.

2. #### Security:

    Ensure that sensitive information such as secret keys and database credentials are stored securely.
    Set up HTTPS for secure communication.

3. #### Django Settings:

    Adjust Django settings for production, including DEBUG, ALLOWED_HOSTS, and other security-related settings.

4. #### Web Server and Application Server:

    Choose a production-ready web server (e.g., Nginx or Apache) to serve static files and handle requests.
    Use a production-ready application server (e.g., Gunicorn) to run the Django application.

### Scaling for 1000 Requests Per Second:

These scaling strategies collectively contribute to building a robust, scalable, and high-performance system capable of handling 1000 requests per second or more. Regular performance testing and optimization are essential to ensure the system's responsiveness and reliability under different loads.

1. #### Load Balancing:
    Load balancing involves distributing incoming traffic across multiple server instances. This ensures that no single server bears the entire load and improves fault tolerance and availability. Popular solutions include Nginx or dedicated load balancers.

2. #### Database Scaling:
   Optimizing database queries is crucial for handling increased traffic. Consider options like read replicas for distributing read queries or database sharding for horizontal partitioning of data.

3. #### Caching Strategies:
    Optimizing caching becomes even more critical at scale. Consider distributed caching solutions to share cached data across multiple server instances. This can reduce the load on the database and improve overall system performance.
   
4. #### Horizontal Scaling:
    Adding more application server instances horizontally scales the system. This can be achieved by deploying additional server instances and using load balancing to distribute incoming requests.
   
5. #### Content Delivery Network (CDN):
    CDNs cache and serve static content from servers located closer to users, reducing the load on application servers. Implementing a CDN improves the overall performance and user experience.
   
6. #### Monitoring and Optimization:
    Implement monitoring tools to identify performance bottlenecks. Optimize database queries, caching strategies, and server configurations based on insights from monitoring tools.
   
7. #### Auto-scaling:
    Implement auto-scaling to dynamically adjust the number of application server instances based on demand. This ensures that the system can efficiently handle varying levels of traffic without manual intervention.