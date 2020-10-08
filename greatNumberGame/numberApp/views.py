from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    #Upon loading, the server should "pick" a random number between 1-100; store the number in session. 

    #initialize reset
    if ('reset' not in request.session):
        request.session['reset'] = True

    # if ('pick' not in request.session):
    if (request.session['reset'] == True):
        # Return a random integer N such that 1 <= N <= 100.
        request.session['pick'] = random.randint(1,100)
        print(request.session['pick'])#print number to console

        #initialize variables:
        request.session['counter'] = 0
        request.session['status'] = ''
        request.session['reset'] = False
    
    #for the leaderboard names   
    if ('players' not in request.session):
        request.session['players'] = []
         
    return render(request, 'index.html')

def submit(request):
    request.session['num'] = int(request.POST['guess'])
    request.session['counter'] += 1

    #BONUS: Only allow the user to guess up to 5 times. If they don't guess it on their 5th attempt, display a "You Lose" message and allow them to try again.
    if (request.session['counter'] == 5 and request.session['num'] != request.session['pick']):
        request.session['status'] = 'game_over'
        return redirect('/')

    if (request.session['num'] < request.session['pick']):
        request.session['status'] = 'Too low!'
    elif (request.session['num'] > request.session['pick']):
        request.session['status'] = 'Too high!'
    else:
        request.session['status'] = 'correct'

    return redirect('/')

def clear(request):
    # request.session.clear()
    request.session['reset'] = True
    return redirect('/')

#If they win, allow the user to submit their name. Have a link to a leaderboard page that shows winners' names and how many attempts they took to guess correctly.
def leaderboard(request):

    #note: you can't append lists to another list IN SESSION! So here is the workaround:
    #first create a temp variable to copy the existing list. The temp variable will not be in session, it is just a copy of the content
    temp = request.session['players']

    #then append the new list
    temp.append({'name': request.POST['name'], 'num': request.session['counter']})

    #finally, put the new list back in session
    request.session['players'] = temp

    ###################
    
    #optional workaround:
    #have your original statement that didn't work (this statement alone kept overriding itself)
    # request.session['players'].append({'name': request.POST['name'], 'num': request.session['counter']})
    # #add this statemet to change the session data
    # request.session.modified = True

    return render(request, "leader.html")