import yaml, json
from yaml.loader import SafeLoader



def readConfig(config_file="share/configuration_test.yaml"):
    with open(config_file) as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data

def getData(hosts_file="share/plates.json"):
    with open(hosts_file) as json_file:
        obj = json.load(json_file)
    return obj