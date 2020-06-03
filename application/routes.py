from application import app, db
from flask import render_template, redirect, flash, url_for,request
# from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from application.models import contactUsQuery,adminLogin,insertProduct
from application.forms import contactUsQueryForm,adminLoginForm,insertProdcutForm
import codecs
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
# patch_request_class(app)  # set maximum file size, default is 16MB


@app.route("/")
def index():
    return render_template("home.html" )


@app.route("/product/")
@app.route("/product/<productType>")
def productPage(productType='award'):
    categoryMapping={}
    categoryMapping['award']='Award'
    categoryMapping['pg']='Personalized Gifts'
    categoryMapping['lapelpin']='Lapel Pin'
    categoryMapping['printing']='Printing'
    
    items=insertProduct.objects(category=categoryMapping[productType])
    # for item in items:
    #     print(item.productName)    
        # base64_data = codecs.encode(item.imageFile.read(), 'base64')
        # image = base64_data.decode('utf-8')
        # t=codecs.encode(item.imageFile.read(), 'base64')
        # t=t.decode('utf-8')
        # return image
    # return None
    return render_template("product.html",productType=productType,items=items,codecs=codecs)

@app.route("/contactus",methods=['GET','POST'])
def contactus():
    form=contactUsQueryForm()
    if form.validate_on_submit():
        email               =   form.email.data
        name                =   form.name.data
        queryDescription    =   form.queryDescription.data
        contactUsQuery(email=email,name=name,queryDescription=queryDescription).save()
        flash("Thank you for your query. We will get back to you soon.",'success')
        return redirect(url_for("index"))
    return render_template("contactus.html",contactus=True,form=form)

@app.route("/adminLogin",methods=['GET','POST'])
def adminLoginView():
    form=adminLoginForm()
    if form.validate_on_submit():
        email               =   form.email.data
        password            =   form.password.data
        # adminLogin(email=email,password=password).save()
        adminFromDB  =   adminLogin.objects(email=email).first()
        if adminFromDB and password == adminFromDB.password:
            flash("Hello Admin",'success')
        return redirect(url_for("admin"))
    # return render_template("contactus.html",contactus=True,form=form)
    return render_template("adminLogin.html",form=form)


@app.route("/admin",methods=['GET','POST'])
def admin():
    form=insertProdcutForm()
    if form.validate_on_submit():
        productName               =   form.productName.data
        category            =   form.category.data
        price   =   form.price.data
        imageFile   =   form.imageFile.data
        insertProduct(productName=productName,category=category,price=int(price),imageFile=imageFile).save()
        flash("Product Added Successfully",'success')
        return redirect(url_for("admin"))
    return render_template("admin.html",form=form)
