import argparse
from access_manager import decision_engine, aws_iam, config, logger

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True)
    parser.add_argument("--geo", default="US")
    parser.add_argument("--risk", default="low")
    args = parser.parse_args()

    user_context = {
        "username": args.user,
        "geo": args.geo,
        "risk": args.risk
    }

    decision = decision_engine.evaluate_access(user_context)
    logger.log_event(f"Access decision for {args.user}: {decision}")

    if decision == "ALLOW":
        aws_iam.create_user(args.user)
        aws_iam.attach_policy(args.user, config.DEFAULT_POLICY_ARN)
        print(f"User {args.user} created with default policy.")
    else:
        print(f"Access denied for user {args.user}.")

if __name__ == "__main__":
    main()
