# Co-Create Backend Tutorial

## Deployment
The `deploy.sh` file is the controller for building the backend service in different deployment modes. It uses the different docker-compose files to run the Docker containers.

### Development
Run `./deploy.sh dev` to create backend on machines with no NGINX/CertBot/Https protection.

### Production
Run `./deploy.sh prod` to create backend on machines with NGINX/CertBot/Https protection.

### Logging
Run `./deploy.sh logs {dev|prod}` to follow your containers' logs.
Run `./deploy.sh {dev|prod} -f` to follow your containers' logs during build.
