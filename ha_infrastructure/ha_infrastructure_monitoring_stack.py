from aws_cdk import core
import aws_cdk.aws_eks as eks

class HaInfrastructureMonitoringStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, cluster: eks.Cluster, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        eks.HelmChart(self, "loki-stack", 
            cluster=cluster,
            chart='loki-stack',
            repository='https://grafana.github.io/helm-charts',
            namespace='kube-system' ,
            values={
                "promtail": {
                    "enabled": True
                },
                "grafana": {
                    "enabled": True,
                    "persistence": {
                        "enabled": True
                    }
                },
                "prometheus": {
                    "enabled": True,
                    "alertmanager": {
                        "persistentVolume": {
                            "enabled": True,
                        },
                    },
                    "server": {
                        "persistentVolume": {
                            "enabled": True
                        },
                    },
                },
                "loki": {
                    "persistence": {
                        "enabled": True,
                        "size": "5Gi"
                    }
                }
            } 
        )