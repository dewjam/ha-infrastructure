#!/usr/bin/env python3

from aws_cdk import core

from ha_infrastructure.ha_infrastructure_stack import HaInfrastructureStack


app = core.App()
HaInfrastructureStack(app, "ha-infrastructure").cluster

app.synth()
