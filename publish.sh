#!/bin/bash
BINARY_NAME=data-scraper
DOCKER_REGISTRY=groupddevops/
VERSION=$(git rev-parse --short HEAD)

echo "tagging"
docker tag $BINARY_NAME $DOCKER_REGISTRY$BINARY_NAME:latest
docker tag $BINARY_NAME $DOCKER_REGISTRY$BINARY_NAME:$VERSION

# Push the docker images
echo "Pushing: " $DOCKER_REGISTRY$BINARY_NAME:latest
docker push $DOCKER_REGISTRY$BINARY_NAME:latest
echo "Pushing: " $DOCKER_REGISTRY$BINARY_NAME:$VERSION
docker push $DOCKER_REGISTRY$BINARY_NAME:$VERSION

echo "Published: " $DOCKER_REGISTRY$BINARY_NAME:latest
echo "Published: " $DOCKER_REGISTRY$BINARY_NAME:$VERSION

