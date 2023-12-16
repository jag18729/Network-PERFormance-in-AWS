#!/bin/bash

# Path to the directory containing the Python script
SCRIPT_DIR="home/misunderst00d"

# Name of the Python script
PYTHON_SCRIPT="iperf3_test.py"

# AWS S3 bucket name
S3_BUCKET="your_s3_bucket_name"

# Run the Python script and get the output filename
RESULT_FILE=$(python3 $SCRIPT_DIR/$PYTHON_SCRIPT)

# Upload the result file to S3
aws s3 cp $SCRIPT_DIR/$RESULT_FILE s3://$S3_BUCKET/$RESULT_FILE
