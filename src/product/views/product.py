from django.core.paginator import Paginator
from django.db.models import Q
from django.views import generic
from product.models import ProductVariant, ProductVariantPrice, Variant


class IndexView(generic.ListView):
    model = ProductVariantPrice
    template_name = 'products/list.html'
    paginate_by = 2
    paginator = Paginator(ProductVariantPrice, 2)
    page_range = paginator.get_elided_page_range(number=4)

    def get_queryset(self, **kwargs):
        title_query = self.request.GET.get('title')
        variant_query = self.request.GET.get('variant')
        price_from_query = self.request.GET.get('price_from')
        price_to_query = self.request.GET.get('price_to')
        date_query = self.request.GET.get('date')
        query = ProductVariantPrice.objects.all()
        if title_query:
            query = query.filter(product__title__icontains=title_query)
        elif variant_query:
            query = query.filter(Q(product_variant_one__variant_title=variant_query)
                                 | Q(product_variant_two__variant_title=variant_query)
                                 | Q(product_variant_three__variant_title=variant_query))
        elif price_from_query:
            query = query.filter(price__gte=price_from_query)
        elif price_to_query:
            query = query.filter(price__lte=price_to_query)
        elif date_query:
            # date not defined in SQL file as shown in diagram
            pass
        return query

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        filter_query = self.request.GET.get('title')
        if filter_query:
            color_query = ProductVariant.objects.filter(product__title__icontains=filter_query).filter(
                    variant__title__icontains='Color').values_list('variant_title', flat=True).distinct()
            size_query = ProductVariant.objects.filter(product__title__icontains=filter_query).filter(
                    variant__title__icontains='Size').values_list('variant_title', flat=True).distinct()
            style_query = ProductVariant.objects.filter(product__title__icontains=filter_query).filter(
                    variant__title__icontains='Style').values_list('variant_title', flat=True).distinct()
            context['color_variants'] = color_query
            context['size_variants'] = size_query
            context['style_variants'] = style_query
        return context

class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
