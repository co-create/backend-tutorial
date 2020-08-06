# Co-Create Backend

## Deployment
The `deploy` file is the controller for building the backend service in different deployment modes. It uses the different docker-compose files to run the Docker containers.

### Development
Run `./deploy dev` to create backend on machines with no NGINX/CertBot/Https protection.

### Production
Run `./deploy prod` to create backend on machines with NGINX/CertBot/Https protection.

### 
