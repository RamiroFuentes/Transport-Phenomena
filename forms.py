from wtforms import Form
from wtforms import StringField, TextField , FloatField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class TransportPhenomena(Form):
    W_Liquido = FloatField('W_Liduido',[validators.Required(message= 'El W Liquido es Requerido')])
    W_Solido = FloatField('W_Solido',[validators.Required(message= 'El W Solido es Requerido')])
    GE = FloatField('GE',[validators.Required(message= 'El GE es Requerido')])

