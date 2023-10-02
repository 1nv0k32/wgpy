# WireGuard management API

## RoadMap
- DB design
- Auth for endpoints
- Create basic Wireguard server
- Generate Wireguard client configs (wg-quick/QR)
- Manage current connections on the system and report
- End2End test using vagrant (Test worker container with linux cap/non-containerized worker)
- Detect IP collisions and default GW
- Configure Firewall and NAT
- Task management and revert
- Advanced routing?


## Requirements
- python >= 3.11
- poetry


## Prepare dev environment
```sh
$ poetry install --sync --with dev --with nox
```

## Run test automation
```sh
$ nox
```


## Run the application
```sh
$ docker-compose up --detach --build
$ xdg-open http://localhost:8888/docs
```
