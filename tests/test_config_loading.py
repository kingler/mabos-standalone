import yaml
import os

def load_config(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    
    # Debugging: Print the configuration
    print("Loaded configuration:", config)
    
    # Check if 'llms' key exists in the config
    if 'llms' not in config:
        raise KeyError("'llms' key not found in the configuration file")
    
    return config

if __name__ == "__main__":
    config_path = '/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/config/llm_config.yaml'  # Update this path to the correct location
    try:
        config = load_config(config_path)
        print("Configuration loaded successfully.")
    except Exception as e:
        print(f"Error: {e}")


