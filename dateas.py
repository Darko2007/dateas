# -*- coding: utf-8 -*-

from colorama import Back, Fore, init
import urllib2

init(autoreset=True)

def dateas():
    while True:
       print '''
########    ###   ##### ######   ###    #####
 #      #  #   #    #   #       #   #  #     #
 #      # #     #   #   #      #     # #
 #      # #     #   #   ###    #     #  #####
 #      # #######   #   #      #######       #
 #      # #     #   #   #      #     # #     #
########  #     #   #   ###### #     #  #####
Version:1.5
Codigo escrito por: Angelo Mass - Darko

El autor no se hace responsable por el uso que le den a la herramienta.

Investigar a personas en venezuela.

1) Investigar por nombre completo.
2) Investigar por primer nombre y primer apellido.
3) Salir.
'''
       opcion = raw_input('Darko@Dateas$ ')
       if opcion == '1':
           investigar_nombre_completo()
       elif opcion == '2':
           investigar_primernombre_primerapellido()
       elif opcion == '3':
           exit()
       else:
           print Fore.RED + '[*]Ingrese un argumento valido.'

def investigar_nombre_completo():
    print '''
########    ###   ##### ######   ###    #####
 #      #  #   #    #   #       #   #  #     #
 #      # #     #   #   #      #     # #
 #      # #     #   #   ###    #     #  #####
 #      # #######   #   #      #######       #
 #      # #     #   #   #      #     # #     #
########  #     #   #   ###### #     #  #####
Version:1.5
Codigo escrito por: Angelo Mass - Darko
'''
    nombre_uno = raw_input('Primer nombre: ')
    nombre_dos = raw_input('Segundo Nombre: ')
    apellido_uno = raw_input('Primer Apellido: ')
    apellido_dos = raw_input('Segundo Apellido: ')
    formatear = 'https://m.dateas.com/es/consulta_venezuela?name=' + apellido_uno + '+' + apellido_dos + '+' + nombre_uno + '+' + nombre_dos + '&cedula='
    url = formatear
    try:
        hdr = {'User-Agent':'Mozilla/5.0'}
        req = urllib2.Request(url,headers=hdr)
        html = urllib2.urlopen(req).read()
        if html.find('<h2 class="title">No') == -1:
            print Fore.GREEN + '[*]Se ha encontrado informacion de la persona. Consulte la siguiente url: ' + url
        else:
            print Fore.RED + '[*]No se ha encontrado informacion de la persona.'
    except:
        print Fore.YELLOW + '[*]Ha ocurrido un problema al tratar de consultar la informacion. Intente nuevamente.'

def investigar_primernombre_primerapellido():
    print '''
########    ###   ##### ######   ###    #####
 #      #  #   #    #   #       #   #  #     #
 #      # #     #   #   #      #     # #
 #      # #     #   #   ###    #     #  #####
 #      # #######   #   #      #######       #
 #      # #     #   #   #      #     # #     #
########  #     #   #   ###### #     #  #####
Version:1.5
Codigo escrito por: Angelo Mass - Darko
'''
    nombre_uno = raw_input('Primer nombre: ')
    apellido_uno = raw_input('Primer Apellido: ')
    formatear = 'https://m.dateas.com/es/consulta_venezuela?name=' + apellido_uno + '+' + nombre_uno + '&cedula='
    url = formatear
    try:
        hdr = {'User-Agent':'Mozilla/5.0'}
        req = urllib2.Request(url,headers=hdr)
        html = urllib2.urlopen(req).read()
        if html.find('<h2 class="title">No') == -1:
            print Fore.GREEN + '[*]Se ha encontrado informacion de la persona. Consulte la siguiente url: ' + url
        else:
            print Fore.RED + '[*]No se ha encontrado informacion de la persona.'
    except:
        print Fore.YELLOW + '[*]Ha ocurrido un problema al tratar de consultar la informacion. Intente nuevamente.'

dateas()

#Codigo escrito por Angelo Mass - Darko.

#La herramienta fue diseñada para el grupo
#"Auditoria global" y para la pagina
#"black hat"

#Hackea El Planeta.
