# equivalence partition is the method to divide the diferent data into equivalence classes
# boundary testing is the process of testing between extreme ends


# class Circle:
#     def describe_circle(self, colour, radius):
#         aria = radius*radius*3.14
#         print(f'aria is: {aria}, and the colour is {colour}')
#
#     def diametrer(self, radius):
#         print(f'diameter is: 2x{radius}')
#
#     def circumferinta(self, radius):
#         print(f'circumferinta este: 2*3.14*{radius}')
#
# circle_object = Circle()
# circle_object.describe_circle(colour='red', radius= 5)
# circle_object.diametrer(radius=5)
# circle_object.circumferinta(radius=5)

# class Dreptunghi:
#     def descriere(self, culoare):
#         print(culoare)
#
#     def aria(self, lungime, latime):
#         aria = lungime*latime
#         print(f'Aria este: {aria}')
#
#     def petrimetru(self, lungime, latime):
#         perimetru = 2*lungime+2*latime
#         print((f'perimetrul este: {perimetru}'))
#
#     def schimba_culoare(self, culoare):
#         noua_culoare = culoare = 'verde'
#
# obiect_dreptunghi = Dreptunghi()
# obiect_dreptunghi.descriere(culoare='galben')
# obiect_dreptunghi.aria(lungime=9, latime=5)
# obiect_dreptunghi.petrimetru(lungime=9, latime=5)
# obiect_dreptunghi.schimba_culoare(culoare= 'verde')

# class Angajat:
#     def descriere(self, nume,prenume, salariu):
#         print(f'Numele este {nume}, prenumele este {prenume}, salariul este {salariu}')
#
#     def nume_complet(self, nume, prenume):
#         print(f'numele complet este {nume} {prenume}')
#
#     def salariu_lunar(self, salariu):
#         print(f'salariul lunar este {salariu}')
#
#     def salariu_anual(self, salariu):
#         total_salariu = 12*salariu
#         print(f'salariul anual este {total_salariu}')
#     def marire_salariu(self, salariu):
#         marirea = 3500*10/100
#         print(f'marirea de salariu este de {marirea} lei')
#
# muncitor_angajat = Angajat()
# muncitor_angajat.descriere(nume='Popescu', prenume= 'Ion', salariu= 3500)
# muncitor_angajat.nume_complet(nume='Popa', prenume='Maria')
# muncitor_angajat.salariu_anual(salariu=3500)
# muncitor_angajat.salariu_lunar(salariu=3500)
# muncitor_angajat.marire_salariu(salariu=3500)


# class Cont:
#     def afisare_sold(self, titular_cont, iban,sold):
#         print(f'titularul {titular_cont} are in contul {iban} suma de {sold}')
#
#     def debitare_cont(self, suma):
#         print(f's-a debitat suma de {suma}')
#
#     def creditare_cont(self, suma):
#         print(f's-a creditat contul cu suma {suma}')
#
# optiuni_cont = Cont()
# optiuni_cont.afisare_sold(titular_cont= 'Ion Costel', iban='ro57ingb0000999912345678', sold=1352.5)
# optiuni_cont.debitare_cont(suma=115.62)
# optiuni_cont.creditare_cont(suma=2556)
from datetime import date


class Factura:
    while True:
        seria_facturii = 'FACT'
        data_facturii = date.today()
        numar_factura = 1
        print(f'factura cu seria{seria_facturii}, numarul {numar_factura}, din data de {data_facturii}')
        numar_factura += 1


    def schimba_cantitatea(self, cantitate):
        print(f'cantitatea este {cantitate}')

    def schimba_pretul(self, pret):
        print(f'pretul este {pret}')

    def schimba_nume_produs(self, nume):
        print(f'nume produs: {nume}')

info_factura = Factura()
info_factura.schimba_cantitatea(cantitate=5)
info_factura.schimba_pretul(pret=152)
info_factura.schimba_nume_produs(nume='masinuta')

