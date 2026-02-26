def add_setting (setting_dic, key_val_tup):
    key1 = key_val_tup[0].lower()
    value1 = key_val_tup[1].lower()
    if key1 in setting_dic.keys():
        return (f"Setting '{key1}' already exists! Cannot add a new setting with this name.")
    else: 
        setting_dic[key1] = value1
        return (f"Setting '{key1}' added with value '{value1}' successfully!")
def update_setting (setting_dic, key_val_tup):
    key = key_val_tup[0].lower()
    value = key_val_tup[1].lower()
    if key in setting_dic.keys():
        setting_dic[key] = value
        return (f"Setting '{key}' updated to '{value}' successfully!")
    else:
        return (f"Setting '{key}' does not exist! Cannot update a non-existing setting.")

def delete_setting (setting_dic, key):
    key1 = key.lower()
    if key1 in setting_dic.keys():
        del setting_dic[key1]
        return (f"Setting '{key1}' deleted successfully!")
    else:
        return ("Setting not found!")

def view_settings (setting_dic):
    if setting_dic == {}:
        return ("No settings available.")
    else:
        s = "Current User Settings:\n"
        for key,value in setting_dic.items():
            s += key.capitalize() + ": "+value +"\n"
        return s
test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}