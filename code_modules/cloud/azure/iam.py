def set_iam_permissions(user_name, policy_arn, cloud_platform):

    iam_client = boto3.client('iam')
    
    try:
        response = iam_client.attach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )
        print(f"Successfully attached policy {policy_arn} to user {user_name}.")
        return response
        
    except ClientError as e:
        print(f"An error occurred: {e}")
        return None
