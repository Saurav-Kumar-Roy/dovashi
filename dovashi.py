from pynput import mouse, keyboard
import pyperclip
import time
import asyncio
from googletrans import Translator
from plyer import notification

kb = keyboard.Controller()
translator = Translator()
last_text = ""

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def get_translation(text):
    try:
        translation = await translator.translate(text, dest="bn")
        return translation.text
    except Exception as e:
        print("Translation error:", e)
        return None


def on_click(x, y, button, pressed):
    global last_text
    # Detect mouse release (end of selection)
    if not pressed and button == mouse.Button.left:
        # Send Ctrl+C
        with kb.pressed(keyboard.Key.ctrl):
            kb.press('c')
            kb.release('c')
        time.sleep(0.2)  # wait for clipboard update
        text = pyperclip.paste()
        if text and text != last_text:
            last_text = text
            try:
                meaning = loop.run_until_complete(get_translation(text))
                if meaning:
                    notification.notify(
                        title="Bengali Meaning",
                        message=f"{text} → {meaning}",
                        timeout=2
                    )
            except Exception as e:
                print(f"Error: {e}")

with mouse.Listener(on_click=on_click) as listener: 
    listener.join()
