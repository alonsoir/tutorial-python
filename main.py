# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from utils import print_something


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


def input_message():
    return input("Introduce el mensajito: ")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press ⌘F8 to toggle the breakpoint.
    print_something(name)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    cabecera()
    print_hi("")
    mensaje = input_message()
    print("Bueno el hash del mensaje", mensaje, "es", hash(mensaje))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
