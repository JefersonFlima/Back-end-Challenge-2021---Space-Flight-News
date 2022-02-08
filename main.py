
import string
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

# Rota Raiz
@app.get("/")
def Raiz():
    return "Back-end Challenge 2021 🏅 - Space Flight News"

# modelo dos dados
class Artigos(BaseModel):
    id: int
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str


# base de dados

base_de_dados = [
    Artigos(id= 1,
      title= "Space Development Agency, General Atomics eye options after setback in laser comms experiment",
      url= "https://spacenews.com/space-development-agency-general-atomics-eye-options-after-setback-in-laser-comms-experiment/",
      imageUrl= "https://spacenews.com/wp-content/uploads/2022/02/featured-LaserCommDemo.jpg",
      newsSite= "SpaceNews",
      summary= "After a setback in a laser communications experiment launched last June, the Space Development Agency and satellite manufacturer General Atomics are considering next steps.",
      publishedAt= "2022-02-06T17:59:37.000Z",
      updatedAt= "2022-02-06T17:59:37.818Z"),
    Artigos(id= 2,
      title= "Expedition 66 begins 2022 aboard the International Space Station",
      url= "https://www.nasaspaceflight.com/2022/02/expedition-66-january-2022/",
      imageUrl= "https://www.nasaspaceflight.com/wp-content/uploads/2022/02/iss-16012022.jpg",
      newsSite= "NASA Spaceflight",
      summary= "The start of 2022 saw no let-up for the Expedition 66 crew aboard the International Space Station, who are continuing their busy schedule of maintenance, science, and operations aboard their outpost in low Earth orbit. January saw the installation of new external experiments, a spacewalk by the two Russian crewmembers, the departure of a Cargo Dragon spacecraft, and the deployment of five small satellites.",
      publishedAt= "2022-02-06T18:50:34.000Z",
      updatedAt= "2022-02-06T18:59:38.926Z"),
    Artigos(id= 3,
      title= "NASA outlines cost savings from ISS transition",
      url= "https://spacenews.com/nasa-outlines-cost-savings-from-iss-transition/",
      imageUrl= "https://spacenews.com/wp-content/uploads/2021/12/ng-spacestation.jpg",
      newsSite= "SpaceNews",
      summary= "NASA expects that retiring the International Space Station in favor of leasing capacity on commercial space stations will ultimately save the agency up to $1.8 billion per year.",
      publishedAt= "2022-02-06T23:49:38.000Z",
      updatedAt= "2022-02-06T23:49:38.329Z"),
    Artigos(id= 4,
      title= "Launcher buys additional SpaceX rideshare missions",
      url= "https://spacenews.com/launcher-buys-additional-spacex-rideshare-missions/",
      imageUrl= "https://spacenews.com/wp-content/uploads/2021/06/launcher-orbiter.jpg",
      newsSite= "SpaceNews",
      summary= "Launcher has purchased slots on three more SpaceX rideshare missions for its Orbiter tug as it continues development of a small launch vehicle.",
      publishedAt= "2022-02-07T11:59:38.000Z",
      updatedAt= "2022-02-07T11:59:38.170Z"),
]

# Rota com todos artigos
@app.get("/Articles")
def Articles():
    return base_de_dados

# Procurar artigo pela ID
@app.get("/articles/{id_user}")
def Article_ID(id_user: int):
    for Artigos in base_de_dados:
           if(Artigos.id==id_user):
                 return Artigos
    return {"Status": 404,"Mensagem":"Usuario não encontrado"}
# Criar novo artigo
@app.post("/Articles")
def New_Article(artigo:Artigos):
    base_de_dados.append(artigo)
    return artigo

# Deletar um artigo
@app.delete("/articles/{id_user}")
def Deletar_Article(id_user:int):
    for Artigos in base_de_dados:
          if(Artigos.id==id_user):
            base_de_dados.remove(Artigos)
            return "Artigo removido com sucesso"
    return {"Status": 404,"Mensagem":"Usuario não encontrado"}
