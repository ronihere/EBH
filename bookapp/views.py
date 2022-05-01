from django.shortcuts import render,redirect
from .models import Book,Category,Review
from .forms import RateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    recommended_books = Book.objects.filter(recommended_books = True)
    fiction_books = Book.objects.filter(fiction_books = True)
    business_books = Book.objects.filter(business_books = True)
    return render(request,'home.html',{'recommended_books':recommended_books,'business_books':business_books,'fiction_books':fiction_books})


def all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html',{'books':books})

def search(request):

        try:

            if request.method == 'POST':
                bookname = request.POST['searched']
                # var = BookSearch(title = bookname)
                # var.save()
                message=''
                searched_book = Book.objects.filter(title__icontains = bookname) or Book.objects.filter(author__icontains = bookname)

                print(searched_book[0])
                searched_book_category = searched_book[0].category.first()
                similar_books = Book.objects.filter(category__name__startswith=searched_book_category)
                return render(request, 'book_detail_search.html', {'searched_book': searched_book,'message':message, 'similar_books': similar_books})
        except:
            print('except')
            message ="No such book is available right now in the library."
            return render(request,'book_detail_search.html', {'message': message} )


def category_detail(request,slug):

    category=Category.objects.get(slug = slug)
    return render(request,'genre_detail.html',{'category':category})


@login_required(login_url='login')
def book_detail(request,slug):








    book = Book.objects.get(slug=slug)
    book_rating = Review.objects.filter(title = book)
    print(book_rating)
    sum=0
    counter=0
    for book_rate in book_rating:
        counter+=1
        sum+=book_rate.rating
    if counter==0:
        sum=0
    else:
        sum=sum//counter
        counter=(5-sum)

    book_category=book.category.first()
    similar_books = Book.objects.filter(category__name__startswith = book_category)
    return render(request,'book_detail.html',{'book':book,'similar_books':similar_books,'avg':sum,'remaining':counter})

@login_required(login_url='login')
def Rate(request,slug):
    book = Book.objects.get(slug=slug)
    title = book.title
    user = request.user
    if request.method == 'POST':
        text = request.POST['text']
        rating = request.POST['rating']
        rating=int(rating)

        if (Review.objects.filter(user=user)) & (Review.objects.filter(title=title)):
            var = Review.objects.get(title=title,user=user)
            var.rating = rating
            var.text=text
            var.save()
        else:
            var = Review(text=text, rating=rating, user=user, bookm=book, title=title)
            var.save()
        return redirect('/')

    else:
        return render(request,'review.html',{"book":book})





