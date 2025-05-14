import boto3

def create_user(username):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    return response

def attach_policy(username, policy_arn):
    iam = boto3.client('iam')
    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    return response
