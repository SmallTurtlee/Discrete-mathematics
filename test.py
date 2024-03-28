import random
from fpdf import FPDF

def create_function():
    perem = ['x_1', '!x_1', 'x_2', '!x_2', 'x_3', '!x_3']
    random.shuffle(perem)
    oper =  ['V', '/\\', '(+)', '->', '|', '\\|/']
    return '[(' + perem[0] +' '+ random.choice(oper) +' '+ perem[1]+') ' + random.choice(oper) + ' (' + perem[2] +' '+ random.choice(oper) +' '+ perem[3] +')] ' + random.choice(oper) + ' ' + perem[4]
    
def text_of_task_1():
    task1 = 'F(x_1, x_2, x_3) = '
    f = create_function()
    while f.find('x_1') == -1 or f.find('x_2') == -1 or f.find('x_3') == -1:
        f = create_function()
    task1 += f 
    return task1
    
def text_of_task_2():
    list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    my_list =sorted(random.sample(list, k=10))
    func2 = 'F(x_1, x_2, x_3, x_4) = V_1(' 
    for i in my_list:
        func2 += str(i) + ', '
    task2 = func2[:-2] + ')'
    return task2

pdf = FPDF()
pdf.add_font('times', '', 'timesnrcyrmt.ttf', uni=True)
pdf.add_font('timesB', '', 'timesnrcyrmt_bold.ttf', uni=True)
pdf.add_page()
print("Сколько вариантов сгенерировать?")
num = int(input())
for i in range(num):
    pdf.set_font("timesB", size=12)
    pdf.cell(0, 5,'Дискретная математика. РК1 "Теория булевых функций".           Вариант №' + str(i+1),ln=1, align="L")
    pdf.set_font("times", size=12)
    pdf.cell(0, 10, '1. Используя соответствующую методику, аналитически привести заданную булеву функцию к ' + random.choice(['Д', 'К']) + 'НФ.', ln=1)
    pdf.cell(0, 5, text_of_task_1(), ln=1, align="C")
    pdf.cell(0, 5, '2. Построить таблицу истинности и записать СДНФ заданной булевой функции. Получить ', ln=1)
    pdf.cell(0, 5, random.choice(['все её минимальные', 'её минимальную']) + ' ДНФ методом карт Карно.', ln=1)
    pdf.cell(0, 5, text_of_task_2(), ln=1, align="C")
    if i % 5 != 4: pdf.cell(0, 20, "_"*1000, ln=1, align="C")
    else: pdf.cell(0, 10, " " * 1000, ln=1)
pdf.output("demo_rk1.pdf")