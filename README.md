### **Submission of Fetch Take-Home Assignment - Receipt Processor**

Hi There,

Thank you for this wonderful opportunity! I thoroughly enjoyed working on the **Receipt Processor** project. Below, I’ve shared details about the project, how to run it, and the technologies I used.

---

# Receipt Processor

### **Overview**
This is a Flask-based web service that processes receipts and calculates reward points based on predefined rules.

### **How to Run the Application?**

**Prerequisites**
- Ensure to have the following installed:
   - Docker Desktop ([Install Docker](https://docs.docker.com/get-docker/))
   - Docker Compose ([Install Docker Compose](https://docs.docker.com/compose/install/))
   - IDE: Visual Studio Code or similar (local terminal also works)
   - Postman login: To test the endpoints


**Project Structure**
- Main project folder: `fetch-take-home-assignment/receipt_processor/`
- Entry point for the Web service: `fetch-take-home-assignment/receipt_processor/app.py`

**Steps to Run the Application**
1. Clone the Repository in either terminal or VS code:
   - Open your terminal and run:
      `git clone https://github.com/ram-1918/fetch-take-home-assignment.git`

2. Navigate to the Project Folder:
   - Move into the project directory:
   `cd fetch-take-home-assignment`
   Ensure you see the docker-compose.yml file in this folder.

3. There are two ways to Start the Application: **using Docker** or **manually**.
   - **Option 1: Using Docker**
      1. Start the Application:
         - Ensure to login to Docker using `docker login` in the terminal/VS code terminal
         - Then, Run the following command to start the application and Redis:
         ```
         docker compose up --build
         ```

   - **Option 2: Running Manually**
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
   `GET /health`
   ```
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
     `POST /receipts/process`
     ```
     http://127.0.0.1:5002/receipts/process
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
        {"id": "be080fd7-5e16-406d-b0fa-71b4e377944f"}
     ```

   - **Get points for a receipt**: Returns the total points associated with the given id.
     `GET /receipts/{id}/points`
     ```
     http://127.0.0.1:5002/receipts/{id}/points
     ```
     **Sample Response**
     ```
        {"points": 28}
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
      - Used a clear pattern for handling/applying rules(designed for scalability)
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
3. **Posting a Receipt**: Verifying the `/receipts/process` endpoint to ensure receipts are processed successfully.  
4. **Fetching Points**: Testing the `/receipts/{id}/points` endpoint to validate that points are calculated and returned correctly.  

**Steps to Run the Tests locally**
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

### **Points Obtained for Example Receipts**
- **simple-receipt.json**: 31 points
```
{
    "retailer": "Target", ---------> 6 alphanumeric characters => 6 points
    "purchaseDate": "2022-01-02",
    "purchaseTime": "13:13",
    "total": "1.25", --------------> multiple of 0.25 => 25 points
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"}
    ]
}
```

- **morning-receipt.json**: 15 points
```
{
    "retailer": "Walgreens",
    "purchaseDate": "2022-01-02", 0
    "purchaseTime": "08:13", 0
    "total": "2.65", 
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
        {"shortDescription": "Dasani", "price": "1.40"}
    ]
}
```

### **Conclusion**
Once again, thank you so much for this opportunity. I’m excited about the next steps and look forward to hearing from you. Please feel free to reach out if you have any questions or need further details.

---

### **Notion Link**
I used **Notion** to plan and organize my work before starting the project. You can find my planning notes here:
[Fetch's Receipt Processing Challenge - Notion Link](https://wild-sombrero-867.notion.site/Fetch-s-Receipt-Processing-Challenge-188c3d96afe58035b62ae428f6102369)

---

Thank you,

Ram Chandra