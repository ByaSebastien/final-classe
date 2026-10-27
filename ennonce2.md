# Étape 02 : les jobs, le bestiaire et la Forêt de Macalania

> **Chapitre** : 02, héritage, classes abstraites et polymorphisme
> **Point de départ** : votre projet, dans l'état de la démo (`Character`, `Hero`, le Soldat et le Mage noir, le bestiaire des Plaines, le combat d'équipe)
> **Durée** : le palier obligatoire en 1 h 30 environ, puis les bonus
> **Solution** (bonus compris) : [`solution/final-classe/`](solution/final-classe/)

Les Plaines sont derrière vous. À la fin de cette étape, le joueur recrute deux héros de FF, et l'équipe traverse la Forêt de Macalania : Bombos, Ahrimans, un Pampa et ses 1000 épines… puis le Morbol.

**Les règles du projet** : `characters/` n'affiche rien ; chaque comportement propre à un job ou à une espèce vit **dans sa classe**, jamais dans une cascade d'`isinstance`.

---

## Le palier obligatoire

### 1. Se défendre (≈ 15 min)

Tous les héros peuvent se mettre en garde : jusqu'à leur prochain tour, les coups reçus sont divisés par deux.

Dans `Hero` (`heroes.py`) :
- l'attribut `guarding`, à `False` dans `__init__` ;
- `start_turn()` : le début du tour du héros, il quitte sa garde ;
- `defend()` : il se met en garde ;
- **`take_damage`, redéfinie** avec `@override` : en garde, le coup est divisé par deux (`amount //= 2`), puis on laisse la mère faire le reste avec `super().take_damage(amount)`.

Dans `game/battle.py`, `hero_turn` appelle `hero.start_turn()` en premier, et le menu gagne une 4e option :
```text
Vaan : 1. Attaquer  2. Omnislash (12 PM)  3. Potion (x3)  4. Se défendre
> 4
Vaan se met en garde : les coups reçus sont divisés par deux.
```

### 2. Trois nouveaux jobs (≈ 25 min)

Dans `jobs.py`, trois filles de `Hero`. Chacune redéfinit des attributs de classe, et écrit son `skill_effect` avec `@override`.

| Classe | `JOB_NAME` | PV / PM / VIT | `SKILL_NAME`, coût | `SKILL_TARGET` | Effet de `skill_effect(target)` |
|---|---|---|---|---|---|
| `Knight` | Chevalier | 820 / 30 / 8 | Brise-armure, 6 PM | `"ennemi"` | Une attaque, puis la DÉF de la cible est divisée par deux (au minimum 1). Renvoie les dégâts. |
| `Monk` | Moine | 680 / 60 / 11 | Chakra, 10 PM | `"allié"` | Soigne l'allié de MAG × 15 PV. Renvoie les PV rendus. |
| `Thief` | Voleur | 600 / 50 / 16 | Vol, 4 PM | `"ennemi"` | Prend tous les gils de la cible (elle n'en a plus), et les ajoute aux siens. Renvoie le montant volé. |

Chaque job a son `SKILL_TEXT` :
- `"{user} brise l'armure de {target} : {value} dégâts, et sa DÉF est divisée par deux."`
- `"{user} utilise Chakra sur {target} : +{value} PV."`
- `"{user} vole {value} gils à {target}."`

Ajoutez les trois classes à `JOBS` (`creation.py`) et aux réexportations de `characters/__init__.py`.

### 3. Le bestiaire de la Forêt (≈ 25 min)

Dans `Monster` (`monsters.py`), ajoutez la propriété **`warning`** : ce que le monstre laisse deviner de son prochain tour. Par défaut, rien (`None`). Dans `battle.py`, après le tour d'un monstre encore debout, affichez son annonce s'il en a une, en jaune.

Dans `bestiary.py`, quatre espèces :

| Classe | `NAME` | PV | FOR | MAG | DÉF | RÉS | VIT | XP | GIL | Ce qu'elle redéfinit |
|---|---|---|---|---|---|---|---|---|---|---|
| `Bomb` | Bombo | 900 | 28 | 28 | 12 | 12 | 9 | 90 | 70 | `act` : sous la moitié de ses PV, il **explose** sur un héros au hasard (MAG × 20), puis tombe K.O. Sinon, `super().act(heroes)`. |
| `Ahriman` | Ahriman | 780 | 10 | 30 | 10 | 20 | 12 | 90 | 60 | `attack` : il attaque à la magie, `magic_attack(target, 10)`. |
| `Cactuar` | Pampa | 675 | 18 | 1 | 26 | 26 | 20 | 160 | 150 | Voir ci-dessous. |
| `Malboro` | Morbol | 6600 | 38 | 30 | 18 | 14 | 7 | 600 | 500 | Rien : c'est un boss, mais ses attributs suffisent. |

**Le Pampa** compte ses tours :
- son `__init__` appelle `super().__init__(name)`, puis met `self._turn = 0` ;
- `act` : `self._turn += 1`. Un tour sur trois, il lance les **1000 épines** sur un héros au hasard, avec `self.strike(target, 1000)`. Sinon, il attaque normalement, avec `super().act(heroes)` ;
- `warning` : le tour d'avant (`self._turn % 3 == 2`), il annonce `Pampa se hérisse…`.

Chaque coup spécial renvoie un `Hit` qui porte son nom : `Hit("Explosion", …)`, `Hit("1000 épines", …)`.

```text
Pampa : attaque sur Basch, 80 dégâts.
Pampa se hérisse…
…
Pampa : 1000 épines sur Lulu, 550 dégâts.
```

### 4. Le recrutement (≈ 15 min)

Dans un nouveau module `game/recruit.py` :
- `recruits() -> list[Hero]` : les héros disponibles, chacun avec **20 points** répartis sur la base de 10 :

| Héros | Job | FOR | MAG | DÉF | RÉS |
|---|---|---|---|---|---|
| Cloud | `Soldier` | 22 | 12 | 16 | 10 |
| Lulu | `BlackMage` | 10 | 22 | 12 | 16 |
| Basch | `Knight` | 17 | 10 | 20 | 13 |
| Amarant | `Monk` | 18 | 16 | 14 | 12 |
| Djidane | `Thief` | 19 | 12 | 13 | 16 |

- `recruit(hero) -> list[Hero]` : le joueur choisit **deux** compagnons dans la liste (un héros choisi n'y est plus). Renvoie l'équipe, le héros du joueur en premier.

```text
Recrutez un compagnon (1/3) :
  1. Cloud    Soldat     PV 700  VIT 12  compétence : Omnislash
  2. Lulu     Mage noir  PV 520  VIT 10  compétence : Feu
  …
Votre choix : 2
Lulu rejoint l'équipe !
```

### 5. La Forêt de Macalania (≈ 10 min)

Dans `adventure.py` :
- une fonction `cross(zone, heroes, waves) -> bool` traverse une zone vague après vague (le combat, le butin, le repos), et renvoie `False` si l'équipe tombe ;
- dans `reward`, les gils volés par un compagnon rejoignent la bourse du héros du joueur ;
- `run()` : le prologue, la création, le recrutement, les Plaines, puis la Forêt :

```python
forest: list[list[Monster]] = [
    [Bomb(), Ahriman()],
    [Cactuar()],
    [Bomb("Bombo A"), Bomb("Bombo B"), Ahriman()],
    [Malboro()],
]
```

### Vérification
- [ ] Un héros en garde ne perd que la moitié des PV d'un coup, et sa garde tombe au début de son tour suivant.
- [ ] Brise-armure sur le Morbol : sa DÉF passe de 18 à 9.
- [ ] Le Pampa se hérisse au 2e tour, et lance ses 1000 épines au 3e.
- [ ] `grep isinstance` dans `characters/` ne trouve rien.

---

## Les bonus

Chaque bonus est indépendant. Faites-les dans l'ordre qui vous plaît.

### ★ 1. La Mauvaise haleine du Morbol
Comme le Pampa, le Morbol compte ses tours. Un tour sur trois, la **Mauvaise haleine** frappe **toute l'équipe** : `act` renvoie un `Hit` par héros debout, chacun avec `self.magic_attack(hero, 10)`. Le tour d'avant : `Morbol prend une grande inspiration…`.

### ★ 2. L'ordre du tour
Au début de chaque tour, `fight` affiche l'ordre de passage des combattants debout, selon leur VIT :
```text
Ordre du tour : Djidane → Pampa → Vaan → Lulu → Basch
```

### ★★ 3. Le Samouraï et l'Archer

| Classe | `JOB_NAME` | PV / PM / VIT | Compétence, coût | Effet | Recrue |
|---|---|---|---|---|---|
| `Samurai` | Samouraï | 760 / 40 / 9 | Lame bannie, 15 PM | FOR × 12 − DÉF × 5 // 2 : la DÉF ne compte qu'à moitié | Auron : 21 / 10 / 17 / 12 |
| `Archer` | Archer | 580 / 50 / 14 | Tir précis, 6 PM | FOR × 12, sans tenir compte de la DÉF | Fran : 18 / 14 / 12 / 16 |

### ★★ 4. Le Ninja
`Ninja` (Ninja, 560 / 50 / 18) et son **Lancer** (8 PM) : `SKILL_TARGET = "ennemis"`. Le combat lui passe **tous** les ennemis debout, `hero.use_skill(*targets)`, et `skill_effect` inflige FOR × 8 − DÉF × 3 à chacun. Sa recrue : Youfie (19 / 12 / 12 / 17).

### ★★★ 5. Le Loup alpha
`Monster.__init__(name=None, **changes)` : les stats partent des attributs de classe, rangées dans un dictionnaire, puis `changes` les écrase. Elles sont ensuite passées à la mère avec `super().__init__(name or self.NAME, **stats)`.
```python
Wolf("Loup alpha", hp=600, strength=20)
```
Le Pampa et le Morbol, qui ont leur propre `__init__`, doivent transmettre `**changes`. La 3e vague des Plaines devient `[Flan(), Wolf("Loup alpha", hp=600, strength=20)]`.

### ★★★ 6. À vous de jouer
Un job ou une espèce de votre invention : un Dragon qui crache du feu sur toute l'équipe, un Mage bleu qui apprend… Toujours la même question : **que redéfinit ma classe, et qu'hérite-t-elle ?**
