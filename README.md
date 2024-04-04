# BoardGameQR

#### The Premise
In BoardGameQR, players step into the shoes of intrepid explorers seeking lost knowledge. Their mission? To use cards encoded with QR codes to interact with an unknown world. The cards may be used to unlock clues, riddles, or even portals to other dimensions. Assemble your team, power up your Raspberry Pi, and let the adventure begin!

#### Game Components
<strong>QR Code Cards:</strong> These mystical cards are the heart of the game. Each card features a unique QR code that conceals secrets, challenges, or pathways. Some might reveal hidden passages, while others trigger traps or grant magical artifacts.

<strong>Raspberry Pi Board:</strong> Your trusty companion! The Raspberry Pi serves as your decoder, scanner, and guide. Connect it to a camera module for real-time QR code scanning. As you explore the game board, your Pi will reveal the mysteries encoded within.

<strong>Explore the Virtual World:</strong> The QR code transports you to a specific location within the virtual world. Maybe it’s a misty forest glade or an ancient library. Explore, collect artifacts, and uncover hidden paths.

<strong>Scan and Decode:</strong> Use your Raspberry Pi to scan QR codes on the game cards. The Pi’s camera captures the codes, and deciphers its messages. Is it a hint? A trap? Or the key to unlocking a secret door?

<strong>Solve Puzzles:</strong> Use the game cards to encounter with various encounters along the way. Solve riddles, anagrams, or logic puzzles to progress. Maybe the answer lies in ancient runes or constellations, trust your intuition!

<strong>Collect Artifacts:</strong> Some cards reveal artifacts—a magical compass, a lantern that reveals invisible ink, or a map to hidden chambers. These items aid your quest and open new avenues.

<strong>Collaborate:</strong> BoardGameQR encourages teamwork. Share discoveries, strategize, and combine your puzzle-solving skills. The more minds, the greater the chance of unraveling hidden mysteries.

#### Victory Awaits
As you delve deeper, you’ll uncover the grand narrative—the lost civilization, the forbidden library, and the ultimate QR code that holds the key to unimaginable power. But beware: darkness also stirs. Sinister forces seek to thwart your progress.

Will you decipher the final QR code, unlock the ancient gate, and reveal the truth? Only the bravest, cleverest, and most collaborative adventurers will prevail in BoardGameQR!


## Hardware

#### Hardware requirements
* <strong>Raspberry Pi</strong>
* <strong>Camera module</strong>
	* Utilized for scanning QR codes.
* <strong>Speaker</strong>
	* Used to play background music and dialogue.
* <strong>Switch</strong>
	* Pressed to activate the card of choice.

#### Connect hardware
![image description](Media/hardware.svg)

## Setup

1. <strong>Install the requirements</strong>
	* Navigate to the project folder
	* Run the following command to install the necessary Python packages
		* pip install -r requirements.txt
2. <strong>Sign Up for ElevenLabs</strong>
	* Visit ElevenLabs and create an account.
	* Obtain your API key.
	* Set the API key as an environment variable
		* export ELEVEN_API_KEY=<your_api_key>
3. <strong>Pre-Generate Dialogue (Optional):</strong>
	* If desired, pre-generate dialogue using ElevenLabs for the game map.
	* run the following command:
		* python GenerateDialogue.py SavedMaps/Tutorial
4. <strong>Add Background Music (Optional):</strong>
	* Enhance the game experience by adding suitable background music.
	* Place your .mp3 files in the Music folder.
5. <strong>Start the Game:</strong>
	* Execute the following command to launch the game:
		* python Game.py


## How to play

In the game, you receive an initial goal, but often lack detailed instructions on how to achieve it or where to begin. During the early stages, focus on exploring the map, paying attention to the terrain, and using actions like scouting to gather information about nearby events. When you encounter events, consider how to interact with them and recall any clues from other locations to piece together the full picture and successfully complete the campaign.

#### Core mechanic

While you have the freedom to play any cards whenever you like, it’s not advisable to use interactions randomly. When a card is played, it gets discarded. Although you can recover discarded cards through a rest action, there’s a trade-off: some cards become permanently unusable for the remainder of the campaign. Therefore, it’s essential to have a valid reason for playing a card; otherwise, you risk depleting your resources and ultimately losing

## Adding content

#### Maps

To add a new map, create a folder in SavedMaps with the desired name. Within this folder create a file name map.json which will store content about terrain, events as well as starting point, opening dialogue etc.

#### New event

To add a new event, create a .json file within the map folder called anything other than map.json and information about name of the event, event status and interactions.

#### New cards

To create a new card, use CardCreator.py [python CardCreator.py] and enter name of the card, action (message encoded in the QR code) and descrption. The new card will be available as a .png image, available to print.