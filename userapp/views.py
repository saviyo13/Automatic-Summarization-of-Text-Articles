from django.shortcuts import render
from adminapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import nltk
import bs4 as bs  
import urllib.request  
import re
from gtts import gTTS
import os


# Create your views here.

def profile(request):
    id=request.session['userid']
    prof=tbl_reg.objects.get(id=id)
    return render(request,"userapp/profile.html",{'prof':prof})

def edit(request,id):
    data=tbl_reg.objects.get(id=id)
    item=tbl_log.objects.get(username=data.email)
    if request.method=="POST":
        na=request.POST.get('t1')
        lna=request.POST.get('t2')
        mail=request.POST.get('t5')
        des=request.POST.get('t6')
        pas=request.POST.get('t7')
        data.name=na
        data.lname=lna
        data.email=mail
        data.designation=des
        item.username=mail
        item.password=pas
        data.save()
        item.save()
        return HttpResponseRedirect(reverse('profile'))
    return render(request,"userapp/edit.html",{'data':data,'item':item})

def search(request):
    return render(request,"userapp/search.html",{})

def sum(request):
    result=""
    if request.method=="POST":
        itext=request.POST.get('text1')
        scraped_data  = itext
        article = scraped_data
        parsed_article = bs.BeautifulSoup(article,'lxml')
        paragraphs = parsed_article.find_all('p')
        article_text = ""
        for p in paragraphs:  
            article_text += p.text
        # Removing Square Brackets and Extra Spaces
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
        article_text = re.sub(r'\s+', ' ', article_text)
        # Removing special characters and digits
        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
        sentence_list = nltk.sent_tokenize(article_text)
        stopwords = nltk.corpus.stopwords.words('english')
        word_frequencies = {}  
        for word in nltk.word_tokenize(formatted_article_text):  
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
        maximum_frequncy = max(word_frequencies.values())
        for word in word_frequencies.keys():  
            word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
        sentence_scores = {}  
        for sent in sentence_list:  
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]
        import heapq  
        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)  
        #data=tbl_text.objects.create(inputtxt=itext,outputtxt=summary)
        myobj=gTTS(text="Here is the summary...                   "+summary+"                summarization completed....           Thank you...",lang='en',slow=False)
        count=0
        loc='media/audio.mp3'
        mp3='audio.mp3'
        while(os.path.isfile(loc)):
            count+=1
            strs="media/"+str(count)+mp3
            loc=strs
        if count==0:
            audio=mp3
        else:
            audio=str(count)+mp3
        myobj.save(loc)
        data=tbl_text.objects.create(inputtype='Text',inputtxt=scraped_data,outputtxt=summary,audio=audio)
        return render(request,"userapp/result.html",{'data':data})
    return render(request,"userapp/sum.html",{})

def result(request):
    return render(request,"userapp/result.html",{})

def fsum(request):
    result=""
    if request.method=="POST":
        try:
            itext=request.FILES['text1'].read()
            scraped_data=itext
            article = scraped_data
            parsed_article = bs.BeautifulSoup(article,'lxml')
            paragraphs = parsed_article.find_all('p')
            article_text = ""
            for p in paragraphs:  
                article_text += p.text
            # Removing Square Brackets and Extra Spaces
            article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
            article_text = re.sub(r'\s+', ' ', article_text)
            # Removing special characters and digits
            formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
            formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
            sentence_list = nltk.sent_tokenize(article_text)
            stopwords = nltk.corpus.stopwords.words('english')
            word_frequencies = {}  
            for word in nltk.word_tokenize(formatted_article_text):  
                if word not in stopwords:
                    if word not in word_frequencies.keys():
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1
            maximum_frequncy = max(word_frequencies.values())
            for word in word_frequencies.keys():  
                word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
            sentence_scores = {}  
            for sent in sentence_list:  
                for word in nltk.word_tokenize(sent.lower()):
                    if word in word_frequencies.keys():
                        if len(sent.split(' ')) < 30:
                            if sent not in sentence_scores.keys():
                                sentence_scores[sent] = word_frequencies[word]
                            else:
                                sentence_scores[sent] += word_frequencies[word]
            import heapq  
            summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
            summary = ' '.join(summary_sentences)  
            #data=tbl_text.objects.create(inputtxt=itext,outputtxt=summary)
            myobj=gTTS(text="Here is the summary...                   "+summary+"                summarization completed....           Thank you...",lang='en',slow=False)
            count=0
            loc='media/audio.mp3'
            mp3='audio.mp3'
            while(os.path.isfile(loc)):
                count+=1
                strs="media/"+str(count)+mp3
                loc=strs
            if count==0:
                audio=mp3
            else:
                audio=str(count)+mp3
            myobj.save(loc)
            data=tbl_text.objects.create(inputtype='File',inputtxt=scraped_data,outputtxt=summary,audio=audio)
            return render(request,"userapp/fresult.html",{'data':data})
        except:
            return render(request,"userapp/ferror.html",{})
    return render(request,"userapp/fsum.html",{})

def ferror(request):
    return render(request,"userapp/ferror.html",{})

def fresult(request):
    return render(request,"userapp/fresult.html",{})

def wsum(request):
    message="Enter the link to summarise the content...."
    if request.method=="POST":
        itext=request.POST.get('text1')
        try:
            scraped_data = urllib.request.urlopen(itext)
            article = scraped_data
            parsed_article = bs.BeautifulSoup(article,'lxml')
            paragraphs = parsed_article.find_all('p')
            article_text = ""
            for p in paragraphs:  
                article_text += p.text
            # Removing Square Brackets and Extra Spaces
            article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
            article_text = re.sub(r'\s+', ' ', article_text)
            # Removing special characters and digits
            formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
            formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
            sentence_list = nltk.sent_tokenize(article_text)
            stopwords = nltk.corpus.stopwords.words('english')
            word_frequencies = {}  
            for word in nltk.word_tokenize(formatted_article_text):  
                if word not in stopwords:
                    if word not in word_frequencies.keys():
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1
            maximum_frequncy = max(word_frequencies.values())
            for word in word_frequencies.keys():  
                word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
            sentence_scores = {}  
            for sent in sentence_list:  
                for word in nltk.word_tokenize(sent.lower()):
                    if word in word_frequencies.keys():
                        if len(sent.split(' ')) < 30:
                            if sent not in sentence_scores.keys():
                                sentence_scores[sent] = word_frequencies[word]
                            else:
                                sentence_scores[sent] += word_frequencies[word]
            import heapq  
            summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
            summary = ' '.join(summary_sentences)  
            #data=tbl_text.objects.create(inputtxt=itext,outputtxt=summary)
            myobj=gTTS(text="Here is the summary...                   "+summary+"                summarization completed....           Thank you...",lang='en',slow=False)
            count=0
            loc='media/audio.mp3'
            mp3='audio.mp3'
            while(os.path.isfile(loc)):
                count+=1
                strs="media/"+str(count)+mp3
                loc=strs
            if count==0:
                audio=mp3
            else:
                audio=str(count)+mp3
            myobj.save(loc)
            data=tbl_text.objects.create(inputtype='Link',inputtxt=scraped_data,outputtxt=summary,audio=audio)
            return render(request,"userapp/wresult.html",{'data':data})
        except:
            message="Please enter a valid url"   
    return render(request,"userapp/wsum.html",{'message':message})

def wresult(request):
    return render(request,"userapp/wresult.html",{})

def ucontact(request):
    id=request.session['userid']
    data=tbl_reg.objects.get(id=id)
    if request.method=="POST":
        na=data.name
        mail=data.email
        sub=request.POST.get('c3')
        msg=request.POST.get('c4')
        var=tbl_contact.objects.create(name=na,email=mail,subject=sub,message=msg)
        return render(request,"userapp/usuccess.html",{})
    return render(request,"userapp/ucontact.html",{'data':data})

def usuccess(request):
    return render(request,"userapp/usuccess.html",{})