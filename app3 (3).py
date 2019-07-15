# DASH APP - ECE PARAGUAY

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table

import pandas as pd
import numpy as np

##################################################
# Data Manipulation
##################################################

# Loading and cleaning data
df = pd.read_csv('ECE.csv')

# Estandarizando el tipo de los datos
for i in df.columns:
    df[i] = pd.to_numeric(df[i], errors='coerce')
# Removiendo NR ("1.000000e+10") de variables de salario   
for i in df.columns:
    df[i].replace(9999999999, np.nan, inplace=True)
# Trimestre y año categoricos
df['trimestre'] = df['trimestre'].astype(str)
#df['year'] = df['year'].astype('category')

    
    
    
    
    
# MAPPING VALUES:

 #1 ED01
di = {1:'Guaraní',2:'Guaraní y castellano', 3:'Castellano', 4:'Otro idioma', 5:'No habla'}   
df['ED01'] = df['ED01'].map(di) 

 #2 Sector Economico RECB02
di2 = {1: 'Agricultura, ganadería, caza, silvicultura y pesca',2:'Explotación de minas y canteras',
       3:'Industrias manufactureras', 4:'Electricidad, gas y agua', 
       5:'Construcciones' , 6:'Comercio al por mayor y menor, restaurantes y hoteles',
       7:'Transporte, almacenamiento y comunicaciones',
       8:'Establecimientos financieros, seguros y bienes inmuebles',
       9:'Servicios comunales, sociales y personales'}
df['RECB02'] = df['RECB02'].map(di2) 

 #3 P04
#di3 = {1:'Hombre',6:'Mujer'}   
#df['P04'] = df['P04'].map(di3)

#4 AÑOESTU (ED04)
di4 = {1: 'Sin instrucción',
 2: 'Jardín o Preescolar',
 3: 'Educ. Especial',
 4: 'EEB 1ª al 6ª (Primaria)',
 5: 'EEB 7º al 9º',
 6: 'Secundario Ciclo Básico',
 7: 'Bachiller Humanístico / Científico',
 8: 'Bachiller Técnico / Comercial',
 9: 'Bachillerato a distancia',
 10: 'Educación Media Científica',
 11: 'Educación Media Técnica',
 12: 'Educ. Básica Bilingüe de Jóvenes y Adultos',
 13: 'Educ. Media a Distancia para Jóvenes y Adultos',
 14: 'Educ. Básica Alternativa de Jóvenes y Adultos',
 15: 'Educ. Media Alternativa de Jóvenes y Adultos',
 16: 'Formación Profesional no Bachillerato de la Media',
 17: 'Programa de Alfabetización',
 18: 'Grado especial / Programas Especiales',
 19: 'Técnica Superior',
 20: 'Formación Docente',
 21: 'Profesionalización Docente',
 22: 'Formación Militar/Policial',
 23: 'Universitario'}
df['AÑOESTU'] = df['AÑOESTU'].map(di4)

#5 Ocupacion RECB01
di5 = {1: 'Sector Publico', 
 2: 'Profesionales científicos e intelectuales',
 3: 'Técnicos y profesionales de nivel medio',
 4: 'Empleados de oficina',
 5: 'Servicios y vendedores de comercios y mercados',
 6: 'Agricultores y trabajadores Agropecuarios y Pesqueros',
 7: 'Oficiales, operarios y artesanos de artes mecánicas y de otros oficios',
 8: 'Operadores de instalaciones y máquinas y montadores',
 9: 'Trabajadores no calificados',
 10: 'Fuerzas armadas',
 99: 'NR'}

df['RECB01'] = df['RECB01'].map(di5) 

#6 Que hizo para conseguir trabajo en el ultimo mes? A06
di6= {1.0: 'Consultó a algún empleador o patrón',
 2.0: 'Consultó en alguna agencia',
 3.0: 'Consultó con amigos o parientes',
 4.0: 'Contestó / publicó avisos en los periódicos',
 5.0: 'Solicitó préstamo para trabajar por su cuenta ',
 6.0: 'Otras gestiones para trabajar por su cuenta',
 7.0: 'Internet',
 8.0: 'Otras gestiones '}
df['A06'] = df['A06'].map(di6)

#7 Cual es la razón principal por la qué no buscó trabajo en la semana pasada o en las 3 semanas anteriores a la semana pasada?
# A09
di7={1: 'No quiere trabajar más',
 2: 'No cree poder encontrar trabajo',
 3: 'Se cansó de buscar',
 4: 'No sabe donde consultar',
 5: 'Es demasiado joven',
 6: 'Se dedica exclusivamente a las labores del hogar',
 7: 'Es estudiante',
 8: 'Inclemencia del tiempo',
 9: 'Buscó y ahora está esperando noticias',
 10: 'Comenzará nuevo trabajo en el próximo mes',
 11: 'Estuvo enfermo',
 12: 'Es anciano o discapacitado',
 13: 'Es rentista',
 14: 'Es jubilado',
 15: 'Es pensionado',
 16: 'Motivos familiares',
 17: 'Otra razón '}
df['A09'] = df['A09'].map(di7)

#8 Categoría o posición que tenía en su última ocupación? A15
di8={1.0: 'Empleado / obrero público',
 2.0: 'Empleado / obrero privado',
 3.0: 'Empleador o patrón',
 4.0: 'Trabajador por cuenta propia',
 5.0: 'Trabajador familiar no remunerado',
 6.0: 'Empleado doméstico'}
df['A15'] = df['A15'].map(di8)

#9 Aproximadamente, cuántas personas trabajan en el establecimiento o negocio donde trabajaba en su última ocupación ? A16
di9={1.0: 'Solo',
 2.0: '2 a 5 personas',
 3.0: '6 a 10 personas',
 4.0: '11 a 20 personas',
 5.0: '21 a 50 personas',
 6.0: '51 a 100 personas',
 7.0: '101 a 500 personas',
 8.0: 'Más de 500 personas',
 9.0: 'Empleado doméstico',
 10.0: 'No sabe'}
df['A16'] = df['A16'].map(di9)

#10 Edades quinquenales
di10 = {1.0: '0 años - 4 años',
 2.0: '5 años - 9 años',
 3.0: '10 años - 14 años',
 4.0: '15 años - 19 años',
 5.0: '20 años - 24 años',
 6.0: '25 años - 29 años',
 7.0: '30 años - 34 años',
 8.0: '35 años - 39 años',
 9.0: '40 años - 44 años',
 10.0: '45 años - 49 años',
 11.0: '50 años - 54 años',
 12.0: '55 años - 59 años',
 13.0: '60 años y más'}
df['EDAD_QUIN'] = df['EDAD_QUIN'].map(di10)

#11 Actividad económica (DESAGREGADA) PEAD
di11={1.0: 'Ocupados (Excluyendo Subocupación Visible + Invisible)',
 2.0: 'Desocupados de 2ª ó más veces',
 3.0: 'Inactivos (Excluyendo Desempleo Oculto)',
 4.0: 'Subocup. Visible',
 5.0: 'Subocup. Invisible',
 6.0: 'Desempleo Oculto',
 7.0: 'Desocupados de 1ª vez',
 0.0: np.nan}

df['PEAD'] = df['PEAD'].map(di11)

#12 Actividad económica (AGRUPADA) PEAA
di12={1.0: 'Ocupados',
 2.0: 'Desocupados',
 3.0: 'Inactivos',
 0.0: np.nan}

df['PEAA'] = df['PEAA'].map(di12)

#13 Cuál es la razón principal por la que dejó su última ocupación ? A18
di13 = {1: 'Ganaba poco',
 2: 'No tenía ingreso',
 3: 'Fue despedido',
 4: 'Cerró el establecimiento',
 5: 'Terminó su contrato',
 6: 'Período de prueba',
 7: 'Es estudiante',
 8: 'Se jubiló',
 9: 'Ambiente inadecuado',
 10: 'Poco estable',
 11: 'Trabajo temporal',
 12: 'Labores del hogar',
 13: 'Falta de pedido',
 14: 'Motivo familiar',
 15: 'Anciano o discapacitado',
 16: 'Enfermedad',
 17: 'Otra razón'}
df['A18'] = df['A18'].map(di13)

#14 Bajo que tipo de contrato trabaja en esta ocupacion? B22
di14 = {1.0: 'Contrato indefinido (nombrado)',
 2.0: 'Contrato definido (temporal)',
 3.0: 'Sin contrato (acuerdo verbal)',
 4.0: 'Período de prueba'}
df['B22'] = df['B22'].map(di14)

#15 Desea mejorar su/sus ocupación/nes o cambiar o adicionar otra ocupación ?D01
di15 = {1.0: 'Sí, mejorar su ocupación',
 2.0: 'Sí, cambiar la o las ocupaciones',
 3.0: 'Sí, adicionar otra ocupación',
 4.0: 'No desea cambiar'}
df['D01'] = df['D01'].map(di15)

#16 Cuál es la razón principal por al que desea mejorar o cambiar o adicionar su empleo actual ? D02
di16 = {1.0: 'Gana poco',
 2.0: 'El trabajo es pesado',
 3.0: 'Desea trabajar menos horas sin ganar menos',
 4.0: 'Desea trabajar menos horas aunque gane menos',
 5.0: 'Desea trabajar más horas y ganar más',
 6.0: 'No aprovecha sus estudios y experiencias',
 7.0: 'Ambiente de trabajo inadecuado',
 8.0: 'Conflictos laborales',
 9.0: 'Poco estable',
 10.0: 'Motivo familiar, personal',
 11.0: 'Otra razón'}

df['D02'] = df['D02'].map(di16)

#17 País de orígen de ingresos del exterior E01GC
di17 = {1.0: 'Argentina',
 2.0: 'Brasil',
 3.0: 'EE.UU.',
 4.0: 'España',
 9.0: 'Otro'}

df['E01GC'] = df['E01GC'].map(di17)




    
# List of variables for second dropdown
drop_dict = {'RECB01':'Ocupación',
             'RECB02':'Sector Económico' ,
             'ED01':'Idioma Principal en Casa',
             'AÑOESTU':'Nivel o Curso más Alto Aprobado',
             'A06' : '¿Qué hizo para conseguir trabajo en el último mes?',
             'A09': 'Razón por la qué no buscó trabajo el último mes', 
             'A15':'Categoría o posición que tenía en su última ocupación',
             'A16': 'Número de personas que trabajan en su establecimiento de trabajo',
             'A18': 'Razón principal por la que dejó su última ocupación',
             'B22': 'Tipo de contrato de trabajo en su ocupacion principal',
             'D01': '¿Desea mejorar su ocupación o cambiar o adicionar otra ocupación?',
             'D02': 'Razón principal por la que desea cambiar o adicionar su empleo actual',
             'E01GC': 'País de orígen de ingresos del exterior',
             'EDAD_QUIN': 'Edad',
             'PEAD':  'Actividad económica (desagregada)',
             'PEAA': 'Actividad económica (agrupada)',
             'trimestre': 'Trimestre',
             
            }



# Function to generate table
def generate_table(dataframe, max_rows=10):
    '''Given dataframe, return template generated using Dash components
    '''
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


# Function to create Pivot table
def generate_pv(frame, variable):
    pv = pd.pivot_table(
    frame, 
    index = variable,
    values = ['P04'],   # sexo
    columns = 'A02',    # A02 tuvo un trabajo en la ultima semana
    aggfunc = len,
    fill_value=0)
    pv[variable] = pv.index
    pv['Total'] = pv.apply(lambda x: x.iloc[0] + x.iloc[1], axis=1)
    pv['Activo'] = (round(pv.iloc[:,0] / pv['Total'],2)*100).astype(str) + '%'
    pv['Inactivo']= (round(pv.iloc[:,1] / pv['Total'],2)*100).astype(str) + '%'
    #pv.drop('5 años - 9 años', inplace=True)
    
    return pv.iloc[:,2:]

def generate_gb(frame, variable):
    pv = frame.groupby([var,'trimestre'])[['trimestre']].count()
    pv = pv.unstack(level=1)
    pv = (100. * pv/ pv.sum()).round(1).astype(str) + '%'
    pv.insert(loc=0, column='RECB02', value=pv.index)
    
    return pv

    




app = dash.Dash()

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

colors = {
    'background': '#0C99F4',
    'plots': 'rgba(217, 217, 217, 0.3)',
    'text': '#7FDBFF'
}




##################################################
# Dashboard Layout / View
##################################################


app.layout = html.Div([  
    
  
    #Page Header
    html.H1("Encuesta Continua de Empleo Paraguay", style={'margin-left':80,
                                                           'margin-right':10,
                                                           'font-family': 'Helvetica',
                                                           "margin-top": 25, 
                                                           "margin-bottom": 25},),
         
    # Dropdown Grid

    html.Div([ 
        html.Div([
         
        # Dropdown año
            html.Div([
                html.Div('Seleccione el Año (Opcional)',
                         style={'font-style': 'bold', 
                                'font-weight': 'bold', 
                                'font-family': 'Helvetica',
                                'fontSize': 18},
                         className='four columns'),
                html.Div(dcc.Dropdown(id="drop-1",
                        options=([{'label': year, 'value': year } for year in df['year'].unique()]),
                        value= None,
                        className='eight columns',  style={'margin-left':10,'margin-right':10}))
                    ]),
      
        
        # Dropdown variable
            html.Div([
                html.Div('Seleccione la Variable', 
                         style={'font-style': 'bold', 
                                'font-weight': 'bold', 
                                'font-family': 'Helvetica',
                                'fontSize': 18}, 
                         className='four columns'),
                html.Div(dcc.Dropdown(id="drop-2",
                        options = ([{'label': label, 'value': var} for var,label in drop_dict.items()]),
                        value= 'EDAD_QUIN',
                        className='eight columns',  style={'margin-left':10,'margin-right':10}))
                    ]),
            
        ], className='six columns'),

        # Empty
        html.Div( className='six columns'), 
    ],   className='twleve columns'),      # Closes dropdown grid

    
    # Graphs grid
    html.Div([

        # Graficos izquierdos 
        html.Div([
            # Graph1
            dcc.Graph(id='funnel-graph-1', style={'height':'500px'}),
            
            # Graph2
            dcc.Graph(id='funnel-graph-2', style={'height': '700px'})
            
            
        ], className='six columns'),
       

        # Graficos derechos 
        html.Div([

            # Graph3
            dcc.Graph(id='funnel-graph-3', style={'height': '700px'}),
            
            # summary table
            html.Table(id='variable-table-1',style={'height': '500px',
                                                   'margin-left':50,
                                                    'margin-right':10}),
            
            # style={},

        ], className='six columns')
       
    ] , style={'backgroundColor':colors['plots']}, className = 'twelve columns'),
    # Third grid
    html.Div([
        
        # Radio
 #       html.Div([
 #           
  #          dcc.RadioItems(id='radio-item',
  #              options=[
   #                     {'label': 'Stack', 'value': 'stack'},
    #                    {'label': 'Grouped', 'value': 'group'},
     #               ],
      #              value='Grouped' ) 
       # ], className = 'one columns'),
        
          # Graph 5
        html.Div([
            dcc.Graph(id='funnel-graph-5', style={'height': '600px'}) ,      
        ], className='twelve columns'),

    ], className = 'twelve columns'),
    
],  style={'backgroundColor': colors['background']})    # Final Structure parenthesis
    
    

##################################################
# Callbacks
##################################################



# 1. Function to update first graph
@app.callback(
    dash.dependencies.Output('funnel-graph-1', 'figure'),
    [dash.dependencies.Input('drop-1', 'value')])

def update_graph_1(year):
    if year == None:
        frame = df.copy()
    else:
        frame = df[df['year'].isin([year])]
    
    variable = 'EDAD_QUIN'   
    
    frame_men = frame[frame['P04']==1]
    frame_women = frame[frame['P04']==6]
    
    pv = generate_pv(frame, variable)
    pv1 = generate_pv(frame_men,variable)
    pv2 = generate_pv(frame_women,variable)
    
    for i in [pv,pv1, pv2]:
        if '5 años - 9 años' in i.index:
            i.drop(['5 años - 9 años'],inplace=True)
    
    trace1 = go.Scatter(x=pv.index, y=pv['Activo'],
                        name='Total Poblacion Activa',
                        marker=dict(color= 'rgba(50, 171, 96, 0.7)'))
    trace2 = go.Scatter(x=pv1.index, y=pv1['Activo'], 
                        name='Poblacion Masculina Activa',
                        marker=dict(color='rgba(55, 128, 191, 0.7)'))
    trace3 = go.Scatter(x=pv2.index, y=pv2['Activo'], 
                        name='Poblacion Femenina Activa',
                        marker=dict(color='rgba(219, 64, 82, 0.7)'))   
    
    if year == None:
        title = 'Todos los Años'
    else:
        title = year
        
    return {
        'data': [trace1, trace2, trace3],
        'layout':
        go.Layout(
            plot_bgcolor=colors['plots'],
            paper_bgcolor= colors['plots'],
            title={"text":'Poblacion Activa por Edad -  {}'.format(title),
                   "font": {"family": 'Helvetica',
                            "size": 24,
                            },
                  },
            )
    }
# 2. Function to update second graph PIE chart
@app.callback(
    dash.dependencies.Output('funnel-graph-2', 'figure'),
    [dash.dependencies.Input('drop-2', 'value'),
    dash.dependencies.Input('drop-1', 'value')] )

def update_graph_2(var, year):
    if year == None:
        frame = df
        
    else:
        frame = df[df['year']==year]
    


    #frame[var].fillna(0,inplace=True)
    pv = frame.groupby([var]).size()
    #pv = (100. * pv/ pv.sum()).round(1)
   
    # Title
    if year!= None:
        title =  drop_dict[var] +' - Distribución - {}'.format(year)
    else:
        title = drop_dict[var] + ' - Distribución - Todos los Años'
        
    return {
        "data": [go.Pie(labels=pv.index.tolist(), values=pv.tolist(),
                        opacity=0.7)],
        "layout": go.Layout(
                            plot_bgcolor=colors['plots'],
                            paper_bgcolor= colors['plots'],
                            title={"text": title,
                                   "font": {"family": 'Helvetica',
                                    "size": 22,
                            },
                  },
                            margin={"l": 200, "r": 200, },
                            legend={"x": 1, "y": 0.7})}


# 3. Function to make table of trimestres
@app.callback(
    dash.dependencies.Output('variable-table-1', 'children'),
    [dash.dependencies.Input('drop-2', 'value'),
    dash.dependencies.Input('drop-1', 'value')] )

def update_table_1 (var, year):
       
    if year == None:
        frame = df[df[var].notnull()]
    else:
        frame = df[(df['year']==year) & (df[var].notnull())]
    
    
    # Title
    if year!= None:
        title =  drop_dict[var] +' - {}'.format(year)
    else:
        title = drop_dict[var] + ' - Todos los Años'
    
    
        
    pv = frame.groupby([var,'trimestre'])[['trimestre']].count()
    pv = pv.unstack(level=1)
    pv = (100. * pv/ pv.sum()).round(1).astype(str) + '%'
    pv.insert(loc=0, column= title, value=pv.index)
    
    return generate_table(pv, max_rows=50)


# 4. Function to update third graph
@app.callback(
        dash.dependencies.Output('funnel-graph-3', 'figure'),
        [dash.dependencies.Input('drop-2', 'value'),
        dash.dependencies.Input('drop-1', 'value')])

def update_graph_3(var, year):    
    if year == None:
        frame = df.copy()
    else:
        frame = df[df['year'].isin([year])]
    
    pv = frame.groupby([var,'P04'])[['P04']].count()
    pv = pv.unstack(level=1)
    pv = (100. * pv/ pv.sum()).round(1).astype(str) + '%'


    trace1 = go.Bar(y=pv.index, x=pv[('P04',1)], 
                    name='Poblacion Masculina', 
                    orientation='h',                
                    marker=dict(color='rgba(55, 128, 191, 0.7)') )
                    
    trace2 = go.Bar(y=pv.index, x=pv[('P04',6)], 
                    name='Poblacion Femenina', 
                    orientation='h',
                    marker=dict(color='rgba(219, 64, 82, 0.7)'))
    #trace3 = go.Bar(x=pv2.index, y=pv2['Activo'], name='Poblacion Femenina',orientation='v')   
    
    if year == None:
        title= drop_dict[var] + (' - Por Género - Todos los Años')
    else:
        title= drop_dict[var] + (' - Por Género - {} '.format(year) )
    
        
    return {
        'data': [trace1, trace2],
        'layout':
        go.Layout(
            plot_bgcolor=colors['plots'],
            paper_bgcolor= colors['plots'],
            yaxis=dict(autorange="reversed",showticklabels=True, automargin=True), 
            title={"text": title,
                   "font": {"family": 'Helvetica',
                            "size": 22,
                            },
                  }, 
        )
    }   
  
    

# 5. Function for fourth graph
#@app.callback(
#    dash.dependencies.Output('funnel-graph-4', 'figure'),
#    [dash.dependencies.Input('drop-1', 'value')])

def update_graph_4(year):
    
    if year == None:
        frame = df.copy()
    else:
        frame = df[df['year'].isin([year])]
    traces = []
    for i in frame.P04.unique():
        
        df_by_gender = frame[frame['P04'] == i]
        
        traces.append(go.Scatter(
            x=df_by_gender['HORABH'],
            y=df_by_gender['E01T'],
            text=df_by_gender['P04'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=str(i)
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            plot_bgcolor=colors['plots'],
            paper_bgcolor= colors['plots'],
            
            xaxis={'type': 'log', 'title': 'Horas Trabajadas Habituales'},
            yaxis={'title': 'Salario Mes Pasado'},
            margin={'l': 50, 'b': 100, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


# 6. Function for fifth graph
@app.callback(
    dash.dependencies.Output('funnel-graph-5', 'figure'),
        [dash.dependencies.Input('drop-2', 'value'),
        dash.dependencies.Input('drop-1', 'value')
        ])


def update_graph_5(var,year):
    
    if year == None:
        frame = df.copy()

    else:
        frame = df[df['year'].isin([year])]
    
    
    pv = frame.groupby([var,'year'])[['E01T']].mean()
    pv = pv.unstack(level=1)
    pv = pv['E01T']
    traces = []
    for i in pv.index.unique():
        #df_plot = df[df[var] == i]

        traces.append(go.Bar(
            x=pv.columns.tolist(),
            y=pv.loc[i,:].tolist(),
            #text= pv.index,
            opacity=0.7,

            name=str(i)
        ))


   
    # Title
    if year == None:
        title= drop_dict[var] + (' - Ingreso Total Promedio ₲ - Todos los Años')
    else:
        title= drop_dict[var] + (' - Ingreso Total Promedio ₲ - {} '.format(year) )
        
    # Radio

        
    return {
        'data': traces,
        'layout':
        go.Layout(
            plot_bgcolor=colors['plots'],
            paper_bgcolor= colors['plots'],
            title={"text": title,
                   "font": {"family": 'Helvetica',
                            "size": 24,
                            },
                  },
            barmode= 'group')
    }






if __name__ == '__main__':
    app.run_server(debug=True)
