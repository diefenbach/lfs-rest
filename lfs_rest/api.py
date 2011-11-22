# tastypie imports
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from tastypie.resources import ModelResource
from tastypie.resources import ALL

# lfs imports
from lfs.catalog.models import Category
from lfs.catalog.models import Product


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        authorization = Authorization()


class CategoryResource(ModelResource):
    parent = fields.ForeignKey("self", "parent", null=True)
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        authorization = Authorization()
        authentication = BasicAuthentication()
        excludes = ["level", "uid"]
        filtering = {
            "name" : ALL,
        }
