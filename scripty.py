from unicodedata import name
import pyautogui
import keyboard
from PIL import ImageGrab
from PIL import _imaging
from datetime import date
from screeninfo import get_monitors


def conver_to_Hex(r, g, b):
    rr = ""
    gg = ""
    bb = ""
    if r <= 15:
        rr = 0
    if g <= 15:
        gg = 0
    if b <= 15:
        bb = 0
    return ('#{}{:X}{}{:X}{}{:X}').format(rr, r, gg, g, bb, b)


class funcoes:
    def __init__(self, x=1, y=""):
        self.x = x
        self.y = y

    def criarDados(self, pagina, TxPosX, TxPosY, TxRGB, TxHex, TxQtdTelas, TxData, TxColor):
        self.x, self.y = pyautogui.position()
        xt, yt = pyautogui.position()
        qtdTelas = 0
        for m in get_monitors():
            qtdTelas += 1
        while keyboard.is_pressed('q') == False:
            self.x, self.y = pyautogui.position()
            if (xt != self.x or yt != self.y):
                tela = ImageGrab.grab()  # Pega um print da tela
                area = tela.getpixel((self.x, self.y))  # Pega a cor do pixel (x,y)
                hexagerado = conver_to_Hex(area[0], area[1], area[2])
                xt = self.x
                yt = self.y
                data_atual = date.today()
                data_atual = data_atual.strftime('%d/%m/%Y')

                # alimentando as caixas
                TxPosX.delete(0, 'end')
                TxPosX.insert(0, self.x)
                TxPosY.delete(0, 'end')
                TxPosY.insert(0, self.y)
                TxRGB.delete(0, 'end')
                TxRGB.insert(0, area)
                TxHex.delete(0, 'end')
                TxHex.insert(0, hexagerado)
                TxColor.config(background=hexagerado)
                TxQtdTelas.delete(0, 'end')
                TxQtdTelas.insert(0, qtdTelas)
                TxData.delete(0, 'end')
                TxData.insert(0, data_atual)
                pagina.update()
