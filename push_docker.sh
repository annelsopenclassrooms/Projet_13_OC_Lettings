#!/bin/bash

# Exit immediately if a command fails
set -e

# Variables
USERNAME="annels"
REPO="oc-lettings-site"
TAG="latest"
GIT_HASH=$(git rev-parse --short HEAD)

# Build Docker image
echo "🔨 Building Docker image..."
docker build -t $REPO:$TAG .

# Tag images
echo "🏷️  Tagging images..."
docker tag $REPO:$TAG $USERNAME/$REPO:$TAG
docker tag $REPO:$TAG $USERNAME/$REPO:$GIT_HASH

# Push images
echo "📤 Pushing images to Docker Hub..."
docker push $USERNAME/$REPO:$TAG
docker push $USERNAME/$REPO:$GIT_HASH

echo "✅ Done! Images available as:"
echo "   - $USERNAME/$REPO:$TAG"
echo "   - $USERNAME/$REPO:$GIT_HASH"
