This project demonstrates how to run background tasks in a Django application using Celery and Redis. It enables time-consuming operations—such as sending emails, processing files, or generating reports—to run 
asynchronously in the background, allowing Django to respond instantly without delays. Celery acts as the task manager that handles job execution, while Redis serves as the message broker to store and deliver 
tasks efficiently. This setup improves performance, scalability, and user experience by offloading heavy tasks from the main application process.
