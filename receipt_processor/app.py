from flask import Flask, request, jsonify
import redis, logging, os
from utils import generate_uuid
from schema import ReceiptSchema
from service import ReceiptProcessorService

from marshmallow import ValidationError

# Initialize logging object
logger = logging.getLogger(__name__)

# Initialize Flask App
app = Flask(__name__)

# Connect to Redis
redis_client = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, db=0)

try:
    redis_client.ping()
except:
    logger.info("Failed to connect with Redis!")

# Endpoints
@app.route('/receipt/process', methods=['POST'])
def post_receipt():
    """
        POST /receipts
        - Receives receipt data as JSON payload.
        - Validates the payload against 'ReceiptSchema' (schema.py). 
            - Raises BadRequest("The receipt is invalid.") if validation fails.
        - Generates a unique ID for the receipt.
        - Processes the payload using business rules to calculate total points.
        - Stores the ID and associated points in Redis.
        - Returns the unique ID in the response.
    """
    logger.info(f'A POST HTTP request made for processing a receipt!')

    # Extract the paylaod from the request object
    payload = request.json

    # Validate the payload against the schema
    logger.info(f'STEP: Receipt information validation!')
    
    try:
        validated_data = ReceiptSchema().load(payload)
    except ValidationError as e:
        logger.info(f'STEP: Error occured while validating Receipt Information, {e.messages}')
        return jsonify({"error": f"The receipt is invalid. {e}"}), 400

    # If the receipt is valid,
    logger.info(f'STEP: UUID Generation!')
    uniqueID = str(generate_uuid())

    logger.info(f'STEP: Process the validated receipt data to obtain points!')
    
    receipt_process_instance = ReceiptProcessorService(logger)
    total_points_for_receipt = receipt_process_instance.get_points(validated_data)
    
    logger.info(f'STEP: Store ID and the total points obtained for the receipt on Redis!')
    redis_client.set(uniqueID, total_points_for_receipt)

    logger.info(f'STEP: Propagate the response!')

    response_data = {"id": uniqueID}
    return jsonify(response_data), 200

@app.route('/receipt/<id>/points', methods=['GET'])
def get_points(id):
    """
        GET /receipts/{id}/points
        - Receives an ID parameter.
        - Validates if the ID exists in Redis.
            - Raises a suitable error if not found.
        - Retrieves the total points associated with the ID.
        - Returns the points in the response.
    """
    logger.info(f'STEP: Retrieve points associated with the ID from Redis')
    points_for_the_id = redis_client.get(id)

    if not points_for_the_id:
        logger.info(f'STEP: Error occured while points retrieval for the ID {id}')
        return jsonify({"error": "No receipt found for that ID."}), 404
    
    logger.info(f'STEP: Propagate the response!')
    return jsonify({"points": int(points_for_the_id)}), 200

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"message": "Service is active!"}), 200

# Run the Flask Application
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    app.run(host='0.0.0.0', port=5003)