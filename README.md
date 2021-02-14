<p align="center">
  <img src="./readme-image.png" alt="Legacy Edition" height="300" />
</p>
<p align="center">
  <strong>🏆 SFU Fall Hack 2020 Winner 🏆</strong></br>
  <em>Team: Legacy Edition</em></br>
  <a href="https://raw.githubusercontent.com/asim-shrestha/mountain-madness-2021/master/frontend/public/hero.png" target="_blaank">Demo</a></p>
<p align="center">
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/fastapi" />
<img alt="npm" src="https://img.shields.io/npm/v/npm" />
</p>

---
Built using python, fastapi, Firebase, and Next,  **The Meme Machine**, inspired by Susan Blackmore's book of the same name, seeks to bring the title to life.
This web app is a collaborative meme building platform that allows users to communicate solely in memes. Users can upload a meme template of their liking, 

## Tech Stack and Deployment
LEAF's backend is coded using [fastapi](https://fastapi.tiangolo.com/) and python 3.8. LEAF's frontend is coded 
using [next.js](https://nextjs.org) (a React framework) and React Bootstrap.
LEAF uses Firebase to store meme data such as images and various python libraries to not only create memes, but deep fry them 🔥.

### Running LEAF
To install LEAF, please follow the steps in order below.
**Note:** Docker and docker-compose is required to run this application (Needed for mongodb). 


**Backend**

Installing and running backend.  **Note**: python > 3.5 is required. 
```bash 
cd backend
pip install -r requirements.txt
python asgi.py
```
The backend should now be visible in a browser at `localhost:5000`. It may take minute for the database to initialize.

**Frontend**
Installing and running frontend.  **Note**: nodejs is required.
```bash
cd frontend
npm install
npm run dev
```
The frontend should now be visible in a browser at `localhost:3000`.  The application should now be fully functional.
