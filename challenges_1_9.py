# -*- coding: utf-8 -*-
"""Reto_Consolidado_1-9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VEOC-e89GubZRF0bsDIiLD5oalQa7CdD
"""

from random import seed
from random import randint


def add_data():
  print('------------------------------------------------------------')
  b={}
  b['Id_product']=int(input('Ingresa la identificacion del producto: '))
  a=input('Escriba el nombre del producto --> ')
  lis_Pro.append(a)
  b['Product_Name']=a
  b['Unit_Price']=int(input('Ingresa el precio por unidad: '))
  a=int(input('Escriba la categoria del producto: 00 \n 11 \n 22 '))
  if a==00:
    b['Category_ID']=categorias[0]
  elif a==11:
    b['Category_ID']=categorias[1]
  else:
    b['Category_ID']=categorias[2]
  Producto['Producto 1']=b
  print('------------------------------------------------------------')
  bb={}
  bb['Id_product']=int(input('Ingresa la identificacion del producto: '))
  a=input('Escriba el nombre del producto --> ')
  lis_Pro.append(a)
  bb['Product_Name']=a
  bb['Unit_Price']=int(input('Ingresa el precio por unidad: '))
  a=int(input('Escriba la categoria del producto: 00 \n 11 \n 22 \n'))
  if a==00:
    bb['Category_ID']=categorias[0]
  elif a==11:
    bb['Category_ID']=categorias[1]
  else:
    bb['Category_ID']=categorias[2]
  Producto['Producto 2']=bb
  print('------------------------------------------------------------')
  ab={}
  ab['Id_product']=int(input('Ingresa la identificacion del producto: '))
  a=input('Escriba el nombre del producto --> ')
  lis_Pro.append(a)
  ab['Product_Name']=a
  ab['Unit_Price']=int(input('Ingresa el precio por unidad: '))
  a=int(input('Escriba la categoria del producto: 00 \n 11 \n 22 '))
  if a==00:
    ab['Category_ID']=categorias[0]
  elif a==11:
    ab['Category_ID']=categorias[1]
  else:
    ab['Category_ID']=categorias[2]
  Producto['Producto 3']=ab
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  cb={}
  cb['Customer_id']=int(input('Ingresa la identificacion del Cliente: '))
  cb['Name']=str(input('Ingresa el primero y segundo nombre: '))
  cb['Gender']=str(input('M/F '))
  a=int(input('Ingrese 1 para si tiene credito \n otro para no '))
  if a==1:
    cb['Credit']= True
  else:
    cb['Credit']= False
  Customer['Client 1']=cb
  print('------------------------------------------------------------')
  eb={}
  eb['Customer_id']=int(input('Ingresa la identificacion del Cliente: '))
  eb['Name']=str(input('Ingresa el primero y segundo nombre: '))
  eb['Gender']=str(input('M/F '))
  a=int(input('Ingrese 1 para si tiene credito \n otro para no '))
  if a==1:
    eb['Credit']= True
  else:
    eb['Credit']= False
  Customer['Client 2']=eb
  print('------------------------------------------------------------')
  rb={}
  rb['Customer_id']=int(input('Ingresa la identificacion del Cliente: '))
  rb['Name']=str(input('Ingresa el primero y segundo nombre: '))
  rb['Gender']=str(input('M/F '))
  a=int(input('Ingrese 1 para si tiene credito \n otro para no '))
  if a==1:
    rb['Credit']= True
  else:
    rb['Credit']= False
  Customer['Client 3']=rb
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  qb={}
  qb['Sales_Rep_id']=int(input('Ingresa la identificacion del Vendedor: '))
  qb['Name']=str(input('Ingresa el primero y segundo nombre: '))
  qb['Numero']=int(input('Ingresa el numero movil: '))
  qb['COMMISSION_PCT']=int(input('Ingresa el Porcentaje de comisión por ventas: '))
  Sales_Rep['Vendedor 1']=qb
  print('------------------------------------------------------------')
  zb={}
  zb['Sales_Rep_id']=int(input('Ingresa la identificacion del Vendedor: '))
  zb['Name']=str(input('Ingresa el primero y segundo nombre: '))
  zb['Numero']=int(input('Ingresa el numero movil: '))
  zb['COMMISSION_PCT']=int(input('Ingresa el Porcentaje de comisión por ventas: '))
  Sales_Rep['Vendedor 2']=zb
  print('------------------------------------------------------------')
  mb={}
  mb['Sales_Rep_id']=int(input('Ingresa la identificacion del Vendedor: '))
  mb['Name']=str(input('Ingresa el primero y segundo nombre: '))
  mb['Numero']=int(input('Ingresa el numero movil: '))
  mb['COMMISSION_PCT']=int(input('Ingresa el Porcentaje de comisión por ventas: '))
  Sales_Rep['Vendedor 3']=mb
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')

def add_fac():
  c=Producto.copy()
  order=[] #code of products in order
  non=[]  #code of products in aleatorio
  for j in range(5):
    f = randint(10000, 99999)
    non.append(f)
    order.append(f)
    order_code.append(f)
  order.sort()
  order_code.sort()
  print('------------------------------------------------------------')
  oo={}
  oo['Dia']=int(input('Ingresa el dia: '))
  oo['Mes']=int(input('Ingresa el mes: '))
  oo['Año']=int(input('Ingresa el Año: '))
  print('Codigo de factura_1: ',order[0])
  oo['Codigo']=order[0]
  print('Desea ingresar el producto ',lis_Pro[0],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      oo['PRODUCT_1']=Producto['Producto 1']
      oo['Quantity_1']=x
    else:
      print('Cantidad incorrecta')
  print('Desea ingresar el producto ',lis_Pro[1],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      oo['PRODUCT_2']=Producto['Producto 2']
      oo['Quantity_2']=x
    else:
      print('Cantidad incorrecta')
  print('Desea ingresar el producto ',lis_Pro[2],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      oo['PRODUCT_3']=Producto['Producto 3']
      oo['Quantity_3']=x
    else:
      print('Cantidad incorrecta')
  print('------------------------------------------------------------')
  print('Presione 1 para ingresar el cliente 1: ',Customer['Client 1'])
  print('Presione 2 para ingresar el cliente 2: ',Customer['Client 2'])
  print('Presione otro para ingresar el cliente 3: ',Customer['Client 3'])
  x=int(input())
  if x==1:
    oo['Customer']=Customer['Client 1']
  elif x==2:
    oo['Customer']=Customer['Client 2']
  else:
    oo['Customer']=Customer['Client 3']
  print('------------------------------------------------------------')
  print('Presione 1 para ingresar el vendedor 1: ',Sales_Rep['Vendedor 1'])
  print('Presione 2 para ingresar el vendedor 2: ',Sales_Rep['Vendedor 2'])
  print('Presione otro para ingresar el vendedor 3: ',Sales_Rep['Vendedor 3'])
  x=int(input())
  if x==1:
    oo['Sales_Rep']=Sales_Rep['Vendedor 1']
  elif x==2:
    oo['Sales_Rep']=Sales_Rep['Vendedor 2']
  else:
    oo['Sales_Rep']=Sales_Rep['Vendedor 3']
  Facturas['Factura 1']=oo
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  PP={}
  PP['Dia']=int(input('Ingresa el dia: '))
  PP['Mes']=int(input('Ingresa el mes: '))
  PP['Año']=int(input('Ingresa el Año: '))
  print('Codigo de factura_2: ',order[1])
  PP['Codigo']=order[1]
  print('Desea ingresar el producto ',lis_Pro[0],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      PP['PRODUCT_1']=Producto['Producto 1']
      PP['Quantity_1']=x
    else:
      print('Cantidad incorrecta')
  print('Desea ingresar el producto ',lis_Pro[1],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      PP['PRODUCT_2']=Producto['Producto 2']
      PP['Quantity_2']=x
    else:
      print('Cantidad incorrecta')
  print('Desea ingresar el producto ',lis_Pro[2],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      PP['PRODUCT_3']=Producto['Producto 3']
      PP['Quantity_3']=x
    else:
      print('Cantidad incorrecta')
  print('------------------------------------------------------------')
  print('Presione 1 para ingresar el cliente 1: ',Customer['Client 1'])
  print('Presione 2 para ingresar el cliente 2: ',Customer['Client 2'])
  print('Presione otro para ingresar el cliente 3: ',Customer['Client 3'])
  x=int(input())
  if x==1:
    PP['Customer']=Customer['Client 1']
  elif x==2:
    PP['Customer']=Customer['Client 2']
  else:
    PP['Customer']=Customer['Client 3']
  print('------------------------------------------------------------')
  print('Presione 1 para ingresar el vendedor 1: ',Sales_Rep['Vendedor 1'])
  print('Presione 2 para ingresar el vendedor 2: ',Sales_Rep['Vendedor 2'])
  print('Presione otro para ingresar el vendedor 3: ',Sales_Rep['Vendedor 3'])
  x=int(input())
  if x==1:
    PP['Sales_Rep']=Sales_Rep['Vendedor 1']
  elif x==2:
    PP['Sales_Rep']=Sales_Rep['Vendedor 2']
  else:
    PP['Sales_Rep']=Sales_Rep['Vendedor 3']
  Facturas['Factura 2']=PP
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  LL={}
  LL['Dia']=int(input('Ingresa el dia: '))
  LL['Mes']=int(input('Ingresa el mes: '))
  LL['Año']=int(input('Ingresa el Año: '))
  print('Codigo de factura_3: ',order[2])
  LL['Codigo']=order[2]
  print('Desea ingresar el producto ',lis_Pro[0],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      LL['PRODUCT_1']=Producto['Producto 1']
      LL['Quantity_1']=x
    else:
      print('Cantidad incorrecta')
  print('Desea ingresar el producto ',lis_Pro[1],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      LL['PRODUCT_2']=Producto['Producto 2']
      LL['Quantity_2']=x
    else:
      print('Cantidad incorrecta')
  print('Desea ingresar el producto ',lis_Pro[2],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      LL['PRODUCT_3']=Producto['Producto 3']
      LL['Quantity_3']=x
    else:
      print('Cantidad incorrecta')
  print('------------------------------------------------------------')
  print('Presione 1 para ingresar el cliente 1: ',Customer['Client 1'])
  print('Presione 2 para ingresar el cliente 2: ',Customer['Client 2'])
  print('Presione otro para ingresar el cliente 3: ',Customer['Client 3'])
  x=int(input())
  if x==1:
    LL['Customer']=Customer['Client 1']
  elif x==2:
    LL['Customer']=Customer['Client 2']
  else:
    LL['Customer']=Customer['Client 3']
  print('------------------------------------------------------------')
  print('Presione 1 para ingresar el vendedor 1: ',Sales_Rep['Vendedor 1'])
  print('Presione 2 para ingresar el vendedor 2: ',Sales_Rep['Vendedor 2'])
  print('Presione otro para ingresar el vendedor 3: ',Sales_Rep['Vendedor 3'])
  x=int(input())
  if x==1:
    LL['Sales_Rep']=Sales_Rep['Vendedor 1']
  elif x==2:
    LL['Sales_Rep']=Sales_Rep['Vendedor 2']
  else:
    LL['Sales_Rep']=Sales_Rep['Vendedor 3']
  Facturas['Factura 3']=LL
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  AAA={}
  AAA['Dia']=int(input('Ingresa el dia: '))
  AAA['Mes']=int(input('Ingresa el mes: '))
  AAA['Año']=int(input('Ingresa el Año: '))
  print('Codigo de factura_4: ',order[3])
  AAA['Codigo']=order[3]
  print('Desea ingresar el producto ',lis_Pro[0],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      AAA['PRODUCT_1']=Producto['Producto 1']
      AAA['Quantity_1']=x
    else:
      print('Cantidad incorrecta')
  print('Desea ingresar el producto ',lis_Pro[1],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      AAA['PRODUCT_2']=Producto['Producto 2']
      AAA['Quantity_2']=x
    else:
      print('Cantidad incorrecta')
  print('Desea ingresar el producto ',lis_Pro[2],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      AAA['PRODUCT_3']=Producto['Producto 3']
      AAA['Quantity_3']=x
    else:
      print('Cantidad incorrecta')
  print('------------------------------------------------------------')
  print('Presione 1 para ingresar el cliente 1: ',Customer['Client 1'])
  print('Presione 2 para ingresar el cliente 2: ',Customer['Client 2'])
  print('Presione otro para ingresar el cliente 3: ',Customer['Client 3'])
  x=int(input())
  if x==1:
    AAA['Customer']=Customer['Client 1']
  elif x==2:
    AAA['Customer']=Customer['Client 2']
  else:
    AAA['Customer']=Customer['Client 3']
  print('------------------------------------------------------------')
  print('Presione 1 para ingresar el vendedor 1: ',Sales_Rep['Vendedor 1'])
  print('Presione 2 para ingresar el vendedor 2: ',Sales_Rep['Vendedor 2'])
  print('Presione otro para ingresar el vendedor 3: ',Sales_Rep['Vendedor 3'])
  x=int(input())
  if x==1:
    AAA['Sales_Rep']=Sales_Rep['Vendedor 1']
  elif x==2:
    AAA['Sales_Rep']=Sales_Rep['Vendedor 2']
  else:
    AAA['Sales_Rep']=Sales_Rep['Vendedor 3']
  Facturas['Factura 4']=AAA
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  AAB={}
  AAB['Dia']=int(input('Ingresa el dia: '))
  AAB['Mes']=int(input('Ingresa el mes: '))          #STOP
  AAB['Año']=int(input('Ingresa el Año: '))
  print('Codigo de factura_5: ',order[4])
  AAB['Codigo']=order[4]
  print('Desea ingresar el producto ',lis_Pro[0],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      AAB['PRODUCT_1']=Producto['Producto 1']
      AAB['Quantity_1']=x
    else:
      print('Cantidad incorrecta')
  print('Desea ingresar el producto ',lis_Pro[1],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      AAB['PRODUCT_2']=Producto['Producto 2']
      AAB['Quantity_2']=x
    else:
      print('Cantidad incorrecta')
  print('Desea ingresar el producto ',lis_Pro[2],'?')
  a=int(input('1 para si otro para no '))
  if a==1:
    x=int(input('Ingrese la cantidad: '))
    if x > 0:
      AAB['PRODUCT_3']=Producto['Producto 3']
      AAB['Quantity_3']=x
    else:
      print('Cantidad incorrecta')
  print('------------------------------------------------------------')
  print('Presione 1 para ingresar el cliente 1: ',Customer['Client 1'])
  print('Presione 2 para ingresar el cliente 2: ',Customer['Client 2'])
  print('Presione otro para ingresar el cliente 3: ',Customer['Client 3'])
  x=int(input())
  if x==1:
    AAB['Customer']=Customer['Client 1']
  elif x==2:
    AAB['Customer']=Customer['Client 2']
  else:
    AAB['Customer']=Customer['Client 3']
  print('------------------------------------------------------------')
  print('Presione 1 para ingresar el vendedor 1: ',Sales_Rep['Vendedor 1'])
  print('Presione 2 para ingresar el vendedor 2: ',Sales_Rep['Vendedor 2'])
  print('Presione otro para ingresar el vendedor 3: ',Sales_Rep['Vendedor 3'])
  x=int(input())
  if x==1:
    AAB['Sales_Rep']=Sales_Rep['Vendedor 1']
  elif x==2:
    AAB['Sales_Rep']=Sales_Rep['Vendedor 2']
  else:
    AAB['Sales_Rep']=Sales_Rep['Vendedor 3']
  Facturas['Factura 5']=AAB
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')

def Most_Sell():
  AAC={}
  AAC=Facturas.copy()
  AAD=[]
  AAD= AAC.popitem()   #takes the last key and values out of ACC
  f= AAD[1]         #takes the values of the facture
  AAE=f.get('Mes')
  MMes=[]
  MMes.append(AAE)    #List with all the months
  PP51=f.get('PRODUCT_1',0)
  if PP51 !=0:
    PP51=PP51.get('Unit_Price',0)
  QQ51=f.get('Quantity_1',0)
  try_1= PP51*QQ51
  PP52=f.get('PRODUCT_2',0)
  if PP52 !=0:
    PP52=PP52.get('Unit_Price',0)
  QQ52=f.get('Quantity_2',0)
  try_2= PP52*QQ52
  PP53=f.get('PRODUCT_3',0)
  if PP53 !=0:
    PP53=PP53.get('Unit_Price',0)
  QQ53=f.get('Quantity_3',0)
  try_3= PP53*QQ53
  tryy= try_1 + try_2 + try_3
  pay_amount.append(tryy)
  AAD= AAC.popitem()   #takes the last key and values out of ACC FACTURA 4
  f= AAD[1]         #takes the values of the facture
  AAE=f.get('Mes')
  MMes.append(AAE)    #List with all the months
  PP41=f.get('PRODUCT_1',0)
  if PP41 !=0:
    PP41=PP41.get('Unit_Price',0)
  QQ41=f.get('Quantity_1',0)
  try_1= PP41*QQ41
  PP42=f.get('PRODUCT_2',0)
  if PP42 !=0:
    PP42=PP42.get('Unit_Price',0)
  QQ42=f.get('Quantity_2',0)
  try_2= PP42*QQ42
  PP43=f.get('PRODUCT_3',0)
  if PP43 !=0:
    PP43=PP43.get('Unit_Price',0)
  QQ43=f.get('Quantity_3',0)
  try_3= PP43*QQ43
  tryy= try_1 + try_2 + try_3
  pay_amount.append(tryy)
  AAD= AAC.popitem()   #takes the last key and values out of ACC FACTURA 3
  f= AAD[1]         #takes the values of the facture
  AAE=f.get('Mes')
  MMes.append(AAE)    #List with all the months
  PP31=f.get('PRODUCT_1',0)
  if PP31 !=0:
    PP31=PP31.get('Unit_Price',0)
  QQ31=f.get('Quantity_1',0)
  try_1= PP31*QQ31
  PP32=f.get('PRODUCT_2',0)
  if PP32 !=0:
    PP32=PP32.get('Unit_Price',0)
  QQ32=f.get('Quantity_2',0)
  try_2= PP32*QQ32
  PP33=f.get('PRODUCT_3',0)
  if PP33 !=0:
    PP33=PP33.get('Unit_Price',0)
  QQ33=f.get('Quantity_3',0)
  try_3= PP33*QQ33
  tryy= try_1 + try_2 + try_3
  pay_amount.append(tryy)
  AAD= AAC.popitem()   #takes the last key and values out of ACC FACTURA 2
  f= AAD[1]         #takes the values of the facture
  AAE=f.get('Mes')
  MMes.append(AAE)    #List with all the months
  PP21=f.get('PRODUCT_1',0)
  if PP21 !=0:
    PP21=PP21.get('Unit_Price',0)
  QQ21=f.get('Quantity_1',0)
  try_1= PP21*QQ21
  PP22=f.get('PRODUCT_2',0)
  if PP22 !=0:
    PP22=PP22.get('Unit_Price',0)
  QQ22=f.get('Quantity_2',0)
  try_2= PP22*QQ22
  PP23=f.get('PRODUCT_3',0)
  if PP23 !=0:
    PP23=PP23.get('Unit_Price',0)
  QQ23=f.get('Quantity_3',0)
  try_3= PP23*QQ23
  tryy= try_1 + try_2 + try_3
  pay_amount.append(tryy)
  AAD= AAC.popitem()   #takes the last key and values out of ACC FACTURA 1
  f= AAD[1]         #takes the values of the facture
  AAE=f.get('Mes')
  MMes.append(AAE)    #List with all the months
  PP11=f.get('PRODUCT_1',0)
  if PP11 !=0:
    PP11=PP11.get('Unit_Price',0)
  QQ11=f.get('Quantity_1',0)
  try_1= PP11*QQ11
  PP12=f.get('PRODUCT_2',0)
  if PP12 !=0:
    PP12=PP12.get('Unit_Price',0)
  QQ12=f.get('Quantity_2',0)
  try_2= PP12*QQ12
  PP13=f.get('PRODUCT_3',0)
  if PP13 !=0:
    PP13=PP13.get('Unit_Price',0)
  QQ13=f.get('Quantity_3',0)
  try_3= PP13*QQ13
  tryy= try_1 + try_2 + try_3
  pay_amount.append(tryy)
  askk=int(input('Please enter the number of the month'))
  Result_1=0
  Result_2=0
  Result_3=0
  if ((askk==MMes[0]) or (askk==MMes[1]) or (askk==MMes[2]) or (askk==MMes[3]) or (askk==MMes[4])):
    if askk==MMes[4]: #Factura 1
      Result_1=Result_1 + QQ11
      Result_2=Result_2 + QQ12
      Result_3=Result_3 + QQ13
    if askk==MMes[3]: #Factura 2
      Result_1=Result_1 + QQ21
      Result_2=Result_2 + QQ22
      Result_3=Result_3 + QQ23
    if askk==MMes[2]: #Factura 3
      Result_1=Result_1 + QQ31
      Result_2=Result_2 + QQ32
      Result_3=Result_3 + QQ33
    if askk==MMes[1]: #Factura 4
      Result_1=Result_1 + QQ41
      Result_2=Result_2 + QQ42
      Result_3=Result_3 + QQ43
    if askk==MMes[0]: #Factura 5
      Result_1=Result_1 + QQ51
      Result_2=Result_2 + QQ52
      Result_3=Result_3 + QQ53
    if Result_1==Result_2 and Result_1==Result_3:
      print('los productos: ',lis_Pro[0],',',lis_Pro[1],',',lis_Pro[2],' fueron vendidos por igual: ', Result_1)
    elif Result_1==Result_2 and Result_1 > Result_3:
      print('Los productos: ',lis_Pro[0],',',lis_Pro[1], ' fueron vendidos por igual: ',Result_1)
    elif Result_2==Result_3 and Result_2 > Result_1:
      print('Los productos: ',lis_Pro[1],',',lis_Pro[2], ' fueron vendidos por igual: ',Result_2)
    elif Result_1 > Result_2 and Result_1 > Result_3:
      print('El producto mas vendido fue: ', lis_Pro[0],' con ', Result_1,' Unidades')
    elif Result_2 > Result_1 and Result_2 > Result_3:
      print('El producto mas vendido fue: ', lis_Pro[1],' con ', Result_2,' Unidades')
    elif Result_3 > Result_2 and Result_3 > Result_1:
      print('El producto mas vendido fue: ', lis_Pro[2],' con ', Result_3,' Unidades')
    print('------------------------------------------------------------')
    print('------------------------------------------------------------')
    print('------------------------------------------------------------')      
  else:
    print('Zero sells, You need to get a JOB')
    print('------------------------------------------------------------')
    print('------------------------------------------------------------')
    print('------------------------------------------------------------')

def search():
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  valor_fac=int(input('Por favor ingrese el codigo de 5 digitos de la factura: '))
  if valor_fac==order_code[0]:
    print('El valor de la factura ', order_code[0],' es:  ',pay_amount[4])
  elif valor_fac==order_code[1]:
    print('El valor de la factura ', order_code[1
                                                ],' es:  ',pay_amount[3])
  elif valor_fac==order_code[2]:
    print('El valor de la factura ', order_code[2],' es:  ',pay_amount[2])
  elif valor_fac==order_code[3]:
    print('El valor de la factura ', order_code[3],' es:  ',pay_amount[1])
  elif valor_fac==order_code[4]:
    print('El valor de la factura ', order_code[4],' es:  ',pay_amount[0])
  else:
    print('Esa factura no existe!')
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')
  print('------------------------------------------------------------')


n=0
categorias=(00,11,22) #'Accesorios','PC','Phone'
lis_Pro=[] #Name of products
order_code=[] #Numero de las facturas
pay_amount=[] #Amount pay ----
Producto={} #Productos all infor
Customer={}
Sales_Rep={}
Facturas={}
while n==0:
  try:
    a=input("Por favor ingrese el Numero 1: para ingresar datos \n Numero 2: para añadir factura \n Numero 3: Producto mas vendido \n Numero 4: Consultar factura \n    0 para salir \n")
    a=int(a)
    if a==1:
      add_data()
    elif a==2:
      add_fac()
    elif a==3:
      Most_Sell()
    elif a==4:
      search()
    elif a==0:
      print('Customer',Customer)
      print('Sales_Rep',Sales_Rep)
      print('Producto',Producto)
      print('Lis_Pro',lis_Pro)
      print('Facturas',Facturas)
      print('order_code',order_code)
      print('pay_amount',pay_amount)
      break
    else:
      print("Ingrese un numero valido")
  except:
    print("Ingrese un valor valido")