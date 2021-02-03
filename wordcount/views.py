from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
	#return HttpResponse('Hi. I am here')
	#return render(request, 'home.html', {'xyz': "This is cool!"})
	return render(request, 'home.html')

#def eggs(request):
#	return HttpResponse("Hi. I don't eat eggs")

def count(request):
	fulltext = request.GET['fulltext']
	#print(fulltext)
	wordlist = fulltext.split()
	wdict = {}
	for word in wordlist:
		if word in wdict:
			wdict[word] += 1
		else:
			wdict[word] = 1
	sortedwords = sorted(wdict.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 
		'wdict': wdict, 'sortedwords': sortedwords})

def about(request):
	return render(request, 'about.html')