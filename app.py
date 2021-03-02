#!/usr/bin/env python3

from aws_cdk import core

from ha_infrastructure.ha_infrastructure_stack import HaInfrastructureStack
from ha_infrastructure.ha_infrastructure_monitoring_stack import HaInfrastructureMonitoringStack
from ha_infrastructure.ha_infrastructure_hello_world_stack import HaInfrastructureHelloWorldStack


app = core.App()
HaInfrastructureCluster = HaInfrastructureStack(app, "ha-infrastructure").cluster
HaInfrastructureMonitoringStack(app, "ha-infrastructure-monitoring", HaInfrastructureCluster)
HaInfrastructureHelloWorldStack(app, "ha-hello-world", HaInfrastructureCluster)

app.synth()
