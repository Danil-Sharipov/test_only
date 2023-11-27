import docker

containers = docker.from_env().containers.list()

for i in containers:
    # != jupyter
    if i.name != "jupyter":
        exit_code,output = i.exec_run("pip install pyspark",user='0')
        if exit_code != 0:
            raise Exception("pyspark can't be install")

        #########
        # code
        for j in ['autoscale.py','decommissioning.py','decommissioning_cleanup.py','py_container_checks.py','python_executable_check.py']:
            temp = 'python3 /opt/spark/tests/'+j
            exit_code,output = i.exec_run(temp,user='0')
            if exit_code!=0:
                print(output)
                raise Exception(f"{j} can't be run")

        #########
        exit_code,output = i.exec_run("pip uninstall --yes pyspark",user='0')
        if exit_code != 0:
            print(output)
            raise Exception("pyspark can't be uninstall")