#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="${IMAGE_NAME:-devops-demo}"
IMAGE_TAG="${IMAGE_TAG:-local}"

docker build -f docker/Dockerfile -t "${IMAGE_NAME}:${IMAGE_TAG}" .
echo "Built ${IMAGE_NAME}:${IMAGE_TAG}"
