from os import write
from tkinter import ttk
from tkinter import *
import os
import math
import threading

class main():
    def __init__(self):
        self.gage_count = 0
        self.nowfilename = ""
        self.savefilename = ""
        self.now = 0
        self.score_name = ""
        self.field_save =[]
        self.command_save = []
        self.save_initial = ""
        self.save_initial_after = ""
        self.exe_command = ""
        self.exe_command_after = ""
        self.gage_image = [0,0,0,0]
        self.alpha = 0
        self.calc_get = []
        self.calc_str = ""
        self.now_command_writer = 0
        self.command_save2 = []
        self.exe_command2 = ""
        self.calc_get2 = []
        self.calc_str2 = ""
        self.exe_command_after2 = ""
        self.command_save3 = []
        self.exe_command3 = ""
        self.calc_get3 = []
        self.calc_str3 = ""
        self.exe_command_after3 = ""
        self.command_save4 = []
        self.exe_command4 = ""
        self.calc_get4 = []
        self.calc_str4 = ""
        self.exe_command_after4 = ""
        self.calcstr = ""
        self.calcstr2 = ""
        self.calcstr3 = ""
        self.calcstr4 = ""

    def ReInitialize(self):
        self.gage_count = 0
        self.nowfilename = ""
        self.savefilename = ""
        self.now = 0
        self.score_name = ""
        self.field_save =[]
        self.command_save = []
        self.save_initial = ""
        self.save_initial_after = ""
        self.exe_command = ""
        self.exe_command_after = ""
        self.alpha = 0
        self.calc_get = []
        self.calc_str = ""
        self.now_command_writer = 0
        self.command_save2 = []
        self.exe_command2 = ""
        self.calc_get2 = []
        self.calc_str2 = ""
        self.exe_command_after2 = ""
        self.command_save3 = []
        self.exe_command3 = ""
        self.calc_get3 = []
        self.calc_str3 = ""
        self.exe_command_after3 = ""
        self.command_save4 = []
        self.exe_command4 = ""
        self.calc_get4 = []
        self.calc_str4 = ""
        self.exe_command_after4 = ""
        self.calcstr = ""
        self.calcstr2 = ""
        self.calcstr3 = ""
        self.calcstr4 = ""
        self.cv.delete("light_on_gage")
        self.cv.delete("gage_true")
        self.label_move_text["text"] = f"進捗：ファイル生成が完了しました"
        self.enter_button["state"] = "normal"
        self.textbox_binary_tree_min["state"] = "normal"
        self.textbox_binary_tree["state"] = "normal"
        self.textbox_command["state"] = "normal"
        self.textbox_command_main["state"] = "normal"
        self.textbox_command_main2["state"] = "normal"
        self.textbox_command_main3["state"] = "normal"
        self.textbox_command_main4["state"] = "normal"
        self.textbox_filename["state"] = "normal"

    def start_before(self):
        self.start_thread = threading.Thread(target=self.start_prog)
        self.start_thread.start()

    def start_prog(self):
        self.textbox_binary_tree_min["state"] = "readonly"
        self.textbox_binary_tree["state"] = "readonly"
        self.textbox_command["state"] = "readonly"
        self.textbox_command_main["state"] = "readonly"
        self.textbox_command_main2["state"] = "readonly"
        self.textbox_command_main3["state"] = "readonly"
        self.textbox_command_main4["state"] = "readonly"
        self.textbox_filename["state"] = "readonly"
        self.enter_button["state"] = "disable"
        

        self.command_set()
        if self.textbox_command_main2.get() != "":
            self.command_set2()
            if self.textbox_command_main3.get() != "":
                self.command_set3()
                if self.textbox_command_main4.get() != "":
                    self.command_set4()
        self.filemake()

    def command_set(self):
        write_command,self.dolor_check,cut_flag,j,c = self.textbox_command_main.get(),self.textbox_command_main.get(),1,0,0
        for i in range(len(self.dolor_check)):
            if cut_flag == 1:
                if self.dolor_check[i] != "$":
                    self.command_save.append(self.dolor_check[i])
                    self.exe_command += self.command_save[j]
                    j+=1
                else:
                    cut_flag += 1
            elif cut_flag == 2:#$の中身をスルー(変更：計算倍率用記憶文字列記憶)
                if self.dolor_check[i] == "$":
                    cut_flag += 1
                if cut_flag == 2 : 
                    self.calc_get.append(self.dolor_check[i])
                    self.calc_str += self.calc_get[c]
                    c+=1
            else:
                if self.dolor_check[i] != "$":
                    self.command_save.append(self.dolor_check[i])
                    self.exe_command_after += self.command_save[j]
                    j += 1

    def command_set2(self):
        write_command,self.dolor_check2,cut_flag,j,c = self.textbox_command_main2.get(),self.textbox_command_main2.get(),1,0,0
        for i in range(len(self.dolor_check2)):
            if cut_flag == 1:
                if self.dolor_check2[i] != "$":
                    self.command_save2.append(self.dolor_check2[i])
                    self.exe_command2 += self.command_save2[j]
                    j+=1
                else:
                    cut_flag += 1
            elif cut_flag == 2:#$の中身をスルー(変更：計算倍率用記憶文字列記憶)
                if self.dolor_check2[i] == "$":
                    cut_flag += 1
                if cut_flag == 2 : 
                    self.calc_get2.append(self.dolor_check2[i])
                    self.calc_str2 += self.calc_get2[c]
                    c+=1
            else:
                if self.dolor_check2[i] != "$":
                    self.command_save2.append(self.dolor_check2[i])
                    self.exe_command_after2 += self.command_save2[j]
                    j += 1

    def command_set3(self):
        write_command,self.dolor_check3,cut_flag,j,c = self.textbox_command_main3.get(),self.textbox_command_main3.get(),1,0,0
        for i in range(len(self.dolor_check3)):
            if cut_flag == 1:
                if self.dolor_check3[i] != "$":
                    self.command_save3.append(self.dolor_check3[i])
                    self.exe_command3 += self.command_save3[j]
                    j+=1
                else:
                    cut_flag += 1
            elif cut_flag == 3:#$の中身をスルー(変更：計算倍率用記憶文字列記憶)
                if self.dolor_check3[i] == "$":
                    cut_flag += 1
                if cut_flag == 3 : 
                    self.calc_get3.append(self.dolor_check3[i])
                    self.calc_str3 += self.calc_get3[c]
                    c+=1
            else:
                if self.dolor_check3[i] != "$":
                    self.command_save3.append(self.dolor_check3[i])
                    self.exe_command_after3 += self.command_save3[j]
                    j += 1

    def command_set4(self):
        write_command,self.dolor_check4,cut_flag,j,c = self.textbox_command_main4.get(),self.textbox_command_main4.get(),1,0,0
        for i in range(len(self.dolor_check4)):
            if cut_flag == 1:
                if self.dolor_check4[i] != "$":
                    self.command_save4.append(self.dolor_check4[i])
                    self.exe_command4 += self.command_save4[j]
                    j+=1
                else:
                    cut_flag += 1
            elif cut_flag == 4:#$の中身をスルー(変更：計算倍率用記憶文字列記憶)
                if self.dolor_check4[i] == "$":
                    cut_flag += 1
                if cut_flag == 4 : 
                    self.calc_get4.append(self.dolor_check4[i])
                    self.calc_str4 += self.calc_get4[c]
                    c+=1
            else:
                if self.dolor_check4[i] != "$":
                    self.command_save4.append(self.dolor_check4[i])
                    self.exe_command_after4 += self.command_save4[j]
                    j += 1


    #ファイル生成
    def filemake(self):
        cut_flag = 1
        j = 0
        write_command = self.textbox_command.get()
        self.double_coron_delete = self.textbox_command.get()
        for i in range(len(self.double_coron_delete)):
            if cut_flag == 1 or cut_flag ==2:                           #スコアの名前の終わりまでを記憶
                if self.double_coron_delete[i] != "$":
                    self.field_save.append(self.double_coron_delete[i])
                    self.save_initial += self.field_save[j]
                    j += 1
                else:
                    cut_flag += 1
            else:                                                       #その後を記憶
                if self.double_coron_delete[i] != "$":
                    self.field_save.append(self.double_coron_delete[i])
                    self.save_initial_after += self.field_save[j]
                    j += 1
        for i in range(len(write_command)):
            if write_command[i] == "$":
                while True:
                    i += 1
                    if write_command[i] == "$":
                        self.filemake_main(int(self.textbox_binary_tree_min.get()),int(self.textbox_binary_tree.get()),"")
                        return
                    
                    self.score_name += write_command[i]
        

    def filemake_main(self,low,high,nowdirectory):#low : 最小の値 high: 最大の値

        self.calcstr = float(self.calc_str)
        if self.calcstr % 1 == 0.0 : self.calcstr = int(self.calcstr)
        if self.calc_str2 != "":
            self.calcstr2 = float(self.calc_str2)
            if self.calcstr2 % 1 == 0.0 : self.calcstr2 = int(self.calcstr2)
            if self.calc_str3 != "":
                self.calcstr3 =float(self.calcstr3)
                if self.calcstr3 % 1 == 0.0 : self.calcstr3 = int(self.calcstr3)
                if self.calc_str4 != "":
                    self.calcstr4 = float(self.calcstr4)
                    if self.calcstr4 % 1 == 0.0 : self.calcstr4 = int(self.calcstr4)

        nowdirectory += f"{self.textbox_filename.get()}_{low}_{high}/"
        if nowdirectory != "" : os.makedirs("./output/"+nowdirectory,exist_ok=True)#ディレクトリが移動しているならフォルダを生成する
        if math.floor(low + (high - low) / 2) - int(low) >= 1 and int(high) - (math.floor(low + (high - low) / 2) + 1) >= 1:#これは両フォルダが生成されないと話にならないのでおとなしくifにかけられてもらう
            with open(f"./output/{nowdirectory}{self.textbox_filename.get()}.mcfunction","w") as makefile:#./output/現在ディレクトリ/命名.mcfunctionを生成
                makefile.write(f"{self.save_initial}={int(low)}..{math.floor(low + (high - low) / 2)}{self.save_initial_after}/{nowdirectory}{self.textbox_filename.get()}_{int(low)}_{math.floor(low + (high - low) / 2)}/{self.textbox_filename.get()}" + "\n" + f"{self.save_initial}={math.floor(low + (high - low) / 2) + 1}..{int(high)}{self.save_initial_after}/{nowdirectory}{self.textbox_filename.get()}_{math.floor(low + (high - low) / 2) + 1}_{int(high)}/{self.textbox_filename.get()}")#書き込み

        elif math.floor(low + (high - low) / 2) - int(low) >= 1:#一つ目のフォルダを生成して二つ目のファイルが生成されなかったなら
            with open(f"./output/{nowdirectory}{self.textbox_filename.get()}.mcfunction","w") as makefile:#./output/現在ディレクトリ/命名.mcfunctionを生成
                makefile.write(f"{self.save_initial}={int(low)}..{math.floor(low + (high - low) / 2)}{self.save_initial_after}/{nowdirectory}{self.textbox_filename.get()}_{int(low)}_{math.floor(low + (high - low) / 2)}/{self.textbox_filename.get()}" + "\n" + f"{self.save_initial}={math.floor(low + (high - low) / 2) + 1}..{int(high)}{self.save_initial_after}/{nowdirectory}{self.textbox_filename.get()}_{math.floor(low + (high - low) / 2) + 1}")#書き込み
            with open(f"./output/{nowdirectory}{self.textbox_filename.get()}_{math.floor(low + (high - low) / 2) + 1}.mcfunction","w") as newfile:
                self.label_move_text["text"] = f"進捗：ファイルの生成中(./output/{nowdirectory}{self.textbox_filename.get()}_{math.floor(low + (high - low) / 2) + 1}.mcfunction)"
                newfile.write(f"{self.exe_command}{(math.floor(low + (high - low) / 2) + 1 ) * self.calcstr}{self.exe_command_after}" + "\n" + f"{self.exe_command2}{(math.floor(low + (high - low) / 2) + 1 ) * self.calcstr2}{self.exe_command_after2}" + "\n" + f"{self.exe_command3}{(math.floor(low + (high - low) / 2) + 1 ) * self.calcstr3}{self.exe_command_after3}" + "\n" + f"{self.exe_command4}{(math.floor(low + (high - low) / 2) + 1 ) * self.calcstr4}{self.exe_command_after4}")
                self.filemake_success()

        elif int(high) - (math.floor(low + (high - low) / 2) + 1) >= 1:#2つ目のフォルダを生成して1つ目のファイルが生成されなかったなら
            with open(f"./output/{nowdirectory}{self.textbox_filename.get()}.mcfunction","w") as makefile:#./output/現在ディレクトリ/命名.mcfunctionを生成
                makefile.write(f"{self.save_initial}={int(low)}..{math.floor(low + (high - low) / 2)}{self.save_initial_after}/{nowdirectory}{self.textbox_filename.get()}_{int(low)}" + "\n" + f"{self.save_initial}={math.floor(low + (high - low) / 2) + 1}..{int(high)}{self.save_initial_after}/{nowdirectory}{self.textbox_filename.get()}_{math.floor(low + (high - low) / 2) + 1}_{int(high)}/{self.textbox_filename.get()}")#書き込み
            with open(f"./output/{nowdirectory}{self.textbox_filename.get()}_{int(low)}.mcfunction","w") as newfile:
                self.label_move_text["text"] = f"進捗：ファイルの生成中(./output/{nowdirectory}{self.textbox_filename.get()}_{int(low)}.mcfunction)"
                newfile.write(f"{self.exe_command}{int(low) * self.calcstr}{self.exe_command_after}" + "\n" + f"{self.exe_command2}{int(low) * self.calcstr2}{self.exe_command_after2}" + "\n" + f"{self.exe_command3}{int(low) * self.calcstr3}{self.exe_command_after3}" + "\n" + f"{self.exe_command4}{int(low) * self.calcstr4}{self.exe_command_after4}")
                self.filemake_success()

        else:#最終書き込み命令
            with open(f"./output/{nowdirectory}{self.textbox_filename.get()}_{math.floor(low + (high - low) / 2) + 1}.mcfunction","w") as newfile:
                self.label_move_text["text"] = f"進捗：ファイルの生成中(./output/{nowdirectory}{self.textbox_filename.get()}_{math.floor(low + (high - low) / 2) + 1}.mcfunction)"
                newfile.write(f"{self.exe_command}{(math.floor(low + (high - low) / 2) + 1 ) * self.calcstr}{self.exe_command_after}" + "\n" + f"{self.exe_command2}{(math.floor(low + (high - low) / 2) + 1 ) * self.calcstr2}{self.exe_command_after2}" + "\n" + f"{self.exe_command3}{(math.floor(low + (high - low) / 2) + 1 ) * self.calcstr3}{self.exe_command_after3}" + "\n" + f"{self.exe_command4}{(math.floor(low + (high - low) / 2) + 1 ) * self.calcstr4}{self.exe_command_after4}")
                self.filemake_success()
            with open(f"./output/{nowdirectory}{self.textbox_filename.get()}_{int(low)}.mcfunction","w") as newfile:
                self.label_move_text["text"] = f"進捗：ファイルの生成中(./output/{nowdirectory}{self.textbox_filename.get()}_{int(low)}.mcfunction)"
                newfile.write(f"{self.exe_command}{int(low) * self.calcstr}{self.exe_command_after}" + "\n" + f"{self.exe_command2}{int(low) * self.calcstr2}{self.exe_command_after2}" + "\n" + f"{self.exe_command3}{int(low) * self.calcstr3}{self.exe_command_after3}" + "\n" + f"{self.exe_command4}{int(low) * self.calcstr4}{self.exe_command_after4}")
                self.filemake_success()
            with open(f"./output/{nowdirectory}{self.textbox_filename.get()}.mcfunction","w") as makefile:#./output/現在ディレクトリ/命名.mcfunctionを生成
                makefile.write(f"{self.save_initial}={int(low)}..{math.floor(low + (high - low) / 2)}{self.save_initial_after}/{nowdirectory}{self.textbox_filename.get()}_{int(low)}_{math.floor(low + (high - low) / 2)}/{self.textbox_filename.get()}" + "\n" + f"{self.save_initial}={math.floor(low + (high - low) / 2) + 1}..{int(high)}{self.save_initial_after}/{nowdirectory}{self.textbox_filename.get()}_{math.floor(low + (high - low) / 2) + 1}_{int(high)}/{self.textbox_filename.get()}")
        

        if math.floor(low + (high - low) / 2) - int(low) >= 1:#要素が2以上あるなら二分技を継続
            self.filemake_main(int(low),math.floor(low + (high - low) / 2),nowdirectory)
        if int(high) - (math.floor(low + (high - low) / 2) + 1) >= 1 :
            self.filemake_main(math.floor(low + (high - low) / 2)+1,int(high),nowdirectory)

    def filemake_success(self):
        self.gage_count += 1
        

    def filemake_success_draw(self):
        try:
            if self.alpha < (502 / ( int(self.textbox_binary_tree.get()) - int(self.textbox_binary_tree_min.get()) + 1)) * (self.gage_count):
                print(self.gage_count)
                self.filemake_success_plus()
            
        finally: 
            self.cv.after(1,self.filemake_success_draw)
            if self.gage_count == int(self.textbox_binary_tree.get()) - int(self.textbox_binary_tree_min.get()) + 1:#終了時初期化
                print("init")
                self.ReInitialize()

    def filemake_success_plus(self):
        self.cv.delete("light_on_gage")
        self.alpha += 1
        self.cv.create_image(48+self.alpha , 300 , image = self.gage_image[2],tag="gage_true")
        self.cv.create_image(48+self.alpha , 300 , image = self.gage_image[3],tag="light_on_gage")



    #ウィンドウの初期設定
    def main(self):
        self.master = Tk()
        self.master.title("binary tree maker")
        self.cv = Canvas(self.master,height=400,width=800)
        self.cv.pack()



        self.gage_image[0] = PhotoImage(file="./assets/gage/background.png")
        self.gage_image[1] = PhotoImage(file="./assets/gage/false.png")
        self.gage_image[2] = PhotoImage(file="./assets/gage/true.png")
        self.gage_image[3] = PhotoImage(file="./assets/gage/light.png")

        self.mark_image = PhotoImage(file="./assets/mark/mitsukiGroup.png")

        #label create--------------------------------------------------------
        self.label_binary_tree = ttk.Label(self.master,text="binary number min-max")
        self.label_binary_tree.place(x=10 ,y =30)
        self.label_command = ttk.Label(self.master,text="execute if command")
        self.label_command.place(x=10,y=80)
        self.label_command_2 = ttk.Label(self.master,text="($score名$ : socre名=数値)")
        self.label_command_2.place(x=20,y=100)
        self.label_command_main = ttk.Label(self.master,text="executing command")
        self.label_command_main.place(x=10,y=130)
        self.label_command_main_2 = ttk.Label(self.master,text="(二分技の先で実行されるコマンド[$倍率$])")
        self.label_command_main_2.place(x=20,y=150)
        self.label_filename = ttk.Label(self.master,text="file name")
        self.label_filename.place(x=10,y=240)

        self.label_move_text = ttk.Label(self.master)
        self.label_move_text.place(x=30,y=270)
        self.label_move_text["text"] = "condition："

        self.group_lisence = ttk.Label(self.master,text="Copyright © mitsukiGroup 2022")
        self.group_lisence.place(x=120,y=350)
        self.lisence = ttk.Label(self.master,text="This Software is MIT Lisence")
        self.lisence.place(x=120,y=370)
        #label create--------------------------------------------------------

        self.textbox_binary_tree_min = ttk.Entry(self.master,width=4,textvariable="0")
        self.textbox_binary_tree_min.insert(0,"0")
        self.textbox_binary_tree_min.place (x=300, y = 30)
        self.textbox_binary_tree = ttk.Entry(self.master,width = 4,textvariable="1")#二分技の数
        self.textbox_binary_tree.insert(0,"1")
        self.textbox_binary_tree.place (x = 330, y = 30)
        self.textbox_command = ttk.Entry(self.master,width = 80)#判定コマンドを入力してもらい$$があればその中にtextbox_binary_treeを代入する
        self.textbox_command.place (x = 300, y = 80)
        self.textbox_command_main = ttk.Entry(self.master,width=80)#実行コマンドを入力してもらう
        self.textbox_command_main.place (x = 300, y = 130)
        self.textbox_command_main2 = ttk.Entry(self.master,width=80)#実行コマンドを入力してもらう(第二)
        self.textbox_command_main2.place (x = 300, y = 150)
        self.textbox_command_main3 = ttk.Entry(self.master,width=80)#実行コマンドを入力してもらう(第三)
        self.textbox_command_main3.place (x = 300, y = 170)
        self.textbox_command_main4 = ttk.Entry(self.master,width=80)#実行コマンドを入力してもらう(第四)
        self.textbox_command_main4.place (x = 300, y = 190)
        self.textbox_filename = ttk.Entry(self.master,width = 10)#ファイル名を聞く
        self.textbox_filename.place (x = 300, y = 240)

        
        self.exit_button = ttk.Button (self.master,text="exit",command=exit)
        self.exit_button.place(x = 600, y = 320)
        self.enter_button = ttk.Button (self.master,text="make file",command=self.start_before,default = "active")
        self.enter_button.place(x = 700, y = 320)


        self.cv.create_image(55,355,image = self.mark_image)
        


        threading.Thread(target=self.filemake_success_draw).start()

        self.cv.create_image(300,300,image=self.gage_image[0])


        self.master.mainloop()


if __name__ == "__main__":
    mainclass = main()
    mainclass.main()

def exe():
    mainclass = main()
    mainclass.main()