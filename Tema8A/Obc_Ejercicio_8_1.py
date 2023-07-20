def main():
    lineas = ['Esta es la primera línea del archivo\n',
              'Esta es la línea final en la lista\n']
    
    f = open('Obc_Ejercicio_8_1.txt', 'wt', encoding='utf8')
    f.writelines(lineas)
    f.close()

    f = open('Obc_Ejercicio_8_1.txt', 'at', encoding='utf8')
    f.write('Esta línea se agrega al archivo\n')
    f.write('Línea final del archivo.\n')
    f.close()

if __name__ == '__main__':
    main()
    