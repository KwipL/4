import wikipedia

def get_article(article):
    wikipedia.set_lang('ru')
    try:
        return wikipedia.summary(article)
    except wikipedia.WikipediaException:
        return 'По данному вопросу ничего не найдено'