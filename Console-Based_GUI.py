# Console-based cheat GUI
def activate_feature(feature_name):
    print(f"{feature_name} Activated")

def deactivate_feature(feature_name):
    print(f"{feature_name} Deactivated")

print(r'''
 .dP"Y8 88""Yb  dP"Yb   dP"Yb  88  dP 
`Ybo." 88__dP dP   Yb dP   Yb 88odP  
o.`Y8b 88"""  Yb   dP Yb   dP 88"Yb  
8bodP' 88      YbodP   YbodP  88  Yb   v1.0.3 console-based 

===========================================================
''')

print("Available Features:")
features = ["ESP", "Wallhack", "Aimbot", "Auto Trigger", "Speed Hack", "God Mode", "No Recoil"]
for idx, feature in enumerate(features, start=1):
    print(f"{idx}. {feature}")

selected_features = []
while True:
    choice = input("Select a feature number to activate or 'done' to finish: ")
    if choice.lower() == 'done':
        break
    try:
        feature_idx = int(choice) - 1
        if feature_idx < 0 or feature_idx >= len(features):
            print("Invalid feature number. Please try again.")
            continue
        selected_feature = features[feature_idx]
        if selected_feature in selected_features:
            print(f"{selected_feature} is already activated.")
        else:
            selected_features.append(selected_feature)
            activate_feature(selected_feature)
    except ValueError:
        print("Invalid input. Please enter a feature number or 'done'.")

print("\nSelected Features:")
for feature in selected_features:
    print(feature)

print("\nCheat GUI configuration completed.")
