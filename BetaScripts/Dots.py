import nuke

def Dots():
    dotList,dotListX= [],[]
    Dsize = int(nuke.toNode("preferences")['dot_node_scale'].value()*12)
    nodes = nuke.selectedNodes()
    count = 0
    same = 1
    old = ""
    for selected in nodes:
        selectedX,selectedY = int(selected.xpos()),int(selected.ypos())
        selectedW,selectedH = int(selected.screenWidth()),int(selected.screenHeight())

        # checking inputs and assigning variables
        try:# check if input 0 is exist
            A = selected.input(0)
            AX = int(A.xpos())
            AY = int(A.ypos())
            AW = int(A.screenWidth())
            AH = int(A.screenHeight())
            AClass = A.Class()
            if count == 0:
                old = A
                count = count+1
            else:
                if old != A:
                    same = 0
        except:
            AX,AY = int(selected.xpos()),int(selected.ypos())
            AW,AH = int(selected.screenWidth()),int(selected.screenHeight())
            AClass = "no classs"
        try:# check if input 1 is exist
            B = selected.input(1)
            BX,BY = int(B.xpos()),int(B.ypos())
            BW,BH = int(B.screenWidth()),int(B.screenHeight())
            BClass = B.Class()
            #print (" Input 1 found   " + B['name'].value())
        except:
            BX,BY = int(selected.xpos()),int(selected.ypos())
            BW,BH = int(selected.screenWidth()),int(selected.screenHeight())
            BClass = "no classs"
            #print (" no input1 found        ")
        try:# check if input 2 is exist
            C = selected.input(2)
            CX,CY = int(C.xpos()),int(C.ypos())
            CW,CH = int(C.screenWidth()),int(C.screenHeight())
            CClass = C.Class()
            #print (" Input 2 found   " + C['name'].value())
        except:
            pass



        # setting position
        if B and not C:  # two inputs found
           
            # 'normal merge case'
            create_dot_for_B = True  
            # Create a dot only if there is no node already in position where dot should appear
            if B is not None:
                BY = int(B.ypos())
                BH = int(B.screenHeight())
                if B.Class() == "Dot" and BY == selectedY + selectedH/2 - Dsize/2:
                    create_dot_for_B = False
                # Comprobar si el nodo B no es un Dot pero su centro en Y coincide con el centro en Y del nodo seleccionado
                elif BY + BH/2 == selectedY + selectedH/2:
                    create_dot_for_B = False

            if create_dot_for_B:
                Dot = nuke.nodes.Dot()
                Dot.setInput(0, B)
                selected.setInput(1, Dot)
                Dot.setXYpos(int(BX+BW/2-Dsize/2), int(selectedY+selectedH/2-Dsize/2))

            if A is not None:  # Asegurarse de que A no es None
                AX = int(A.xpos())
                if A.Class() == "Dot":
                    selected.knob("xpos").setValue(int(AX-selectedW/2+Dsize/2))
                else:
                    selected.knob("xpos").setValue(int(AX))

            #print('two inputs found')

       
        elif C:#three inputs found
            if "Scanline" in selected.Class():
                if BClass != "no classs":
                    if B.Class() == "Dot":
                        selected.setXYpos(int(BX-selectedW/2+Dsize/2), int(selectedY))
                    else:
                        selected.setXYpos(int(BX), int(selectedY))

                # Comprobar para C antes de crear y conectar un nuevo Dot
                # Create a dot only if there is no node already in position where dot should appear
                create_dot_for_C = True
                if C is not None:
                    CY = int(C.ypos())
                    CH = int(C.screenHeight())
                    if C.Class() == "Dot" and CY == selectedY + selectedH/2 - Dsize/2:
                        create_dot_for_C = False
                    elif CY + CH/2 == selectedY + selectedH/2:
                        create_dot_for_C = False

                if create_dot_for_C:
                    dot = nuke.nodes.Dot(xpos=CX+CW/2-Dsize/2, ypos=selectedY+selectedH/2-Dsize/2)
                    dot.setInput(0, C)
                    selected.setInput(2, dot)

                # Comprobar para A antes de crear y conectar un nuevo Dot
                # Create a dot only if there is no node already in position where dot should appear
                create_dot_for_A = True
                if A is not None and AClass != "no classs":
                    AY = int(A.ypos())
                    AH = int(A.screenHeight())
                    if A.Class() == "Dot" and AY == selectedY + selectedH/2 - Dsize/2:
                        create_dot_for_A = False
                    elif AY + AH/2 == selectedY + selectedH/2:
                        create_dot_for_A = False

                if create_dot_for_A:
                    dot = nuke.nodes.Dot(xpos=AX+AW/2-Dsize/2, ypos=selectedY+selectedH/2-Dsize/2)
                    dot.setInput(0, A)
                    selected.setInput(0, dot)

                #print("Scanline")

            if "Merge" in selected.Class() or "Roto" in selected.Class()or "Keymix" in selected.Class():
                
                if A.Class()== "Dot":
                    selected.knob("xpos").setValue(int(AX-selectedW/2+Dsize/2))
                else:        
                    selected.knob("xpos").setValue(int(AX))
                
                create_dot_for_C = True
                if C.Class() == "Dot" and CY == selectedY + selectedH/2 - Dsize/2:
                    create_dot_for_C = False
                elif CY + CH/2 == selectedY + selectedH/2:
                    create_dot_for_C = False
                
                if create_dot_for_C:
                    # crear el nodo DOT a la derecha
                    dot = nuke.nodes.Dot(xpos=CX+CW/2-Dsize/2, ypos=selectedY+selectedH/2-Dsize/2)
                    # conectar el nodo dot al output del nodo anterior
                    dot.setInput(0,C)
                    # conectar el nodo dot al input  del nodo seleccioniado
                    selected.setInput(2,dot)

                create_dot_for_B = True
                if B.Class() == "Dot" and BY == selectedY + selectedH/2 - Dsize/2:
                    create_dot_for_B = False
                # Comprobar si el nodo B no es un DOT y su centro en Y es el mismo que el centro del nodo seleccionado
                elif BY + BH/2 == selectedY + selectedH/2:
                    create_dot_for_B = False

                if create_dot_for_B:
                    # crear el nodo DOT a la derecha
                    dot = nuke.nodes.Dot(xpos=BX+BW/2-Dsize/2, ypos=selectedY+selectedH/2-Dsize/2)
                    # conectar el nodo dot al output del nodo anterior
                    dot.setInput(0,B)
                    # conectar el nodo dot al input del nodo seleccionado
                    selected.setInput(1,dot)

                #print ('three input found')

        else:#one input found
            #print ('one input found')
            Dot = nuke.nodes.Dot()
            Dot.setInput(0,A)
            selected.setInput(0,Dot)        
            Dot.setXYpos(int(selectedX+selectedW/2-Dsize/2),int(AY+AH/2-Dsize/2) )
            dotList.append(Dot)
            dotListX.append(Dot.xpos())