from django.shortcuts import render
from .forms import Form
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import math
# Create your views here.

def index(request):
	form = Form(request.POST)
	form.use_required_attribute = False
	form.auto_id = False
	form.label_suffix = ''
	if request.method == 'POST':
		if form.is_valid:
			teeth = request.POST.get('teeth')
			module = request.POST.get('module')
			if teeth == '' or module == '':
				template = 'blog/noresponse.html'
				context = {'non_field_errors': 'please felan'}
			else:
				teeth, module = int(teeth), float(module)
				teta = 90/teeth
				cos = math.cos(math.radians(teta))
				sin = math.sin(math.radians(teta))
				pi = math.pi
				rad = 90 / (180.0 * pi)
				p = module * pi
				do = (module * teeth)
				da = do + (module *2)
				df = module * (teeth - 2.334)
				c = 0.167 * module
				Ha = module
				Hf = module + c
				H = Ha + Hf
				b = (10 * module)
				s = (19/40) * p
				I = (21/40) * p
				ss = (module * teeth * sin)
				q = module * (1 + teeth * ((1 - cos)/2))
				template = 'blog/response.html'
				context = {
					'form' : form,
					'module' : module,
					'teeth' : teeth,
					'form' : form,
					'teta' : teta,
					'cos' : cos,
					'sin' : sin,
					'rad' : rad,
					'p' : p,
					'do' : do,
					'da' : da,
					'df' : df,
					'c' : c,
					'Ha' : Ha,
					'Hf' : Hf,
					'H' : H,
					'b' : b,
					's' : s,
					'I' : I,
					'ss' : ss,
					'q' : q,
				}
			# return HttpResponseRedirect('/thanks/')
			# return JsonResponse(context)
			return render(request, template, context)

	return render(request, 'blog/gear.html', {'form' : form})

	
	# return render(request, 'blog/gear.html')

# def index(request):
# 	pass