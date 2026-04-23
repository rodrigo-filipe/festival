# festival

Descreva aqui as alterações/correções que fez

## Criei um venv 

criei um virtual enviroment para instalar django, de modo a poder dar run do site

## Corrigir as views (views.py)

Faltava dar import de varias views (Dia e Concerto), importei tambem o get_object_or_404() e Criei as views:

+ Palco
+ index
+ Dias

```python

def index_view(request):
    return render(request, 'festival/index.html')

def dias_view(request):
    dias = Dia.objects.all()
    return render(request, 'festival/dias.html', {'dias': dias})

def palcos_view(request):
    palcos = Palco.objects.prefetch_related('concertos').all()
    return render(request, 'festival/palcos.html', {'palcos': palcos})

```

de seguida "Arranjei" a view do concerto:

```python

def concerto_view(request, id):
    concerto = get_object_or_404(Concerto, pk=id)
    return render(request, 'festival/concerto.html', {'concerto': concerto})

```

## Corrigir os URLs (urls.py)

Adicionei uma rota dapa o dias

```python

 path('dias/', views.dias_view, name='dias'),

```

## Criação do dias.html

Não havia nenhuma pagina com os concertos e respetivos dias por isso criei uma

```html
{% extends 'festival/layout.html' %}

{% block content %}
    <h1>Dias</h1>
    
    {% for dia in dias %}
    <section>
        <h2>{{ dia.data }}</h2>
        
        {% for concerto in dia.concertos.all %}
        <article class="card">
            <a href="{% url 'concerto' concerto.id %}">{{ concerto.banda.nome }} - {{ concerto.palco }}, {{ concerto.hora }}</a>
        </article>
        {% endfor %}
    </section>
    {% endfor %}

{% endblock %}

```

## Link para a banda em palcos

Ao clicar na banda na pagina de palcos não estava a ir para os detalhes do concerto, por isso corrigi o link ao clicar no card

```html
<article class="card">
            <a href="{% url 'concerto' concerto.id %}">{{ concerto.banda.nome }} - {{ concerto.dia }}, {{ concerto.hora }}</a>
        </article>

```



