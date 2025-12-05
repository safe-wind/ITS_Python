import request

if __name__ == "__main__":

    headers = {
        'Content-type':'application/json',
        'Accept':'application/json'
    }

#ESEMPIO DI GET
response = request.get(
    url='http://localhost:5000/libri',
    headers=headers
)

print("Risposta GET:", response.json())

#ESEMPIO DI POST
payload = {
    "nome":"Marius",
    "azione":"crea"
}

response_post = request.post(
    url="http://localhost:500/api/utenti", #esempio di endpoint
    json=payload,
    headers=headers
)

print("Risposta POST:", response_post.json())

