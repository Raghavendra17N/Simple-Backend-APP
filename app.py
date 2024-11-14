from google.cloud import storage
from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import os
app = Flask(__name__)

project_id = os.getenv("project")
bucket_name = os.getenv("gcs_bucket")
CORS(app)
@app.route('/api/generate-signed-url', methods=['POST'])
def generate_signed_url():
    bucket_name = bucket_name 
    file_name = request.json.get('fileName')

    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    url = blob.generate_signed_url(
        version="v4",
        expiration=datetime.timedelta(minutes=15),  # Set expiration time for the URL
        method="PUT",
        content_type="application/octet-stream"  # Use appropriate content type
    )

    return jsonify({'url': url})

if __name__ == '__main__':
    app.run()
