from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView


from e_shop.form import *
from e_shop.models import *


# def hello_world(request):
#   return HttpResponse("Hello, World!")


def main(request):
    items = Item.objects.all()
    items_list = Item.objects.all()
    categories = Category.objects.all()
    category_counts = {}
    for category in categories:
        count = Item.objects.filter(category=category).count()
        category_counts[category.name] = count




    return render(request, 'main.html', {'items': items,'user': request.user, 'category_counts': category_counts, 'categories': categories})


def product_list(request):
    items = Item.objects.all()
    # Assuming you have an item_id passed to the view
    item_id = request.GET.get('item_id')  # Adjust this depending on your URL structure
    item = Item.objects.get(id=item_id)

    # For simplicity, let's fetch all items for pagination
    all_items = Item.objects.order_by('name')  # Replace 'name' with the actual field you want to order by

    # Number of items to show per page
    items_per_page = 6

    paginator = Paginator(all_items, items_per_page)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        items = paginator.page(paginator.num_pages)

    return render(request, 'ex2.html', {'item': item, 'items': items})


# Create your views here.
def log_out(request):
    logout(request)
    redirect('main')

def item_detail(request, item_id):
    categories = Category.objects.all()
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item_detail.html', {'item': item,'categories':categories})

@login_required
def create_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the created_by field before saving
            form.instance.created_by = request.user
            form.save()
            return HttpResponse("Product created successfully!")
    else:
        form = ItemForm()

    return render(request, 'create_product.html', {'form': form,'categories':categories})


def signup_view(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            # login(request, form)  # Uncomment this line if needed
            return redirect('/login/')  # Redirect to your home page after signup
        else:
            form=SignupForm()
            # If the form is not valid, print the errors
            #print(form.errors)
            # Add additional logic to handle the invalid form, e.g., return an error response
            # For now, you can render the form again with the errors
            return render(request, 'sighn_up.html', {'form': form})
    else:
        form = SignupForm()
        # Add this code to render the form in case of a GET request
        return render(request, 'sighn_up.html', {'form': form ,'categories':categories})

@login_required
def user_products(request):
    categories = Category.objects.all()
    # Get the current user's products
    user_products = Item.objects.filter(created_by=request.user)

    return render(request, 'user_products.html', {'user_products': user_products , 'categories':categories})

@login_required
def delete_items(request,item_id):
      item = get_object_or_404(Item, pk=item_id, created_by=request.user)
      item.delete()
      return redirect('main')


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = ItemEditForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', item_id=item_id)  # Redirect to the item detail page
    else:
        form = ItemEditForm(instance=item)

    return render(request, 'edit_item.html', {'form': form, 'item': item})

def test_search(request):
    return render(request,'item.html' )
"""

def custom_login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        # Redirect the user to a different page if they are already authenticated
        return redirect('signup/')  # Change 'home' to the name of your home URL pattern

    # If the request method is POST, it means the user is submitting the form
    if request.method == 'GET':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            return LoginView.as_view(template_name='login.html', authentication_form=LoginForm)(request, *args, **kwargs)
    else:
        # If the request method is GET, just display the login form
        form = LoginForm()


    return render(request, 'login.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm()
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to your home page URL or any other success page
            return redirect('/home/')  # Change this to your home page URL
        else:
            # Check if both username and password are incorrect
            if 'username' in form.errors and 'password' in form.errors:
                error_message = 'Username and password are incorrect.'
            elif 'username' in form.errors:
                error_message = 'Username is incorrect.'
            elif 'password' in form.errors:
                error_message = 'Password is incorrect.'
            else:
                error_message = 'Invalid username or password.'
    else:
     #   form = AuthenticationForm()
        error_message = None

    return render(request, 'login.html', {'form': form, 'error_message': error_message})
    
    """

"""
def search_items(request):

    query = request.GET.get('q')
    if query:
        items = Item.search(query)
    else:
        items = Item.objects.all()

    # Your remaining logic here...

    return render(request, 'item.html', {'items': items, 'query': query})
"""



def item_list(request):
    query = request.GET.get('q')
    items = Item.objects.all()

    if query:
        items = items.filter(name__icontains=query)

    return render(request, 'main.html', {'items': items})


@login_required
def chatMessage(request, item_pk):
    categories = Category.objects.all()
    conversation1 = Conversation.objects.filter(members__in=[request.user.id])
    forms = ConversationMessageForm()
    item = get_object_or_404(Item, pk=item_pk)
    if item.created_by == request.user:
        return redirect('main')

    conversation  =  Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversation:
        return redirect('detail', pk=conversation.first().id)
    if request.method == 'POST':
        forms = ConversationMessageForm(request.POST)
        conversation = Conversation.objects.create(item=item)
        conversation.members.add(request.user)
        conversation.members.add(item.created_by)
        conversation.save()
        conversation_message = forms.save(commit=False)
        conversation_message.conversation =conversation
        conversation_message.created_by =request.user
        conversation_message.save()
        return redirect('item_detail',item_id=item_pk)

    else:
        forms = ConversationMessageForm()

    return render(request, 'chat.html',{'forms': forms, 'conversation1': conversation1,'categories':categories})


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    categories = Category.objects.all()

    return render(request, 'inbox.html', {
        'conversations': conversations,
        'categories':categories
    })



@login_required
def detail(request, pk):
    categories = Category.objects.all()

    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'detail.html', {
        'conversation': conversation,
        'form': form,
        'categories':categories
    })
def category_items(request, category_id):
    categories = Category.objects.all()
    # Retrieve the category object using its ID

    category = get_object_or_404(Category, id=category_id)

    if category:
        items = category.items.all()

    # Retrieve all items associated with the category

    # You can add additional context data if needed
        context = {
         'category': category,
            'items': items,
            'categories': categories
        }

    # Render the template with the context data

    return render(request, 'category_items.html', context)
