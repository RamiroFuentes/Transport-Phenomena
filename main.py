from flask import Flask
from flask import render_template
from flask import request
import forms #Directorio propio
from Control  import TransportPhenomenaGUI#Funciones del Controlador

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def Transport_GUI():
    title= "Fenomenos de Trasnporte"
    informacion = forms.TransportPhenomena(request.form)

    if request.method == 'POST' and informacion.validate(): #Validacion para el envio de datos
        W_Liquido = informacion.W_Liquido.data
        W_Solido = informacion.W_Solido.data
        GE = informacion.GE.data # Tiempo de asentamiento aun no usado
        inf = True
        (Cv,Mup_Mu) = TransportPhenomenaGUI(W_Liquido,W_Solido,GE)
        
    else:
       W_Liquido = None
       W_Solido = None
       GE = None
       inf = False
       Cv = None
       Mup_Mu = None

    return render_template('GUI.html',form = informacion, W_Liquido=W_Liquido,W_Solido=W_Solido,GE=GE,Cv=Cv,Mup_Mu=Mup_Mu,inf=inf)

if __name__ == '__main__':
    app.run(debug=True,port=8000)