import screeninfo as screen
import PySimpleGUI as sg
c = 0

print(screen.get_monitors()[0], type(screen.get_monitors()[0]))
for m in screen.get_monitors():
    c+= 1
    print(m.width)
    print(f"Monitor {c}: {str(m)}")


sg.popup("TESTING FONTS", font='Arial 16,5')
