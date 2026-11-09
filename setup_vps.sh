
#!/usr/bin/env bash
set -Eeuo pipefail

# Использование:
# ./setup_vps.sh https://github.com/USERNAME/REPOSITORY.git

REPO_URL="${1:-}"
PROJECT_DIR="/opt/colizeum"

if [[ -z "$REPO_URL" ]]; then
    echo "Usage: $0 <public-git-repository-url>"
    exit 1
fi

if [[ ! -f /etc/os-release ]]; then
    echo "Cannot identify operating system."
    exit 1
fi

source /etc/os-release

if [[ "$ID" != "ubuntu" || "$VERSION_ID" != "24.04" ]]; then
    echo "This script supports Ubuntu 24.04 only."
    exit 1
fi

echo "==> Updating packages..."
sudo apt-get update
sudo apt-get install -y ca-certificates curl git

echo "==> Adding Docker repository..."
sudo install -m 0755 -d /etc/apt/keyrings

sudo curl -fsSL \
    https://download.docker.com/linux/ubuntu/gpg \
    -o /etc/apt/keyrings/docker.asc

sudo chmod a+r /etc/apt/keyrings/docker.asc

sudo tee /etc/apt/sources.list.d/docker.sources > /dev/null <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: ${UBUNTU_CODENAME:-$VERSION_CODENAME}
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

echo "==> Installing Docker..."
sudo apt-get update

sudo apt-get install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin

echo "==> Enabling Docker..."
sudo systemctl enable --now docker

echo "==> Cloning project..."

if [[ -e "$PROJECT_DIR" ]]; then
    echo "Directory already exists: $PROJECT_DIR"
    echo "Refusing to overwrite existing project."
    exit 1
fi

sudo install -d -o "$USER" -g "$(id -gn)" "$PROJECT_DIR"

git clone "$REPO_URL" "$PROJECT_DIR"

cd "$PROJECT_DIR"

if [[ ! -f compose.yaml && ! -f compose.yml && \
      ! -f docker-compose.yaml && ! -f docker-compose.yml ]]; then
    echo "Compose file not found in project root."
    exit 1
fi

echo
echo "==> Setup completed!"
echo "Project directory: $PROJECT_DIR"
echo
echo "Next steps:"
echo "1. Create $PROJECT_DIR/.env"
echo "2. Check your Docker Compose configuration."
echo "3. Start the project."
echo
echo "Docker version:"
sudo docker --version
sudo docker compose version
