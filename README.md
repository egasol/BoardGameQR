# BoardGameQR

#### The Premise
In BoardGameQR, players step into the shoes of intrepid explorers seeking lost knowledge. Their mission? To use cards encoded with QR codes to interact with a unknown world. The cards may be used to unlock clues, riddles, or even portals to other dimensions. Assemble your team, power up your Raspberry Pi, and let the adventure begin!

#### Game Components
<strong>QR Code Cards:</strong> These mystical cards are the heart of the game. Each card features a unique QR code that conceals secrets, challenges, or pathways. Some might reveal hidden passages, while others trigger traps or grant magical artifacts.
<strong>Raspberry Pi Board:</strong> Your trusty companion! The Raspberry Pi serves as your decoder, scanner, and guide. Connect it to a camera module for real-time QR code scanning. As you explore the game board, your Pi will reveal the mysteries encoded within.
<strong>Explore the Virtual World:</strong> The QR code transports you to a specific location within the virtual world. Maybe it’s a misty forest glade or an ancient library. Explore, collect artifacts, and uncover hidden paths.
<strong>Scan and Decode:</strong>Use your Raspberry Pi to scan QR codes on the game cards. The Pi’s camera captures the codes, and deciphers its messages. Is it a hint? A trap? Or the key to unlocking a secret door?
<strong>Solve Puzzles:</strong> Use the game cards to encounter with various encounters along the way. Solve riddles, anagrams, or logic puzzles to progress. Maybe the answer lies in ancient runes or constellations, trust your intuition!
<strong>Collect Artifacts:</strong> Some cards reveal artifacts—a magical compass, a lantern that reveals invisible ink, or a map to hidden chambers. These items aid your quest and open new avenues.
<strong>Collaborate:</strong> BoardGameQR encourages teamwork. Share discoveries, strategize, and combine your puzzle-solving skills. The more minds, the greater the chance of unraveling hidden mysteries.
#### Victory Awaits
As you delve deeper, you’ll uncover the grand narrative—the lost civilization, the forbidden library, and the ultimate QR code that holds the key to unimaginable power. But beware: darkness also stirs. Sinister forces seek to thwart your progress.

Will you decipher the final QR code, unlock the ancient gate, and reveal the truth? Only the bravest, cleverest, and most collaborative adventurers will prevail in BoardGameQR!


## Hardware

#### Hardware requirements
* Raspberry Pi
* Camera module
* Speaker
* Switch

#### Connect hardware
![image description](Media/hardware.svg)

## Setup

* Install the requirements
	* pip install -r requirements.txt
* (optional) Pre-generate dialogue for the map, not required but will make dialogue load faster during game.
	* Ex: python GenerateDialogue.py SavedMaps/Tutorial
* (optional) Add music
	* Add suitable background music by adding .mp3 files in the Music folder
* Start the game
	* python Game.py


## How to play

The goal of the game is given at the starting round, but normally very little information about how to complete the mission or even where to start. The initial part of the game should be used to navigate and explore the map by keeping track of the terrain when moving around and using actions such as scouting to gather information about nearby events. When encountering events it's important to think about how to interact with them and to remember clues given at other locations to get the whole picture and complete the campaign.

#### Core mechanic

While it's possible to use cards at will, it's not a good idea to just use interactions at random since the card played will be discarded. It's possible to regain use of a discarded cards by using a rest action, but the cost is that some cards will be permanently unplayable for the rest of the campaign. So it's best to have a good reason for using a card or you will run out of them, and lose.

## Adding content

#### Maps

To add a new map, create a folder in SavedMaps with the desired name. Within this folder create a file name map.json which will store content about terrain, events as well as starting point, opening dialogue etc.

#### New event

To add a new event, create a .json file within the map folder called anything other than map.json and information about name of the event, event status and interactions.

#### New cards

To create a new card, use CardCreator.py [python CardCreator.py] and enter name of the card, action (message encoded in the QR code) and descrption. The new card will be available as a .png image, available to print.