from flask import Flask,render_template,request,url_for,redirect
from db import Notes,engine
from sqlalchemy import select,update,Delete
from sqlalchemy.orm import sessionmaker

sess=sessionmaker(bind=engine)

con=sess()



app=Flask(__name__)


@app.route("/")
def home():
    
    data=con.execute(select(Notes))
    res=data.scalars().all()
    

    
    return render_template("home.html",data=res)

@app.route("/viewarticle/<id>")
def viewarticle(id):
    
    data=con.execute(select(Notes).where(Notes.id==id))
    res=data.scalars().one()
    

    
    return render_template("view.html",data=res)



@app.route("/add",methods=["GET","POST"])
def addnotes():
    if request.method =="POST":
        title=request.form["title"]
        desc=request.form["desc"]
        note=Notes(title,desc)
        if title!=None:
          try:
            con.add(note)
            con.commit()
            return redirect(url_for("home"))
          except Exception as e:
              return str(e)  
    else:
        return render_template("add.html")
    
@app.route("/editnotes/<id>")
def editnotes(id):
    
        data=con.execute(select(Notes).where(Notes.id==id))
        res=data.scalars().one()
        return render_template("edit.html",data=res)
   
@app.route("/edit",methods=["GET","POST"])
def edit():
    if request.method =="POST":
        
        print(id)
        try:
            stmt=update(Notes).where(Notes.id==request.form.get("id")).values(title=request.form.get('title'),description=request.form.get('desc'))
            print(stmt)
            con.execute(stmt)
            con.commit()
            return redirect(url_for("home"))
        except Exception as e:
              return str(e)
        
@app.route("/delete/<id>",methods=["GET","POST"])
def delete(id):
    
        try:
            
           
            con.execute(Delete(Notes).where(Notes.id==id))
            con.commit()
            return redirect(url_for("home"))
        except Exception as e:
              return str(e)

if __name__=="__main__":
    app.run()