import time
import winsound

def set_alarm():
    alarm_time = input("Define la alarma en HH:MM formato: ")
    return alarm_time

def play_alarm_sound():
    duration = 1000  # milliseconds
    frequency = 440  # Hz (A4 note)
    winsound.Beep(frequency, duration)

def main():
    print("Bienvenido a tu alarma!")
    alarm_time = set_alarm()

    while True:
        current_time = time.strftime("%H:%M")
        
        if current_time == alarm_time:
            print("Buenos dias Dormilon!")
            play_alarm_sound()
            break
        
        time.sleep(60)  # Check the time every minute

if __name__ == "__main__":
    main()
