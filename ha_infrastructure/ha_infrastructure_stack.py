from aws_cdk import core
import aws_cdk.aws_eks as eks


class HaInfrastructureStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.cluster = eks.Cluster(self, "ha-infra",
            version=eks.KubernetesVersion.V1_19,
            output_config_command=True
        )
