import tkinter as tk
import random
import time
import threading




class window(tk.Frame):

    

    def __init__( self ):
        self.clickx = 1
        self.clicks = 0
        self.bought1 = 0
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Clicker")
        self.canvas = tk.Canvas(self , width=300, height=300)
        self.grid = tk.Grid()
        self.button1 = tk.Button( self.canvas, text = "CLICK ME", width = 25,
                               command = self.click )    
        self.button1.pack(side= tk.TOP)    
        
        self.clickcounter = tk.Text(self.canvas , height=20, width=40) 
        self.log = tk.Text(self.canvas, height= 9, width= 40, background= "red")
        rudolf = tk.PhotoImage(file="Rudolf.png", height=200, width=200)
        self.img = tk.Label(self.canvas, image=rudolf)   
        self.img.image = rudolf
        self.img.pack()   
        self.clickcounter.pack()
        self.log.pack()

        self.afkbuy = tk.Button(self.canvas ,text = "Buy AFK+1 for 50", width = 25,
                               command = self.buy1 )
        self.afkbuy.pack()
        self.clickbuy = tk.Button(self.canvas, text = "Buy a Click Boost of 1 for 25", width= 25, command = self.boost)
        self.clickbuy.pack()
        
        self.canvas.pack()

        x = threading.Thread(target=self.passiv, daemon=True)
        x.start()  
        self.logging("Programm started")   


    def refresh_clickcounter(self):
        self.clickcounter.delete('1.0', tk.END)
        self.clickcounter.insert(tk.END, str(self.clicks) + "\n" + str(self.bought1)+ " Passiv Clicks")


    def click(self):
        self.clicks += self.clickx
        self.refresh_clickcounter()
        print(self.clicks)
    
    def buy1(self):
        if self.clicks >= 50:
            self.clicks -= 50            
            self.bought1 += 1
            self.refresh_clickcounter()
            self.logging("Bought 1 Passiv")
    
    def passiv(self):        
        while True:
            self.clicks += self.bought1
            self.refresh_clickcounter()
            time.sleep(5)

    def logging(self, logged):
        self.log.insert(tk.END, "\n" + str(logged))
        self.log.see("end")
    
    def boost(self):
        if self.clicks >= 25:
            self.clicks -=25
            self.clickx += 1
            self.refresh_clickcounter()
            self.logging(("Clicks are now worth " + str(self.clickx)))

def main():
    window().mainloop()




if __name__ == '__main__':
    main()
    #window.logging(window, "Programm started")



#self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = tk.W+tk.E+tk.N+tk.S )
#self.clickcounter.grid( row = 0, column = 1, columnspan = 2, sticky = tk.W+tk.E+tk.N+tk.S )
