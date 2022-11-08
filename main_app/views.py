from django.shortcuts import render

class Record:
  def __init__(self, title, artist, genre, releaseYear, catalogNum):
    self.title = title
    self.artist = artist
    self.genre = genre
    self.releaseYear = releaseYear
    self.catalogNum = catalogNum

records = [
  Record('Tango In the Night', 'Fleetwood Mac', 'pop-rock', 1987, '9254711'),
  Record('Plantasia', 'Mort Garson', 'experimental', 1975, 'SBR-3030'),
  Record('South of the Border', 'Herb Alpert and the Tijuana Brass', 'jazz', 1964, 'V 1747'),

]

# View functions

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def records_index(request):
  return render(request, 'records/index.html', { 'records': records })