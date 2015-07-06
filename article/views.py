# -*8 coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import articleModel
from config import webConfig
from article import article_head

def article_list(request, page = '1'):
    title = '城镇规划展示'
    article_instance = articleModel()
    if not page:
        page = '1'
    articles = article_instance.getArticleList(page=int(page))
    # print len(articles)
    articlesForHtml = []
    for temp in articles:
        article_head_temp = article_head(temp)
        # print article_head_temp.title
        articlesForHtml.append(article_head_temp)

    article_num = article_instance.getArticleNum()
    page_totle = article_num / webConfig.PAGENUM + 1

    if page == '1':
        previous_page = '1'
    else:
        previous_page = str(int(page) - 1)

    if page == str(page_totle):
        next_page = str(page_totle)
    else:
        next_page = str(int(page) + 1)

    ye = (int(page) - 1) / 5
    pages = []
    for i in range(5):
        pages.append(ye * 5 + i + 1)
    if int(page) > (int(page_totle) - int(page_totle) % 5):
        pages = []
        pages.append(int(page_totle) - 4)
        pages.append(int(page_totle) - 3)
        pages.append(int(page_totle) - 2)
        pages.append(int(page_totle) - 1)
        pages.append(int(page_totle))

    return render_to_response("index.html",
                              {
                                  "title": title,
                                  'articles': articlesForHtml,
                                  'project_name': webConfig.PROJECTNAME,
                                  'toplabel1': webConfig.TOPLABEL1,
                                  'toplabel2': webConfig.TOPLABEL2,
                                  'toplabel3': webConfig.TOPLABEL3,
                                  'toplabel4': webConfig.TOPLABEL4,
                                  'page_total': page_totle,
                                  'page': page,
                                  'previous_page': previous_page,
                                  'next_page': next_page,
                                  'pages': pages,

                              }
                              )
