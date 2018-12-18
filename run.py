# /run.py
import os

from app.app import create_app

if __name__ == '__main__':
  env_name = os.getenv('FLASK_ENV')
  app, product = create_app(env_name)

  print(product)

  # run app
  app.run()
