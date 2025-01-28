Project Documentation: Sentiment Analysis API with Prometheus and Grafana Monitoring
1. Project Overview
This project implements a Sentiment Analysis API using FastAPI and HuggingFace's pre-trained cardiffnlp/twitter-roberta-base-sentiment-latest model. The API allows users to send text and receive sentiment analysis results (positive, negative, or neutral). To monitor the application's performance and metrics, Prometheus is used for gathering data and Grafana is employed to visualize those metrics.

The system is containerized using Docker, and Docker Compose is utilized to manage the various services (FastAPI, Prometheus, and Grafana). The project focuses on deploying a highly scalable and monitored API service.

2. Design Choices
FastAPI:

Chosen for its high performance and easy integration with machine learning models. FastAPI enables rapid development of APIs and provides automatic documentation through Swagger UI.
HuggingFace Model:

The model cardiffnlp/twitter-roberta-base-sentiment-latest was selected due to its high accuracy in sentiment analysis for social media text. It is a robust pre-trained model that handles various types of input text effectively.
Prometheus and Grafana:

Prometheus was chosen for monitoring the API because of its efficiency in scraping and storing metrics. It can be configured to collect and query metrics, making it perfect for API performance monitoring.
Grafana is used for data visualization, providing an intuitive dashboard to track metrics such as response times, error rates, and throughput.
Docker & Docker Compose:

Docker was used to containerize the application, ensuring portability and scalability. Docker Compose simplifies the management of multi-container applications, enabling seamless deployment of FastAPI, Prometheus, and Grafana together.
3. Implementation Details
FastAPI Application:

The API exposes two endpoints:
A GET / endpoint that returns a welcome message.
A POST /analyze-sentiment/ endpoint that accepts text input and returns sentiment analysis results.
The HuggingFace pipeline is used to perform sentiment analysis on the input text.
Prometheus Monitoring:

Metrics from FastAPI are exposed to Prometheus via the prometheus-fastapi-instrumentator. It automatically exposes the default set of application metrics (e.g., request count, response time).
Prometheus is configured to scrape the metrics from the FastAPI service every 15 seconds, as defined in the prometheus.yml configuration file.
Grafana Visualization:

Grafana is set up to connect to Prometheus as a data source. A simple dashboard is created to visualize the metrics being scraped by Prometheus.
Key metrics displayed in Grafana include the total request count, response time distribution, and error rates.
Containerization:

The project is containerized using Docker. A Dockerfile was created to set up the FastAPI environment and install necessary dependencies. The docker-compose.yml file defines the services for FastAPI, Prometheus, and Grafana and ensures they are deployed together.
4. Results
API Performance:

The FastAPI service performs sentiment analysis on text data and returns results quickly. The integration with HuggingFace's model allows for high-quality analysis, even for large datasets of social media text.
Monitoring and Metrics:

Prometheus collects metrics such as request count, response duration, and error rates. These metrics are displayed in Grafana dashboards, enabling easy visualization of system performance.
Monitoring metrics allow for proactive identification of issues, such as slow response times or high error rates.
Deployment and Scalability:

The application is successfully containerized and can be easily deployed in any environment that supports Docker. Docker Compose manages the services, ensuring they are properly configured and running in sync.
The use of Docker allows for easy scaling by adding more FastAPI instances if necessary.
5. Challenges and Solutions
Container Orchestration:

Managing multiple services (FastAPI, Prometheus, and Grafana) using Docker Compose was straightforward. However, scaling the application to handle more traffic may require additional configuration, such as using Kubernetes for orchestrating containers in a production environment.
Model Response Time:

Initially, the sentiment analysis model had slower response times, especially when handling multiple requests in parallel. This was mitigated by using FastAPI’s asynchronous features and optimizing the model’s inference process.
Prometheus and Grafana Setup:

Configuring Prometheus to scrape metrics from FastAPI and setting up Grafana dashboards required fine-tuning. However, once properly configured, the integration was seamless and provided useful insights into API performance.

An overview of the project is the following:

1. FastAPI: The core of the application
Main function: FastAPI is the web framework used to build the API that provides sentiment analysis services. Users can send texts via a POST request to an endpoint, and the app will return the sentiment (positive, negative, or neutral) associated with that text.
Functionality:
Endpoint / (GET): A welcome endpoint that returns a welcome message.
Endpoint /analyze-sentiment/ (POST): Accepts a text via a JSON payload, sends it to the HuggingFace model for sentiment analysis, and returns the sentiment prediction (positive, neutral, or negative) for the text.ù

3. HuggingFace (Sentiment Analysis):
Main function: The model used for sentiment analysis is a pre-trained model from HuggingFace, called cardiffnlp/twitter-roberta-base-sentiment-latest. This model was trained on tweets and can identify if the text is positive, negative, or neutral.
Model loading: When the FastAPI app is started, the model is loaded into memory and is ready to make predictions on the texts sent via the API.

4. Prometheus: Performance Monitoring
Main function: Prometheus is used to collect monitoring metrics from your FastAPI service. These metrics can include, for example, the number of requests received, response times, and other useful statistics to monitor the performance of the service.
Configuration: Prometheus is configured to scrape metrics from FastAPI every 15 seconds, using an endpoint exposed by FastAPI through the prometheus-fastapi-instrumentator library.

5. Grafana: Metric Visualization
Main function: Grafana is used to visualize the metrics collected by Prometheus. It allows you to create interactive dashboards that show real-time graphs of the API's performance.
Configuration: After starting the project with Docker, you can access Grafana through your browser at port 3000 and view the Prometheus data on a well-structured dashboard.

6. Docker and Docker Compose:
Main function: Docker and Docker Compose make the entire project easy to run on any machine. Instead of manually installing all dependencies, you can simply start the containers with a single command, and the whole system will be configured automatically.
FastAPI: Runs as a Docker container.
Prometheus: Runs as a Docker container for monitoring.
Grafana: Runs as a Docker container for visualizing metrics.

7. CI/CD (GitHub Actions):
Main function: The CI/CD pipeline automates the build, test, and deployment process. Every time you make a change to the code and push it to GitHub, the pipeline automatically performs the following steps:
Build the Docker Image: Creates the Docker image for the application.
Push the Image to Docker Hub: Uploads the Docker image to your Docker Hub account.
Deploy the Project Using Docker Compose: Starts the containers for FastAPI, Prometheus, and Grafana.
Test the Application: Runs a test to check if the API is functioning correctly.

What the Project Does:
Sentiment Analysis: The application provides an API that analyzes the sentiment of a given text using a pre-trained HuggingFace model. Users can send a text via a POST request and receive a response with the identified sentiment (positive, negative, neutral).
Monitoring and Visualization:
Prometheus collects performance metrics of the API (e.g., number of requests, response time).
Grafana visualizes these metrics in a clear and interactive way.
Automation: Using GitHub Actions, every new change to the code automatically triggers a process of testing, building, deploying, and monitoring.
Results:
Working API: The API is able to respond to sentiment analysis requests.
Monitoring: The performance of the API is monitored in real time via Prometheus and visualized in Grafana.
Automation: Every new version of the code is automatically built, tested, and deployed, reducing the risk of errors and improving efficiency.

6. Conclusion
The Sentiment Analysis API successfully processes and analyzes text input for sentiment. With the added integration of Prometheus and Grafana, the application is not only able to provide sentiment analysis but also allows for detailed monitoring and performance tracking. Docker ensures portability and scalability, while the use of a pre-trained HuggingFace model allows for accurate sentiment analysis out-of-the-box.

Future improvements could include:

Enhanced Dashboard: Adding more detailed metrics and alerts in Grafana.
Model Updates: Fine-tuning the sentiment analysis model with domain-specific data to improve accuracy.
Deployment: Moving to a production-grade environment with Kubernetes for better orchestration and auto-scaling.

