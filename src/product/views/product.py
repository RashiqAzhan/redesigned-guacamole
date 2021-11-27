from django.core.paginator import Paginator
from django.views import generic
from product.models import ProductVariantPrice, Variant


class IndexView(generic.ListView):
    model = ProductVariantPrice
    template_name = 'products/list.html'
    paginate_by = 2
    paginator = Paginator(ProductVariantPrice, 2)
    page_range = paginator.get_elided_page_range(number=4)

    def get_queryset(self, **kwargs):
        query = ProductVariantPrice.objects.all()
        return query

class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
