
# HA-Infrastructure Deployment instructions
This is a CDK stack that deploys a basic EKS cluster.

## Deploy via Docker
Build the docker image locally. (This image is also used for a Github Action)
```
$ docker build -t aws-cdk-action/python ./.github/actions/
```

Run the docker container to synthesize the templates
```
docker run --rm -v $(pwd):/workdir -e GITHUB_WORKSPACE=/workdir -e INPUT_CDK_COMMAND=synthesize aws-cdk-action/python
```

Deploy the stack to AWS (you must supply valid credentials via the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environmental variables)
```
docker run --rm -v $(pwd):/workdir -e GITHUB_WORKSPACE=/workdir -e INPUT_CDK_COMMAND=synthesize -e AWS_ACCESS_KEY_ID=<key> -e AWS_SECRET_ACCESS_KEY=<secret_key> aws-cdk-action/python
```

## Deploy using manual steps
Activate the python virtualenv
```
$ source .venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

Then to deploy the stack execute the following:
```
$ cdk deploy
```
(You must supply valid AWS credentials)

## Other commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation