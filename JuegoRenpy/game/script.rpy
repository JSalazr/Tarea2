# eg. image eileen happy = "eileen_happy.png"
image presentador = im.FactorScale("Presentador.png", 3.0)
image Nino = ("E/nino_incredulo.png")
image Lata = im.Scale("lata.jpg", 200, 200)
image Tv = im.Scale("tve.png", 250, 200)
image Mac = im.Scale("macintosh.png", 200, 200)
image Map = im.Scale("map.png", 200, 200)
image Bmw = im.Scale("bmw.png", 300, 150)
image dinero = im.Scale("dinero.png", 200, 200)
image fondo = im.Scale("fondo.jpg", 1000, 600)
image jugador = im.FactorScale("Jugador.png", 1.1)
#aqui se le dan las imagenes que aparecera en el juego JuanCarranza

# Declare characters used by this game.
define e = Character('Presentador', color="#c8ffc8") #Aqui declaramos los personajes, sus nombres y el color en el cual aparecera. JonathanSalazar
define f = Character('Modelo', color="#DF0174")
define n = Character('Carlos (Vendedor de Chicles)', color="#c8c8ff")

# La ayuda para las estructuras y demas que usamos para la elaboracion del codigo viene de http://www.renpy.org/wiki/renpy/spa/doc/tutorials/Tutorial_Web_de_Ren%27Py
#Edgar Contreras, Jonathan Salazar, Juan Carranza
# The game starts here.
label start:
    $ Puntos_Juego = 0       #Usamos la variable para poder crear distintos finales dependiendo de la cantidad de puntos acumulada a traves del curso del juego. EdgarContreras
    $ RespuestaX = "UFF NO! INCORRECTO! RESPONDIO COMO USTED Y COMO YO TELEVIDENTE"
    $ RespuestaY = "EXCELENTE MI QUERIDO COMPATRIOTA"
    $ RespuestaC = False
    
    scene fondo #A partir de aqui se empiezan a aparecer los personajes JuanCarranza
    
    show presentador
    
    play music "Musica.mp3"
   
    e  "Bienvenidos ciudadanos Hondureños de Honduras!" 
   
    play sound "Aplauso.mp3" 
   
    e  "Esto es Equis Cero No da Dinero"
        
    $ p = renpy.input("Cual es el nombre de nuestro participante? ") #Con esto pedimos al usuario que eliga su nombre para dar una mejor experiencia.Edgar Contreras
    
    show presentador:                          #Ponemos las imagenes de los jugadores en lados distintos. Edgar Contreras
        left
    show jugador:
        right
        
    p  "Hola! Es un placer poder -"
    
    e "Muy bien! Un placer %(p)s, continuemos!" 
    
    e  "En este juego de preguntas muy original!"
    
    e  "El participante debe elegir la  mejor respuesta segun sus conocimientos! Entendido %(p)s?"
    
    p "Tengo una pregunta..."
     
    
    jump Primera_Ronda               

label Primera_Ronda:
    
    e "Preguntas al final, por favor."
    
    play sound "Aplauso.mp3" 
    
    e "Muy bien! Como se encuentra el publico? " 
    
    e "Muy bien seguiremos con la primera pregunta del dia, por favor mostrar la pregunta #1."
    
    hide jugador
    
    e "Si Timmy es el sobrino de mi esposa, que es Tommy de mi?"
    
    hide presentador
    
    menu:                  #Las opciones del menu sumaran puntos para el usuario y tambien trazaran el camino del juego.EdgarContreras
        "No se puede Saber":
            $Puntos_Juego += 5
            $RespuestaC = True      #La variable de respuesta correcta la usamos para desencadenar procesos distintos a los que se dan con las respuestas incorrectas.EdgarContreras
            play sound "Sonido correcto.mp3"
            jump Segunda_RondaA         #Usamos el salto para arrancar la segunda pregunta y ordenar de mejor manera el curso del juego.EdgarContreras
        "Tambien mi sobrino":                                         
            play sound "Sonido incorrecto.mp3"
            jump Segunda_RondaA
        "Mi mejor amigo":
            play sound "Sonido incorrecto.mp3"
            jump Segunda_RondaA
        
        
   
label Segunda_RondaA:
    
     
    if RespuestaC == False:     
        e "%(RespuestaX)s"
        #Dependiendo el valor de la variable "RespuestaC" se desencadenara un proceso acorde a la respuesta del usuario, usamos "if" para trazar los distintos
        #Sucesos que se pueden dar. EdgarContreras 
    if RespuestaC == True:
        e "%(RespuestaY)s"
        $ RespuestaC = False #Re-declaramos la variable como falsa para poder usarla nuevamente mas tarde y asi no crear conflictos en si la respuesta es correcta
                            # O no. Esto para no tener que declarar la variable como falsa siempre que la respuesta sea incorrecta.Edgar Contreras
        
    show presentador:
        left
    show jugador:
        right

        
    e "Usted lleva %(Puntos_Juego)d puntos señor %(p)s" #Esto lo usamos para notificar al usuario cual es su desempeño.EdgarContreras
      
    e "Participante como se siente? Listo para seguir?"
      
    p "Bery gud, yo me sentir bien" 
      
            #A partir de aqui la estructura del codigo no cambia, solamente el texto y el valor de las variables, para darle fluides al juego.
            #Esto sucede hasta la hora de elegir el final del juego.EdgarContreras
    e "Eehhh muy bien..."
    
    play sound "Aplauso.mp3" #se le agregan efectos de sonidos para ambientarse en el juego JuanCarranza
    
    e "Vamos con la segunda pregunta!! Que grite el publico! Ahora una mas dificil! Pondremos a prueba su analisis"
    
    hide jugador
    
    e "En cual de estos paises no hay ningun desierto?"
    
    hide presentador
    
    menu:
        "Honduras ":
            play sound "Sonido incorrecto.mp3"
            jump Tercera_R
        "Alemania ":
            $Puntos_Juego += 5
            $RespuestaC = True
            play sound "Sonido correcto.mp3"
            jump Tercera_R
        "Mexico ":
            play sound "Sonido incorrecto.mp3"
            jump Tercera_R
              
label Tercera_R:
         
    if RespuestaC == False:   
        e "%(RespuestaX)s"
            
    if RespuestaC == True:
        e "%(RespuestaY)s"
        $ RespuestaC = False
    
    show presentador:
        left
    show jugador:
        right
    
    e "Usted lleva %(Puntos_Juego)d %(p)s"
    
    e "Muy bien, continuemos! La tercera pregunta dice asi:"
    
    hide jugador
    
    e "Cual de estos lugares tiene la mayor cantidad de ganadoras del titulo 'Miss Universo'?"
    
    hide presentador
    
    menu:
        "Colombia":
            play sound "Sonido incorrecto.mp3"
        "Mexico":
            play sound "Sonido incorrecto.mp3"
        "La tierra":
            $Puntos_Juego +=5
            play sound "Sonido correcto.mp3"
            $RespuestaC= True
            

            
    if Puntos_Juego == 15:
        jump Cuarta_RB                  #Aqui dividimos los caminos que puede tomar el juego abriendo un set de preguntas alterno.Edgar Contreras
            
label Cuarta_RA:
         
    if RespuestaC == False:   
        e "%(RespuestaX)s"
            
    if RespuestaC == True:
        e "%(RespuestaY)s"
        $ RespuestaC = False
        
    show presentador:
        left
    show jugador:
        right
    
    e "Usted lleva %(Puntos_Juego)d!"
    
    e "Pues bien, solo faltan 2 preguntas mas!"
    
    e "Como esta nuestro amigo?"
    
    p "Bien bien! Listo para la recta final."
    
    e "Muy bien la pregunta dice asi:"
    
    hide jugador
    
    e "De que color se ven los camaleones en el espejo?" 
    
    hide presentador
    
    menu:
        "Verde":
            $Puntos_Juego +=5
            play sound "Sonido correcto.mp3"
            $RespuestaC= True
        "Transparente":
            play sound "Sonido incorrecto.mp3"
        "Color Espejo":
            play sound "Sonido incorrecto.mp3"
            
         
    if RespuestaC == False:   
        e "%(RespuestaX)s"
            
    if RespuestaC == True:
        e "%(RespuestaY)s"
        $ RespuestaC = False
        
    show presentador:
        left
    show jugador:
        right
    
    e "Usted lleva %(Puntos_Juego)d."
        
    e "Bien estamos llegando al final de este fantastico juego!"
    
    e "Como se siente?"
    
    p "No pues, hemos hecho lo que nos dijo el profe y gracias a Dios todo bien!"
    
    e "Ok,"
    
    e "La ultima pregunta dice asi:"
    
    hide jugador
    
    e "Como me llamo yo?"
    
    hide presentador
    
    menu:
        "Presentador":
            $Puntos_Juego += 5
            play sound "Sonido correcto.mp3"
            $RespuestaC= True
        "No se":
            play sound "Sonido incorrecto.mp3"
        "Kamil, el todopoderoso":
            play sound "Sonido incorrecto.mp3"
            
    jump final

label Cuarta_RB:
         
    if RespuestaC == False:   
        e "%(RespuestaX)s"
            
    if RespuestaC == True:
        e "%(RespuestaY)s"
        $ RespuestaC = False
    
    show presentador:
        left
    show jugador:
        right
    
    e "Usted lleva %(Puntos_Juego)d "
    
    e "Ya que su desempeño a superado la expectativas nosotros le realizaremos preguntas de mayor nivel"
    
    e "Estan listoos!?"
    
    p "no"
    
    e "callate"
    
    e "Dos preguntas mas... Esta pregunta dice asi"
    
    hide jugador
    
    e "En donde esta lo que los Estado Unidenses llaman 'Hell' ?"
    
    hide presentador
    
    menu:
        "Debajo de la Tierra":
            play sound "Sonido incorrecto.mp3"
        "Mexico":
            play sound "Sonido incorrecto.mp3"
        "Michigan":
            $Puntos_Juego += 5
            play sound "Sonido correcto.mp3"
            $RespuestaC= True
            
    show presentador:
        left
    show jugador:
        right
    
    e "Usted lleva %(Puntos_Juego)d "
    
    e "Ahora finalmente la ultima pregunta!!"
    
    p "Tengo que ser siempre el mejor!"
    
    e "Por haber llegado al maximo nivel al responder correctamente esta pregunta te llevas UN MILLON DE DOLARES"
    
    hide jugador
    
    e "Cual es la masa del Sol?"
    
    hide presentador
    
    menu:
        "12 kg":
            play sound "Sonido incorrecto.mp3"
        "45 x 10^28 Kg":
            play sound "Sonido incorrecto.mp3"
        "12,45 x 10^52 kg":
            play sound "Sonido incorrecto.mp3"
        "1,989 x 10^30 kg":
            $Puntos_Juego += 5
            play sound "Sonido correcto.mp3"
            $RespuestaC = True 
        "525,53 x 10^12 Kg":
            play sound "Sonido incorrecto.mp3"
            
    if RespuestaC == False:   
        e "%(RespuestaX)s"
            
    if RespuestaC == True:
        e "%(RespuestaY)s"
        $ RespuestaC = False
            
label final:

    show presentador:
        left
    show jugador:
        right
    
    e "Y su resultado final es..!!!!!"
            
    e "%(Puntos_Juego)d puntos!"
    
    e "Y su premio es..."
    
    e "Pero antes permitannos conocer mejor a nuestro concursante! Y para eso hemos traido desde muy lejos al fan #1 de nuestro parcticipante!"
    
    e "Con ustedes CARLOS!"
    
    hide presentador
    show fondo
    show Nino:
        left
    n "Holi"
    
    p "Hola señor quien es usted?"
    
    n "Soy Carlos,y tengo un master en ventas"
    
    p "Woow"
    
    e "Ahora nuestro nuevo amigo le tiene una pregunta a %(p)s ! Vamos compañero Carlos"
    
    n "Señor %(p)s en su larga carrera respondiendo preguntas que es para usted el juego de 'Responder Preguntas'"
    
    e "Algunas personas consideran esto como algo de vida o muerte, pero te aseguro que es mucho mas que eso"
    
    n "#Respect"
    
    hide nino
    
    show presentador:
        left
    
    p "Bueno despues de ese momento muy intimo no gay... Procedamos"
    
    p "Y SU PREMIO ES...!"
   
    
    
    hide presentador
    

    if Puntos_Juego == 25: #En esta parte se cuentan la cantidas de puntos que el jugdor adquirio, y dependiendo de eso el final sera diferente. Y usamos un if para poder lograrlo. JonathanSalazar
        jump ending6
        $Puntos_Juego += 35
    
    elif Puntos_Juego == 20:
        jump ending2
        $Puntos_Juego += 35
    
    elif Puntos_Juego == 15:
        jump ending3
        $Puntos_Juego += 35
    
    elif Puntos_Juego ==10:
        jump ending4
        $Puntos_Juego += 35
    
    elif Puntos_Juego == 5:
        jump ending5
        $Puntos_Juego += 35
    
    else:
        jump ending1
        
        
label ending1: #Y aqui tenemos los diferentes finales con sus dialogos. JonathanSalazar
    show Lata:
        right
    p "Una lata de maiz!"
    play sound "Aplausolargo.mp3"
    show presentador
    e "Le damos las gracias a nuestro concursante por participiar en otra edicion de Equis Cero No da Dinero."
    
return

label ending2:
    show Tv:
        right
    p "Un Televisor! Felicidades!"
    play sound "Aplausolargo.mp3"
    show presentador
    e "Le damos las gracias a nuestro concursante por participiar en otra edicion de Equis Cero No da Dinero."
    
return    
    
label ending3:
    show Mac: 
        right
    p "Una Computadora Mac!"
    play sound "Aplausolargo.mp3"
    show presentador
    e "Le damos las gracias a nuestro concursante por participiar en otra edicion de Equis Cero No da Dinero."
    
return

label ending4:
    show Map: 
        right
    p "Un viaje por toda Europa!"
    play sound "Aplausolargo.mp3"
    show presentador
    e "Le damos las gracias a nuestro concursante por participiar en otra edicion de Equis Cero No da Dinero."
    
return

label ending5:
    show Bmw:
        right
    p "Un Carro 2015! Marca BMW! Muchas Felicidades!"  
    play sound "Aplausolargo.mp3"
    show presentador
    e "Le damos las gracias a nuestro concursante por participiar en otra edicion de Equis Cero No da Dinero."
    
return
    
label ending6: 
    show dinero: 
        right
    p "Un Millon de Dolares!"
    play sound "Aplausolargo.mp3"
    show presentador
    e "Le damos las gracias a nuestro concursante por participiar en otra edicion de Equis Cero No da Dinero."
    
return
