"""smartdevice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import companycontroller
from . import statecitycontrol
from . import admincontroller
from . import categorycontroller
from . import subcategorycontroller
from . import modelcontroller
from . import companylogin
from . import ProductController
from . import customercontroller





urlpatterns = [
    path('admin/', admin.site.urls),
    # path('adminlogin/',companycontroller.adminlogin),

    # company

    path('compinter/', companycontroller.companyinterface),
    path('subcompinter', companycontroller.submitcompanyinterface),
    path('disallcomp/', companycontroller.displayallcompanies),
    path('compdisplaybyid/', companycontroller.compdisplaybyid),
    path('subcompdisplaybyid/', companycontroller.subcompdisplaybyid),
    path('picdisplaybyid/', companycontroller.picdisplaybyid),
    path('subpicdisplaybyid', companycontroller.subpicdisplaybyid),
    # path('deletebyid/', companycontroller.deletebyid),

    # *******

    # category

    path('catint/', categorycontroller.categoryinterface),
    path('subcatint', categorycontroller.submitcategoryinterface),
    path('disallcat/', categorycontroller.displayallcategories),
    path('catpicdisplaybyid/', categorycontroller.catpicdisplaybyid),
    path('subcatpicdisplaybyid', categorycontroller.subcatpicdisplaybyid),
    path('catdisplaybyid/', categorycontroller.catdisplaybyid),
    path('subcatdisplaybyid/', categorycontroller.subcatdisplaybyid),


    # *******
    # subcategory

    path('subbcatint/', subcategorycontroller.subcategoryinterface),
    path('subsubbcatint', subcategorycontroller.submitsubcategoryinterface),
    path('disallsubcat/', subcategorycontroller.displayallsubcategory),
    path('subbcatpicdisplaybyid/', subcategorycontroller.subcatpicdisplaybyid),
    path('subsubcatpicdisplaybyid', subcategorycontroller.subsubcatpicdisplaybyid),
    path('subbcatdisplaybyid/', subcategorycontroller.subcatdisplaybyid),
    path('subsubcatdisplaybyid/', subcategorycontroller.subsubcatdisplaybyid),




    # *******

    # model

    path('modelint/', modelcontroller.modelinterface),
    path('submodelint', modelcontroller.submitmodelinterface),
    path('disallmod/', modelcontroller.displayallmodel),
    path('moddisplaybyid/', modelcontroller.modeldisplaybyid),
    path('submoddisplaybyid/', modelcontroller.submodeldisplaybyid),


    # *******

    path('fchstates/', statecitycontrol.fetchstates),
    path('fchcity/', statecitycontrol.fetchcity),
    path('fetchcategories/', categorycontroller.fetchcategories),
    path('fetchsubcategories/', subcategorycontroller.fetchsubcategories),
    path('fetchmodels/', modelcontroller.fetchmodels),
    path('fetchcompanies/', companycontroller.fetchcompanies),
    path('fetchprods/', ProductController.fetchprods),





    # admin login

    path('adminlogin', admincontroller.adminlogin),
    path('adminlogincheck', admincontroller.adminlogincheck),
    path('logout', admincontroller.logout),

    # *******

    # company login

    path('complogin', companylogin.complogin),
    path('complogincheck', companylogin.complogincheck),
    path('complogout', companylogin.complogout),



    # *******

    # customerlogin
    path('custint', customercontroller.customerinterface),
    path('subcustint', customercontroller.subcustomerinterface),
    path('custlogin', customercontroller.customerlogin),
    path('custlogincheck', customercontroller.customerlogincheck),
    path('categories', customercontroller.categories),
    path('companysubcategories', customercontroller.subcatdisplaybycatid),
    path('companyproducts', customercontroller.productdisplaybysubcatid),
    path('index/', customercontroller.index),

    # *********


    #  product
    path('productinterface/', ProductController.ProductInterface),
    path('submitproduct', ProductController.submitproduct),
    path('allproducts/', ProductController.Listallproducts),
    path('displaybyproductid/', ProductController.displaybyproductid),
    path('editdeleteproductrecord/', ProductController.editdeleteproductrecord),
    path('displayproductpicture/', ProductController.displayproductpicture),
    path('editproductpicture', ProductController.editproductpicture),

    # *******

]
