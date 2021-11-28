from drf_writable_nested.serializers import WritableNestedModelSerializer
from product.models import Product, ProductVariant, ProductVariantPrice, Variant, ProductImage
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('__all__')

class ProductImageSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductImage
        fields = ('__all__')

class ProductVariantSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    variant = VariantSerializer()
    product = ProductSerializer()

    class Meta:
        model = ProductVariant
        fields = ('__all__')

class ProductVariantPriceSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    product = ProductSerializer()
    product_variant_one = ProductVariantSerializer()
    product_variant_two = ProductVariantSerializer()
    product_variant_three = ProductVariantSerializer()

    class Meta:
        model = ProductVariantPrice
        fields = ('__all__')
