import sys
import os
import subprocess
import shutil
import boto3

# Constants
S3_BUCKET = 'S3_BUCKET'
LAYER_DIR = '/tmp/python'
ZIP_FILE = '/tmp/python_layer.zip'
S3_KEY = 'lambda-layers/python_layer.zip'

# Clean up any previous runs
def lambda_handler(event, context):
    if os.path.exists(LAYER_DIR):
        shutil.rmtree(LAYER_DIR)
    if os.path.exists(ZIP_FILE):
        os.remove(ZIP_FILE)

    # Create directory for the layer
    os.makedirs(LAYER_DIR)

    # Install Pillow in the specified directory
    layers = ['pillow', 'numpy']
    for layer in layers:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', layer, '-t', LAYER_DIR])

    # Zip the contents of the directory
    shutil.make_archive('/tmp/python_layer', 'zip', '/tmp', 'python')

    # Upload the zip file to S3
    s3_client = boto3.client('s3')
    s3_client.upload_file(ZIP_FILE, S3_BUCKET, S3_KEY)

    print(f'Uploaded {ZIP_FILE} to s3://{S3_BUCKET}/{S3_KEY}')
