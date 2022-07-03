# CeneoWebScraper
# CeneoScraper

## Struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa opinii|Selektor|Nazwa zmiennej|Typ danych|
|---------------|--------|--------------|----------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id||
|autor opinii|span.user-post__author-name|author||
|rekomendacja autora|span.user-post__author-recomendation > em|recommendation||
|liczba gwiazdek|span.user-post__score-count|stars||
|treść opinii|div.user-post__text|content||
|lista zalet|div\[class$=positives\] ~ div.review-feature__item|pros||
|lista wad|div\[class$=negatives\] ~ div.review-feature__item|cons||
|dla ilu osób przydatna|button.vote-yes > span|useful||
|dla ilu osób nieprzydatna|button.vote-no > span|useless||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)\["datetime"\]|published||
|data zakupu produktu|span.user-post__published > time:nth-child(2)\["datetime"\]|purchased||

## Etapy pracy nad projektem strukturalnym
1. Pobranie elementów pojedynczej opinii do niezależnych zmiennych
2. Zapisanie wszystkich elemntów pojedynczej opinii do jednej zmiennej \(słownik\)
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i dodnie ich do listy
4. Pobranie wszystkich opinii o produkcie z wszystkich stron i zapisanie ich do pliku .json
5. Dodanie możliowści podania id produktu przez użytkownika za pomocą klawiatury
6. Refaktoryzacja \(optymalizacja\) kodu:
    1. utworzenie funkcji do pobierania składowych strony HTML
    2. utworzenie słownika opisującego strukturę opinii wraz z selektorami poszczególnych elementów
    3. zamiana instrukcji pobierających składowe opinii do pojedynczych zmiennych i tworzących z nich słownik na wyrażenie słownikowe \(dictionary comprehension\) tworzące słownik reprezentujący pojedynczą opinię na podstawie słownika selektorów
7. Analiza opinii o wybranym produkcie
    1. wczytanie wszystkich opinii o wskazanym produkcie do obiektu DataFrame
    2. wyliczenie podstawowych statystyk na podstawie opinii
        1. liczba wszystkich opinii o produkcie
        2. liczba opinii w których autor podał listę zalet produktu
        3. liczba opinii w których autor podał listę wad produktu
        4. średnia ocena produktu
    3. przygotowanie wykresów na podstawie zawartości opinii
        1. udział poszczególnych rekomendacji w ogólnej liczbie opinii
        2. histogram częstości występowania poszczególnych ocen (liczby gwiazdek)
8. Wykonanie listy bibliotek użytych w projekcie

# Lista bibliotek użytych w projekcie

beautifulsoup -Beautiful Soup to pakiet Pythona do analizowania dokumentów HTML i XML. Tworzy drzewo wyprowadzenia dla przeanalizowanych stron, które można wykorzystać do wyodrębnienia danych z HTML.

certifi - Certifi dostarcza Mozilli starannie wyselekcjonowaną kolekcję certyfikatów głównych do sprawdzania wiarygodności certyfikatów SSL podczas weryfikacji tożsamości hostów TLS.

charset-normalizer - Biblioteka, która pomaga odczytać tekst z kodowania charset.

click - Click służy do tworzenia pięknych interfejsów linii poleceń w sposób kompozycyjny z tak małą ilością kodu, jak to konieczne.

colorama - Sprawia, że sekwencje wyjścia ANSI (do tworzenia kolorowego tekstu terminala i pozycjonowania kursora) działają pod MS Windows.

cycler - służy do łatwego cyklicznego przeglądania pojedynczego stylu.

Flask - mikro framework aplikacji webowych napisany w języku Python. Jest sklasyfikowany jako micro-framework, ponieważ nie wymaga określonych narzędzi ani bibliotek.

fonttools - fontTools to biblioteka do manipulowania czcionkami, napisana w Pythonie. Projekt zawiera narzędzie TTX, które może konwertować czcionki TrueType i OpenType do i z formatu tekstowego XML, który jest również nazywany TTX.

idna - Obsługa protokołu Internationalised Domain Names in Applications (IDNA) określonego w RFC 5891. Jest to najnowsza wersja protokołu i jest czasami określana jako "IDNA 2008".

importlib-metadata - jest biblioteką zapewniającą dostęp do metadanych zainstalowanych pakietów. Zbudowana częściowo na systemie importu Pythona, biblioteka ta zamierza zastąpić podobną funkcjonalność w API punktu wejścia i API metadanych pkg_resources.

itsdangerous -  przekazać dane do niezaufanego środowiska i odzyskać je bezpiecznie. Dane są podpisane kryptograficznie, aby zapewnić, że token nie został naruszony.

Jinja2 - ilnik szablonów dla języka programowania Python pozwalający na separację logiki aplikacji od jej warstwy prezentacyjnej. Oprogramowanie o otwartym kodzie źródłowym, udostępnianym na zasadach licencji BSD. 

kiwisolver - Kiwi jest wydajną implementacją w języku C++ algorytmu rozwiązywania ograniczeń Cassowary. Kiwi jest implementacją algorytmu opartego na oryginalnym artykule Cassowary. Nie jest to refaktoryzacja oryginalnego solwera w C++.

MarkupSafe - MarkupSafe implementuje obiekt tekstowy, dzięki czemu można go bezpiecznie używać w HTML i XML. Znaki, które mają specjalne znaczenie są zastępowane tak, aby wyświetlały się jako rzeczywiste znaki.

matplotlib - biblioteka do tworzenia wykresów dla języka programowania Python i jego rozszerzenia numerycznego NumPy.

numpy - to biblioteka programistyczna dla języka Python, dodająca obsługę dużych, wielowymiarowych tabel i macierzy.

packaging - This library provides utilities that implement the interoperability specifications which have clearly one correct behaviour (eg: PEP 440) or benefit greatly from having a single shared implementation (eg: PEP 425).

pandas - pandas to biblioteka oprogramowania napisana dla języka programowania Python do manipulacji i analizy danych. W szczególności oferuje struktury danych i operacje służące do manipulowania tabelami liczbowymi i szeregami czasowymi.

Pillow - rozszerzenie dla Pythona, które dodaje obsługę grafiki np. otwieranie, modyfikowanie, zapisywanie plików graficznych.

pyparsing - Moduł pyparsing jest alternatywnym podejściem do tworzenia i wykonywania prostych gramatyk, w stosunku do tradycyjnego podejścia lex/yacc, lub użycia wyrażeń regularnych.

python-dateutil - Moduł dateutil obsługuje parsowanie dat w dowolnym formacie łańcuchowym. Ten moduł zapewnia wewnętrzne aktualne dane dotyczące światowej strefy czasowej. Moduł ten pomaga w obliczaniu względnych delt.

requests - Biblioteka requests jest de facto standardem wykonywania żądań HTTP w Pythonie. Abstrahuje ona od złożoności wykonywania żądań za pomocą pięknego, prostego API, dzięki czemu można skupić się na interakcji z usługami i konsumpcji danych w aplikacji.

six - Six jest biblioteką kompatybilności Pythona 2 i 3. Zapewnia funkcje użytkowe do wygładzania różnic między wersjami Pythona, mając na celu pisanie kodu Pythona, który jest kompatybilny na obu wersjach Pythona.

soupsieve - Soup Sieve to biblioteka selektorów CSS zaprojektowana do użycia z Beautiful Soup 4. Jej celem jest zapewnienie wybierania, dopasowywania i filtrowania przy użyciu nowoczesnych selektorów CSS.

urllib3 - urllib3 is a powerful, user-friendly HTTP client for Python. 

Werkzeug - Werkzeug jest wszechstronną biblioteką aplikacji internetowych WSGI. Werkzeug nie wymusza żadnych zależności. Do dewelopera należy wybór silnika szablonu, adaptera bazy danych, a nawet sposobu obsługi żądań.

zipp - Kompatybilny z pathlibem wrapper obiektu Zipfile. Oficjalny backport obiektu Path biblioteki standardowej.

Markdown – język znaczników przeznaczony do formatowania tekstu
