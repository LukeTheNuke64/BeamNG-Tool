import json, os
from pathlib import Path

def info(message):
       print("[INFO] " + message) 

def error(message):
      print("[ERROR] " + message) 

def clear():
    os.system('cls')

info("Updating player money and XP!")

def update_player():
    base_path = Path(os.getenv("LOCALAPPDATA")) / "BeamNG.drive/0.34/settings/cloud/saves"
    profiles = ["Profile 1", "Profile 2"]
    autosaves = [f"autosave{i}" for i in range(1, 11)]  # autosave1 to autosave10
    updated_count = 0

    for profile in profiles:
        for autosave in autosaves:
            file_path = base_path / profile / autosave / "career/playerAttributes.json"
            
            try:
                if not file_path.exists() or file_path.stat().st_size == 0:
                    continue
                
                with file_path.open('r', encoding="utf-8") as file:
                    data = json.load(file)

                if not isinstance(data, dict):
                    clear()
                    error(f"Error in {file_path}: json structure invalid or corrupted")
                    continue
                
                updated = False
                
                if "money" in data and "value" in data["money"]:
                    data["money"]["value"] = 9999999
                    updated = True

                if "beamXP" in data and "level" in data["beamXP"]:
                    data["beamXP"]["level"] = 100
                     updated = True
                
                if updated:
                    with file_path.open('w', encoding="utf-8") as file:
                        json.dump(data, file, indent=4)
                    updated_count += 1
                
            except json.JSONDecodeError as e:
                clear()
                error(e)
            except PermissionError:
                clear()
                error("An error occured, make sure the process has correct permissions")
            except Exception as e:
                clear()
                error(e)

    if updated_count == 0:
        clear()
        error("Couldn't find any files to update!")
    else:    
        info("Done!")
        info(f"Total files updated: {updated_count}")


if __name__ == "__main__":
    update_player()
    input()
