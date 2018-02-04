<!DOCTYPE html>
<html>
    <head>
        <title>Fréttir</title>
        <link rel="stylesheet" href="/static/styles.css">
        <meta charset="utf-8">
    </head>
    <body>
        % include('header.tpl')
        <h1>{{frettir[0]['fyrirsogn']}}</h1>
        <img src="/static/{{frettir[0]['mynd']}}" alt='Frett'>

        <ul>
            <li><a href="/frettir/0">{{frettir[0] ['fyrirsogn']}}</a></li>
            <li><a href="/frettir/1">{{frettir[1] ['fyrirsogn']}}</a></li>
            <li><a href="/frettir/2">{{frettir[2] ['fyrirsogn']}}</a></li>
            <li><a href="/frettir/3">{{frettir[3] ['fyrirsogn']}}</a></li>
        </ul>

        % include('footer.tpl')
    </body>
</html>