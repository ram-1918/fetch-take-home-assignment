from marshmallow import Schema, fields

class ItemSchema(Schema):
    """
    Item:
        type: object
        required:
            - shortDescription
            - price
    """
    shortDescription = fields.Str(required=True)
    price = fields.Str(required=True)

class ReceiptSchema(Schema):
    """
    Receipt:
    type: object
    required:
        - retailer
        - purchaseDate
        - purchaseTime
        - items
        - total
    """
    retailer = fields.Str(required=True)
    purchaseDate = fields.Str(required=True)
    purchaseTime = fields.Str(required=True)
    items = fields.List(fields.Nested(ItemSchema), required=True)
    total = fields.Str(required=True)