from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string
# from django.template.loader import render_to_string
# Create your views here.
# def index(request):
#     return HttpResponse("This worsks!")

# def feburary(request):
#     return HttpResponse("This is febuaray")
monthly_challenges_dic = {
    'january':'This is january',
    'febuary':'This is febuary',
    'march':'This is march',
    'april':'This is april',
    'may':'This is may',
    'june':'This is june',
    'july':'This is july',
    'august':'This is august',
    'september':'This is september',
    'october':'This is october',
    'november':'This is november',
    'december':None,
}
def index(request):
    months_list = list(monthly_challenges_dic.keys())
    # listItem = ""
    # for month in months_list:
    #     path = reverse('month-challenge',args = [month]) #/challenge/january
    #     listItem += f"<h1> <li>  <a href = {path}>{month}</a> </li> </h1>"
        
    # responce_data = f"<ul>{listItem}</ul>"
    # return HttpResponse(responce_data)
    return render(request,'challenges/index.html',{
        "months":months_list,
    })

def monthly_challenges_by_number(request, month):
    months_keys_list = list(monthly_challenges_dic.keys())

    if month > len(months_keys_list) or month <= 0:
        return HttpResponseRedirect("Invalid month")

    redirect_month = months_keys_list[month - 1]
    redirect_path = reverse('month-challenge',args = [redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)  

def montyly_challenges(request,month):
    challenge_text = None
    # if month == 'january':
    #     challenge_text = "This is january" 
    # elif month == 'febuary':
    #     challenge_text = 'This is febuary'
    # elif month == 'march':
    #     challenge_text = 'This is march'
    # else:
    #     return HttpResponseNotFound("This month is not supported")
    # return HttpResponse(challenge_text)

    # Through dictionary
    try:
        challenge_text = monthly_challenges_dic[month]
        # html_responce = f"<h1 style = 'text-align: center'>{challenge_text}</h1>"
        # html_responce = render_to_string('challenges/challenge.html')
        # return HttpResponse(html_responce)
        return render(request,'challenges/challenge.html',{
            "challenge_text":challenge_text,
            "challenge_name":month.capitalize(),
        })
    except:
        # bad_template_include = render_to_string("404.html")
        # return HttpResponseNotFound('<h1 style = "text-align:center"> This month is not supported </h1>')
        # return HttpResponseNotFound(bad_template_include)
        raise Http404()



