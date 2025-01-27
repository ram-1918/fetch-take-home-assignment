import uuid

def generate_uuid():
    # This function geneates a universally unique indentifier version 4, 
    # which is made up of 32 hexadecimal character in 5 groups
    # for example, "7fb1377b-b223-49d9-a31a-5a02701dd310"
    return uuid.uuid4()