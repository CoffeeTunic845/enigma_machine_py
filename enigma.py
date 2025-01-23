import tkinter as tk
from tkinter import Canvas

class EnigmaMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma Machine Simulator")
        self.create_widgets()
    
    def create_widgets(self):
        # Create a canvas for visualization
        self.canvas = Canvas(self.root, width=800, height=600, bg="lightgray")
        self.canvas.pack()
        
        # Keyboard buttons
        self.keyboard_frame = tk.Frame(self.root)
        self.keyboard_frame.pack()
        
        self.keys = {}
        key_layout = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        
        for row_index, row in enumerate(key_layout):
            frame = tk.Frame(self.keyboard_frame)
            frame.pack()
            for char in row:
                btn = tk.Button(frame, text=char, width=4, height=2, command=lambda c=char: self.on_key_press(c))
                btn.pack(side=tk.LEFT)
                self.keys[char] = btn
                
        # Display rotors
        self.rotor_labels = []
        for i in range(3):
            lbl = tk.Label(self.root, text=f"Rotor {i+1}: A")
            lbl.pack()
            self.rotor_labels.append(lbl)
    
    def on_key_press(self, char):
        print(f"Pressed: {char}")
        # Update rotors and simulate encryption (to be implemented)
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = EnigmaMachineGUI(root)
    root.mainloop()
