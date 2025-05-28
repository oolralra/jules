# Multi-Service Application

This application consists of three web services, each built with a different Python/Java web framework, and orchestrated using Docker Compose.

## Services

The application includes the following services:

*   **Main Service (`main_service`)**:
    *   Technology: **Spring Boot (Java)**
    *   Description: This is the primary entry point of the application. It provides a simple HTML page with buttons to navigate to the "like" and "hate" services.
    *   Accessible at: `http://211.183.3.99:5001`
*   **Like Service (`like_service`)**:
    *   Technology: **FastAPI (Python)**
    *   Description: This service displays a friendly message: "강사님을 좋아하는 천사들".
    *   Accessible at: `http://211.183.3.99:5002`
*   **Hate Service (`hate_service`)**:
    *   Technology: **Flask (Python)**
    *   Description: This service displays a different message: "강사님을 싫어하는 악마들".
    *   Accessible at: `http://211.183.3.99:5003`

## Prerequisites

*   Docker
*   Docker Compose

## Building and Running the Application

1.  **Clone the repository (if you haven't already):**
    ```bash
    # git clone <repository_url>
    # cd <repository_directory>
    ```

2.  **Build and run the services using Docker Compose:**
    From the root directory of the project (where `docker-compose.yml` is located):
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker images for each service (if they don't exist or if the source code has changed) and then start the containers.

3.  **Accessing the services:**
    Once the containers are running, you can access the services through the URLs mentioned above using the IP address `211.183.3.99`.

4.  **Stopping the application:**
    To stop the services, press `Ctrl+C` in the terminal where `docker-compose up` is running. To stop and remove the containers, you can run:
    ```bash
    docker-compose down
    ```

## Project Structure

```
.
├── docker-compose.yml      # Docker Compose configuration
├── main_service/           # Main service (Spring Boot)
│   ├── pom.xml
│   ├── src/main/java/com/example/mainservice/
│   │   ├── MainServiceApplication.java
│   │   └── MainController.java
│   ├── src/main/resources/static/
│   │   └── index.html
│   └── Dockerfile
├── like_service/           # Like service (FastAPI)
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── hate_service/           # Hate service (Flask)
│   ├── app.py
│   └── Dockerfile
└── README.md               # This file
```
