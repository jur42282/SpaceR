single_char_unbreakable = ['a', 'i', 'k', 'o', 's', 'u', 'v', 'z']

def single_char_detector(text):
    for c in single_char_unbreakable:
        text = text.replace(f' {c} ', f' {c}~')
        text = text.replace(f' {c.upper()} ', f' {c.upper()}~')
        text = text.replace(f'~{c} ', f'~{c}~')
    return text

def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        unbreakable_text = single_char_detector(text)
        
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(unbreakable_text)

if __name__ == '__main__':
    main()