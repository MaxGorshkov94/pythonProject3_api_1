import requests


def hero_intelligence(name):
    url1 = 'https://superheroapi.com/api/2619421814940190/search/name/powerstats'
    url2 = url1.replace('name', name)
    response = requests.get(url2)
    response_json = response.json()
    results = response_json['results'][0]
    powerstats = results['powerstats']
    return powerstats['intelligence']


if __name__ == '__main__':
    name_list = ['Hulk', 'Captain America', 'Thanos']
    hero_dict = {}
    intel_list = []
    for hero in name_list:
        intell = int(hero_intelligence(hero))
        pre_dict = {'Name': hero, 'Intelligence': intell}
        intel_list.append(pre_dict)
    low_high_list = sorted(intel_list, key=lambda i: i['Intelligence'], reverse=True)
    print(f'Самый умный - {low_high_list[0]["Name"]}, его интеллектуальный уровень - {low_high_list[0]["Intelligence"]}')