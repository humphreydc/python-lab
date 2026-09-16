speed = float(input("Enter vehicle speed (km/ph): "))

if speed > 80:
    print(f"Warning: Speed limit exceeded! ({speed}km/ph) Fine issued.{"\n"}Speed radar system active.")
else:
    print("Drive safely, God bless!")