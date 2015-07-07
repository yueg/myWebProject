# -*8 coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import articleModel
from config import webConfig
from article import article_head
from article import article_info

def article_list_view(request, category = 'index', page = '1'):
    print category
    print page
    title = '城镇规划展示'
    article_instance = articleModel()
    if not page:
        page = '1'

    if category == 'zcfb':
        article_type = 1
        category_name = webConfig.TOPLABEL1
    elif category == 'gsgg':
        article_type = 2
        category_name = webConfig.TOPLABEL2
    elif category == 'lddt':
        article_type = 3
        category_name = webConfig.TOPLABEL3
    elif category == 'hydt':
        article_type = 4
        category_name = webConfig.TOPLABEL4
    elif category == 'dfdt':
        article_type = 5
        category_name = webConfig.TOPLABEL5
    elif category == 'qtwz':
        article_type = 0
        category_name = webConfig.TOPLABEL6
    elif category == 'index':
        article_type = -1
        category_name = webConfig.TOPLABEL0
    else:
        article_type = -1
        category_name = webConfig.TOPLABEL0

    articles = article_instance.getArticleList(page=int(page), article_type = article_type)
    articlesForHtml = []
    for temp in articles:
        article_head_temp = article_head(temp)
        # print article_head_temp.title
        articlesForHtml.append(article_head_temp)

    article_num = article_instance.getArticleNum(article_type)
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
                                  'toplabel0': webConfig.TOPLABEL0,
                                  'toplabel1': webConfig.TOPLABEL1,
                                  'toplabel2': webConfig.TOPLABEL2,
                                  'toplabel3': webConfig.TOPLABEL3,
                                  'toplabel4': webConfig.TOPLABEL4,
                                  'toplabel5': webConfig.TOPLABEL5,
                                  'toplabel6': webConfig.TOPLABEL6,
                                  'page_total': page_totle,
                                  'page': page,
                                  'previous_page': previous_page,
                                  'next_page': next_page,
                                  'pages': pages,
                                  'category': category,
                                  'category_name': category_name

                              }
                              )


def article_info_view(request, id):
    article_instance = articleModel()
    article_temp = article_instance.getArticleInfoFromId(id)
    article = article_info(article_temp)
    max_id = article_instance.getMaxArticleId()
    min_id = article_instance.getMinArticleId()
    if int(id) == max_id:
        next_id = id
    else:
        next_id = str(int(id) + 1)
    if int(id) == min_id:
        previous_id = id
    else:
        previous_id = str(int(id) - 1)

    article_type = int(article.article_type)

    if article_type == 1:
        category = 'zcfb'
        category_name = webConfig.TOPLABEL1
    elif article_type == 2:
        category = 'gsgg'
        category_name = webConfig.TOPLABEL2
    elif article_type == 3:
        category = 'lddt'
        category_name = webConfig.TOPLABEL3
    elif article_type == 4:
        category = 'hydt'
        category_name = webConfig.TOPLABEL4
    elif article_type == 5:
        category = 'dfdt'
        category_name = webConfig.TOPLABEL5
    elif article_type == 0:
        category = 'qtwz'
        category_name = webConfig.TOPLABEL6
    else:
        category = 'index'
        category_name = webConfig.TOPLABEL0


    title = article.title
    content = []
    for temp in article.content.strip().split('\n'):
        temp = temp.strip()
        print temp.decode('utf-8')
        if temp.decode('utf-8') == '':
            continue
        content.append(temp)


    return render_to_response("article.html",
                              {
                                  "title": title,
                                  'article': article,
                                  'project_name': webConfig.PROJECTNAME,
                                  'toplabel0': webConfig.TOPLABEL0,
                                  'toplabel1': webConfig.TOPLABEL1,
                                  'toplabel2': webConfig.TOPLABEL2,
                                  'toplabel3': webConfig.TOPLABEL3,
                                  'toplabel4': webConfig.TOPLABEL4,
                                  'toplabel5': webConfig.TOPLABEL5,
                                  'toplabel6': webConfig.TOPLABEL6,
                                  'previous_id': previous_id,
                                  'next_id': next_id,
                                  'category': category,
                                  'category_name': category_name,
                                  'content': content,

                              }
                              )
