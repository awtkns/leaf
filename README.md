<p align="center">
  <img src="./readme-image.png" alt="Legacy Edition" height="300" />
</p>
<p align="center">
  <em>Fallhacks 2020 Submission</em></br>
  <sub>Team: Legacy Edition</sub>
</p>
<p align="center">
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/fastapi" />
<img alt="npm" src="https://img.shields.io/npm/v/npm" />
</p>

---
Build using python, fastapi, socketio, and nuxt,  **L**egacy **E**dition: **A**cronym **F**inder is a multiplayer acronym
game motivated by a simple problem; acronym recognition. Gameplay involves being the first person amongst an unlimited playerbase 
to correctly guess what the underlying phrase of an acronym. Points are then awarded and stored on a global leaderboard.

> Example: You are given SFU, and options would include Sloths For Us, Simon Fraser University, etc.

**L**egacy **E**dition: **A**cronym **F**inder, LEAF for short, is:
- **R**eady for online multiplayer
- **E**veryone of your friends can play
- **A**ll sorts of acronyms!
- **D**on't ever fail a hackathon again
- **Mo**ney will be yours!
- **E**dition is Legacy

## Tech Stack and Deployment
LEAF's backend is coded using [fastapi](https://fastapi.tiangolo.com/) and python 3.8. LEAF's frontend is coded 
using [nuxt.js](https://nuxtjs.org) (a vuejs framework) and the [vuetify](https://vuetifyjs.com/) material design framework.
LEAF uses a self developed framework to scrape the web for acronyms and then generate different incorrect versions of the same acronym.
We implemented an algorithm to generate incorrect acronym within a certain degree of "closeness" to the real acronym

### Running LEAF
To install LEAF, please follow the steps in order below.
**Note:** Docker an docker-compose is required to run this application (Needed for mongodb). 

**Mongo DB**
```bash
docker-compose up -d 
```

**Backend**
Installing and running backend.  **Note**: python > 3.5 is required. 
```bash 
cd backend
pip install -r requirements.txt
python asgi.py
```
The backend should now be visible in a browser at `localhost:5000`. It may take minute for the database to initialize.

**Frontend**
Installing and running frontend.  **Note**: nodejs lts is required.
```bash
cd frontent
npm install
npm run dev
```
The frontend should now be visible in a browser at `localhost:3000`.  The application should now be fully functional.

## Credits
- Word frequency data for acronym generation was found [here](http://norvig.com/ngrams/).
- https://stackoverflow.com/a/7331558/7910261
- https://github.com/ConnorSMaynes/allacronyms

