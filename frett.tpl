<!DOCTYPE html>
<html>
    <head>
        <title>{{frettir[int(n)]['fyrirsogn']}}</title>
        <link rel="stylesheet" href="/static/styles.css">
        <meta charset="utf-8">
    </head>
    <body>
        % include('header.tpl')
        <h1>{{frettir[int(n)]['fyrirsogn']}}</h1>
        <img src="/static/{{frettir[int(n)]['mynd']}}" alt='Frett'>
        <p>{{frettir[int(n)] ['texti']}}</p>
        <h3>{{frettir[int(n)] ['email']}}</h3>

        <a href="/">Til baka</a>
        % include('footer.tpl')
    </body>
</html>