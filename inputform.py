import csv
import customtkinter as ctk

FONT_TYPE = "meiryo"
DIM_DIR = '../dimension.csv'
VARIABLES = [
    '植栽密度(本/ha)', '下刈り省力化',
    # '下刈り開始齢(年生)', '下刈り終了齢(年生)',
    # '除伐齢(年生)', '除伐率',
    # '初回間伐齢(年生)', '初回間伐率',
    # '2回目間伐齢(年生)', '2回目間伐率',
    # '伐採齢(年生)'
             ]


class MyScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, fonts, dims, variables):
        super().__init__(master, width=1200, height=500, label_text=title, label_font=fonts)
        self.fonts = fonts
        self.grid_columnconfigure(0, weight=1)
        self.dims = dims
        self.variables = variables
        self.create_widgets()

    def create_widgets(self):
        for k, dim in enumerate(self.dims):
            land_label = ctk.CTkLabel(master=self, text=dim, font=self.fonts)
            land_label.grid(row=k+1, column=0, padx=10, pady=(10,0), sticky="w")

        for k, var in enumerate(self.variables):
            type_label = ctk.CTkLabel(master=self, text=var, font=self.fonts)
            type_label.grid(row=0, column=k+1, padx=10, pady=(10,0), sticky="w")

        self.textboxes = []
        for i in range(len(self.variables)):
            row_textboxes = []
            for j in range(len(self.dims)):
                textbox = ctk.CTkEntry(master=self, width=100, font=self.fonts)
                textbox.grid(row=j+1, column=i+1, padx=10, pady=(10,0), sticky="w")
                textbox.insert(0, 60)  # Default value
                row_textboxes.append(textbox)
            self.textboxes.append(row_textboxes)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.fonts = (FONT_TYPE, 15)
        self.geometry("1500x800")
        self.title("Forestry params settings")
        self.setup_form()

    def setup_form(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        dims = self.read_dims(DIM_DIR)
        self.scrollable_frame = MyScrollableFrame(self, title='施業体系パラメータ設定', fonts=self.fonts, dims=dims, variables=VARIABLES)
        self.scrollable_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky='nsew')

        self.button = ctk.CTkButton(master=self, text="csv出力", command=self.button_function, font=self.fonts)
        self.button.grid(row=1, column=0, padx=10, pady=10)

    def read_dims(self, dir):
        dims = None
        try:
            with open(dir, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header
                dims = [row[0] for row in reader]
        except Exception as e:
            print(f"Error reading CSV file: {e}")
        finally:
            if csvfile:
                csvfile.close()
        return dims

    def button_function(self):
        # Perform action on button click
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()

'''
import customtkinter as ctk
import pandas as pd

FONT_TYPE = "meiryo"
dim_dir = '../dimension.csv'
variables = [
    '植栽密度(本/ha)', '下刈り省力化',
            #  '下刈り開始齢(年生)', '下刈り終了齢(年生)',
            #  '除伐齢(年生)', '除伐率',
            #  '初回間伐齢(年生)', '初回間伐率',
            #  '2回目間伐齢(年生)', '2回目間伐率',
            #  '伐採齢(年生)'
             ]

class MyScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, fonts):
        super().__init__(master, width=800, height=500, label_text=title, label_font=fonts)
        self.fonts = fonts
        self.grid_columnconfigure(0, weight=1)
        self.lands = []
        self.types = []
        self.textboxes = []
        self.dims = self.readdim(dim_dir)
        self.vars = variables

        for k,v in enumerate(self.dims):
            lands = ctk.CTkLabel(master=self,
                                 text=v,
                                 font=self.fonts)
            lands.grid(row=k+1, column=0, padx=10, pady=(10,0), sticky="w")
            self.lands.append(lands)
        
        for k,v in enumerate(self.vars):
            types = ctk.CTkLabel(master=self,
                                 text=v,
                                 font=self.fonts)
            types.grid(row=0, column=k+1, padx=10, pady=(10,0), sticky="w")
            self.types.append(types)
        
        for i,_ in enumerate(self.vars):
            for j,_ in enumerate(self.dims):
                textboxes = ctk.CTkEntry(master=self,
                                        width=100,
                                        font=self.fonts)
                textboxes.grid(row=j+1, column=i+1, padx=10, pady=(10,0), sticky="w")
                textboxes.insert(0, 60)
                self.textboxes.append(textboxes)

    def readdim(self, dir):
        self.name = pd.read_csv(dir,header=0)
        self.name = self.name.T.values.tolist()
        return self.name[0]

'''
'''
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
'''
'''

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # メンバー変数の設定
        self.fonts = (FONT_TYPE, 15)
        # フォームサイズ設定
        self.geometry("1000x750")
        self.title("Forestry params settings")

        # フォームのセットアップをする
        self.setup_form()
    
    def setup_form(self):
        # CustomTkinter のフォームデザイン設定
        ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        # テキストボックスを表示する
        self.scrollable_frame = MyScrollableFrame(self, title='施業体系パラメータ設定', fonts=self.fonts)
        self.scrollable_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky='nsew')

        # ボタンを表示する
        self.button = ctk.CTkButton(master=self, text="csv出力", command=self.button_function, font=self.fonts)
        self.button.grid(row=1, column=0, padx=10, pady=10)
    
    def button_function(self):
        # テキストボックスに入力されたテキストを表示する
        print(self.textbox.get())


if __name__ == "__main__":
    # アプリケーション実行
    app = App()
    app.mainloop()
'''