import web
import json

urls = (
  '/magicnight', 'magicnight'
)

app = web.application(urls, globals())

class magicnight:
  def GET(self):
    response = { 'response': 'hello Magic Night!' }
    web.header('Content-Type', 'application/json')
    return json.dumps(response)

if __name__ == "__main__":
  app.run()
