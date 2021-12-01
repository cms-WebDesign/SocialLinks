from django.shortcuts import render
from django.http import HttpResponse
from .models import styleEditor, profilePic, backgroundPic, links

# Create your views here.

def index(request):
    editor = styleEditor.objects.get(pk=1)
    imageModel = profilePic.objects.get(pk=1)
    backgroundModel = backgroundPic.objects.get(pk=1)
    linksModel = links.objects.get(pk=1)

    return render(
        request,
        "SocialLinks/index.html",
        {
            "web_title":editor.Title,
            "linkcolor":editor.Link_Color,
            "linkfont":editor.Link_Font_Style,
            "linkbc":editor.Link_Background_Color,
            "link_hover_color":editor.Link_Hover_Color,
            "profile_pic_title":imageModel.title,
            "profile_pic":imageModel.image,
            "background_pic_title":backgroundModel.title,
            "background_pic":backgroundModel.image,
            "link1":linksModel.link1,
            "link2":linksModel.link2,
            "link3":linksModel.link3,
            "link4":linksModel.link4,
            "link5":linksModel.link5,
            "link6":linksModel.link6,
            "link7":linksModel.link7
        }
    )
