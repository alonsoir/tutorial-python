# Este código vamos a ejecutarlo en PyCharm
import signal
import sys
import time


def imprimir_tiempo():
    print(f'Son las {time.strftime("%H:%M:%S")}')


def manejador_interrupcion(signal, frame):
    print("El programa ha sido interrumpido por el usuario.")
    sys.exit(0)


signal.signal(signal.SIGINT, manejador_interrupcion)


def cabecera():
    print(
        """
    //    _____             _____   _                                     __                                           _                               
//   |  __ \           / ____| | |                                   / _|                                  /\     | |                              
//   | |__) |  _   _  | |      | |__     __ _   _ __   _ __ ___     | |_   _ __    ___    _ __ ___        /  \    | |   ___    _ __    ___    ___  
//   |  ___/  | | | | | |      | '_ \   / _` | | '__| | '_ ` _ \    |  _| | '__|  / _ \  | '_ ` _ \      / /\ \   | |  / _ \  | '_ \  / __|  / _ \ 
//   | |      | |_| | | |____  | | | | | (_| | | |    | | | | | |   | |   | |    | (_) | | | | | | |    / ____ \  | | | (_) | | | | | \__ \ | (_) |
//   |_|       \__, |  \_____| |_| |_|  \__,_| |_|    |_| |_| |_|   |_|   |_|     \___/  |_| |_| |_|   /_/    \_\ |_|  \___/  |_| |_| |___/  \___/ 
//              __/ |                                                                                                                              
//             |___/                                                                                                                               
//                                                                                                                                                 
//                                                                                                                                                 
//                                                                                                                                                 
//                                                                                                                                                 
//                                                                                                                                                 
//                                                                                                                                                 
//                                                                                                                                                 
//                                                                                                                                                 
//                      _                                                                                                                          
//      ____           (_)                                                                                                                         
//     / __ \    __ _   _   _ __    ___    _ __    _ __ ___     __ _   _ __                                                                        
//    / / _` |  / _` | | | | '__|  / _ \  | '_ \  | '_ ` _ \   / _` | | '_ \                                                                       
//   | | (_| | | (_| | | | | |    | (_) | | | | | | | | | | | | (_| | | | | |                                                                      
//    \ \__,_|  \__,_| |_| |_|     \___/  |_| |_| |_| |_| |_|  \__,_| |_| |_|                                                                      
//     \____/                                                                                                                                      
//                                                                                                                                                 

    """
    )


def funcion():
    # ese join es el equivalente a invocar a toString en un objeto tipo lista en java.
    print("Pulsa la q e intro para acabar.")
    print("sys.path: " + "".join(sys.path))
