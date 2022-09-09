
from distutils.command.clean import clean
import PySimpleGUI as sg
import pandas as pd
import statistics as st
import webbrowser

#Para que los print aparezcan en una ventana nueva
print=sg.Print

#Ceación del formulario
def formulario():
    #Creación de las preguntas con sus inputs
    descripcion = sg.Text("Recopilación de datos sobre violencia por narcotráfico")
    genero_texto = sg.Text("Genero")
    #Input COMBO
    genero_combo = sg.Combo(("hombre","mujer","otro"),key="GENERO")
    edad_texto=sg.Text("Edad")
    #Input SPIN que va del 1 al 150
    edad_spin=sg.Spin(tuple(range(1,150)),key="EDAD")
    experiencia_texto=sg.Text("¿Has sido victima o has presenciado algún crimen de violencia por narcotráfico?")
    #Input COMBO
    experiencia_combo=sg.Combo(("victima","presenciado","no"),key="EXPERIENCIA")
    año_texto=sg.Text("¿En qué año sucedió el crimen?")
    #Input COMBO que va de 1900 a 2022
    año_combo=sg.Combo(tuple(range(1900,2022)),key='AÑO')
    denuncia_texto=sg.Text('¿Denunciaste el crímen?')
    #INPUT COMBO
    denuncia_combo=sg.Combo(('Si','No','No aplica'), key="DENUNCIA")
    estado_texto=sg.Text("¿En qué estado sucedió?")
    #Tupla de todos los estados de México
    estados=('No aplica','Aguascalientes','Baja California','Baja California Sur','Campeche','Chiapas','Chihuahua','Coahuila de Zaragoza',
            'Colima','Ciudad de Mexico','Durango','Guanajuato','Guerrero','Hidalgo','Jalisco','Estado de Mexico','Michoacan de Ocampo',
            'Morelos','Nayarit','Nuevo Leon','Oaxaca','Puebla','Queretaro de Arteaga',	'Quintana Roo','San Luis Potosi','Sinaloa', 'Sonora',
            'Tabasco','Tamaulipas','Tlaxcala','Veracruz de Ignacio de la Llave','Yucatan','Zacatecas')
    #Input COMBO con la tupa anterior como opciones
    estado_combo=sg.Combo(estados,key="ESTADO")
    motivo_texto=sg.Text('¿Cuál de las siguientes opciones describe mejor el crimen?')
    motivo_opc=('Ajuste de cuentas','Lucha entre carteles','Enfrentamiento con la policia','Violencia contra civiles','No aplica')
    #Input COMBO
    motivo_combo=sg.Combo(motivo_opc,key="MOTIVO")
    #Botón para grabar los datos en mi base de datos
    btn_grabar=sg.Button("GRABAR",key="BTN_GRABAR")
    #Botón para regresar al menu
    btn_rmenu=sg.Button("REGRESAR A MENU",key="BTN_RMENU")
    
    #Layout del formulario con formato PREGUNTA-RESPUESTA
    layout_formulario=[[descripcion],[genero_texto,genero_combo],[edad_texto,edad_spin],[experiencia_texto,experiencia_combo],
            [año_texto,año_combo],[denuncia_texto,denuncia_combo],[estado_texto,estado_combo],
            [motivo_texto,motivo_combo],[btn_grabar,btn_rmenu]]
    
    #Creación del frame del formulario
    frame_formulario=sg.Frame("Formulario", layout_formulario, key="FRAME_FORMULARIO", visible="True")
    return frame_formulario

#Función para validar el ingreso del usuario por medio de una contraseña
def validar_ingreso():
    texto_password = sg.Text("Teclea la contraseña " )
    #Input con caracteres de tipo * para evitar que se vea lo que se escribe
    password = sg.Input(password_char = "*" , key = 'PASSWORD', text_color = "black")
    #Botón para verificar contraseña
    b1 = sg.Button("Validar Ingreso", key = 'BTN_PASSWORD',
                   pad = ((135, 100), (20, 20)) , button_color = "lightblue", border_width = 5 )
    #Imagen de un candado
    imagen = sg.Image(filename="candado2.png")
    #Layput de la ventana de contraseña
    layout =  [[texto_password, password ],
             [b1],
             [imagen]]
                         
    #crear el frame - ventana para ingresar los datos del password
    frame_password = sg.Frame("Validar Ingreso", layout, key = "FRAME_PASSWORD", visible = True)
                         
    return frame_password 

#Creación del menú
def menu():
    
    #Uso de imagenes como botones
    #Formulario
    b1 = sg.Button( key = "BTN_FORMULARIO", border_width = 5, image_filename = "formulario2.png",size=(10,10) ) 
    #Link a maps
    b2 = sg.Button( key = "BTN_MAPS", border_width = 5, image_filename = "maps2.png",size=(10,10) ) 
    #Estadisticas de mi base de datos
    b3 = sg.Button( key = "BTN_ESTADISTICAS", border_width = 5, image_filename = "reporte2.png",size=(10,10) ) 
    #Link a video
    b4 = sg.Button( key = "BTN_VIDEO", border_width = 5, image_filename = "video2.png",size=(10,10) ) 
    #Estadisticas de la base de datos agena
    b5 = sg.Button( key = "BTN_ESTADISTICAS2", border_width = 5, image_filename = "reporte3.png",size=(10,10) )
    #Salida
    b6= sg.Button( key = "BTN_SALIDA", border_width = 5, image_filename = "salida2.png",size=(10,10) )
    
    #Layout del menú
    layout_menu = [ [b1, b2 ] ,
                    [b3, b4],
                    [b5, b6]]
    
    #Frame del menú
    frame_menu = sg.Frame("Menu", layout_menu, key = "FRAME_MENU", visible = True)
    
    return frame_menu

 

#Uso del tema LightBlue3 para darle color a las ventanas
sg.theme("LightBlue3")

#Variable form que almacena el frame del formulario
form=formulario()

#Variable opc que almacena el frame del menú
opc = menu()

#Función que manda a llamar la ventana de contraseña
def password_window():
    #llamamos al frame de contraseña
    contraseña=validar_ingreso()
    #Creación de layout
    layout_contra=[[contraseña]]
    #Creación de ventana de contraseña
    window_contra= sg.Window("Emiliano Bizet", layout_contra,size=(600,500),location=(0,0))

    while True:
        event, values=window_contra.read()
        #Si el usuario cierra la ventana regresamos 0
        if event==sg.WIN_CLOSED:
            return 0
        #Usuario oprime botón para validar contraseña
        elif event =='BTN_PASSWORD':
                password= values["PASSWORD"]
                #Si la contraseña es correcta cerramos ventana y regresamos 1
                if password=="123":
                    sg.popup("Bienvenido Emiliano")
                    window_contra.close() 
                    return 1
                #Si la contraseña es incorrecta mandamos mensaje para intentar nuevamente 
                #Se repite el while
                else:
                    sg.popup("Contraseña incorrecta, \nintente nuevamente")
                    
#Función para la reación de la ventana del formulario                    
def formulario_window():
    #Creación del layout, recibe el frame del formulario
    layout_formulario=[[form]]
    #Creación de la ventana
    window_formulario= sg.Window("Emiliano Bizet", layout_formulario,size=(600,500),location=(0,0))
    #Inciamos el ciclo
    while True:
        event, values=window_formulario.read()
        #Usuario cierra la ventana
        if event==sg.WIN_CLOSED:
                return
        #Usuario oprime el botón para grabar datos
        if event=="BTN_GRABAR":
            #Abrimos nuestra base de datos
            with open("MiBase.csv","a") as archivo:
                genero=values["GENERO"]
                edad=values["EDAD"]
                experiencia=values["EXPERIENCIA"]
                año=values["AÑO"]
                denuncia=values["DENUNCIA"]
                estado=values["ESTADO"]
                motivo=values["MOTIVO"]
                #Creamos el sting para enviar los datos
                row=genero + "," + str(edad) + "," + experiencia + "," + str(año) + "," + denuncia + "," + estado + "," + motivo + "\n"
                #Escribimos los datos en la base
                archivo.write(row)
                sg.popup("Datos guardados correctamente")
                #Cerramos el formulario
                window_formulario.close()
                return
        #Si oprime regresar al menú, se cierra el formulario
        elif event=="BTN_RMENU":
            window_formulario.close()
            return

#Función para la creación de la ventana del menú, recibe el valor que regresamos en la función de contraseña
def menu_window(contra):
    #Si el valor es igual a 0 la función termina
    if contra == 0:
        return 0
    #Si el valor es diferente de 0 es que la contraseña fue correcta
    else:
        #Creamos el layout con el frame del menú
        layout_menu=[[opc]]
        #Creamos la ventana
        window_menu= sg.Window("Emiliano Bizet", layout_menu,size=(600,720),location=(0,0))

        while True:
            event, values=window_menu.read()
            #Usuario cierra la ventana
            if event==sg.WIN_CLOSED:
                break
            #Oprime botón de estadisicas de nuestra base de datos
            if event=="BTN_ESTADISTICAS":
                #leemos la base de datos
                df=pd.read_csv("MiBase.csv")
                #Contamos las veces que aparece cada estado
                edos={}
                for i in df.iloc[:,5]:
                    if i in edos:
                        edos[i]+=1
                    else:
                        edos[i]=1
                print("Crimenes por estado")
                for i in edos:
                    print(i,":",edos[i])
                #Contamos las veces que aparece cada genero
                print('Crimenes por género:\n', df['GENERO'].value_counts(sort=True))
                #Contamos las veces que la gente denunció o no
                print('Denuncias: \n', df.iloc[:,4].value_counts()) 
                #Contamos los tipos de crimenes
                crim={}
                for i in df.iloc[:,6]:
                    if i in crim:
                        crim[i]+=1
                    else:
                        crim[i]=1
                print("Conteo por tipo de crimen")
                for i in crim:
                    print(i,":",crim[i])
            
            #Si el usuario oprime el botón de Maps lo manda a un link externo con los lugares en los que puede denunciar
            elif event=="BTN_MAPS":
                webbrowser.open("https://www.google.com/maps/search/ministerio+publico+monterrey/@25.7119864,-100.3760887,13z/data=!3m1!4b1?hl=es-419")
            
            #Si el usuario oprime el botón de video lo manda a un link externo con un documental
            elif event=="BTN_VIDEO":
                webbrowser.open("https://www.youtube.com/watch?v=pCSwRPSvgY4")    
            
            #Si el usuario oprime el botón del formulario abre el formulario
            elif event=="BTN_FORMULARIO":
                formulario_window()

            #Si el usuario oprime el botón de salida se rompe el ciclo y termina el programa
            elif event =="BTN_SALIDA":
                sg.popup("Adios")
                break
            #Generamos las estadisticas de la base de datos agena
            elif event == "BTN_ESTADISTICAS2":
                df=pd.read_csv("128_Informes-PF.csv")
                #Contamos los municipios
                print('Crimenes por municipio:\n', df['Municipio'].value_counts(sort=True))
                
                #Contamos los estados
                edos={}
                for i in df.iloc[:,5]:
                    if i in edos:
                        edos[i]+=1
                    else:
                        edos[i]=1
                print("Crimenes por estado")
                for i in edos:
                    print(i,":",edos[i])
                #Contamos los tipos de crimen
                print('Tipos de crimen: \n', df["Tipo de evento"].value_counts()) 
                
                
                
                       

        
menu_window(password_window())               

