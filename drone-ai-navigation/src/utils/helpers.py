def load_config(config_file):
    import json
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def save_results(results, output_file):
    import json
    with open(output_file, 'w') as file:
        json.dump(results, file, indent=4)