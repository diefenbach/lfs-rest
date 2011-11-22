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
    categories = fields.ToManyField("lfs_rest.api.CategoryResource", "categories", null=True)

    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        authorization = Authorization()
        authentication = BasicAuthentication()
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
        resource_name = 'category'
        authorization = Authorization()
        authentication = BasicAuthentication()
        excludes = ["level", "uid"]
        filtering = {
            "name": ALL,
        }
