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
6. Conclusion
The Sentiment Analysis API successfully processes and analyzes text input for sentiment. With the added integration of Prometheus and Grafana, the application is not only able to provide sentiment analysis but also allows for detailed monitoring and performance tracking. Docker ensures portability and scalability, while the use of a pre-trained HuggingFace model allows for accurate sentiment analysis out-of-the-box.

Future improvements could include:

Enhanced Dashboard: Adding more detailed metrics and alerts in Grafana.
Model Updates: Fine-tuning the sentiment analysis model with domain-specific data to improve accuracy.
Deployment: Moving to a production-grade environment with Kubernetes for better orchestration and auto-scaling.
