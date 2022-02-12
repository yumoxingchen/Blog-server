def findArticleList():
  with open("database/articleList/data.json","r") as f:
    result = f.read()  
  return result