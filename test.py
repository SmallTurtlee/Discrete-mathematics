import random
from fpdf import FPDF
import matplotlib.pyplot as plt
import os

def create_function():
    perem = ['x_1', '\\overline{x_1}', 'x_2', '\\overline{x_2}', 'x_3', '\\overline{x_3}']
    random.shuffle(perem)
    oper =  ['\\vee', '\\wedge', '\\oplus', '\\rightarrow', '\\mid', '\\downarrow', '\\sim']
    return '[(' + perem[0] +' '+ random.choice(oper) +' '+ perem[1]+') ' + random.choice(oper) + ' (' + perem[2] +' '+ random.choice(oper) +' '+ perem[3] +')] ' + random.choice(oper) + ' ' + perem[4] + '$'
    
    
def text_of_task_1(i):
    task1 = '$f(x_1, x_2, x_3) = '
    f = create_function()
    while f.find('x_1') == -1 or f.find('x_2') == -1 or f.find('x_3') == -1:
        f = create_function()
    task1 += f 
    get_first_answer(f, i)
    return task1

def text_of_task_2():
    list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    my_list =sorted(random.sample(list, k=10))
    func2 = '$F(x_1, x_2, x_3, x_4) = V_1(' 
    for i in my_list:
        func2 += str(i) + ', '
    task2 = func2[:-2] + ')$'
    return task2

def formula(i, nn):
    if nn==1: tex = text_of_task_1(i)
    elif nn==2: tex = text_of_task_2()
    else: tex = nn
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.set_axis_off()
    t = ax.text(0.5, 0.5, tex,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=3, color='black')
    ax.figure.canvas.draw()
    bbox = t.get_window_extent()
    fig.set_size_inches(bbox.width/80,bbox.height/80) # dpi=1000
    plt.savefig(os.getcwd()+'/pictures/test'+str(i)+'.png', dpi=1000)
    plt.close(fig)

def get_first_answer(text, i):
    list =[]
    list.append(['x_1', 'x_2', 'x_3', 'x_4', 'x_5', 'x_6', 'f'])
    list.append([0,0,0,0,1,1,1,1])
    list.append([0,0,1,1,0,0,1,1])
    list.append([0,1,0,1,0,1,0,1])
    word = text.split()
    list.append(getlogic(word[0], word[1], word[2], list))
    list.append(getlogic(word[4],word[5], word[6], list))
    list.append(getlogic("x_4", word[3], "x_5", list))
    list.append(getlogic("x_6", word[7], word[8], list))
    answtex='1.' +str(list[-1][0])+str(list[-1][1])+str(list[-1][2])+str(list[-1][3])+str(list[-1][4])+str(list[-1][5])+str(list[-1][6])+str(list[-1][7])
    pdfanswer.cell(0, 5, answtex , ln=1)
    list_of_dis= ['\\overline{x_1} \\overline{x_2} \\overline{x_3}', '\\overline{x_1} \\overline{x_2} x_3', '\\overline{x_1} x_2 \\overline{x_3}', '\\overline{x_1} x_2 x_3', 'x_1 \\overline{x_2} \\overline{x_3}', 'x_1 \\overline{x_2} x_3', 'x_1 x_2 \\overline{x_3}', 'x_1 x_2 x_3']
    answdnf='$'
    list_of_kon=['(\\overline{x_1} \\vee \\overline{x_2} \\vee \\overline{x_3})', '(\\overline{x_1} \\vee \\overline{x_2} \\vee x_3)', '(\\overline{x_1} \\vee x_2 \\vee \\overline{x_3})', '(\\overline{x_1} \\vee x_2  \\vee x_3)', '(x_1 \\vee \\overline{x_2} \\vee \\overline{x_3})', '(x_1 \\vee \\overline{x_2}  \\vee x_3)', '(x_1 \\vee x_2 \\vee \\overline{x_3})', '(x_1 \\vee x_2 \\vee x_3)']
    answknf='$'
    sum = 0
    for j in range(8):
        if list[-1][j] == 1: 
            answdnf += list_of_dis[j] + '\\vee '
            sum+=1
        else: answknf += list_of_kon[7-j] + '  '
    pdfanswer.cell(0,5,"СДНФ:", ln=1)
    if sum==0: pdfanswer.cell(0,5,"0", ln =1)
    elif sum==8: pdfanswer.cell(0,5,"1", ln =1)
    else:
        formula(i+2,answdnf[:-5]+'$')
        pdfanswer.image(os.getcwd()+"/pictures/test"+str(i+2)+".png", h=10)
    pdfanswer.cell(0,5,"СКНФ:", ln=1)
    if sum==0: pdfanswer.cell(0,5,"0", ln =1)
    elif sum==8: pdfanswer.cell(0,5,"1", ln =1)
    else:
        formula(i+3, answknf+'$')
        pdfanswer.image(os.getcwd()+"/pictures/test"+str(i+3)+".png", h=7)
    
def getlogic(n, oper, m, list):
    x=[]
    y=[]
    k = int(n[n.find('x')+2])
    l = int(m[m.find('x')+2])
    for i in range(8):
        if n.find('overline') == -1: x.append(list[k][i]) 
        else: x.append(int(not(list[k][i])))
        if m.find('overline') == -1: y.append(list[l][i])
        else: y.append(int(not(list[l][i])))
    return(dologic(x, y, oper))
    
def dologic(x, y, oper):
    a = []
    if oper.find('vee') != -1: 
        for i in range(8):
            a.append(int(bool(x[i]) or bool(y[i])))
    elif oper.find('wedge') != -1: 
        for i in range(8):
            a.append(int(bool(x[i]) and bool(y[i])))
    elif oper.find('oplus') != -1: 
        for i in range(8):
            a.append(int(not(bool(x[i])) and bool(y[i]) or bool(x[i]) and not(bool(y[i]))))
    elif oper.find('rightarrow') != -1: 
        for i in range(8):
            a.append(int(not(bool(x[i])) or bool(y[i])))
    elif oper.find('sim') != -1: 
        for i in range(8):
            a.append(int(bool(x[i]) == bool(y[i])))
    elif oper.find('mid') != -1: 
        for i in range(8):
            a.append(int(not(bool(x[i]) and bool(y[i]))))
    elif oper.find('downarrow') != -1: 
        for i in range(8):
            a.append(int(not(bool(x[i]) or bool(y[i]))))
    return a

pdf = FPDF()
pdfanswer = FPDF()
if not(os.path.exists(os.path.join(os.getcwd(), "pictures"))): os.mkdir("pictures")
pdf.add_font('times', '', 'timesnrcyrmt.ttf', uni=True)
pdf.add_font('timesB', '', 'timesnrcyrmt_bold.ttf', uni=True)
pdfanswer.add_font('times', '', 'timesnrcyrmt.ttf', uni=True)
pdf.add_page()
pdfanswer.add_page()
pdfanswer.set_font("times", size=12)
print("Сколько вариантов сгенерировать?")
num = int(input())
for i in range(num):
    pdfanswer.cell(0, 5, "Вариант №"+str(i+1), ln=1)
    pdf.set_font("timesB", size=12)
    pdf.cell(0, 5,'Дискретная математика. РК1 "Теория булевых функций".           Вариант №' + str(i+1),ln=1, align="L")
    pdf.set_font("times", size=12)
    pdf.cell(0, 5, '1. Используя соответствующую методику, аналитически привести заданную булеву функцию к ' + random.choice(['Д', 'К']) + 'НФ.', ln=1)
    formula(i*4, 1)
    pdf.image(os.getcwd()+"/pictures/test"+str(i*4)+".png", w=100)
    pdf.cell(0, 5, '2. Построить таблицу истинности и записать СДНФ заданной булевой функции. Получить ', ln=1)
    pdf.cell(0, 5, random.choice(['все её минимальные', 'её минимальную']) + ' ДНФ методом карт Карно.', ln=1)
    formula(i*4+1, 2)
    pdf.image(os.getcwd()+"/pictures/test"+str(i*4+1)+".png", w=100)
    if i % 5 != 4: pdf.cell(0, 18, "_"*1000, ln=1, align="C")
    else: pdf.cell(0, 7, " " * 1000, ln=1)

pdf.output("demo_rk1.pdf")
pdfanswer.output("answers.pdf")