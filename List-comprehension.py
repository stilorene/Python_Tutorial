
def convert_to_snakecase(MeinString):
    snake_cased_string = [
        '_' + char.lower() if char.isupper() #Überprüfung ob Buchstaben groß geschrieben, dann kleiner machen, sonst einfach nichts machen
        else char
          for char in MeinString]
    
    return ''.join(snake_cased_string).strip('_')



def main():
    print(convert_to_snakecase('DAsIstWohlDerStringLOL'))

main()