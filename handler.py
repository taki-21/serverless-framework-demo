def hello(event, context):
    body = {
        "plan_size": {
            "width": 3309.0,
            "height": 2339.0
        }
    }

    # body = {
    #     "message": "Go Serverless v3.0! Your function executed successfully!",
    #     "input": event,
    # }

    return {"statusCode": 200, "body": body}
