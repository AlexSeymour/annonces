from django.shortcuts import render, redirect, get_object_or_404
from annonces.models import Annonce, Image
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, InvalidPage
from django.contrib.auth.decorators import login_required
from annonces.forms import AnnonceForm
from django.forms import modelformset_factory

#TODO: Renommer AnnonceList (PEP8)


def AnnonceList(request, page="1"):
    annonces_list = Annonce.objects.all()

    paginator = Paginator(annonces_list, 5)

    try:
        annonces = paginator.page(page)

    except InvalidPage:
        annonces = paginator.page(1)

    return render(request, 'annonces/list.html', {'annonces':annonces})

"""
class AnnonceDetail(DetailView):
    template_name = 'annonces/detail.html'
    slug_field = 'slug_title'
    model = Annonce
"""

def annonce_detail(request, slug):
    annonce = Annonce.objects.prefetch_related('images').get(slug_title=slug)
    images = annonce.images.all()
    return render(request, 'annonces/detail.html', {'annonce': annonce, 'images': images})


@login_required
def create_annonce(request):
    ImageFormset = modelformset_factory(Image, fields=('image',), extra=3)

    if request.method == "POST":
        annonce_form = AnnonceForm(request.POST)
        if annonce_form.is_valid():
            annonce = annonce_form.save(commit=False)
            annonce.user = request.user.profile
            annonce.slug_title = slugify(annonce.title)
            annonce.save()

            image_formset = ImageFormset(request.POST, request.FILES)

            if image_formset.is_valid():
                instances = image_formset.save(commit=False)

                for instance in instances:
                    instance.annonce = annonce
                    instance.save()

            messages.add_message(request, messages.INFO, "Vous avez déposé une annonce.")
            return redirect(reverse('annonce:list'))
    else:
        annonce_form = AnnonceForm()
        image_formset = ImageFormset(queryset=Image.objects.none())
    return render(request, 'annonces/create_annonce.html', {'annonce_form': annonce_form, 'image_formset': image_formset})


@login_required
def update(request, pk):
    annonce = get_object_or_404(Annonce, pk=pk, user=request.user.profile)
    ImageForset = modelformset_factory(Image, fields=('image',))

    if request.method == "POST":
        annonce_form = AnnonceForm(request.POST, instance=annonce)
        if annonce_form.is_valid():
            annonce_form.save()
            messages.add_message(request, messages.INFO, "Vous avez mis à jour une annonce.")
            image_formset = ImageForset(request.POST, request.FILES)

            if image_formset.is_valid():

                instances = image_formset.save(commit=False)

                for instance in instances:
                    instance.annonce = annonce
                    instance.save()
            return redirect(reverse('annonce:list'))

    else:
        image_formset = ImageForset(queryset=Image.objects.filter(annonce=annonce))
        annonce_form = AnnonceForm(instance=annonce)

    return render(request, 'annonces/update_annonce.html', {'annonce_form':annonce_form, 'image_formset':image_formset})


class AnnonceDelete(DeleteView):
    model = Annonce
    success_url = reverse_lazy('annonce:list', kwargs={'page': '1'})
    slug_field = 'slug_title'


    def post(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, "Votre annonce vient d' être supprimée")

        return super(AnnonceDelete, self).post(request, *args, **kwargs)



def user_annonce_list(request, page="1"):
    annonces_list = Annonce.objects.filter(user=request.user.profile)

    paginator = Paginator(annonces_list, 5)

    try:
        annonces = paginator.page(page)

    except InvalidPage:
        annonces = paginator.page(1)

    return render(request, 'annonces/my_list.html', {'annonces': annonces})
