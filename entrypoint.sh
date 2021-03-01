#!/bin/sh

function runCDK() {
    echo "Running CDK command $INPUT_CDK_COMMAND"

    case $INPUT_CDK_COMMAND in
        diff)
            cdk diff $INPUT_CDK_STACK;;
        synthesize)
            cdk synth $INPUT_CDK_STACK;;
        deploy)
            cdk deploy $INPUT_CDK_STACK;;
        *)
            echo "Command is not valid.  Please use one of 'diff', 'synthesize', or 'deploy'."
    esac
}

function setup() {
    cd ${GITHUB_WORKSPACE}

    if [ -e "requirements.txt" ]; then
        echo "Activating Python Environment..."
        python3 -m venv .venv
        source .venv/bin/activate
        echo "Installing Python Packages.."
        pip install -r requirements.txt
    else 
        echo "No CDK Stacks exist in this repository.. skipping setup..."
    fi
}

function main() {
    setup
    runCDK
}

main