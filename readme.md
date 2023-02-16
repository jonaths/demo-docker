# Ejemplo mínimo Docker

Crear imagen: `docker build -t docker-demo -f Dockerfile` 

Correr contenedor: `docker run -d -t --name docker-demo-container docker-demo:latest`

Correr tests: `docker exec -it docker-demo-container python test_basic.py`

Correr comando: `docker exec -it docker-demo-container python cmd_sum.py --val1 2 --val2 5`