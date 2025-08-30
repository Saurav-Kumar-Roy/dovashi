import time
import pyperclip
import mouse
import pyautogui
import asyncio
import keyboard
from googletrans import Translator
from plyer import notification

translator = Translator()
last_text = ""

# Create a single event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def get_translation(text):
    try:
        translation = await translator.translate(text, dest="bn")
        return translation.text
    except Exception as e:
        print("Translation error:", e)
        return None

print("Background translator running... Select text with your mouse to see Bengali meaning.", flush=True)

while True:
    if keyboard.is_pressed("t"):  
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.3)

        text = pyperclip.paste().strip()
        if text and text != last_text:
            last_text = text
            try:
                meaning = loop.run_until_complete(get_translation(text))
                if meaning:
                    notification.notify(
                        title="Bengali Meaning",
                        message=f"{text} → {meaning}",
                        timeout=4
                    )
            except Exception as e:
                print(f"Error: {e}", flush=True)

    time.sleep(0.1)
