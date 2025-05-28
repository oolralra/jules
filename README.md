# Multi-Service Application

This application consists of three simple web services built with Flask and orchestrated using Docker Compose.

## Services

The application includes the following services:

*   **Main Service**: This is the primary entry point of the application. It provides a simple HTML page with buttons to navigate to the "like" and "hate" services.
    *   Accessible at: `http://localhost:5001`
*   **Like Service**: This service displays a friendly message: "강사님을 좋아하는 천사들".
    *   Accessible at: `http://localhost:5002`
*   **Hate Service**: This service displays a different message: "강사님을 싫어하는 악마들".
    *   Accessible at: `http://localhost:5003`

## Prerequisites

*   Docker
*   Docker Compose

## Building and Running the Application

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Build and run the services using Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker images for each service (if they don't exist or if the source code has changed) and then start the containers.

3.  **Accessing the services:**
    Once the containers are running, you can access the services through the URLs mentioned above:
    *   Main Service: `http://localhost:5001`
    *   Like Service: `http://localhost:5002`
    *   Hate Service: `http://localhost:5003`

4.  **Stopping the application:**
    To stop the services, press `Ctrl+C` in the terminal where `docker-compose up` is running. To stop and remove the containers, you can run:
    ```bash
    docker-compose down
    ```

## Project Structure

```
.
├── docker-compose.yml      # Docker Compose configuration
├── main_service/           # Main service code and Dockerfile
│   ├── app.py
│   └── Dockerfile
├── like_service/           # Like service code and Dockerfile
│   ├── app.py
│   └── Dockerfile
├── hate_service/           # Hate service code and Dockerfile
│   ├── app.py
│   └── Dockerfile
└── README.md               # This file
```
