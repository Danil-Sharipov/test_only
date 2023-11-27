import docker

# Получите список всех контейнеров
containers = docker.from_env().containers.list()

# Проверьте, что все контейнеры запущены
for container in containers:
    if not container.status == "running":
        raise Exception("Container {} is not running".format(container.name))
else:
    if len(containers)!=3:
        raise Exception("Not all container exist")

# Выведите сообщение об успехе
print("All containers are up and running")