import json

def update_reviews(filepath, lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # We need to construct 8 reviews
    if lang == 'zh':
        data['reviews']['items'] = [
            {
                "name": "Sarah W.",
                "date": "近期",
                "rating": 5,
                "text": "离机场非常近的完美第一站！公园里有巨大的芒果树，我们还在树枝上看到了一只可爱的树懒。"
            },
            {
                "name": "David M.",
                "date": "近期",
                "rating": 5,
                "text": "当地人聚集的中心，非常有烟火气，大教堂的钟声和广场上的鸽子让人感觉很放松。"
            },
            {
                "name": "María José",
                "date": "1个月前",
                "rating": 5,
                "text": "美丽的公园，周围环境优美。距离大教堂很近，是游览阿拉胡埃拉时的必访之地。"
            },
            {
                "name": "Carlos A.",
                "date": "2个月前",
                "rating": 5,
                "text": "美丽、珍贵且宁静的地方。古老而传统，充满阿拉胡埃拉的生活气息。"
            },
            {
                "name": "Ana V.",
                "date": "3个月前",
                "rating": 4,
                "text": "很棒的城市公园，有巨大的芒果树提供舒适的阴凉。非常适合在这里休息片刻。"
            },
            {
                "name": "Roberto G.",
                "date": "半年多前",
                "rating": 5,
                "text": "一个非常美丽、历史悠久的地方。很干净，人流量很大。旁边还有美丽的图书馆和大教堂。"
            },
            {
                "name": "Elena R.",
                "date": "1年前",
                "rating": 5,
                "text": "漂亮的地方，经常有即兴表演。非常适合在这里散步，感受哥斯达黎加的纯正风情。"
            },
            {
                "name": "Luis F.",
                "date": "近期",
                "rating": 4,
                "text": "维护得很好的公共空间，中心有凉亭。可以在这里观看人来人往，非常放松。"
            }
        ]
    elif lang == 'en':
        data['reviews']['items'] = [
            {
                "name": "Sarah W.",
                "date": "Recently",
                "rating": 5,
                "text": "The perfect first stop very close to the airport! There are giant mango trees in the park, and we even saw a cute sloth on the branches."
            },
            {
                "name": "David M.",
                "date": "Recently",
                "rating": 5,
                "text": "A center where locals gather, very lively. The cathedral bells and pigeons in the square make you feel very relaxed."
            },
            {
                "name": "María José",
                "date": "1 month ago",
                "rating": 5,
                "text": "Beautiful park with nice surroundings. Very close to the cathedral, a must-visit when touring Alajuela."
            },
            {
                "name": "Carlos A.",
                "date": "2 months ago",
                "rating": 5,
                "text": "Beautiful, precious and quiet place. Old and traditional, it truly reflects life in Alajuela."
            },
            {
                "name": "Ana V.",
                "date": "3 months ago",
                "rating": 4,
                "text": "Great city park with giant mango trees providing comfortable shade. Perfect for taking a break."
            },
            {
                "name": "Roberto G.",
                "date": "Over 6 months ago",
                "rating": 5,
                "text": "A very beautiful place rich in history. Very clean with a lot of people. There's a beautiful library and cathedral next to it."
            },
            {
                "name": "Elena R.",
                "date": "1 year ago",
                "rating": 5,
                "text": "Nice place, often with improvised shows. Great for walking around and feeling the authentic Costa Rican vibe."
            },
            {
                "name": "Luis F.",
                "date": "Recently",
                "rating": 4,
                "text": "Well-maintained public space with a kiosk in the center. Very relaxing to just sit and people-watch."
            }
        ]
    elif lang == 'es':
        data['reviews']['items'] = [
            {
                "name": "Sarah W.",
                "date": "Recientemente",
                "rating": 5,
                "text": "¡La primera parada perfecta muy cerca del aeropuerto! Hay enormes árboles de mango en el parque, e incluso vimos un lindo perezoso en las ramas."
            },
            {
                "name": "David M.",
                "date": "Recientemente",
                "rating": 5,
                "text": "Un centro donde se reúnen los lugareños, muy animado. Las campanas de la catedral y las palomas en la plaza te hacen sentir muy relajado."
            },
            {
                "name": "María José",
                "date": "Hace 1 mes",
                "rating": 5,
                "text": "Hermoso parque con un entorno agradable. Muy cerca de la catedral, una visita obligada al recorrer Alajuela."
            },
            {
                "name": "Carlos A.",
                "date": "Hace 2 meses",
                "rating": 5,
                "text": "Bello lugar precioso y tranquilo. Es antiguo, tradicional, es muy tranquilo y es la vida en Alajuela."
            },
            {
                "name": "Ana V.",
                "date": "Hace 3 meses",
                "rating": 4,
                "text": "Un gran parque en el centro de Alajuela, con árboles de mango que brindan una sombra cómoda. Perfecto para tomar un descanso."
            },
            {
                "name": "Roberto G.",
                "date": "Hace más de 6 meses",
                "rating": 5,
                "text": "Un lugar muy bonito y rico en historia. Local bien conservado y limpio. Gran circulación de personas. Bella biblioteca y catedral."
            },
            {
                "name": "Elena R.",
                "date": "Hace 1 año",
                "rating": 5,
                "text": "Bonito lugar, con espectáculos improvisados. Genial para caminar y sentir la auténtica vibra costarricense."
            },
            {
                "name": "Luis F.",
                "date": "Recientemente",
                "rating": 4,
                "text": "Espacio público bien mantenido con un quiosco en el centro. Muy relajante para simplemente sentarse y observar a la gente."
            }
        ]

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

update_reviews('src/messages/zh.json', 'zh')
update_reviews('src/messages/en.json', 'en')
update_reviews('src/messages/es.json', 'es')
print("Reviews expanded to 8 items in all languages!")
