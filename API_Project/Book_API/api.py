import flask
from flask import request, jsonify
import flask_profiler

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# You need to declare necessary configuration to initialize
# flask-profiler as follows:
app.config["flask_profiler"] = {
    "enabled": app.config["DEBUG"],
    "storage": {
        "engine": "sqlite"
    },
    "basicAuth":{
        "enabled": True,
        "username": "admin",
        "password": "admin"
    },
    "ignore": [
	    "^/static/.*"
	]
}

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    [
  {
    "author": "Ann Leckie ",
    "first_sentence": "The body lay naked and facedown, a deathly gray, spatters of blood staining the snow around it.",
    "id": "null",
    "published": 2014,
    "title": "Ancillary Justice"
  },
  {
    "author": "John Scalzi",
    "first_sentence": "From the top of the large boulder he sat on, Ensign Tom Davis looked across the expanse of the cave, toward Captain Lucius Abernathy, Science Officer Q\u2019eeng and Chief Engineer Paul West perched on a second, larger boulder, and thought, Well, this sucks.",
    "id": "null",
    "published": 2013,
    "title": "Redshirts"
  },
  {
    "author": "Jo Walton",
    "first_sentence": "The Phurnacite factory in Abercwmboi killed all the trees for two miles around.",
    "id": "null",
    "published": 2012,
    "title": "Among Others"
  },
  {
    "author": "Connie Willis",
    "first_sentence": "By noon Michael and Merope still hadn\u2019t returned from Stepney, and Polly was beginning to get really worried.",
    "id": "null",
    "published": 2011,
    "title": "Blackout, All Clear (Vol. 2 - Blackout)"
  },
  {
    "author": "Paolo Bacigalupi",
    "first_sentence": "\u201cNo! I don\u2019t want the mangosteen.\u201d",
    "id": "null",
    "published": 2010,
    "title": "The Windup Girl"
  },
  {
    "author": "China Mieville",
    "first_sentence": "I could not see the street or much of the estate.",
    "id": "null",
    "published": 2010,
    "title": "The City & The City"
  },
  {
    "author": "Neil Gaiman",
    "first_sentence": "Nobody Owens, known to his friends as Bod, is a normal boy.",
    "id": "null",
    "published": 2009,
    "title": "The Graveyard Book"
  },
  {
    "author": "Michael Chabon",
    "first_sentence": "Nine months Landsman\u2019s been flopping at the Hotel Zamenhof without any of his fellow residents managing to get themselves murdered.",
    "id": "null",
    "published": 2008,
    "title": "The Yiddish Policemen's Union"
  },
  {
    "author": "Vernor Vinge",
    "first_sentence": "The first bit of dumb luck came disguised as a public embarrassment for the European Center for Defense Against Disease.",
    "id": "null",
    "published": 2007,
    "title": "Rainbows End"
  },
  {
    "author": "Robert Charles Wilson",
    "first_sentence": "One night in October when he was ten years old, Tyler Dupree stood in his back yard and watched the stars go out.",
    "id": "null",
    "published": 2006,
    "title": "Spin"
  },
  {
    "author": "Susanna Clarke",
    "first_sentence": "Some years ago there was in the city of York a society of magicians.",
    "id": "null",
    "published": 2005,
    "title": "Jonathan Strange and Mr. Norrell"
  },
  {
    "author": "Lois McMaster Bujold",
    "first_sentence": "Sta leaned forward between the crenellations atop the gate tower, the stone gritty beneath her pale hands, and watched in numb exhaustion as the final mourning party cleared the castle gate below.",
    "id": "null",
    "published": 2004,
    "title": "Paladin of Souls"
  },
  {
    "author": "Robert J. Sawyer",
    "first_sentence": "The blackness was absolute.",
    "id": "null",
    "published": 2003,
    "title": "Hominids"
  },
  {
    "author": "Neil Gaiman",
    "first_sentence": "Shadow had done three years in prison.",
    "id": "null",
    "published": 2002,
    "title": "American Gods"
  },
  {
    "author": "J. K. Rowling",
    "first_sentence": "The villagers of Little Hangleton still called it \u201cthe Riddle House,\u201d even though it had been many years since the Riddle family had lived there.",
    "id": "null",
    "published": 2001,
    "title": "Harry Potter and the Goblet of Fire"
  },
  {
    "author": "Vernor Vinge",
    "first_sentence": "The manhunt extended across more than one hundred light-years and eight centuries.",
    "id": "null",
    "published": 2000,
    "title": "A Deepness in the Sky"
  },
  {
    "author": "Connie Willis",
    "first_sentence": "There were five of us\u2014Carruthers and the new recruit and myself, and Mr. Spivens and the verger.",
    "id": "null",
    "published": 1999,
    "title": "To Say Nothing of the Dog"
  },
  {
    "author": "Joe Haldeman",
    "first_sentence": "It was not quite completely dark, thin blue moonlight threading down through the canopy of leaves.",
    "id": "null",
    "published": 1998,
    "title": "Forever Peace"
  },
  {
    "author": "Kim Stanley Robinson",
    "first_sentence": "Mars is free now. We\u2019re on our own. No one tells us what to do.",
    "id": "null",
    "published": 1997,
    "title": "Blue Mars"
  },
  {
    "author": "Neal Stephenson",
    "first_sentence": "The bells of St. Mark's were ringing changes up on the mountain when Bud skated over to the mod parlor to upgrade his skull gun.",
    "id": "null",
    "published": 1996,
    "title": "The Diamond Age"
  },
  {
    "author": "Lois McMaster Bujold",
    "first_sentence": "The row of comconsole booths lining the passenger concourse of Escobar's largest commercial orbital transfer station had mirrored doors, divided into diagonal sections by rainbow-colored lines of lights.",
    "id": "null",
    "published": 1995,
    "title": "Mirror Dance"
  },
  {
    "author": "Kim Stanley Robinson",
    "first_sentence": "The point is not to make another Earth. Not another Alaska or Tibet, not a Vermont nor a Venice, not even an Antarctica. The point is to make something new and strange, something Martian.",
    "id": "null",
    "published": 1994,
    "title": "Green Mars"
  },
  {
    "author": "Vernor Vinge",
    "first_sentence": "The coldsleep itself was dreamless.",
    "id": "null",
    "published": 1993,
    "title": "A Fire Upon the Deep"
  },
  {
    "author": "Connie Willis",
    "first_sentence": "Mr. Dunworthy opened the door to the laboratory and his spectacles promptly steamed up.",
    "id": "null",
    "published": 1993,
    "title": "Doomsday Book"
  },
  {
    "author": "Lois McMaster Bujold",
    "first_sentence": "I am afraid.",
    "id": "null",
    "published": 1992,
    "title": "Barrayar"
  },
  {
    "author": "Lois McMaster Bujold",
    "first_sentence": "\"Ship duty!\" chortled the ensign four ahead of Miles in line.",
    "id": "null",
    "published": 1991,
    "title": "The Vor Game"
  },
  {
    "author": "Dan Simmons",
    "first_sentence": "The Consul awoke with the peculiar headache, dry throat, and sense of having forgotten a thousand dreams which only periods in cryogenic fugue could bring.",
    "id": "null",
    "published": 1990,
    "title": "Hyperion"
  },
  {
    "author": "C. J. Cherryh",
    "first_sentence": "It was from the air that the rawness of the land showed most: vast tracts where humanity had as yet made no difference, deserts unclaimed, stark as moons, scrag and woolwood thickets unexplored except by orbiting radar.",
    "id": "null",
    "published": 1989,
    "title": "Cyteen"
  },
  {
    "author": "David Brin",
    "first_sentence": "There had never been such traffic at Port Helenia\u2019s sleepy landing field\u2014not in all the years Fiben Bolger had lived here.",
    "id": "null",
    "published": 1988,
    "title": "The Uplift War"
  },
  {
    "author": "Orson Scott Card",
    "first_sentence": "Rooter was at once the most difficult and the most helpful of the pequeninos.",
    "id": "null",
    "published": 1987,
    "title": "Speaker for the Dead"
  },
  {
    "author": "Orson Scott Card",
    "first_sentence": "The monitor lady smiled very nicely and tousled his hair and said, \u201cAndrew, I suppose by now you\u2019re just absolutely sick of having that horrid monitor.",
    "id": "null",
    "published": 1986,
    "title": "Ender's Game"
  },
  {
    "author": "William Gibson",
    "first_sentence": "The sky above the port was the color of television, tuned to a dead channel.",
    "id": "null",
    "published": 1985,
    "title": "Neuromancer"
  },
  {
    "author": "David Brin",
    "first_sentence": "Fins had been making wisecracks about human beings for thousands of years.",
    "id": "null",
    "published": 1984,
    "title": "Startide Rising"
  },
  {
    "author": "Isaac Asimov",
    "first_sentence": "\u201cI don\u2019t believe it, of course,\u201d said Golan Trevize, standing on the wide steps of Seldon Hall and looking out over the city as it sparkled in the sunlight.",
    "id": "null",
    "published": 1983,
    "title": "Foundation's Edge"
  },
  {
    "author": "C. J. Cherryh",
    "first_sentence": "The stars, like all man\u2019s other ventures, were an obvious impracticality, as rash and improbable an ambition as the first venture of man onto Earth\u2019s own great oceans, or into the air, or into space.",
    "id": "null",
    "published": 1982,
    "title": "Downbelow Station"
  },
  {
    "author": "Joan D. Vinge",
    "first_sentence": "Here on Tiamat, where there is more water than land, the sharp edge between ocean and sky is blurred; the two merge into one.",
    "id": "null",
    "published": 1981,
    "title": "The Snow Queen"
  },
  {
    "author": "Arthur C. Clarke",
    "first_sentence": "The crown grew heavier with each passing year.",
    "id": "null",
    "published": 1980,
    "title": "The Fountains of Paradise"
  },
  {
    "author": "Vonda N. McIntyre",
    "first_sentence": "The little boy was frightened.",
    "id": "null",
    "published": 1979,
    "title": "Dreamsnake"
  },
  {
    "author": "Frederik Pohl",
    "first_sentence": "My name is Robinette Broadhead, in spite of which I am male.",
    "id": "null",
    "published": 1978,
    "title": "Gateway"
  },
  {
    "author": "Kate Wilhelm",
    "first_sentence": "What David always hated most about the Sumner family dinners was the way everyone talked about him as if he were not there.",
    "id": "null",
    "published": 1977,
    "title": "Where Late the Sweet Birds Sang"
  },
  {
    "author": "Joe Haldeman",
    "first_sentence": "\u201cTonight we\u2019re going to show you eight silent ways to kill a man.\u201d",
    "id": "null",
    "published": 1976,
    "title": "The Forever War"
  },
  {
    "author": "Ursula K. Le Guin",
    "first_sentence": "There was a wall.",
    "id": "null",
    "published": 1975,
    "title": "The Dispossessed"
  },
  {
    "author": "Arthur C. Clarke",
    "first_sentence": "Sooner or later, it was bound to happen.",
    "id": "null",
    "published": 1974,
    "title": "Rendezvous with Rama"
  },
  {
    "author": "Isaac Asimov",
    "first_sentence": "\u201cLet me give you a lesson in practical politics.\u201d",
    "id": "null",
    "published": 1973,
    "title": "The Gods Themselves"
  },
  {
    "author": "Philip Jose Farmer",
    "first_sentence": "All those who ever lived on Earth have found themselves resurrected--healthy, young, and naked as newborns--on the grassy banks of a mighty river, in a world unknown.",
    "id": "null",
    "published": 1972,
    "title": "To Your Scattered Bodies Go"
  },
  {
    "author": "Larry Niven",
    "first_sentence": "In the nighttime heart of Beirut, in one of a row of general-address transfer booths, Louis Wu flicked into reality.",
    "id": "null",
    "published": 1971,
    "title": "Ringworld"
  },
  {
    "author": "Ursula K. Le Guin",
    "first_sentence": "I'll make my report as if I told a story, for I was taught as a child on my homeworld that Truth is a matter of the imagination.",
    "id": "null",
    "published": 1970,
    "title": "The Left Hand of Darkness"
  },
  {
    "author": "John Brunner",
    "first_sentence": "SCANALYZE MY NAME",
    "id": "null",
    "published": 1969,
    "title": "Stand on Zanzibar"
  },
  {
    "author": "Roger Zelazny",
    "first_sentence": "It is said that fifty-three years after his liberation he returned from the Golden Cloud, to take up once again the gauntlet of Heaven, to oppose the Order of Life and the gods who ordained it so.",
    "id": "null",
    "published": 1968,
    "title": "Lord of Light"
  },
  {
    "author": "Robert A. Heinlein",
    "first_sentence": "I see in Lunaya Pravda that Luna City Council has passed on first reading a bill to examine, license, inspect\u2014and tax\u2014public food vendors operating inside municipal pressure.",
    "id": "null",
    "published": 1967,
    "title": "The Moon Is a Harsh Mistress"
  },
  {
    "author": "Roger Zelazny",
    "first_sentence": "\u201cYou are a Kallikanzaros,\u201d she announced suddenly.",
    "id": "null",
    "published": 1966,
    "title": "And Call Me Conrad (aka. This Immortal)"
  },
  {
    "author": "Frank Herbert",
    "first_sentence": "In the week before their departure to Arrakis, when all the final scurrying about had reached a nearly unbearable frenzy, an old crone came to visit the mother of the boy, Paul.",
    "id": "null",
    "published": 1966,
    "title": "Dune"
  },
  {
    "author": "Fritz Leiber",
    "first_sentence": "Some stories of terror and the supernormal start with a moonlit face at a diamond-paned window, or an old document in spidery handwriting, or the baying of a hound across lonely moors.",
    "id": "null",
    "published": 1965,
    "title": "The Wanderer"
  },
  {
    "author": "Clifford D. Simak",
    "first_sentence": "The noise was ended now.",
    "id": "null",
    "published": 1964,
    "title": "Here Gather the Stars"
  },
  {
    "author": "Philip K. Dick",
    "first_sentence": "For a week Mr. R. Childan had been anxiously watching the mail.",
    "id": "null",
    "published": 1963,
    "title": "The Man in the High Castle"
  },
  {
    "author": "Robert A. Heinlein",
    "first_sentence": "Once upon a time when the world was young there was a Martian named Smith.",
    "id": "null",
    "published": 1962,
    "title": "Stranger in a Strange Land"
  },
  {
    "author": "Walter M. Miller Jr.",
    "first_sentence": "Brother Francis Gerard of Utah might never have discovered the blessed documents, had it not been for the pilgrim with girded loins who appeared during that young novice\u2019s Lenten fast in the desert.",
    "id": "null",
    "published": 1961,
    "title": "A Canticle for Leibowitz"
  },
  {
    "author": "Robert A. Heinlein",
    "first_sentence": "I always get the shakes before a drop.",
    "id": "null",
    "published": 1960,
    "title": "Starship Troopers"
  },
  {
    "author": "James Blish",
    "first_sentence": "The stone door slammed.",
    "id": "null",
    "published": 1959,
    "title": "A Case Of Conscience"
  },
  {
    "author": "Fritz Leiber",
    "first_sentence": "My name is Greta Forzane.",
    "id": "null",
    "published": 1958,
    "title": "The Big Time"
  },
  {
    "author": "Robert A. Heinlein",
    "first_sentence": "If a man walks in dressed like a hick and acting as if he owned the place, he\u2019s a spaceman.",
    "id": "null",
    "published": 1956,
    "title": "Double Star"
  },
  {
    "author": "Mark Clifton and Frank Riley",
    "first_sentence": "Just ahead, on Third Street, the massive facade of San Francisco's Southern Pacific depot loomed, half hidden in the swirling fog and January twilight.",
    "id": "null",
    "published": 1955,
    "title": "They'd Rather Be Right"
  },
  {
    "author": "Ray Bradbury",
    "first_sentence": "It was a pleasure to burn.",
    "id": "null",
    "published": 1954,
    "title": "Fahrenheit 451"
  },
  {
    "author": "Alfred Bester",
    "first_sentence": "Explosion!",
    "id": "null",
    "published": 1953,
    "title": "The Demolished Man"
  },
  {
    "author": "Robert A. Heinlein",
    "first_sentence": "Our troop had been up in the High Sierras that day and we were late getting back.",
    "id": "null",
    "published": 1951,
    "title": "Farmer in the Sky"
  },
  {
    "author": "Isaac Asimov",
    "first_sentence": "Bel Riose traveled without escort, which is not what court etiquette prescribes for the head of a fleet stationed in a yet-sullen stellar system on the Marches of the Galactic Empire.",
    "id": "null",
    "published": 1946,
    "title": "The Mule"
  },
  {
    "author": "T. H. White",
    "first_sentence": "ender",
    "id": "null",
    "published": 1939,
    "title": "The Sword in the Stone (Part 1 of The Once and Future King)"
  }
]
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books?id=0', methods=['GET'])
def id0():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

flask_profiler.init_app(app)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_title():
    if 'title' in requests.args:
        title = string(request.args['title'])
    else:
        return "error."

    results = []

    for book in books:
        if book['title'] == title:
            results.append(book)
    return jsonify(results)

# All the endpoints declared so far will be tracked by flask-profiler.

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
