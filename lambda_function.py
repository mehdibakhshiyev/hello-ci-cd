import json
import logging

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        logger.info("Lambda execution started")
        logger.info(f"Request ID: {context.aws_request_id}")
        logger.info(f"Incoming event: {json.dumps(event)}")

        # Example logic
        result = {
            "message": "Lambda executed successfully in Github Actions",
            "request_id": context.aws_request_id
        }

        logger.info("Lambda execution completed successfully")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(result)
        }

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}", exc_info=True)

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Internal Server Error",
                "request_id": context.aws_request_id
            })
        }
