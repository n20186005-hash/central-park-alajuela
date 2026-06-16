import json

def fix_intro_description(filepath, lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    desc = data.get('intro', {}).get('description', '')
    if '优越的地理位置' in desc:
        if lang == 'en':
            data['intro']['description'] = desc.replace('优越的地理位置', 'excellent geographical location')
        elif lang == 'es':
            data['intro']['description'] = desc.replace('优越的地理位置', 'excelente ubicación geográfica')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

fix_intro_description('src/messages/en.json', 'en')
fix_intro_description('src/messages/es.json', 'es')
print("Intro descriptions fixed!")
