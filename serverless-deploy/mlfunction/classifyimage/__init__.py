import logging

import azure.functions as func
import json

# Import helper script
from .predict import predict_image_from_url

def main(msg: func.QueueMessage) -> str:
    image_url = msg.get_body().decode('utf-8')
    results = predict_image_from_url(image_url)
    logging.info(f"{results['predictedTagName']} {image_url}")
    return json.dumps({
        'target': 'newResult',
        'arguments': [{
            'predictedTagName': results['predictedTagName'],
            'url': image_url
        }]
    })