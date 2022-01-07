from django.urls import path
from .import views
from .views import Views_contact, Views_blog, Views_about, detailcheckout, Views_information,View_resetpass
from .views import LoginUser, RegisterUser
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('product/', views.view_product, name='view_product'),
   path('raucu/', views.view_category, name='view_category'),
   path('traicay/', views.view_category1, name='view_category1'),
   path('nuocep/', views.view_category2, name='view_category2'),
   path('cacloaihat/', views.view_category3, name='view_category3'),
   path('detailproduct/<int:id>/', views.detailproduct,name='detailproduct'),
   path('login/', LoginUser.as_view(), name='LoginUser'),
   path('logout/', views.log_out, name='LogoutUser'),
   path('register/', RegisterUser.as_view(), name='RegisterUser'),
   path('contact/', Views_contact.as_view(), name='about_name'),
   path('blog/', Views_blog.as_view(), name='blog_name'),
   path('information/', Views_information.as_view(), name='Views_information'),
   path('views_order/', views.Views_pendingpPr, name='Views_order'),
   path('resetpass/', View_resetpass.as_view(), name='resetpass'),
   path('about/', Views_about.as_view(), name='contact_name'),
   path('detailcheckout/', detailcheckout.as_view(), name='View_detailcheckout'),
   path('addtocart/', views.addcart, name='addcart'),
   path('detailcart/removecart/', views.removecart, name='remove'),
   path('detailcart/<int:id>/', views.detailcart, name='detailcart'),
   path('detailorder/', views.detailorder, name='detailorder'),
   path('check_login/', views.check_login, name='check_login'),
   path('admin/manage-order/', views.manage, name='manage'),
   path('admin/statistic-order/', views.statistic, name='statistic'),
   path('get-order/', views.get_all_order, name='get-order'),
   path('change_state/', views.change_state, name='change_state'),
   path('change_state_remove/', views.change_state_remove, name='change_state_remove'),
   path('export/<int:id>', views.export_invoice, name='export'),
   path('product_sold/', views.product_sold, name='product_sold'),
   path('order_sold/', views.order_sold, name='order_sold'),
   path('all_product/', views.all_product, name='all_product'),
   path('product_import/', views.product_import, name='product_import'),
]

