print("""
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/\n""")

print("""Bem vindo a ilha do Tesouro!

Seu obejetivo é encontrar o tesouro de Askanor "O Pirata".
Para conseguir este feito é necessário ter a coragem que poucos marujos possuem.
\n
""")

escolha = int(input("""[1] - Para iniciar o jogo
[2] - Para sair\n
Escolha um numero: """))

if escolha == 1:
    print("""\n------------------------------------------------------------------------------------------------------------------------------\n
Finalmente estamos aqui na ilha de Askanor, onde os perigos rodeiam os caminhos e as surpresas espreitam a cada esquina.

       _,-._
        ; ___ :           ,------------------------------.
    ,--' (. .) '--.__    | O tesouro que procuramos está  |
  _;      |||        \   |  escondido na ilha, há muitos  |
 '._,-----''';=.____,"   |  riscos e perigos a frente.    |
   /// < o>   |##|       |                                |
   (o        \`--'       //`-----------------------------'
  ///\ >>>>  _\ <<<<    //
 --._>>>>>>>><<<<<<<<  / 
 ___() >>>[||||]<<<<
 `--'>>>>>>>><<<<<<<
      >>>>>>><<<<<<
        >>>>><<<<<
         >>ctr<<

Mas todo pirata sabe que quanto maior for o risco maior será a recompensa.

Não é verdade pirata?

Escolha com sabedoria o seu caminho!\n
------------------------------------------------------------------------------------------------------------------------------
\n""")

    escolha2 = int(
        input("""Há 3 caminhos a sua frente:\n
[1] - Píer abandonado
[2] - Casabre estranho na mata
[3] - Pilha de barcos\n
Escolha um número: """),
            )

    if escolha2 == 1:
        print("""\nNão há nada aqui que valha o seu tempo.
Aparentemente o píer está abandonado.""")

    elif escolha2 == 2:
        print("""------------------------------------------------------------------------------------------------------------------------------\n
Você """)