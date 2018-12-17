import os, sys, jinja2, time



#waar op je computer zit de grand review folder
grand_review_path ='/Users/Ben/Library/Mobile Documents/com~apple~CloudDocs/ArtEZ/3y1s/Digital Media/theGrandReview/the_grand_review_2018_2019'
sys.path.append(grand_review_path)

#daar importeren we de review_parser van
from review_parser import *

data = parse(os.path.join(grand_review_path,'reviews'))

reviews = data[0]
errors = data[1]

page_template = jinja2.Template(open('templates/page.html').read())

index_template = jinja2.Template(open('templates/index.html').read())

mapje = 'website'


if not os.path.exists(mapje):
	os.mkdir(mapje)

gif_index = []

for review in reviews:

	application = review['title']
	good = review['the_good']
	bad = review['the_bad']
	name = review['author']
	bottom = review ['the_bottomline']
	rate = review['rating']
	version = review['version']
	date = review['date'].replace('/', '-')
	title = review['title'].strip(' ')

	#veranderd bestandsnaam (personaliseert het bestand in de naam+ de aplicatie die gevieuwt is zodat we per bestand kunnen zien wie en wat het bestand is) en haald spaties er uit.
	bestandsnaam = application +"_"+ name
	bestandsnaam = bestandsnaam.replace(' ', '_')
	bestandsnaam1 = 'final'+review['title'].strip(' ')+review['date'].replace('/', '-')

	bestandsnaam1 = bestandsnaam1.replace(' ', '-')
	bestandsnaam1 = bestandsnaam1.lower()



	html_file = os.path.join(mapje,bestandsnaam+'.html')
	gif = os.path.join(bestandsnaam1+'.gif')


	#which html file belongs to which gif
	gif_index.append((bestandsnaam+'.html', bestandsnaam1+'.gif'))

	with open(html_file, 'w') as f:
		content = page_template.render( title=application, rating=rate, the_good=good, the_bad=bad, the_bottomline=bottom, author=name,)
		f.write(content)

	# time.sleep(0.5)

#outside the loop
with open(os.path.join(mapje,'index.html'),'w') as f:
	f.write(index_template.render(gif_index=gif_index))
