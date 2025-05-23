import marimo

__generated_with = "0.11.25"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        jupyter: python3
        eval: false
        ---

        # Introduction au langage Python {#sec-chap00}

        Dans ce chapitre, nous présentons quelques éléments essentiels du langage Python qui nous seront utiles dans ce manuel. Python est un langage très riche et peut aboutir à des projets logiciels très sophistiqués. Il est important de comprendre que la programmation Python n'est pas ici une fin en soi, mais plutôt un outil de scriptage et de manipulation des données satellitaires.

        :::::: bloc_objectif
        :::: bloc_objectif-header
        ::: bloc_objectif-icon
        :::

        **Objectifs d'apprentissage visés dans ce chapitre**
        ::::

        ::: bloc_objectif-body
        À la fin de ce chapitre, vous devriez être en mesure de :

        -   connaître les principales distributions de Python;
        -   installer un environnement d'exécution du code de cet ouvrage;
        -   comprendre les structures de base du langage Python;
        :::
        ::::::

        Python, créé par [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) en 1991, est un langage de programmation polyvalent et facile à apprendre, souvent comparé à un couteau suisse numérique pour sa simplicité et sa polyvalence. Comme un outil multifonction, Python peut être utilisé pour une variété de tâches, du développement web à l'analyse de données, en passant par l'intelligence artificielle.

        ## Les distributions

        Il existe plusieurs [distributions](https://wiki.python.org/moin/PythonDistributions) du langage Python, ces distributions sont comme différentes saveurs de votre glace préférée - chacune a ses propres caractéristiques uniques, mais elles sont toutes fondamentalement Python. Voici un aperçu des principales distributions :

        -   [CPython](https://www.python.org/downloads/) est la distribution "vanille" officielle, comme la recette originale de Python. Elle est ainsi le choix idéal pour la compatibilité et la conformité aux standards.

        -   [Anaconda](https://www.anaconda.com/download). Pensez-y comme à un sundae tout garni. Elle vient avec de nombreuses bibliothèques scientifiques préinstallées, ce qui est idéal pour l'analyse de données et l'apprentissage automatique (*machine learning*).

        -   [Miniconda](https://docs.anaconda.com/miniconda/miniconda-install/) est une distribution légère de Python qui vous permet d'ajouter au besoin d'autres bibliothèques.

        -   [PyPy](https://pypy.org/) : est une version turbo de Python, optimisée pour la vitesse.

        Chaque distribution a ses forces, que ce soit la simplicité, la vitesse ou des fonctionnalités spécifiques. Le choix dépend donc de vos besoins, comme choisir entre une glace simple ou une glace royal (banana split) élaboré.

        ## Les styles de programmation en Python

        Il existe plusieurs approches pour programmer en Python. La plus directe est en version interactive en tapant `python` et de rentrer des commandes ligne par ligne.

        ### Les outils de programmation

        Un code python prend la forme d'un simple fichier texte avec l'extension `.py` et peut être modifié avec un simple éditeur de texte. Cependant, il n'y aura pas de rétroactions immédiates de l'interpréteur Python, ce qui rend la correction d'erreurs (débogage) beaucoup plus laborieux.

        Un IDE (*Integrated Developement Environnement*) est comme une boîte à outils complète pour les programmeurs, vous trouverez :

        -   Un éditeur de texte amélioré pour écrire votre code, avec des fonctionnalités comme la coloration syntaxique qui rend le code plus lisible.

        -   Un compilateur qui transforme votre code en instructions que l'ordinateur peut comprendre.

        -   Un débogueur pour trouver et corriger les erreurs, tel un détective numérique.

        -   Des outils d'automatisation qui effectuent des tâches répétitives, comme un assistant virtuel pour le codage.

        -   L'accès à la documentation des différentes librairies.

        Ces outils intégrés permettent aux développeurs de travailler plus efficacement, en passant moins de temps à jongler entre différentes applications et plus de temps à produire du code.

        Voici quelques options populaires :

        -   [PyCharm](https://www.jetbrains.com/pycharm/): est un des outils les plus utilisés dans l'industrie. Il offre une multitude de fonctionnalités comme l'autocomplétion intelligente et le débogage intégré, idéal pour les grands projets. Cependant, cet outil peut être assez gourmand en mémoire et en CPU. Notez qu'il existe une version gratuite et une version professionnelle.

        -   [Visual Studio Code](https://code.visualstudio.com/) : gratuit, léger mais puissant, il est personnalisable avec des extensions pour Python.

        -   [Spyder](https://www.spyder-ide.org/) : logiciel libre et gratuit, orienté vers les applications scientifiques.

        -   [Jupyter Notebooks](https://jupyter.org/) : imaginez un cahier interactif pour le code. Idéal pour l'analyse de données et l'apprentissage, il permet de mélanger code, texte et visualisations. Des services gratuits dans le **cloud** sont disponibles comme Google Colab et Kaggle. Ces environnements sont néanmoins moins appropriés pour des grands projets et le débogage. Jupyter peut souffrir de problèmes de reproductibilité dus à l'exécution arbitraire des cellules.

        -   [Marimo](https://marimo.io/) se veut une version plus moderne des *notebooks jupyter*. Contrairement à Jupyter, Marimo garantit la cohérence entre le code, les sorties et l'état du programme. Il analyse intelligemment les relations entre les cellules et réexécute automatiquement celles qui sont affectées par des changements, éliminant ainsi les problèmes d'état caché.

        ## Bonnes pratiques

        Python est un langage très dynamique, qui évolue constamment. Cela pose certains défis pour la gestion du code à long terme. Il est fortement conseillé d'utiliser des environnements virtuels pour gérer vos différentes bibliothèques (*libraries*). Voici quelques bonnes pratiques à suivre :

        1.  **N'installez par la toute dernière version de Python** : Il est recommandé d'installer 1 ou 2 version antérieure, par exemple si 3.13 est [la version plus récente](https://www.python.org/downloads/), installer plutôt la version 3.11. Les versions trop récentes peuvent être instables. La version de python désirée peut être spécifiée au moment de la création d'un environnement virtuel (voir plus bas). Vous pouvez afficher la liste des versions de python avec la commande `conda search --full-name python`.

        2.  **N'utilisez pas de version obsolète de Python**. Cela peut sembler contradictoire avec le point précédent mais c'est l'excès inverse. Si vous utilisez une version trop ancienne alors toutes vos librairies cesseront d'évoluer et peuvent devenir obsolètes.

        3.  **Utilisez des environnements virtuels**. Pensez-y comme à des compartiments séparées pour chaque projet. Cela évite les conflits entre les différentes versions de bibliothèques (*libraries*)et garde votre système propre. Par exemple, si vous souhaitez vérifier une nouvelle version de Python, utilisez un environnement : `conda create --name test python=3.11`

        4.  **Vérifiez l'installation**. Après l'installation, ouvrez un terminal et tapez `python --version` pour vous assurer que tout fonctionne correctement.

        ### Création d'un environnement virtuel {#sec-00-01}

        Il y a deux façons d'installer un environnement virtuel selon votre distribution de Python:

        1.  **Option 1**. Vous utilisez [Anaconda](https://www.anaconda.com/download) ou [Miniconda](https://docs.anaconda.com/miniconda/miniconda-install/). La commande `conda` est utilisée pour créer un environnement test avec Python 3.10:

        ``` bash
        conda env -n test python=3.10
        conda activate test
        ```

        2.  **Option 2**. Vous utilisez [CPython](https://www.python.org/downloads/)

        ``` bash
        conda env -n test python=3.10
        conda activate test
        ```

        ### Création d'un environnement de travail local (avancé)

        **Note**: les notebooks peuvent fonctionner localement uniquement sous Linux ou avec WSL2.

        Les notebooks Python fonctionnent par défaut dans l'environnement [Google Colab](https://colab.google/). Si vous souhaitez faire fonctionner ces notebook localement, vous pouvez installer un environnement local avec un serveur [Jupyter](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html). Il suffit de suivre les étapes suivantes:

        1\. Installer `WSL2` sous [Windows](https://learn.microsoft.com/en-us/windows/wsl/install)

        2\. Installer [vscode](https://code.visualstudio.com/docs/setup/windows)

        3\. Installer [Miniconda](https://docs.anaconda.com/miniconda/install/#quick-command-line-install)

        4\. Faire une installation du contenu du livre soit en utilisant une commande `git clone` ou en récupérant le `.zip` du livre

        5\. Ouvrir WSL2 et placer vous dans le répertoire du livre `TraitementImagesPythonVol1`. Assurez vous que vous avez accès à conda en tapant `conda --version`

        6\. Lancer la commande `conda env create -f jupyter_env.yaml`

        7\. Activer le nouvel environnement: `conda activate jupyter_env`

        8\. Le serveur jupyter peut ensuite être lancé avec la commande suivante: `jupyter lab --ip='*' --NotebookApp.token='' --NotebookApp.password=''`

        Une fenêtre devrait alors apparaître dans votre fureteur. Dans le menu de gauche vous pouvez accéder aux notebooks dans le répertoire `notebooks`:

        ![Fenêtre principale du serveur Jupyter Lab.](images/jupyter-accueil.png){#fig-jupyterlab fig-scap="Client Jupyter Lab" width="100%" fig-align="center"}

        ## Les structures de base en Python

        Il y a essentiellement deux structures de données que Python manipule : les listes et les dictionnaires.

        ### Les listes

        Les listes sont comme des boites extensibles où vous pouvez ranger différents types d'objets:

        -   Représentées par des crochets : `[1, 2, 3, "python"]`.

        -   Ordonnées et modifiables (*mutable*), vous pouvez récupérer une valeur par sa position avec `[]`.

        -   Permettent les doublons (deux fois la même valeur).

        -   Idéales pour stocker des collections d'éléments que vous voulez modifier

        ### Les tuples

        Les tuples sont similaires aux listes, mais les boîtes sont scellées:

        -   Représentés par des parenthèses : `(1, 2, 3, "python")`.

        -   Ordonnés mais non modifiables (*immutable*).

        -   Permettent les doublons.

        -   Souvent utilisés pour stocker des données qui ne doivent pas changer (comme des paramètres).

        ### Les ensembles (Sets)

        Les ensembles sont comme des boites magiques qui ne gardent qu'un exemplaire de chaque objet:

        -   Représentés par des accolades : `{1, 2, 3}`.

        -   Non ordonnés et modifiables.

        -   N'autorisent pas les doublons.

        -   Utiles pour éliminer les doublons et effectuer des opérations mathématiques sur des ensembles.

        ## Dictionnaires

        Les dictionnaires sont comme des boites avec des étiquettes sur chcune d'elle :

        -   Représentés par des accolades avec des paires clé-valeur : `{"nom": "Python", "année": 1991}`.

        -   Non ordonnés et modifiables.

        -   Les clés doivent être uniques, mais les valeurs peuvent être dupliquées

        -   Utiles pour stocker des données associatives ou pour créer des tables de recherche rapide

        ## Programmation objet

        La programmation orientée objet (POO) en Python est comme construire avec des blocs LEGO. Chaque objet est un bloc LEGO avec ses propres caractéristiques (attributs) et capacités (méthodes). Les classes sont les plans pour créer ces blocs. Par exemple, une classe "Voiture" pourrait avoir des attributs comme "couleur" et "vitesse", et des méthodes comme "démarrer" et "accélérer".

        Python rend la POO accessible avec des fonctionnalités conviviales:

        1.  **Encapsulation**: comme emballer un cadeau, elle cache les détails internes d'un objet.

        2.  **Héritage**: permet de créer de nouvelles classes basées sur des classes existantes, comme un enfant héritant des traits de ses parents.

        3.  **Polymorphisme**: permet à différents objets de répondre au même message de manière unique, comme si différents animaux répondaient différemment à "fais du bruit".

        Ces caractéristiques font de Python un excellent choix pour apprendre et appliquer les concepts de la POO, rendant le code plus organisé et réutilisable

        :::::: bloc_package
        :::: bloc_package-header
        ::: bloc_package-icon
        :::

        **Liste des *packages* utilisés dans ce chapitre**
        ::::

        ::: bloc_package-body
        -   Pour importer et manipuler des fichiers géographiques :
            -   `numpy` pour manipuler des données matricielles.
            -   `rasterio` pour importer et manipuler des données matricielles.
        -   Pour construire des cartes et des graphiques :
            -   `matplotlib` est certainement le *package* le plus complet pour l'affichage général.
            -   `seaborn` pour construire des graphiques plus détaillés en particulier pour les statistiques.
        :::
        ::::::
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
