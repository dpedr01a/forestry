import customtkinter as ctk

FONT_TYPE = "meiryo"

class MyScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, fonts):
        super().__init__(master, height=500, label_text=title, label_font=fonts)
        self.fonts = fonts
        self.grid_columnconfigure(0, weight=1)
        self.years = []
        self.textboxes = []

        for i in range(1,61):
            years = ctk.CTkLabel(master=self,
                                 text=f'{i}年目',
                                 font=self.fonts)
            years.grid(row=i-1, column=0, padx=10, pady=(10,0), sticky="w")
            self.years.append(years)
            textboxes = ctk.CTkEntry(master=self,
                                     width=100,
                                     font=self.fonts)
            textboxes.grid(row=i-1, column=1, padx=10, pady=(10,0), sticky="w")
            textboxes.insert(0, 60)
            self.textboxes.append(textboxes)

        '''
        def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
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
        self.scrollable_frame = MyScrollableFrame(self, title='伐採齢', fonts=self.fonts)
        self.scrollable_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky='nsew')

        # ボタンを表示する
        self.button = ctk.CTkButton(master=self, text="クリックしてね", command=self.button_function, font=self.fonts)
        self.button.grid(row=1, column=0, padx=10, pady=10)
    
    def button_function(self):
        # テキストボックスに入力されたテキストを表示する
        print(self.textbox.get())


if __name__ == "__main__":
    # アプリケーション実行
    app = App()
    app.mainloop()
