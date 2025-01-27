import unittest
import requests

valid_receipt = {
    "retailer": "M&M Corner Market",
    "purchaseDate": "2022-03-20",
    "purchaseTime": "14:33",
    "items": [
    {
        "shortDescription": "Gatorade",
        "price": "2.25"
    },
    {
        "shortDescription": "Gatorade",
        "price": "2.25"
    },
    {
        "shortDescription": "Gatorade",
        "price": "2.25"
    },
    {
        "shortDescription": "Gatorade",
        "price": "2.25"
    }
    ],
    "total": "9.00"
}

valid_receipt1 = {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
        },
        {
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
        },
        {
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
        },
        {
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
        },
        {
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
        }
    ],
    "total": "35.35"
}

invalid_receipt_missing_feild = {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "items": [
        {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
        },
        {
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
        },
        {
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
        },
        {
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
        },
        {
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
        }
    ],
    "total": "35.35"
},
        
invalid_receipt_misspelled_feild = {
    "retailers": "Target",
    "purchaseDate": "2022-01-01",
    "items": [
        {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
        },
        {
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
        },
        {
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
        },
        {
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
        },
        {
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
        }
    ],
    "total": "35.35"
},
        
invalid_receipt_misspelled_item_feild = {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "items": [
        {
            "shortDescriptio": "Mountain Dew 12PK",
            "price": "6.49"
        },
        {
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
        },
        {
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
        },
        {
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
        },
        {
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
        }
    ],
    "total": "35.35"
},


BASE_URL = "http://127.0.0.1:5002"

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        """Set up any shared resources for the tests."""
        self.client = requests

    # /receipt/process
    def test_post_points_valid_receipt(self):
        response = self.client.post(f'{BASE_URL}/receipt/process', json=valid_receipt)
        self.assertEqual(response.status_code, 200, "Expected 200 for valid receipt")

        json_data = response.json()
        self.assertIn("id", json_data, "Response JSON should contain 'id'")

    def test_post_points_invalid_receipt1(self):
        response = self.client.post(f'{BASE_URL}/receipt/process', json=invalid_receipt_missing_feild)
        self.assertEqual(response.status_code, 400, "Expected 400 for invalid data")

        json_data = response.json()
        self.assertIn("error", json_data, "Response JSON should contain 'error' for invalid data")

    def test_post_points_invalid_receipt2(self):
        response = self.client.post(f'{BASE_URL}/receipt/process', json=invalid_receipt_misspelled_feild)
        self.assertEqual(response.status_code, 400)

        json_data = response.json()
        self.assertIn("error", json_data)

    def test_post_points_invalid_receipt3(self):
        response = self.client.post(f'{BASE_URL}/receipt/process', json=invalid_receipt_misspelled_item_feild)
        self.assertEqual(response.status_code, 400)

        json_data = response.json()
        self.assertIn("error", json_data)

    # /receipt/{id}/process
    def test_get_points_valid(self):
        process_response = self.client.post(f'{BASE_URL}/receipt/process', json=valid_receipt)
        self.assertEqual(process_response.status_code, 200, "Expected 200 for valid receipt")

        process_json = process_response.json()
        receipt_id = process_json.get("id")
        self.assertIsNotNone(receipt_id, "Response should contain 'id' key")

        response = self.client.get(f'{BASE_URL}/receipt/{receipt_id}/points')
        self.assertEqual(response.status_code, 200)

        json_data = response.json()
        self.assertIn("points", json_data, "Response JSON should contain 'points'")
        self.assertEqual(json_data["points"], 109, "Expected points value to be 28")

    def test_get_points_invalid_id(self):
        invalid_id = "e81edc82-48e2-44f6-8979-invalid-id"
        response = self.client.get(f'{BASE_URL}/receipt/{invalid_id}/points')
        self.assertEqual(response.status_code, 404, "Expected 404 for invalid ID")

        json_data = response.json()
        self.assertIn("error", json_data, "Response JSON should contain 'error'")

if __name__ == '__main__':
    unittest.main()
