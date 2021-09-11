# Notas del proyecto

## Ejecutar app
```
# uvicorn main:app --reload
```

## Deploy en Heroku

https://towardsdatascience.com/how-to-deploy-your-fastapi-app-on-heroku-for-free-8d4271a4ab9

```
heroku login
heroku create nombre-app
heroku apps
git remote -v
heroku git:remote -a nombre-app

git commit -m "bla bla"
git push heroku master ó git push heroku main
heroku open
heroku logs
heroku info

```

https://janrax-translate.herokuapp.com/languages_list

https://janrax-translate.herokuapp.com/translate/

https://janrax-translate.herokuapp.com/docs
