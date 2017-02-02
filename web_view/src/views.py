from django.shortcuts import render
from django.shortcuts import render_to_response
import re, sys


# Create your views here.
def IndexView(request):
    return render(request, 'index.html')

def getfile(request):
    #get the fileitem
	fileitem=request.FILES['userfile']
	m=fileitem.file.read().split('\n')
	ifc2html(m,"ifc.html")
	return render(request, 'ifc.html')

def ifc2html(ifc, html):
    file = open("src/templates/"+html, 'w')

    file.write('<html>'+'\n'+'<body>'+'\n')

    for i in [fi.rstrip('\n') for fi in ifc]:
	sp = i.split('=')
	if len(sp) > 1:
	    a=re.sub('#([0-9]+)', '<div id="'+r'\1'+'">#'+r'\1'+'=', sp[0])
	    b=re.sub('#([0-9]+)', '<a href="#'+r'\1'+'">#'+r'\1'+'</a>', sp[1])
	    file.write(a+b+'</div>'+'\n')
	else:
	    file.write('<div>'+i+'</div>'+'\n')

    file.write('</body>'+'\n'+'</html>')
    file.close()
