**Subject: Submission of Fetch Take-Home Assignment - Receipt Processor**

Hi Team,

Thank you for this wonderful opportunity! I thoroughly enjoyed working on the **Receipt Processor** project. Below, I’ve shared details about the project, how to run it, and the technologies I used.

---

# Receipt Processor

### Overview
This is a Flask-based web service that processes receipts and calculates reward points based on predefined rules.

### Prerequisites
- Docker Desktop ([Install Docker](https://docs.docker.com/get-docker/))
- Docker Compose ([Install Docker Compose](https://docs.docker.com/compose/install/))
- Docker Login using `docker login`

### **How to Run the Application?**
There are two ways to run the application: **using Docker** or **manually**.

#### **Option 1: Using Docker**
1. Pull the Docker image:
   ```
   docker pull ram1918/receipt_processor:latest
   ```  
2. Start the application:
   ```
   docker compose up
   ```

#### **Option 2: Running Manually**
1. Navigate to the project folder: 
   ```
   cd fetch-take-home-assignment
   ```
2. Set up the environment:
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   cd receipt_processor
   python app.py
   ```

---

### **How to Access the Application? API Endpoints**
1. Check if the web service is active:
   ```
   GET 
   http://127.0.0.1:5002/health
   ```
   **Sample Response**
   ```
    {
        "message": "Service is active!"
    }
   ```
2. If the service is active:  
   - **Process a receipt**: Accepts JSON data for a purchase receipt and returns an id.
     ```
     POST 
     http://127.0.0.1:5002/receipt/process
     ```

     **Sample Request Body**
     ```
        {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
        }
     ```

     **Sample Response**
     ```
        {
            "id": "be080fd7-5e16-406d-b0fa-71b4e377944f"
        }
     ```

   - **Get points for a receipt**: Returns the total points associated with the given id.
     ```
     GET 
     http://127.0.0.1:5002/receipt/{id}/points
     ```
     **Sample Response**
     ```
        {
            "points": 28
        }
     ```

---

### **Tech Stack Used?**
- **Programming Language**: Python (I’m comfortable with Python but can also switch to Golang if needed).
- **Flask**: A lightweight web framework
- **Redis**: An in-memory data store for fast and efficient data handling.
- **API Style**: RESTful architecture.
- **Docker**: For containerization and easy deployment.
- **GitHub**: For version control and collaboration.

---

### **How I Built It?**
1. **Flask App Setup with Redis**
   - Created a virtual environment and added dependencies in `requirements.txt`.
   - Installed Flask, Redis, and Marshmallow for data validation.
   - Configured Redis to listen on port `6379`.
   - Designed API endpoints and implemented the business logic.
   - Tested the service thoroughly to ensure it works as expected.

2. **Docker Setup**
   - Created a `Dockerfile` with steps to build and run the Flask app.
   - Created a `docker-compose.yml` file to start both the services, `Flask app` and `Redis`.
   - Built the Docker image:
     ```
     docker build -t ram1918/receipt_processor:latest .
     ```
   - Pushed the Docker image:
     ```
     docker push ram1918/receipt_processor:latest
     ```
   - Ran the Docker container:
     ```
     docker run -p 5002:5000 ram1918/receipt_processor:latest
     ```
     *(I used port `5002` because ports `5000` and `5001` were already in use.)*
   - Tested the service to ensure everything works smoothly.

---

### **How I Tested the Application**  
To ensure the application works as expected, I wrote **unit tests** covering various scenarios:  
1. **Valid Receipt**: Testing the application with a correctly formatted receipt.  
2. **Invalid Receipt**: Testing how the application handles incorrect or incomplete receipt data.  
3. **Posting a Receipt**: Verifying the `/receipt/process` endpoint to ensure receipts are processed successfully.  
4. **Fetching Points**: Testing the `/receipt/{id}/points` endpoint to validate that points are calculated and returned correctly.  

#### **Steps to Run the Tests locally**
1. Navigate to the project folder:
   ```
   cd fetch-take-home-assignment/receipt_processor
   ```
2. Run the unit tests:
   ```
   python -m unittest tests.py
   ```

---

### **Stopping the Application**
To stop the application and remove Docker containers, run:  
```
docker compose down
```

---

### **Troubleshooting**
- **Port Conflicts:** Change the port in `docker-compose.yml` if 5002 is in use.
- **Redis Connection Issues:** Check Redis logs using `docker-compose logs redis`.
- **Application Logs:** Debug issues using `docker-compose logs app`.

---

### **Conclusion**
Once again, thank you so much for this opportunity. I’m excited about the next steps and look forward to hearing from you. Please feel free to reach out if you have any questions or need further details.

---

### **Notion Link**
I used **Notion** to plan and organize my work before starting the project. You can find my planning notes here:
[Fetch's Receipt Processing Challenge - Notion Link](https://wild-sombrero-867.notion.site/Fetch-s-Receipt-Processing-Challenge-188c3d96afe58035b62ae428f6102369)

---

Thank you,

Ram Chandra