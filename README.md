# Net worth simulation

## Quickstart (Docker)

### Prerequisites
- Docker Desktop installed and running
- Docker Compose v2 available (`docker compose version`)

### First-time setup
```bash
cp .env.example .env
make dev
```

API will be available at: http://localhost:8000/health


### Stop everything
```make down```

### Common commands
```Start (build + run)  make dev```

### Stop (and remove containers + volumes)
```make down```

### View logs
```make logs```

### Run API tests
```make test```

### Apply DB migrations
```make migrate```

### Create a new migration (autogenerate)
```make makemigrations MSG="describe change"```

### Format / lint (API container)
```
make fmt
make lint
```

### Troubleshooting
Docker not running / compose not found

Ensure Docker Desktop is running:

```
open -a Docker
docker compose version
```

Ports already in use

If you already have services using these ports, stop them or change ports in docker-compose.yml:

Postgres: 5432

Redis: 6379

API: 8000