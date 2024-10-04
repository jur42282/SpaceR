single_char_unbreakable = ['a', 'i', 'k', 'o', 's', 'u', 'v', 'z']
unbreakable_char = "~" #Znak, který zastupuje nezlomitelnou mezeru

def single_char_detector(text):
    for c in single_char_unbreakable:
        text = text.replace(f' {c} ', f' {c}{unbreakable_char}')
        text = text.replace(f' {c.upper()} ', f' {c.upper()}{unbreakable_char}')
        text = text.replace(f'{unbreakable_char}{c} ', f'{unbreakable_char}{c}{unbreakable_char}')
    return text

def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        unbreakable_text = single_char_detector(text)
        
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(unbreakable_text)

if __name__ == '__main__':
    main()