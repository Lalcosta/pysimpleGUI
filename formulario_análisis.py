
import PySimpleGUI as sg
import pandas as pd
import statistics as st
import webbrowser

print=sg.Print



"""
def contraseña():
    contra='12345'
    contra_text=sg.Text("Bienvenido, introduce tu contraseña")
    contra_input=sg.InputText('', key='contraseña', password_char='*')
    ventana_contra=sg.Window(contra_text,contra_input)
    while True:
        
        if contra!= contra_input:
            sg.popup("Contraseña incorrecta",title="Error")
        else:
            sg.popup("Contraseña correcta", title="Bienvenido")
            break
            """
    
def formulario():
    descripcion = sg.Text("Recopilación de datos sobre violencia por narcotráfico")
    genero_texto = sg.Text("Genero")
    genero_combo = sg.Combo(("hombre","mujer","otro"),key="GENERO")
    edad_texto=sg.Text("Edad")
    edad_spin=sg.Spin(tuple(range(1,150)),key="EDAD")
    experiencia_texto=sg.Text("¿Has sido victima o has presenciado algún crimen de violencia por narcotráfico?")
    experiencia_combo=sg.Combo(("victima","presenciado","no"),key="EXPERIENCIA")
    año_texto=sg.Text("¿En qué año sucedió el crimen?")
    año_combo=sg.Combo(tuple(range(1900,2022)),key='AÑO')
    denuncia_texto=sg.Text('¿Denunciaste el crímen?')
    denuncia_combo=sg.Combo(('Si','No','No aplica'), key="DENUNCIA")
    estado_texto=sg.Text("¿En qué estado sucedió?")
    estados=('No aplica','Aguascalientes','Baja California','Baja California Sur','Campeche','Chiapas','Chihuahua','Coahuila de Zaragoza',
            'Colima','Ciudad de México','Durango','Guanajuato','Guerrero','Hidalgo','Jalisco','Estado de Mexico','Michoacan de Ocampo',
            'Morelos','Nayarit','Nuevo Leon','Oaxaca','Puebla','Queretaro de Arteaga',	'Quintana Roo','San Luis Potosi','Sinaloa', 'Sonora',
            'Tabasco','Tamaulipas','Tlaxcala','Veracruz de Ignacio de la Llave','Yucatan','Zacatecas')
    estado_combo=sg.Combo(estados,key="ESTADO")
    motivo_texto=sg.Text('¿Cuál de las siguientes opciones describe mejor el crimen?')
    motivo_opc=('Ajuste de cuentas','Lucha entre carteles','Enfrentamiento con la policia','Violencia contra civiles','No aplica')
    motivo_combo=sg.Combo(motivo_opc,key="MOTIVO")
    btn_grabar=sg.Button("GRABAR",key="BTN_GRABAR")
    btn_rmenu=sg.Button("REGRESAR A MENU",key="BTN_RMENU")
    
    layout_formulario=[[genero_texto,genero_combo],[edad_texto,edad_spin],[experiencia_texto,experiencia_combo],
            [año_texto,año_combo],[denuncia_texto,denuncia_combo],[estado_texto,estado_combo],
            [motivo_texto,motivo_combo],[btn_grabar,btn_rmenu]]
    
    frame_formulario=sg.Frame("Formulario", layout_formulario, key="FRAME_FORMULARIO", visible="True")
    return frame_formulario

def validar_ingreso():
    texto_password = sg.Text("Teclea la contraseña " )
    
    password = sg.Input(password_char = "*" , key = 'PASSWORD', text_color = "lightblue")
    
    b1 = sg.Button("Validar Ingreso", font = ("chalkboard", 25), key = 'BTN_PASSWORD',
                   pad = ((135, 100), (20, 20)) , button_color = "lightblue", border_width = 5 )
    
    imagen = sg.Image(filename="candado.png")
    
    layout =  [[texto_password, password ],
             [b1],
             [imagen]]
                         
    #crear el frame - ventana para ingresar los datos del password
    frame_password = sg.Frame("Validar Ingreso", layout, key = "FRAME_PASSWORD", visible = True)
                         
    return frame_password 

def menu():
    
    b1 = sg.Button( key = "BTN_FORMULARIO", border_width = 5, image_filename = "formulario2.png",size=(10,10) ) # image_filename = " "
    b2 = sg.Button( key = "BTN_MAPS", border_width = 5, image_filename = "maps2.png",size=(10,10) ) # image_filename = " "
    b3 = sg.Button( key = "BTN_ESTADISTICAS", border_width = 5, image_filename = "reporte2.png",size=(10,10) ) # image_filename = " "
    b4 = sg.Button( key = "BTN_VIDEO", border_width = 5, image_filename = "video2.png",size=(10,10) ) # image_filename = " "
    
    # todo frame tiene un layout
    layout_menu = [ [b1, b2 ] ,
                    [b3, b4] ]
    
    frame_menu = sg.Frame("Menu", layout_menu, key = "FRAME_MENU", visible = True)
    
    return frame_menu

def estadisticas():
    df=pd.read_csv("MiBase.csv")
    print('Estado(s) con más registos:',pd.Series(df['ESTADO'].values.flatten()).mode()[0])
    print('Crimenes por género:', df['GENERO'].value_counts())
    print('Denuncias', df['DENUNCIA'].value_counts())    


sg.theme("LightBlue3")
form=formulario()
contraseña=validar_ingreso()
opciones= menu()


layout=[[opciones],
        [form], 
        [contraseña],
        ]

window= sg.Window("Emiliano Bizet", layout,size=(600,500),location=(0,0))

while True:
    event, values=window.read()
    
    if event==sg.WIN_CLOSED:
        break
    
    elif event =='BTN_PASSWORD':
            password= values["PASSWORD"]
            
            if password=="123":
                sg.popup("Bienvenido Emiliano")
                layout[opciones]
            else:
                sg.popup("Contraseña incorrecta, \nintente nuevamente")
    
    
    elif event=="BTN_GRABAR":
        with open("MiBase.csv","a") as archivo:
            genero=values["GENERO"]
            edad=values["EDAD"]
            experiencia=values["EXPERIENCIA"]
            año=values["AÑO"]
            denuncia=values["DENUNCIA"]
            estado=values["ESTADO"]
            motivo=values["MOTIVO"]
            
            row=genero + "," + str(edad) + "," + experiencia + "," + str(año) + "," + denuncia + "," + estado + "," + motivo + "\n"
            archivo.write(row)
    
    elif event=="BTN_ESTADISTICAS":
        df=pd.read_csv("MiBase.csv")
        edos={}
        for i in df.iloc[:,5]:
            if i in edos:
                edos[i]+=1
            else:
                edos[i]=1
        print("Crimenes por estado")
        for i in edos:
            print(i,":",edos[i])
        print('Crimenes por género:\n', df['GENERO'].value_counts(sort=True))
        print('Denuncias: \n', df.iloc[:,4].value_counts()) 
        crim={}
        for i in df.iloc[:,6]:
            if i in crim:
                crim[i]+=1
            else:
                crim[i]=1
        print("Conteo por tipo de crimen")
        for i in crim:
            print(i,":",crim[i])
    
    elif event=="BTN_MAPS":
        webbrowser.open("https://www.google.com/maps/search/ministerio+publico+monterrey/@25.7119864,-100.3760887,13z/data=!3m1!4b1?hl=es-419")
    
    elif event=="BTN_VIDEO":
         webbrowser.open("https://www.youtube.com/watch?v=pCSwRPSvgY4")       

window.close()     