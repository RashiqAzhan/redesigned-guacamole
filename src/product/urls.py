from django.urls import path
from product.views.product import CreateProductView, IndexView
from product.views.variant import VariantCreateView, VariantEditView, VariantView


app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list/', IndexView.as_view(template_name='products/list.html', extra_context={
        'product': True
    }), name='list.product'),
]
