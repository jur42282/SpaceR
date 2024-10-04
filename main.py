import customtkinter as tk
from tkinter import filedialog as fd

single_char_unbreakable = ['a', 'i', 'k', 'o', 's', 'u', 'v', 'z', 'A', 'I', 'K', 'O', 'S', 'U', 'V', 'Z']
unbreakable_char = "~" #Znak, který zastupuje nezlomitelnou mezeru

def main():
    menu.mainloop()

def single_char_detector(text):
    for c in single_char_unbreakable:
        text = text.replace(f' {c} ', f' {c}{unbreakable_char}')
        text = text.replace(f'{unbreakable_char}{c} ', f'{unbreakable_char}{c}{unbreakable_char}')
        text = text.replace(f'.{c}{unbreakable_char}', f'.{c}{unbreakable_char}')
    return text

def unbreakable():
    filename = select_text.cget("text")
    path = select_textp.cget("text")
    end = filename.split('.')[-1]
    # print(filename, path, end)
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            unbreakable_text = single_char_detector(text)
        
        with open(f'{path}/output.{end}', 'w', encoding='utf-8') as f:
            f.write(unbreakable_text)
        final_button.configure(text="Hotovo")
        final_button.configure(fg_color="green")
        final_button.configure(state="disabled")
    except Exception as e:
        print(e)
        final_button.configure(text="Chyba při zpracování")
        final_button.configure(fg_color="red")
        final_button.configure(state="disabled")
        
    

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('text files', '*.tex')
    )
    filename = fd.askopenfilename(
        title='Select a file',
        initialdir='/Downloads',
        filetypes=filetypes
        )
    select_text.configure(text=filename)
    final_button.configure(state="normal")
    return filename

def select_path():
    path = fd.askdirectory()
    select_textp.configure(text=path)
    return path

menu = tk.CTk()
menu.geometry("480x380")
menu.title("SpaceR")
menu.iconbitmap("spacericon.ico")

frame = tk.CTkFrame(menu, width=450, height=100)
frame.grid(row=0, column=0, padx=10, pady=0)
menu.grid_columnconfigure(0, weight=1)

main_label = tk.CTkLabel(frame, text="SpAceR", font=("SpaceX", 24))
main_label.grid(row=0, column=0, columnspan=2, pady=10, padx=150)

frame_select = tk.CTkFrame(menu, width=450, height=300)
frame_select.grid(row=1, column=0, padx=10, pady=20)

input_label = tk.CTkLabel(frame_select, text="Vstupní soubor", font=("Arial", 16, "bold"))
input_label.grid(row=0, column=0, columnspan=2, pady=10, padx=170)

select_text = tk.CTkLabel(frame_select, text="Vyberte soubor, který chcete upravit...", font=("Arial", 16))
select_text.grid(row=1, column=0, pady=10, padx=10)

file_select = tk.CTkButton(frame_select, text="Vyberte soubor", font=("Arial", 16), command=select_file)
file_select.grid(row=1, column=1, pady=10, padx=30, sticky="ew")


frame_selectp = tk.CTkFrame(menu, width=450, height=300)
frame_selectp.grid(row=2, column=0, padx=10, pady=20)

input_label = tk.CTkLabel(frame_selectp, text="Výstupní soubor", font=("Arial", 16, "bold"))
input_label.grid(row=0, column=0, columnspan=2, pady=10, padx=170)

select_textp = tk.CTkLabel(frame_selectp, text="Vyberte cestu, do které chcete soubor uložit", font=("Arial", 16))
select_textp.grid(row=1, column=0, pady=10, padx=5)

path_select = tk.CTkButton(frame_selectp, text="Vyberte cestu", font=("Arial", 16), command=select_path)
path_select.grid(row=1, column=1, pady=10, padx=5, sticky="ew")

final_button = tk.CTkButton(menu, text="Spustit", font=("Arial", 16), command=unbreakable, state="disabled")
final_button.grid(row=3, column=0, pady=10, padx=5, sticky="ew")

if __name__ == '__main__':
    main()

# Lukáš Jurák 2024