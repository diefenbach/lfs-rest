# django imports
from django.contrib.auth.models import User

# tastypie imports
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from tastypie.resources import ModelResource
from tastypie.resources import ALL
from tastypie.serializers import Serializer

# lfs imports
try:
    from lfs.addresses.models import Address
except ImportError:
    from lfs.customer.models import Address

from lfs.catalog.models import Category
from lfs.catalog.models import Product
from lfs.customer.models import Customer
from lfs.order.models import Order
from lfs.order.models import OrderItem


class LFSSerializer(Serializer):
    def to_html(self, data, options=None):
        return self.to_json(data, options)


class ProductResource(ModelResource):
    categories = fields.ToManyField("lfs_rest.api.CategoryResource", "categories", null=True)

    class Meta:
        queryset = Product.objects.all()
        serializer = LFSSerializer()
        resource_name = 'product'
        authorization = Authorization()
        # authentication = BasicAuthentication()
        excludes = ["effective_price"]

        filtering = {
            "sku": ALL,
            "categories": ALL,
    }


class CategoryResource(ModelResource):
    parent = fields.ForeignKey("lfs_rest.api.CategoryResource", "parent", null=True)
    products = fields.ToManyField("lfs_rest.api.ProductResource", "products", null=True)

    class Meta:
        queryset = Category.objects.all()
        serializer = LFSSerializer()
        resource_name = 'category'
        authorization = Authorization()
        authentication = BasicAuthentication()
        excludes = ["level", "uid"]
        filtering = {
            "name": ALL,
        }


class OrderResource(ModelResource):
    items = fields.ToManyField("lfs_rest.api.OrderItemResource", "items", null=True)

    class Meta:
        queryset = Order.objects.all()
        serializer = LFSSerializer()
        resource_name = 'order'

        filtering = {
            "created": ALL,
        }


class OrderItemResource(ModelResource):
    product = fields.ForeignKey("lfs_rest.api.ProductResource", "product", null=True)
    order = fields.ForeignKey("lfs_rest.api.OrderResource", "order")

    class Meta:
        queryset = OrderItem.objects.all()
        serializer = LFSSerializer()
        resource_name = 'order-item'

        filtering = {
            "created": ALL,
        }


class CustomerResource(ModelResource):
    addresses = fields.ToManyField("lfs_rest.api.AddressResource", "addresses", null=True)

    class Meta:
        queryset = Customer.objects.all()
        serializer = LFSSerializer()
        resource_name = 'customer'


class AddressResource(ModelResource):
    customer = fields.ForeignKey("lfs_rest.api.CustomerResource", "customer", null=True)

    class Meta:
        queryset = Address.objects.all()
        serializer = LFSSerializer()
        resource_name = 'address'
