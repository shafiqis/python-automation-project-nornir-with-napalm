import json
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get

# Initialize Nornir
nr = InitNornir(config_file="config.yaml")

# Define a task to retrieve data using NAPALM
def get_router_data(task):
    result = task.run(task=napalm_get, getters=["facts", "interfaces"])
    # Convert result to JSON and print
    print(f"Data for {task.host.name}:")
    print(json.dumps(result.result, indent=4))

# Run the task
nr.run(task=get_router_data)
