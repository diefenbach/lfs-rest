# django imports
from django.conf.urls.defaults import *

# tastypie imports
from tastypie.api import Api

# lfs_rest imports
from lfs_rest.api import ProductResource
from lfs_rest.api import CategoryResource

product_resource = ProductResource()
category_resource = CategoryResource()

v1_api = Api(api_name='api')
v1_api.register(ProductResource())
v1_api.register(CategoryResource())

urlpatterns = patterns('',
    (r'', include(v1_api.urls)),
)
