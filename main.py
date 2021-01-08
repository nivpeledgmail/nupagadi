import tkinter as tk
import ImageTk

FILENAME = "res/image1.jpg"


class Game:
    def start(self):
        pass

if __name__ == '__main__':
    root = tk.Tk()

    root.title("Nu Pagadi")
    canvas = tk.Canvas(root)
    canvas.pack(fill="both", expand=True)

    tk_img = ImageTk.PhotoImage(file=FILENAME)
    print(tk_img.height(), tk_img.width())

    canvas.create_image(10, 10, image=tk_img, anchor='nw')

    quit_button = tk.Button(root, text="PLAY!", command=Game.start, anchor='w',
                            width=10, activebackground="#33B5E5")
    quit_button_window = canvas.create_window(10, 10, anchor='nw', window=quit_button)

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))

    root.mainloop()
