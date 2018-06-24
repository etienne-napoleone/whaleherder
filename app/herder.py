import logging
import docker

_log = logging.getLogger('whaleherder')
_docker = docker.from_env()


def ping() -> bool:
    try:
        return _docker.ping()
    except docker.errors.APIError as e:
        _log.error('Could not communicate with Docker')
        _log.debug(e)
        return False


def get_services() -> dict:
    try:
        services = {}
        for service in _docker.services.list():
            services[service.name] = service.id
        return services
    except docker.errors.APIError as e:
        _log.error('Could not communicate with Docker')
        _log.debug(e)
        return False


def _get_service(name):
    services = get_services()
    if name in services.keys():
        try:
            return _docker.services.get(services[name])
        except docker.errors.APIError as e:
            _log.error('Could not communicate with Docker')
            _log.debug(e)
            return False
    else:
        return False


def reload(name) -> bool:
    service = _get_service(name)
    if not service:
        _log.error(f'Service {name} seems to have vanished')
        return False
    try:
        service.update()
        return True
    except docker.errors.APIError as e:
        _log.error('Could not communicate with Docker')
        _log.debug(e)
        return False
