web_inicio = """
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Janrax's Translator API</title>
</head>

<body>

    <div id="app">

        <div class="container">
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">{{titulo}}</a>
                </div>
            </nav>
            <form action="translate/" method="POST">
                <div class="row mt-3">
                    <div class="col-md-6">
                        <select v-model="src" class="form-select" aria-label="Lenguaje original">
                            <option value="af">afrikaans</option>
                            <option value="sq">albanian</option>
                            <option value="am">amharic</option>
                            <option value="ar">arabic</option>
                            <option value="hy">armenian</option>
                            <option value="az">azerbaijani</option>
                            <option value="eu">basque</option>
                            <option value="be">belarusian</option>
                            <option value="bn">bengali</option>
                            <option value="bs">bosnian</option>
                            <option value="bg">bulgarian</option>
                            <option value="ca">catalan</option>
                            <option value="ceb">cebuano</option>
                            <option value="ny">chichewa</option>
                            <option value="zh-cn">chinese (simplified)</option>
                            <option value="zh-tw">chinese (traditional)</option>
                            <option value="co">corsican</option>
                            <option value="hr">croatian</option>
                            <option value="cs">czech</option>
                            <option value="da">danish</option>
                            <option value="nl">dutch</option>
                            <option value="en">english</option>
                            <option value="eo">esperanto</option>
                            <option value="et">estonian</option>
                            <option value="tl">filipino</option>
                            <option value="fi">finnish</option>
                            <option value="fr">french</option>
                            <option value="fy">frisian</option>
                            <option value="gl">galician</option>
                            <option value="ka">georgian</option>
                            <option value="de">german</option>
                            <option value="el">greek</option>
                            <option value="gu">gujarati</option>
                            <option value="ht">haitian creole</option>
                            <option value="ha">hausa</option>
                            <option value="haw">hawaiian</option>
                            <option value="iw">hebrew</option>
                            <option value="he">hebrew</option>
                            <option value="hi">hindi</option>
                            <option value="hmn">hmong</option>
                            <option value="hu">hungarian</option>
                            <option value="is">icelandic</option>
                            <option value="ig">igbo</option>
                            <option value="id">indonesian</option>
                            <option value="ga">irish</option>
                            <option value="it">italian</option>
                            <option value="ja">japanese</option>
                            <option value="jw">javanese</option>
                            <option value="kn">kannada</option>
                            <option value="kk">kazakh</option>
                            <option value="km">khmer</option>
                            <option value="ko">korean</option>
                            <option value="ku">kurdish (kurmanji)</option>
                            <option value="ky">kyrgyz</option>
                            <option value="lo">lao</option>
                            <option value="la">latin</option>
                            <option value="lv">latvian</option>
                            <option value="lt">lithuanian</option>
                            <option value="lb">luxembourgish</option>
                            <option value="mk">macedonian</option>
                            <option value="mg">malagasy</option>
                            <option value="ms">malay</option>
                            <option value="ml">malayalam</option>
                            <option value="mt">maltese</option>
                            <option value="mi">maori</option>
                            <option value="mr">marathi</option>
                            <option value="mn">mongolian</option>
                            <option value="my">myanmar (burmese)</option>
                            <option value="ne">nepali</option>
                            <option value="no">norwegian</option>
                            <option value="or">odia</option>
                            <option value="ps">pashto</option>
                            <option value="fa">persian</option>
                            <option value="pl">polish</option>
                            <option value="pt">portuguese</option>
                            <option value="pa">punjabi</option>
                            <option value="ro">romanian</option>
                            <option value="ru">russian</option>
                            <option value="sm">samoan</option>
                            <option value="gd">scots gaelic</option>
                            <option value="sr">serbian</option>
                            <option value="st">sesotho</option>
                            <option value="sn">shona</option>
                            <option value="sd">sindhi</option>
                            <option value="si">sinhala</option>
                            <option value="sk">slovak</option>
                            <option value="sl">slovenian</option>
                            <option value="so">somali</option>
                            <option selected value="es">español</option>
                            <option value="su">sundanese</option>
                            <option value="sw">swahili</option>
                            <option value="sv">swedish</option>
                            <option value="tg">tajik</option>
                            <option value="ta">tamil</option>
                            <option value="te">telugu</option>
                            <option value="th">thai</option>
                            <option value="tr">turkish</option>
                            <option value="uk">ukrainian</option>
                            <option value="ur">urdu</option>
                            <option value="ug">uyghur</option>
                            <option value="uz">uzbek</option>
                            <option value="vi">vietnamese</option>
                            <option value="cy">welsh</option>
                            <option value="xh">xhosa</option>
                            <option value="yi">yiddish</option>
                            <option value="yo">yoruba</option>
                            <option value="zu">zulu</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <select v-model="dest" class="form-select" aria-label="Lenguaje a traducir">
                            <option disabled>Lenguaje a traducir</option>
                            <option value="af">afrikaans</option>
                            <option value="sq">albanian</option>
                            <option value="am">amharic</option>
                            <option value="ar">arabic</option>
                            <option value="hy">armenian</option>
                            <option value="az">azerbaijani</option>
                            <option value="eu">basque</option>
                            <option value="be">belarusian</option>
                            <option value="bn">bengali</option>
                            <option value="bs">bosnian</option>
                            <option value="bg">bulgarian</option>
                            <option value="ca">catalan</option>
                            <option value="ceb">cebuano</option>
                            <option value="ny">chichewa</option>
                            <option value="zh-cn">chinese (simplified)</option>
                            <option value="zh-tw">chinese (traditional)</option>
                            <option value="co">corsican</option>
                            <option value="hr">croatian</option>
                            <option value="cs">czech</option>
                            <option value="da">danish</option>
                            <option value="nl">dutch</option>
                            <option default value="en">english</option>
                            <option value="eo">esperanto</option>
                            <option value="et">estonian</option>
                            <option value="tl">filipino</option>
                            <option value="fi">finnish</option>
                            <option value="fr">french</option>
                            <option value="fy">frisian</option>
                            <option value="gl">galician</option>
                            <option value="ka">georgian</option>
                            <option value="de">german</option>
                            <option value="el">greek</option>
                            <option value="gu">gujarati</option>
                            <option value="ht">haitian creole</option>
                            <option value="ha">hausa</option>
                            <option value="haw">hawaiian</option>
                            <option value="iw">hebrew</option>
                            <option value="he">hebrew</option>
                            <option value="hi">hindi</option>
                            <option value="hmn">hmong</option>
                            <option value="hu">hungarian</option>
                            <option value="is">icelandic</option>
                            <option value="ig">igbo</option>
                            <option value="id">indonesian</option>
                            <option value="ga">irish</option>
                            <option value="it">italian</option>
                            <option value="ja">japanese</option>
                            <option value="jw">javanese</option>
                            <option value="kn">kannada</option>
                            <option value="kk">kazakh</option>
                            <option value="km">khmer</option>
                            <option value="ko">korean</option>
                            <option value="ku">kurdish (kurmanji)</option>
                            <option value="ky">kyrgyz</option>
                            <option value="lo">lao</option>
                            <option value="la">latin</option>
                            <option value="lv">latvian</option>
                            <option value="lt">lithuanian</option>
                            <option value="lb">luxembourgish</option>
                            <option value="mk">macedonian</option>
                            <option value="mg">malagasy</option>
                            <option value="ms">malay</option>
                            <option value="ml">malayalam</option>
                            <option value="mt">maltese</option>
                            <option value="mi">maori</option>
                            <option value="mr">marathi</option>
                            <option value="mn">mongolian</option>
                            <option value="my">myanmar (burmese)</option>
                            <option value="ne">nepali</option>
                            <option value="no">norwegian</option>
                            <option value="or">odia</option>
                            <option value="ps">pashto</option>
                            <option value="fa">persian</option>
                            <option value="pl">polish</option>
                            <option value="pt">portuguese</option>
                            <option value="pa">punjabi</option>
                            <option value="ro">romanian</option>
                            <option value="ru">russian</option>
                            <option value="sm">samoan</option>
                            <option value="gd">scots gaelic</option>
                            <option value="sr">serbian</option>
                            <option value="st">sesotho</option>
                            <option value="sn">shona</option>
                            <option value="sd">sindhi</option>
                            <option value="si">sinhala</option>
                            <option value="sk">slovak</option>
                            <option value="sl">slovenian</option>
                            <option value="so">somali</option>
                            <option value="es">spanish</option>
                            <option value="su">sundanese</option>
                            <option value="sw">swahili</option>
                            <option value="sv">swedish</option>
                            <option value="tg">tajik</option>
                            <option value="ta">tamil</option>
                            <option value="te">telugu</option>
                            <option value="th">thai</option>
                            <option value="tr">turkish</option>
                            <option value="uk">ukrainian</option>
                            <option value="ur">urdu</option>
                            <option value="ug">uyghur</option>
                            <option value="uz">uzbek</option>
                            <option value="vi">vietnamese</option>
                            <option value="cy">welsh</option>
                            <option value="xh">xhosa</option>
                            <option value="yi">yiddish</option>
                            <option value="yo">yoruba</option>
                            <option value="zu">zulu</option>
                        </select>
                    </div>


                </div>
                <div class="row mt-3">


                    <div class="col-md-6">
                        <div class="input-group">
                            <span class="input-group-text">Texto original</span>
                            <textarea class="form-control" aria-label="texto original" v-model="text" rows="10">
                            </textarea>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="input-group">
                            <span class="input-group-text">Texto traducido</span>
                            <textarea class="form-control" aria-label="texto final" v-model="resultado"
                                rows="10"></textarea>
                        </div>


                    </div>


                </div>
                <div class="d-grid gap-2 mt-3">
                    <button type="submit" @click.prevent="traducir()" class="btn btn-primary btn-lg"
                        type="button">Traducir</button>

                </div>

            </form>
            <div class="row mt-5">
                <h1>API de janrax's translator</h1>
                <pre>
                - Documentación:  <a href="/docs">/docs</a>
                - Lista de idiomas: <a href="/languages_list">/languages_list</a>
                - Traductor: <a href="/translate/?src=es&dest=en&text=Esto es un texto de prueba">/translate/?src=es&dest=en&text=Esto es un texto de prueba</a>
                </pre>
            </div>
        </div>



    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>

    <script>
        var app = new Vue({
            el: '#app',
            data: {
                titulo: "Janrax's translator",
                text: "Texto a traducir",
                resultado: "",
                src: "es",
                dest: "en"
            },
            methods: {
                async traducir() {

                    const rawResponse = await fetch('translate/', {
                        method: 'POST',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ text: this.text, src: this.src, dest: this.dest })
                    });
                    const content = await rawResponse.json();

                    this.resultado = content.translated_text

                }
            }
        })
    </script>



</body>

</html>
"""
