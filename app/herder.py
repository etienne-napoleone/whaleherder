import docker

_docker = docker.from_env()


def init():
    try:
        _docker.swarm.init()
    except docker.errors.APIError as e:
        pass


def ping() -> bool:
    try:
        return _docker.ping()
    except docker.errors.APIError as e:
        return False


def get_services() -> dict:
    try:
        services = {}
        for service in _docker.services.list():
            services[service.name] = service.id
        return services
    except docker.errors.APIError as e:
        return False


def get_service(name):
    services = get_services()
    if name in services.keys():
        try:
            return _docker.services.get(services[name])
        except docker.errors.APIError as e:
            return False
    else:
        return False


def reload(name) -> bool:
    try:
        get_service(name).update()
        return True
    except docker.errors.APIError as e:
        return False
