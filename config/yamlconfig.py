import yaml

# Load YAML configuration
with open('./application.yaml', 'r') as file:
    config = yaml.safe_load(file)

print(config)
