#es_3C-2

voto_converter: int = int(input("Inserisci il voto di laurea: "))

match voto_converter:

    case voto_converter if voto_converter >=106 and voto_converter <=110:
        print("Voto GPA: 4.0")
    case voto_converter if voto_converter >=101 and voto_converter <=105:
        print("Voto GPA: 3.7")
    case voto_converter if voto_converter >=96 and voto_converter <=100:
        print("Voto GPA: 3.3")
    case voto_converter if voto_converter >=91 and voto_converter <=95:
        print("Voto GPA: 3.0")
    case voto_converter if voto_converter >=86 and voto_converter <=90:
        print("Voto GPA: 2.7")
    case voto_converter if voto_converter >=81 and voto_converter <=85:
        print("Voto GPA: 2.3")
    case voto_converter if voto_converter >=76 and voto_converter <=80:
        print("Voto GPA: 2.0")
    case voto_converter if voto_converter >=70 and voto_converter <=75:
        print("Voto GPA: 1.7")
    case voto_converter if voto_converter >=66 and voto_converter <=69:
        print("Voto GPA: 1.0")
    case _:
        print("Voto non valido")