import json
import os

def update_file(filepath, lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 1. Hero
    if lang == 'zh':
        data['hero']['title'] = "Parque Central de Alajuela"
        data['hero']['subtitle'] = "阿拉胡埃拉中央公园 | 哥斯达黎加的芒果之城"
        data['hero']['openMaps'] = "查看地图导航"
        data['hero']['downloadGuide'] = "周边步行导览下载"
    elif lang == 'en':
        data['hero']['title'] = "Parque Central de Alajuela"
        data['hero']['subtitle'] = "Central Park Alajuela | The City of Mangoes, Costa Rica"
        data['hero']['openMaps'] = "View Map Navigation"
        data['hero']['downloadGuide'] = "Download Walking Guide"
    elif lang == 'es':
        data['hero']['title'] = "Parque Central de Alajuela"
        data['hero']['subtitle'] = "Parque Central de Alajuela | La Ciudad de los Mangos, Costa Rica"
        data['hero']['openMaps'] = "Ver Mapa y Navegación"
        data['hero']['downloadGuide'] = "Descargar Guía Peatonal"
        
    # 2. basicInfo Iconography
    if lang == 'zh':
        data['basicInfo'] = {
            "title": "基础信息",
            "items": [
                {"icon": "time", "label": "开放时间", "value": "24小时免费开放"},
                {"icon": "location", "label": "地址", "value": "阿拉胡埃拉市中心"},
                {"icon": "airport", "label": "机场距离", "value": "距 SJO 机场仅 5-10 分钟车程"},
                {"icon": "feature", "label": "特色", "value": "城市绿肺、历史建筑、野生动物（鬣蜥/鸟类/树懒）"}
            ]
        }
    elif lang == 'en':
        data['basicInfo'] = {
            "title": "Basic Info",
            "items": [
                {"icon": "time", "label": "Hours", "value": "Open 24 hours, Free"},
                {"icon": "location", "label": "Address", "value": "Alajuela City Center"},
                {"icon": "airport", "label": "Airport Distance", "value": "Only 5-10 mins drive from SJO Airport"},
                {"icon": "feature", "label": "Features", "value": "City lung, historical buildings, wildlife (iguanas/birds/sloths)"}
            ]
        }
    elif lang == 'es':
        data['basicInfo'] = {
            "title": "Información Básica",
            "items": [
                {"icon": "time", "label": "Horario", "value": "Abierto 24 horas, Gratis"},
                {"icon": "location", "label": "Dirección", "value": "Centro de Alajuela"},
                {"icon": "airport", "label": "Distancia al Aeropuerto", "value": "A solo 5-10 min en auto del Aeropuerto SJO"},
                {"icon": "feature", "label": "Características", "value": "Pulmón de la ciudad, edificios históricos, fauna (iguanas/aves/perezosos)"}
            ]
        }
        
    # 3. route steps (Timeline cards)
    if lang == 'zh':
        data['route']['steps'] = [
            {"time": "上午 09:00", "icon": "☕", "description": "漫步中央公园，在芒果树下寻找野生鬣蜥。"},
            {"time": "上午 10:00", "icon": "⛪", "description": "走进旁边的 阿拉胡埃拉大教堂 (Catedral de la Virgen del Pilar) 欣赏彩色玻璃。"},
            {"time": "上午 11:00", "icon": "🏛️", "description": "参观 胡安·圣玛丽亚博物馆，了解哥斯达黎加国家英雄的故事。"},
            {"time": "中午 12:00", "icon": "🍽️", "description": "步行前往两街区外的中央市场 (Mercado Central) 品尝地道哥斯达黎加美食 (Casado)。"}
        ]
    elif lang == 'en':
        data['route']['steps'] = [
            {"time": "09:00 AM", "icon": "☕", "description": "Stroll through Central Park and look for wild iguanas under the mango trees."},
            {"time": "10:00 AM", "icon": "⛪", "description": "Step into the adjacent Alajuela Cathedral (Catedral de la Virgen del Pilar) to admire the stained glass."},
            {"time": "11:00 AM", "icon": "🏛️", "description": "Visit the Juan Santamaría Museum to learn about Costa Rica's national hero."},
            {"time": "12:00 PM", "icon": "🍽️", "description": "Walk to the Central Market (Mercado Central) two blocks away to taste authentic Costa Rican food (Casado)."}
        ]
    elif lang == 'es':
        data['route']['steps'] = [
            {"time": "09:00 AM", "icon": "☕", "description": "Pasee por el Parque Central y busque iguanas silvestres bajo los árboles de mango."},
            {"time": "10:00 AM", "icon": "⛪", "description": "Ingrese a la Catedral de Alajuela (Catedral de la Virgen del Pilar) adyacente para admirar los vitrales."},
            {"time": "11:00 AM", "icon": "🏛️", "description": "Visite el Museo Histórico Cultural Juan Santamaría para conocer la historia del héroe nacional de Costa Rica."},
            {"time": "12:00 PM", "icon": "🍽️", "description": "Camine hasta el Mercado Central a dos cuadras de distancia para probar la auténtica comida costarricense (Casado)."}
        ]
        
    # 4. officialManagement (Remove fatal error)
    if lang == 'zh':
        data['officialManagement'] = {
            "title": "关于 Parque Central de Alajuela (阿拉胡埃拉中央公园)",
            "text": "阿拉胡埃拉中央公园不仅是这座城市的地理中心，更是其文化跳动的脉搏。阿拉胡埃拉被誉为“芒果之城 (Ciudad de los Mangos)”，这座公园内便种满了繁茂的百年芒果树。在这里，你不仅能欣赏到中央古典凉亭与喷泉的美景，还能近距离感受哥斯达黎加丰富的生态——仔细观察树冠，你常常能发现悠闲的鬣蜥、松鼠，甚至是偶尔造访的树懒。\n\n结合周围雄伟的阿拉胡埃拉大教堂 (Catedral de la Virgen del Pilar) 与胡安·圣玛丽亚历史文化博物馆，这里是体验纯正哥斯达黎加风情 (Pura Vida) 及其国家历史的最佳起点。更由于其距离 SJO 国际机场仅有 5-10 分钟车程，它成为了无数国际游客抵达哥斯达黎加的第一站。"
        }
    elif lang == 'en':
        data['officialManagement'] = {
            "title": "About Parque Central de Alajuela",
            "text": "Parque Central de Alajuela is not only the geographic center of the city but also its cultural heartbeat. Alajuela is known as the \"City of Mangoes\" (Ciudad de los Mangos), and this park is filled with lush century-old mango trees. Here, you can not only enjoy the beauty of the classic central kiosk and fountain but also experience Costa Rica's rich ecology up close—look closely at the canopy, and you can often spot leisurely iguanas, squirrels, and even the occasional visiting sloth.\n\nCombined with the majestic Alajuela Cathedral (Catedral de la Virgen del Pilar) and the Juan Santamaría Historical and Cultural Museum nearby, this is the best starting point to experience authentic Costa Rican flavor (Pura Vida) and its national history. Moreover, being only a 5-10 minute drive from the SJO International Airport, it has become the first stop for countless international tourists arriving in Costa Rica."
        }
    elif lang == 'es':
        data['officialManagement'] = {
            "title": "Sobre el Parque Central de Alajuela",
            "text": "El Parque Central de Alajuela no es solo el centro geográfico de la ciudad, sino también su latido cultural. Alajuela es conocida como la \"Ciudad de los Mangos\", y este parque está lleno de exuberantes árboles de mango centenarios. Aquí, no solo puede disfrutar de la belleza del clásico quiosco central y la fuente, sino también experimentar de cerca la rica ecología de Costa Rica: observe de cerca el dosel y a menudo podrá ver iguanas tranquilas, ardillas e incluso algún perezoso visitante ocasional.\n\nCombinado con la majestuosa Catedral de Alajuela (Catedral de la Virgen del Pilar) y el Museo Histórico Cultural Juan Santamaría en los alrededores, este es el mejor punto de partida para experimentar el auténtico sabor costarricense (Pura Vida) y su historia nacional. Además, al estar a solo 5-10 minutos en coche del Aeropuerto Internacional SJO, se ha convertido en la primera parada para innumerables turistas internacionales que llegan a Costa Rica."
        }
        
    # 5. Reviews
    if lang == 'zh':
        data['reviews']['items'] = [
            {
                "name": "游客 A",
                "date": "近期",
                "rating": 5,
                "text": "离机场非常近的完美第一站！公园里有巨大的芒果树，我们还在树枝上看到了一只可爱的树懒。"
            },
            {
                "name": "游客 B",
                "date": "近期",
                "rating": 5,
                "text": "当地人聚集的中心，非常有烟火气，大教堂的钟声和广场上的鸽子让人感觉很放松。"
            },
            {
                "name": "María José",
                "date": "近期",
                "rating": 5,
                "text": "美丽的公园，周围环境优美。距离大教堂很近，是游览阿拉胡埃拉时的必访之地。"
            }
        ]
    elif lang == 'en':
        data['reviews']['items'] = [
            {
                "name": "Tourist A",
                "date": "Recently",
                "rating": 5,
                "text": "The perfect first stop very close to the airport! There are giant mango trees in the park, and we even saw a cute sloth on the branches."
            },
            {
                "name": "Tourist B",
                "date": "Recently",
                "rating": 5,
                "text": "A center where locals gather, very lively. The cathedral bells and pigeons in the square make you feel very relaxed."
            },
            {
                "name": "María José",
                "date": "Recently",
                "rating": 5,
                "text": "Beautiful park with nice surroundings. Very close to the cathedral, a must-visit when touring Alajuela."
            }
        ]
    elif lang == 'es':
        data['reviews']['items'] = [
            {
                "name": "Turista A",
                "date": "Recientemente",
                "rating": 5,
                "text": "¡La primera parada perfecta muy cerca del aeropuerto! Hay enormes árboles de mango en el parque, e incluso vimos un lindo perezoso en las ramas."
            },
            {
                "name": "Turista B",
                "date": "Recientemente",
                "rating": 5,
                "text": "Un centro donde se reúnen los lugareños, muy animado. Las campanas de la catedral y las palomas en la plaza te hacen sentir muy relajado."
            },
            {
                "name": "María José",
                "date": "Recientemente",
                "rating": 5,
                "text": "Hermoso parque con un entorno agradable. Muy cerca de la catedral, una visita obligada al recorrer Alajuela."
            }
        ]
        
    # 6. Traffic Info
    if lang == 'zh':
        data['transport']['airportDesc'] = "距胡安·圣玛丽亚国际机场 (SJO) 仅 5-10 分钟车程，建议租车或乘坐出租车前往。很多游客将其作为抵达哥斯达黎加后或离开前游览的第一站或最后一站。"
    elif lang == 'en':
        data['transport']['airportDesc'] = "Only a 5-10 minute drive from Juan Santamaría International Airport (SJO). It is recommended to rent a car or take a taxi. Many tourists make it their first or last stop when visiting Costa Rica."
    elif lang == 'es':
        data['transport']['airportDesc'] = "A solo 5-10 minutos en auto del Aeropuerto Internacional Juan Santamaría (SJO). Se recomienda alquilar un auto o tomar un taxi. Muchos turistas lo convierten en su primera o última parada al visitar Costa Rica."

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

update_file('src/messages/zh.json', 'zh')
update_file('src/messages/en.json', 'en')
update_file('src/messages/es.json', 'es')
print("JSON files updated successfully!")
