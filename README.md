# FastAPI + AWS (Lambda, DynamoDB, Cognito, CloudFront) + GitHub Actions + Serverless Framework

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

- Serverless FastAPI APIs running on AWS Lambda
- DynamoDB as the main database
- Deployment to AWS Lambda using CI/CD on GitHub Actions and Serverless Framework
- Cognito for authentication inside the APIs
- Backend FastAPI API | Frontend Vue
- Vue applications deployed to AWS S3
- Cognito for authentication inside the Vue application
- Applications served with CloudFront CDNs on custom domains
- Monitoring and alerting with CloudWatch

This is a simple app created to get familiar with FastAPI integrated on AWS Serverless Technologies.

## Development

This app aims to follow Test Driven Development (TDD) principles. The tests are written using Pytest.

## Stack

- [Serverless Framework](https://www.serverless.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Vue](https://vuejs.org/)
- [DynamoDB](https://aws.amazon.com/dynamodb/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Cognito](https://aws.amazon.com/cognito/)
- [AWS API Gateway](https://aws.amazon.com/api-gateway/)
- [AWS S3 bucket](https://aws.amazon.com/s3/)
- [GitHub Actions](https://github.com/features/actions)
- [Pytest](https://docs.pytest.org/en/stable/)
