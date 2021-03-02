from aws_cdk import core
import aws_cdk.aws_eks as eks
import aws_cdk.aws_ecr as ecr

class HaInfrastructureHelloWorldStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, cluster: eks.Cluster, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repository = ecr.Repository(self, "ha-hello-world",
            image_scan_on_push=True
        )