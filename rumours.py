# -*- coding: utf8 -*-

teams = {
	'Atleti': {'terms': ['atleti', 'atletico de madrid'], 'tracked': True},
	'ChelseaFC': {'terms': ['chelsea', 'chelseafc', 'cfc'], 'tracked': True},
	'FCBarcelona': {'terms': ['barcelona', 'fcbarcelona', 'barça', 'barca', 'fcb'], 'tracked': True},
	'FCPorto': {'terms': ['porto', 'fcporto'], 'tracked': True},
	'LFC': {'terms': ['liverpool', 'lfc'], 'tracked': True},
	'ManCity': {'terms': ['manchester city', 'mancity', 'man city', 'mcfc'], 'tracked': True},
	'ManUtd': {'terms': ['manchester united', 'manutd', 'man utd', 'mufc'], 'tracked': True},
	'realmadrid': {'terms': ['realmadrid', 'real madrid'], 'tracked': True},
	'SevillaFC': {'terms': ['sevillafc', 'sevilla'], 'tracked': True},
	'SLBenfica': {'terms': ['benfica', 'slbenfica'], 'tracked': True},
	'Sporting_CP': {'terms': ['sporting', 'sporting_cp', 'scp'], 'tracked': True},
	'SpursOfficial': {'terms': ['spursofficial', 'tottenham', 'hotspur', 'spurs'], 'tracked': True},	
	'Arsenal': {'terms': ['arsenal', 'afc', 'gunners'], 'tracked': False},
	'Southampton': {'terms': ['southampton', 'southamptonfc', 'saintsfc'], 'tracked': False},
	'BocaJrsOficial': {'terms': ['boca juniors', 'bocajrsoficial', 'boca'], 'tracked': False},
	'NorwichCityFC': {'terms': ['norwich', 'norwichcityfc', 'ncfc'], 'tracked': False},
	'valenciacf': {'terms': ['valenciacf', 'valencia', 'vcf'], 'tracked': False},
}

rumours = {
	'rumour_1': {'target': ['cristiano', 'ronaldo', 'cr7'], 'to': teams['ManUtd']['terms']},
	'rumour_2': {'target': ['lee grant'], 'to': teams['ManUtd']['terms']},
	'rumour_3': {'target': ['fellaini', 'marouane'], 'to': teams['Arsenal']['terms']},
	'rumour_4': {'target': ['marcoasensio10', 'asensio'], 'to': teams['LFC']['terms']},
	'rumour_5': {'target': ['rubey_lcheek', 'loftus-cheek', 'ruben'], 'to': teams['ChelseaFC']['terms']},
	'rumour_6': {'target': ['polf22', 'pol', 'fernandez', 'fernández'], 'to': teams['SLBenfica']['terms']},
	'rumour_7': {'target': ['juanferquinte10', 'quintero'], 'to': teams['realmadrid']['terms']},
	'rumour_8': {'target': ['clement_lenglet', 'lenglet'], 'to': teams['FCBarcelona']['terms']},
	'rumour_9': {'target': ['kovacic', 'mateo_kova23'], 'to': teams['ManUtd']['terms']},
	'rumour_10': {'target': ['banega', 'ever19banega'], 'to': teams['Arsenal']['terms']},
	'rumour_11': {'target': ['gunn', 'angusgunn01'], 'to': teams['Southampton']['terms']},
	'rumour_12': {'target': ['pareja', 'nicopareja21'], 'to': teams['BocaJrsOficial']['terms']},
	'rumour_13': {'target': ['arthur', 'arthurmeloreal'], 'to': teams['FCBarcelona']['terms']},
	'rumour_14': {'target': ['mooy', 'aaronmooy'], 'to': teams['ManCity']['terms']},
	'rumour_15': {'target': ['kroos', 'tonikroos'], 'to': teams['ManUtd']['terms']},
	'rumour_16': {'target': ['kaseypalmer45', 'kp45', 'palmer'], 'to': teams['NorwichCityFC']['terms']},
	'rumour_17': {'target': ['cristiano', 'ronaldo', 'cr7'], 'to': teams['realmadrid']['terms']},
	'rumour_18': {'target': ['romelulukaku9', 'lukaku', 'romelu'], 'to': teams['realmadrid']['terms']},
	'rumour_19': {'target': ['tfosumensah', 'fosu-mensah', 'mensah'], 'to': teams['valenciacf']['terms']},
	'rumour_20': {'target': ['juanferquinte10', 'quintero'], 'to': teams['SpursOfficial']['terms']},
}

rumour_terms = ['breaking', 'report', 'transfer', 'rumour', 'rumor', 'transferência', 'transferencia', 'fichaje']