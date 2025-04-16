from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import json

# Create your views here.
def main_page(request):
    result = subprocess.run(['python3', 'image_getter.py'], capture_output=True, text=True, check=False)
    output = result.stdout.strip()
    links = output.split('\n')
    link1, link2 = links[0], links[1]
    return render(request, 'main_page.html', {'image1':link1,'image2':link2})