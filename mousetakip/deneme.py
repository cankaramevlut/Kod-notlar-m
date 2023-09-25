import pyautogui
import keyboard
from pynput.mouse import Listener

tiklanan_konumlar = []
dongu = 0

def dongusayisial():
    global dongu  # dongu değişkenini global olarak işaretleyin
    dongu = int(input("kaç dongu olacak: "))

def fare_tiklama(x, y, tus, basili):
    if basili:
        print(f"Tıklanan konum: x={x} y={y}")
        tiklanan_konumlar.append((x, y))

def klavye_tusuna_basildi(e):
    print(len(tiklanan_konumlar))
    temp = 0
    if e.name == 'a':
        print("Tıklama işlemi başlıyor...")
        for konum in tiklanan_konumlar:
            
            if temp == dongu:
                break
            pyautogui.click(konum[0], konum[1], duration=0.5)
            temp = temp+(1/2)

dongusayisial()
keyboard.on_press(klavye_tusuna_basildi)

# Fare tıklama olaylarını dinlemek için Listener'ı başlat
with Listener(on_click=fare_tiklama) as fare_dinleyici:
    # Fare tıklama olaylarını dinlemeyi sürdür
    fare_dinleyici.join()
