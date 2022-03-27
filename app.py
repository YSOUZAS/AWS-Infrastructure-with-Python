#!/usr/bin/env python3

import aws_cdk as cdk

from aws_infrastructure_with_python.aws_infrastructure_with_python_stack import AwsInfrastructureWithPythonStack


app = cdk.App()
AwsInfrastructureWithPythonStack(app, "aws-infrastructure-with-python")

app.synth()
