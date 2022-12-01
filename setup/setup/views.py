from django.shortcuts import render
import json
import requests  # faz requisições HTTP

#url base da API
BASE_URL = "http://127.0.0.1:8000"

def Produtos_base(request):
    #listando produto
    api = BASE_URL + "/produtos"
    requisicao = requests.get(api)

    try:
        lista = requisicao.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "dados": dicionario
    }

    if request.method == "POST":

        nome = request.POST['nome']
        preco = request.POST['preco']
        descricao = request.POST['descricao']
        categoria = request.POST['categoria']

        new_prod = {"nome": nome, "preco": preco,
                      "descricao": descricao, "categoria": categoria}
        #Criando produto
        requests.post(api, data=new_prod)
    
    return render(request, "index.html", contexto)

def Produtos_delete(request, pk):
    
    api = BASE_URL + f"/produtos/{pk}/"
        
    #Deleta o produto
    response = requests.delete(
        api, data=json.dumps(pk), headers ={'content-type':"application/json"}
    )
   

    return render(request, "index.html")


def Produtos_putID(request, pk):
    #Altera o produto
    api = BASE_URL + f"/produtos/{pk}/"
    if request.method == "POST":
        
        nome = request.POST['nome']
        preco = request.POST['preco']
        descricao = request.POST['descricao']
        categoria = request.POST['categoria']

        new_prod = {"nome": nome, "preco": preco,
                      "descricao": descricao, "categoria": categoria}
        
        requisicao = requests.put(api, data=new_prod)
    
    req = requests.get(api).json()
    

    
   

    return render(request, "index.html",{"req": req} )