from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import json

# Create your views here.
def main_page(request):
    # print("VIEWS.PY")
    result = subprocess.run(['python3', 'image_getter.py'], capture_output=True, text=True, check=False)
    # print(f'{result.stdout.strip()=}')
    result_text = result.stdout.strip()

    divider_index = result_text.find('}, ')
    # print(f'{divider_index=}')
    album1, album2 = result_text[1:divider_index+1], result_text[divider_index+3:-1]
    print(f'{album1=}')
    print(f'{album2=}')

    #To Remove
    album1 = eval(album1)
    album2 = eval(album2)

    # print(f'{album1=}')
    # print(f'{album2=}')

    return render(request, 'main_page.html', {'album1_title':album1['title'], 'album2_title':album2['title'],
     'album1_link':album1['link'], 'album2_link':album2['link'],
     'album1_artist':album1['artist'], 'album2_artist':album2['artist']})