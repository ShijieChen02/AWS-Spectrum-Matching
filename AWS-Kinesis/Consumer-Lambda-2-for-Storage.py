def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data']).decode("UTF-8")
        formattedPayload = json.loads(payload)


        s3_cli = boto3.client('s3')
        bucket_name = 'your-storage-path'#different from the distance storage
        current_time = datetime.utcnow()
        object_key = f"{current_time.year}/{current_time.month}/{current_time.day}/{str(current_time)}.json"

        body = json.dumps(formattedPayload, indent=2)
        try:
            response = s3_cli.put_object(Body=body,Bucket = bucket_name, Key = object_key)
            logging.info("Successfully uploaded to {bucket_name}/{object_key}!")
            logging.info(f"response : {response}")
        except Exception as e:
            logging.error(f"Error in uploading to S3 : {e}")
