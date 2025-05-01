import os
import json
from pathlib import Path

def get_folder_structure(root_dir, base_path=""):
    """
    Recursively builds a list of dictionaries representing the folder structure
    Each folder has a path and an empty purpose field
    """
    structure = []
    
    # Get all items in the current directory
    items = os.listdir(root_dir)
    
    for item in items:
        item_path = os.path.join(root_dir, item)
        
        # Skip hidden files and directories
        if item.startswith('.'):
            continue
            
        # Skip if it's a file
        if os.path.isfile(item_path):
            continue
            
        # If it's a directory, add it to the structure
        if os.path.isdir(item_path):
            # Create the full path
            full_path = os.path.join(base_path, item) if base_path else item
            
            # Add the current folder
            structure.append({
                "path": full_path,
                "purpose": ""
            })
            
            # Recursively get subfolders
            subfolders = get_folder_structure(item_path, full_path)
            structure.extend(subfolders)
            
    return structure

def main():
    # Get the Obsidian vault path from config
    import config
    
    if not hasattr(config, 'inbox_path'):
        print("Error: config.inbox_path is not defined")
        return
        
    vault_path = os.path.dirname(config.inbox_path)
    
    if not os.path.exists(vault_path):
        print(f"Error: Vault path {vault_path} does not exist")
        return
        
    print(f"Generating structure for vault at: {vault_path}")
    
    # Generate the structure
    structure = get_folder_structure(vault_path)
    
    # Sort the structure by path
    structure.sort(key=lambda x: x["path"])
    
    # Save to structure.json
    with open('structure.json', 'w', encoding='utf-8') as f:
        json.dump(structure, f, indent=4, ensure_ascii=False)
        
    print("Structure saved to structure.json")

if __name__ == "__main__":
    main() 