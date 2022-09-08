
from distutils.command.clean import clean
import PySimpleGUI as sg
import pandas as pd
import statistics as st
import webbrowser

print=sg.Print

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
    
    layout_formulario=[[descripcion],[genero_texto,genero_combo],[edad_texto,edad_spin],[experiencia_texto,experiencia_combo],
            [año_texto,año_combo],[denuncia_texto,denuncia_combo],[estado_texto,estado_combo],
            [motivo_texto,motivo_combo],[btn_grabar,btn_rmenu]]
    
    frame_formulario=sg.Frame("Formulario", layout_formulario, key="FRAME_FORMULARIO", visible="True")
    return frame_formulario

def validar_ingreso():
    texto_password = sg.Text("Teclea la contraseña " )
    
    password = sg.Input(password_char = "*" , key = 'PASSWORD', text_color = "lightblue")
    
    b1 = sg.Button("Validar Ingreso", font = ("chalkboard", 25), key = 'BTN_PASSWORD',
                   pad = ((135, 100), (20, 20)) , button_color = "lightblue", border_width = 5 )
    
    imagen = sg.Image(filename="candado2.png")
    
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
opc = menu()

 
def password_window():
    contraseña=validar_ingreso()
    layout_contra=[[contraseña]]

    window_contra= sg.Window("Emiliano Bizet", layout_contra,size=(600,500),location=(0,0))

    while True:
        event, values=window_contra.read()
        if event==sg.WIN_CLOSED:
            return 0
        
        elif event =='BTN_PASSWORD':
                password= values["PASSWORD"]
                
                if password=="123":
                    sg.popup("Bienvenido Emiliano")
                    window_contra.close() 
                    return 1
                else:
                    sg.popup("Contraseña incorrecta, \nintente nuevamente")
                    
def formulario_window():
    
    layout_formulario=[[form]]
    window_formulario= sg.Window("Emiliano Bizet", layout_formulario,size=(600,500),location=(0,0))
    
    while True:
        event, values=window_formulario.read()
        if event==sg.WIN_CLOSED:
                return
        if event=="BTN_GRABAR":
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
                sg.popup("Datos guardados correctamente")
                window_formulario.close()
                return
                
        elif event=="BTN_RMENU":
            window_formulario.close()
            return

            
        
                    
    
def menu_window(contra):
    clean
    if contra == 0:
        return 0
    else:
        layout_menu=[[opc]]

        window_menu= sg.Window("Emiliano Bizet", layout_menu,size=(600,500),location=(0,0))

        while True:
            event, values=window_menu.read()
            if event==sg.WIN_CLOSED:
                break
            if event=="BTN_ESTADISTICAS":
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
            
            elif event=="BTN_FORMULARIO":
                formulario_window()
                
                       

        
menu_window(password_window())               

