from flask import Flask, request, jsonify
import redis
from utils import generate_uuid
from schema import ReceiptSchema, ItemSchema
from service import ReceiptProcessorService

# Initialize Flask App
app = Flask(__name__)

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Endpoints
@app.route('/receipt/process', methods=['POST'])
def post_receipt():
    # Extract the paylaod from the request object
    data = request.json

    # Validate the payload against the schema
    try:
        validated_data = ReceiptSchema().load(data)
    except:
        return jsonify({"description": "The receipt is invalid."}), 400
    
    # If the receipt is valid,
    # Generate a unique ID
    uniqueID = str(generate_uuid())

    # Process the validated receipt data
    receipt_process_instance = ReceiptProcessorService()
    total_points_for_receipt = receipt_process_instance.get_points(validated_data)

    # Store the total points obtained for the receipt on redis under the ID
    redis_client.set(uniqueID, total_points_for_receipt)

    # Send the ID as the Response
    response_data = {"id": uniqueID}
    return jsonify(response_data), 200

@app.route('/receipt/<id>/points', methods=['GET'])
def get_points(id):
    # Retrieve the points associated with the ID stored in Redis
    points_for_the_id = redis_client.get(id)
    print(id, points_for_the_id)
    if not points_for_the_id:
        return jsonify({"description": "No receipt found for that ID."}), 404
    return jsonify({"points": int(points_for_the_id)}), 200

# Run the Flask Application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)